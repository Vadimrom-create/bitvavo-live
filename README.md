# Bitvavo — baseline V4 et infrastructure de mesure V5

Le pipeline fonctionne sans clé Bitvavo. Le résultat prioritaire est `v5_report.md`, sa version structurée `v5_report.json`, l’état de fraîcheur `pipeline_health.json` et les mesures `evaluation.json`.

```bash
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
| `email_alert_v4.py` | Email uniquement pour nouvel épisode d’achat ou amélioration majeure ; cooldown |
| `scripts/publish_data.py` | Publication avant notification et résolution des écritures concurrentes indépendantes |

## Données et historique

`history/YYYY-MM-DD/<scan_id>.json.gz` est le journal de référence. Il est publié dans Git après chaque scan valide. Il contient les observations de tous les marchés, décisions brutes et stabilisées, features, exclusions, métadonnées et bougies 5m closes. Une réexécution ne remplace jamais un journal existant. L’index SQLite ne contient aucune donnée irremplaçable.

Les snapshots complets d’entrée et réponses API sont dans les artifacts Actions `scan-replay-*`, conservés 90 jours. Télécharger un artifact permet de rejouer la V4 d’origine sur les mêmes entrées et de vérifier l’égalité du résultat. La conservation indéfinie des journaux entraîne une croissance du dépôt : migrer vers SQLite/PostgreSQL sur un stockage durable dédié avant que le volume rende Git inadapté. Aucun historique absent n’est reconstruit artificiellement avec les vainqueurs actuels.

## Fréquence et fraîcheur

Demande cron : toutes les 5 minutes, décalée à :02/:07/:12… UTC. Donnée principale de décision : 15 minutes. GitHub Actions n’assure pas cette fréquence réelle : le rapport mesure les heures réelles, sans promettre un horaire. Un service continu sur une machine durable serait nécessaire pour une cadence stricte.

Le journal distingue heure Bitvavo, récupération de chaque requête, ouverture/clôture de la bougie et calcul du scan. Une bougie 15m fraîchement close peut légitimement avoir une ouverture datant de près de 30 minutes juste avant la prochaine clôture. Les marchés présentant des trous, des données manquantes ou un prix trop ancien ne produisent pas d’alerte. Un échec global est `FAILED`/`DEGRADED`, jamais une preuve d’absence d’opportunité.

## Alertes et exécution

Réutilise `vars.ALERT_GMAIL_USER`, `vars.ALERT_EMAIL_TO` et `secrets.GMAIL_APP_PASSWORD`. Destination configurée dans le dépôt : bellonirom@gmail.com. Aucun mot de passe n’est présent dans le code. Aucun email de scan vide, de routine ou de test automatique.

Un signal continu identique est envoyé une seule fois, même en REENTRY_READY. Nouvel épisode après disparition ou amélioration conjointe significative des scores ; délai global de 30 minutes et délai par marché de 4 heures. Les données sont publiées avant SMTP et l’état de livraison est persisté après. SMTP ne fournit pas d’idempotence : une panne après acceptation mais avant persistance peut encore laisser une livraison incertaine ; cette limite doit être traitée par un fournisseur à clé d’idempotence ou un registre de livraison indépendant avant une garantie stricte d’exactement un email.

`proposed_orders.json` est toujours `dry_run=true`, statut `PROPOSED_REQUIRES_HUMAN_APPROVAL`. Aucun ordre n’est soumis. Le cash (1 200 €), la réserve (500 €), l’exposition existante et les frais sont des hypothèses de simulation, pas des soldes privés lus sur Bitvavo. Ne pas utiliser ces montants comme état actuel du compte. Le stop tient compte du support et de l’ATR ; les objectifs 2R/3R sont des scénarios, pas des projections de prix. La taille est arrondie vers le bas et tient compte du risque, des minimums d’ordre et des plafonds cumulés. Des propositions corrélées ou de corrélation inconnue nécessitent un examen et ne sont pas empilées automatiquement.

## Évaluation avant optimisation

Lire [le protocole](docs/EVALUATION.md) et [l’audit](docs/AUDIT_2026-09-08.md). Aucune V5 optimisée n’est déclarée supérieure à V4. Les probabilités +10/+20/+30/+40 % restent nulles jusqu’à calibration hors échantillon. Les statistiques en cours ne remplacent pas un backtest ex ante complet.
