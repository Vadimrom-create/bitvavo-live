# Bitvavo — baseline V4 et infrastructure de mesure V5

Le pipeline fonctionne sans clé Bitvavo. Le résultat prioritaire est `v5_report.md`, sa version structurée `v5_report.json`, l’état de fraîcheur `pipeline_health.json` et les mesures `evaluation.json`.

```bash
python -m pip install -r requirements-monitoring.txt
python -m unittest discover -s tests -v
PYTHONHASHSEED=0 python pipeline.py
python -m research.replay runtime/replay-*.json.gz
python pipeline.py --evaluate-only
```

`pipeline.py` enchaîne collecte, V3, V4, stabilisation, contrôle global, carnets publics, historique et évaluation. Les scripts V3/V4 sont conservés ; la seule modification du détecteur est un point d’observation après calcul de toutes les lignes. Les sources d’origine sont dans `baseline/v4_20260908/`, identifiées par commit et SHA-256.

Tous les marchés EUR actifs reçoivent une collecte 5m/15m et un diagnostic explicite. La sélection d’entrée V4 reste limitée à 72 marchés : enlever ce cap constituerait une modification de politique à comparer séparément. L’enrichissement historique 1h/4h/quotidien est conservé. Les nouvelles features fermées, le chase risk numérique et le proxy structurel NIL sont des diagnostics non calibrés, de poids nul dans V4.

## Modules

| Module | Responsabilité |
|---|---|
| `collector-2.py`, `v3_*`, `v4_*` | Politique V4 de référence et état historique hérité |
| `research/http.py` | API publique, retries bornés, quotas, réponses horodatées, replay sans accès réseau |
| `research/features.py` | Features de bougies closes, mèches, volatilité, diagnostics et explication du score |
| `research/history.py` | Journaux immuables gzip et index SQLite reconstructible |
| `research/evaluation.py` | Horizons, seuils, censure des données absentes, faux négatifs et simulations |
| `research/risk.py` | Stop structurel, sizing en EUR, plafonds cumulés et propositions dry-run |
| `email_alert_v4.py` | Détection des épisodes d’achat V4 et cooldown historique |
| `monitoring/`, `scripts/send_useful_alert.py` | Soldes en lecture seule, suivi de chaque position, quatre actions utiles, état chiffré |
| `scripts/publish_data.py` | Publication avant notification et résolution des écritures concurrentes indépendantes |

## Données et historique

`history/YYYY-MM-DD/<scan_id>.json.gz` est le journal de référence. Il est publié dans Git après chaque scan valide. Il contient les observations de tous les marchés, décisions brutes et stabilisées, features, exclusions, métadonnées et bougies 5m closes. Une réexécution ne remplace jamais un journal existant. L’index SQLite ne contient aucune donnée irremplaçable.

Les bougies sont conservées une seule fois, à leur première observation, y compris lorsqu’une ancienne bougie arrive tardivement. Reconstruire l’index nécessite tous les journaux ; les features de chaque observation restent complètes. Les réponses brutes intégrales sont dans les artifacts Actions `scan-replay-*`, conservés 90 jours. Télécharger un artifact permet de rejouer la V4 d’origine sur les mêmes entrées et de vérifier l’égalité du résultat. La conservation indéfinie des journaux entraîne encore une croissance du dépôt : migrer vers SQLite/PostgreSQL sur un stockage durable dédié avant que le volume rende Git inadapté. Aucun historique absent n’est reconstruit artificiellement avec les vainqueurs actuels.

## Fréquence et fraîcheur

Demande cron : toutes les 5 minutes, décalée à :02/:07/:12… UTC. Donnée principale de décision : 15 minutes. GitHub Actions n’assure pas cette fréquence réelle : le rapport mesure les heures réelles, sans promettre un horaire. Un service continu sur une machine durable serait nécessaire pour une cadence stricte.

Le journal distingue heure Bitvavo, récupération de chaque requête, ouverture/clôture de la bougie et calcul du scan. Une bougie 15m fraîchement close peut légitimement avoir une ouverture datant de près de 30 minutes juste avant la prochaine clôture. Les marchés présentant des trous, des données manquantes ou un prix trop ancien ne produisent pas d’alerte. Un échec global est `FAILED`/`DEGRADED`, jamais une preuve d’absence d’opportunité.

## Alertes et exécution

Réutilise `vars.ALERT_GMAIL_USER` et `secrets.GMAIL_APP_PASSWORD`. Destination vérifiée : bellonirom@gmail.com. Aucun mot de passe n’est présent dans le code. Aucun email de scan vide, de routine, de maintien de position ou de test automatique.

Le workflow appelle le suivi des positions **à chaque cycle**, même si la prospection ou sa publication échoue, dans un checkout isolé. Il contrôle tous les soldes spot non nuls, indépendamment du top 50 V4. Un email peut uniquement contenir **ACHÈTE**, **VENDS**, **PRENDS PARTIELLEMENT TES PROFITS**, **RELÈVE LE STOP**. L’absence de source privée produit `UNCONFIGURED`, jamais un portefeuille supposé vide. Les achats par email exigent un compte frais et des limites réelles vérifiables. Le rapport public reste exploitable sans clé.

Les quatre secrets d’activation et les règles précises sont décrits dans [le suivi des positions](docs/POSITION_MONITORING.md). Le statut public `position_monitor_status.json` distingue disponibilité et absence d’action ; il ne divulgue aucun actif, solde, coût de revient ou niveau privé. Le registre privé est chiffré et authentifié avant publication.

Un achat continu identique est envoyé une seule fois, même en REENTRY_READY ; un nouvel épisode doit aussi respecter le délai de 4 heures par marché. Les actions non urgentes ont un délai global de 30 minutes. Une sortie sur stop préempte ce délai. Une proposition de stop doit améliorer son niveau, avec au moins une heure entre deux alertes. Un TP1 ou une sortie identique sur la même position ne se répète pas. Les nouvelles analyses d’achat sont publiées avant SMTP et l’état de livraison est persisté après. SMTP ne fournit pas d’idempotence : une panne après acceptation mais avant persistance peut encore laisser une livraison incertaine ; un fournisseur à clé d’idempotence ou un registre de livraison indépendant est nécessaire avant de promettre exactement un email.

`proposed_orders.json` est toujours `dry_run=true`, statut `PROPOSED_REQUIRES_HUMAN_APPROVAL`. Aucun ordre n’est soumis. Le cash (1 200 €), la réserve (500 €), l’exposition existante et les frais sont des hypothèses de simulation, pas des soldes privés lus sur Bitvavo. Ne pas utiliser ces montants comme état actuel du compte. Le stop tient compte du support et de l’ATR ; les objectifs 2R/3R sont des scénarios, pas des projections de prix. La taille est arrondie vers le bas et tient compte du risque, des minimums d’ordre et des plafonds cumulés. Des propositions corrélées ou de corrélation inconnue nécessitent un examen et ne sont pas empilées automatiquement.

## Évaluation avant optimisation

Lire [le protocole](docs/EVALUATION.md), [l’audit](docs/AUDIT_2026-09-08.md) et [le compte rendu de livraison](docs/DELIVERY_2026-09-08.md). Aucune V5 optimisée n’est déclarée supérieure à V4. Les probabilités +10/+20/+30/+40 % restent nulles jusqu’à calibration hors échantillon. Les statistiques en cours ne remplacent pas un backtest ex ante complet.
