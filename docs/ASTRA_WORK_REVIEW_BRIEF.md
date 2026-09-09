# Brief d'audit indépendant — Astra / ChatGPT Work

## Mission

Auditer indépendamment le process du dépôt `Vadimrom-create/bitvavo-live`, depuis la baseline V4 jusqu'à la `Decision Layer V1` shadow et au monitoring des positions.

Ne pas supposer que les améliorations successives sont réellement des améliorations. Le but est de déterminer :

- ce qui est techniquement correct ;
- ce qui est statistiquement démontré ;
- ce qui est seulement heuristique ;
- ce qui risque de réduire le rappel ou d'augmenter les faux positifs ;
- ce qui peut contenir un bug d'intégration ou une fuite temporelle ;
- ce qui est prêt pour un usage réel en lecture seule ;
- ce qui doit rester shadow / dry-run.

Document principal à lire en premier : `docs/PROCESS_CHANGELOG_AND_AUDIT_TRAIL_2026-09-10.md`.

Documents complémentaires :

- `docs/AUDIT_2026-09-08.md`
- `docs/DELIVERY_2026-09-08.md`
- `docs/EVALUATION.md`
- `docs/POSITION_MONITORING.md`
- `README.md`

Code critique :

- `pipeline.py`
- `research/decision_layer.py`
- `research/features.py`
- `research/history.py`
- `research/evaluation.py`
- `research/risk.py`
- `scripts/run_decision_layer.py`
- `scripts/publish_data.py`
- `scripts/send_useful_alert.py`
- `monitoring/`
- `.github/workflows/update.yml`
- `.github/workflows/ci.yml`
- `tests/`

## Baseline à préserver pendant l'audit

La V4 est considérée comme baseline figée. Vérifier que les changements de mesure, qualité et Decision Layer ne modifient pas silencieusement ses scores ou seuils.

Référence initiale auditée : `ab25cdd5951448e6ac889bd1d1b8fd3defc93e12`.

Jalon principal d'infrastructure : `1056ae4d1766047d57c608b11be9e570d479bbf5`.

## Points d'audit prioritaires

### 1. Reproductibilité / absence de fuite temporelle

Vérifier :

- replay V4 strictement déterministe ;
- aucune donnée future utilisée dans features, évaluation ou classement ;
- bougies closes réellement closes au moment du signal ;
- historique first-seen ne réécrit pas silencieusement le passé ;
- les horizons d'évaluation ne contaminent jamais la décision courante.

### 2. Qualité de données et rappel

Question centrale : la politique de qualité protège-t-elle correctement ou élimine-t-elle trop de marchés ?

Examiner particulièrement :

- `INVALID_5M`
- `INVALID_15M`
- `MISSING_5M`
- `MISSING_15M`
- `MISSING_LATEST_CLOSED_CANDLE`
- `LOW_LIQUIDITY`
- `WIDE_SPREAD_RISK`

Distinguer impérativement :

- impossible d'évaluer l'opportunité ;
- opportunité observable mais impossible à exécuter immédiatement ;
- marché dangereux ;
- simple absence d'une feature secondaire.

Vérifier si les mêmes flags devraient être veto pour **achat immédiat** mais seulement dégrader/reclasser un **latent accelerator**.

### 3. Decision Layer V1

Auditer `research/decision_layer.py` ligne par ligne.

Questions :

- les seuils 7,40 / 7,30 / 6,80 / 5,80 / 7,60 ont-ils une justification suffisante pour un shadow test ?
- les poids 0,46 / 0,36 / 0,12 sont-ils cohérents ou redondants avec Opportunity qui contient déjà Trend/ignition ?
- y a-t-il du double comptage entre Opportunity et Trend ?
- la pénalité `change24 > 10 %` est-elle correctement dimensionnée ?
- le chase est-il pénalisé deux fois via V4/risk flags + ranking ?
- la récurrence `distinct_15m_periods` apporte-t-elle un signal réel ou favorise-t-elle mécaniquement les candidats persistants sans information nouvelle ?
- `pullback_like` est-il trop large ? Une variation 24 h négative suffit-elle vraiment ?
- la séparation limite passive / latent accelerator est-elle logique ?
- un `TOO LATE` devrait-il être un veto pour achat immédiat seulement, ou affecter aussi latent/re-entry ?

### 4. Vérification spécifique du diagnostic de mèches

Le ranking lit actuellement `wick_setup.is_wick_setup`.

Le producteur historique de `research/features.py` expose surtout un `status` :

- `NORMAL`
- `POTENTIALLY_EXPLOITABLE`
- `WAIT_FOR_DIRECTION`
- `DANGEROUS_STRUCTURE`

Vérifier le payload réel construit par `pipeline.py`.

Si aucun booléen `is_wick_setup` n'est créé ailleurs, la pénalité wick du ranking peut être inactive. Confirmer ou infirmer avec preuve de code / replay.

### 5. Cas IOST-like

Le test suivant est volontairement codé :

- Opportunity = 7,474
- Trend = 7,65
- Entry = 4,5

La couche doit conserver ce profil comme `LATENT_ACCELERATOR` si aucune défaillance structurelle n'existe.

Auditer la logique, mais ne pas utiliser le mouvement réel ultérieur d'IOST comme justification rétroactive du seuil.

### 6. Ranking cross-sectionnel

Vérifier si le ranking compare réellement les marchés sur une base homogène.

Points à challenger :

- marchés avec features manquantes ;
- biais vers gros volumes ou historiques complets ;
- double comptage de variables dérivées ;
- sensibilité des rangs à de petites variations de score ;
- stabilité du top 3 d'un scan au suivant ;
- nécessité éventuelle d'un percentile/rank normalisé plutôt qu'une somme fixe.

### 7. Protocole statistique

Vérifier que les conclusions restent compatibles avec la faiblesse actuelle de l'échantillon.

Exiger :

- séparation développement / validation ;
- critères définis avant résultats ;
- gestion des observations corrélées et répétées ;
- épisodes distincts plutôt que scans répétés comme pseudo-échantillons indépendants ;
- intervalles de confiance lorsque l'échantillon devient exploitable ;
- comparaison V4 vs Decision Layer sur les **mêmes fenêtres temporelles** ;
- pas de sélection a posteriori de l'horizon le plus favorable.

Ne pas produire de probabilités +10/+20/+30/+40 % tant qu'elles ne sont pas calibrées.

### 8. Monitoring des positions

Auditer :

- lecture seule réelle de l'adaptateur ;
- aucun endpoint de trading accessible ;
- priorité VENDS > profits partiels > relèvement stop > achat ;
- stop jamais abaissé ;
- sortie possible même si la prospection est corrompue ;
- fraîcheur compte/carnet ;
- déduplication ;
- confidentialité du registre chiffré ;
- absence de données privées dans `position_monitor_status.json` ;
- comportement fail-closed quand les secrets/plans manquent.

Au dernier état consigné : monitoring `UNCONFIGURED`, `READ_ONLY`, `dry_run=true` car secrets/paramètres manquants. Ne pas considérer cette couche validée en conditions réelles tant qu'une lecture réelle n'a pas été démontrée.

### 9. Alertes / publication / concurrence

Vérifier :

- publication avant alerte d'achat ;
- rebase borné ;
- pas d'écrasement automatique des fichiers générés en conflit ;
- écritures concurrentes du suivi privé préservées ;
- fenêtre d'incertitude SMTP correctement documentée ;
- impossibilité qu'une erreur Decision Layer shadow bloque une alerte de sortie urgente.

### 10. Performance opérationnelle

La cadence GitHub Actions réelle a été plus lente que le cron théorique.

Mesurer :

- durée totale d'un cycle ;
- latence jusqu'au signal ;
- proportion de marchés avec données admissibles ;
- impact de la cadence sur les opportunités courtes ;
- intérêt éventuel de séparer collecte rapide, scanner et évaluation lourde.

## Commits méthodologiques à inspecter

- `1056ae4d1766047d57c608b11be9e570d479bbf5`
- `bae1a2eb90ba53fbdcde12a6d379a92dc95f1411`
- `216aa6cfbc792662eb110505eff6ffa647fa93fa`
- `d957b817b9073be5ab5fd463ce69c824ae7d1b35`
- `9df2d08af6e35023051d82596338733628f0fdd0`
- `aeffd34c6c00908cf3e427d040bae28b1cce1784`
- `38e8d0f9842756c62ed5e8e70df6569d7f30c3b7`
- `011ee512211aafd93f1020e12b511d3fca805700`
- `db352541f034da1ccd14f4f2ddc93b1e82fb20ec`
- `7d7440c184dce145974563dc762d909d60ef6fb9`

Ignorer comme changements méthodologiques les nombreux commits automatiques `Record fresh scan and complete V4 measurement journal` et `Persist alert delivery state`, sauf pour auditer la robustesse du mécanisme de publication.

## Incident à reproduire mentalement / vérifier

Premier run réel de la Decision Layer : échec de `scripts/run_decision_layer.py` avec `ModuleNotFoundError: No module named 'research'`.

Correctif : ajout du root du repo au path dans le runner (`7d7440c...`). Le run suivant est passé intégralement.

Vérifier qu'aucune dépendance similaire au current working directory ne subsiste dans d'autres scripts.

## État technique de référence au moment du handoff

Dernier cycle complet vérifié : succès des étapes suivantes :

- tests ;
- collecte et scan ;
- replay V4 ;
- Decision Layer shadow ;
- publication ;
- monitoring positions (non configuré, donc fail-closed) ;
- GitHub Pages.

Suite de tests après Decision Layer : 61 tests réussis.

Dernière sortie Decision Layer consignée :

- achat immédiat : aucun ;
- limite passive : aucun ;
- latent accelerator : aucun ;
- meilleur pullback/re-entry : USELESS-EUR ;
- suivants : SYRUP-EUR, VVV-EUR.

Ce snapshot ne doit pas servir à évaluer la performance de la politique ; il sert seulement à vérifier que la couche tourne réellement.

## Format de restitution demandé au reviewer

Produire un rapport classé par sévérité :

### A. Bugs / erreurs certaines

Pour chaque point : fichier, fonction/ligne, mécanisme, impact, test de reproduction, correction minimale.

### B. Risques méthodologiques élevés

Fuite temporelle, biais de sélection, double comptage, sur-veto, mauvais protocole statistique, métrique trompeuse.

### C. Choix heuristiques acceptables en shadow mais non validés

Seuils, poids, catégories ou timing nécessitant accumulation prospective.

### D. Ce qui est solide et doit être conservé

Identifier explicitement les protections ou séparations d'architecture qui réduisent réellement le risque d'erreur.

### E. Plan de correction priorisé

Maximum 5 actions, ordonnées selon :

1. sécurité / intégrité ;
2. exactitude des données ;
3. qualité de décision ;
4. mesure statistique ;
5. performance opérationnelle.

Ne pas proposer de réécriture complète si une correction locale et testable suffit.

## Règle de gouvernance après review

Toute modification des seuils/poids/filters de décision devra être :

1. motivée par un problème précis ;
2. codée comme nouvelle politique/version ;
3. testée sans effacer V4 ni Decision Layer V1 ;
4. évaluée prospectivement ;
5. comparée sur les mêmes données ;
6. journalisée avec le commit, la justification et le résultat.

Le but n'est pas d'empiler des couches. Le but est de pouvoir supprimer celles qui n'apportent pas une amélioration mesurable.
