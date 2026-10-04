# Validation live après #102 — 5 octobre 2026

Toutes les heures ci-dessous sont UTC, le 4 octobre 2026. Contrôle réalisé depuis `main` à `f6264fd76aa905c0540547c12c3c546ce3de67d6`. Aucun audit historique, rendement, cohorte ou stock stale n'a été recalculé. Aucune modification de code pendant cette validation.

## Cycles réellement exécutés et persistés

Premier cycle post-#102 : [37222907201](https://github.com/Vadimrom-create/bitvavo-live/actions/runs/37222907201), créé à 18:03:34, exécuté à partir de 18:14:34 après la fin du job précédent. Input réel du checkout : `c8cacf4028d1ec42e2ebace570e1d831ca8e2934`. Publication finale : [`aac2989`](https://github.com/Vadimrom-create/bitvavo-live/commit/aac29893f4fe8946c3e8e4cc8566761ff01b18e2), à 18:26:06. Tous les steps ont terminé avec succès ; les statuts métier d'évaluation conservent leurs erreurs de sources.

Dernier cycle prospectif complet observé : [37229636329](https://github.com/Vadimrom-create/bitvavo-live/actions/runs/37229636329), input `4a82b834efd972fae287579b06f632892e2623fb`, publication [`d08f5d6`](https://github.com/Vadimrom-create/bitvavo-live/commit/d08f5d661e72c9919b20c7fdfe2116f5943d8ad4) à 20:03:35.

Les heures sont celles de début des commandes, distinctes des heures de fin et de publication. Tous les steps d'un cycle héritent de son unique `SOLAIRE_INPUT_SHA`, visible dans les logs.

| Étape | Premier cycle | Dernier cycle | Statut métier / sortie effectivement conservée |
|---|---|---|---|
| Input neutre | 18:14:34 | 19:48:32 | OK, 426 marchés ; `v3_universe.json` dans l'artefact du run |
| V3 | 18:14:34 | 19:49:45 | OK_WITH_SOURCE_GAPS ; `solaire_v3_status.json`, candidates, journal, state, theses |
| Évaluation V3 | 18:15:35 | 19:50:36 | OK_WITH_SOURCE_GAPS ; `solaire_v3_evaluation_status.json`, comparison, journal ; erreurs candles notamment ICX/ONG/A puis ICX/ONG/ONT |
| V3.1 | 18:23:30 | 19:59:57 | OK ; `solaire_v31_status.json`, candidates, journal, state, portfolios |
| Évaluation V3.1 | 18:23:38 | 20:00:12 | OK_WITH_SOURCE_GAPS ; `solaire_v31_evaluation_status.json`, comparison ; erreurs ICX candles |
| Phase C | 18:23:58 | 20:00:45 | 15/15 OBSERVED chaque fois ; `phase_c_observation_status.json`, state et 15 nouveaux fichiers `execution_observations/` par cycle |
| Prix funnel | 18:24:07 | 20:00:54 | OK, 426 prix ; `funnel_prices.json` dans l'artefact |
| Full-funnel | 18:24:08 | 20:00:54 | OK ; status, report, state, journal |
| Policy challengers | 18:24:10 | 20:00:56 | OK ; `solaire_policy_challengers_status.json`, journal, portfolios |
| Évaluation policies | 18:24:12 | 20:00:59 | OK_WITH_SOURCE_GAPS ; evaluation_status et comparison ; erreurs ICX/A candles |
| Persistance | 18:25:56 | 20:03:22 | Commits publiés à 18:26:06 / 20:03:35 ; artefacts conservés ensuite |

Les changements de fichiers ont été vérifiés dans les deux commits de publication, pas seulement dans les messages de succès des jobs. Le premier run dure environ 11 min 32 s une fois démarré ; son attente préalable n'est pas du temps d'exécution.

## Full-funnel : correction démontrée

| Champ | Premier cycle | Dernier cycle |
|---|---|---|
| Statut | OK | OK |
| `price_source_path` | `runtime/prospective_inputs/funnel_prices.json` | identique |
| Source | `BITVAVO_PUBLIC_TICKER_PRICE_MEASUREMENT_ONLY` | identique |
| Génération du prix | 18:24:08.233799 | 20:00:54.986442 |
| Âge UNIVERSE à la mesure | 0,100139 s | 0,065609 s |
| Âge V3 / V3.1 | 573,522 / 37,546 s | 669,314 / 57,136 s |
| `input_health` | Les trois sources `ok=true` | Les trois sources `ok=true` |
| `inputs_ok` du report | true | true |
| `FUNNEL_INPUT_GAP` retenus dans le journal | 0 | 0 |
| `CENSORED_INPUT_GAP` | 0 | 0 |
| Épisodes actifs | 338 | 419 |
| Contrôle C0 au démarrage V3 | CURRENT | UNKNOWN_STALE_CONTROL |

Ces nombres d'épisodes ne sont ni des entrées exécutables ni des trades. La fraîcheur indiquée est celle de la mesure, pas l'âge du fichier au moment d'une consultation ultérieure.

## Même input réellement transmis aux trois consommateurs

Les logs des deux runs montrent, pour **chacun** des trois processus V3, V3.1 et policy challengers, `SOLAIRE_V3_UNIVERSE_PATH=runtime/prospective_inputs/v3_universe.json`. Le fichier est préparé une seule fois, dans le même workspace du job. Aucun step intermédiaire ne l'écrit ; le rebase de persistance intervient après les trois consommateurs. Le code réellement exécuté lit ce chemin ; avec cette variable définie, il n'existe pas de fallback automatique vers le snapshot production en cas de fichier absent.

Les artefacts ont été téléchargés et leur digest ZIP vérifié contre GitHub. Empreintes SHA-256 du fichier neutre :

| Run | Génération snapshot | SHA-256 `v3_universe.json` | Provenance |
|---|---|---|---|
| 37222907201 | 18:09:47.819614 | `0f1303da8f5f4688b0729910de3dac27e25470b2e8106ca23ec870d63e625803` | Copie explicite du snapshot production encore frais, âge 286,783 s. Les consommateurs lisent la copie research. |
| 37229636329 | 19:48:32.709498 | `5564ef30b834d07cdb9564ef7cdd5d8943cfd94f3191b850df10711752fb22ec` | Recalcul neutre isolé ; snapshot production initial vieux de 766,790 s. Aucun sender ni publication production. |

Artefacts : `11311332165` et `11312544720`. Preuve combinée : environnement des processus réellement exécutés, fichier unique conservé, absence de réécriture intermédiaire et correspondance du timestamp/provenance dans V3. Les anciens statuts V3.1/policy ne contiennent pas un reçu de lecture SHA individuel ; on ne prétend pas qu'un tel reçu existait.

## Phase C en conditions réelles

À la révision vérifiée : 63 observations persistées, dont 19 validations production et 44 captures indépendantes. Les deux cycles strictement post-#102 en ont ajouté 15 chacun. Tous les fichiers portent `research_only=true`, `affects_buy_gate=false`, `affects_email=false`, `orders_submitted=false`.

| Cas réel | Heure | Observation | Résultat |
|---|---|---|---|
| STRK BUY livré | 22:20:21 | `observation_0c53d73754098b32df512730c2fa5e9e` | PASS ; deux côtés, timestamps, fraîcheur, profondeur, VWAP 50/100/150, frais, liquidation immédiate et scénario adverse présents |
| GTC spread | 18:11:04 | `observation_0dbc4bdf3333b27a03cfc98ed17d954f` | SPREAD_TOO_WIDE ; carnet et coûts conservés |
| ZEUS liquidité | 19:19:48 | `observation_71da6d7c46e14edbfc74943519c64339` | INSUFFICIENT_EXECUTION_LIQUIDITY ; `BOOK_NOT_REQUESTED_OR_UNAVAILABLE` explicite, pas de prix/profondeur/VWAP inventés |
| VVV range | 22:35:29 | `observation_df09f3542022fbaaa1adf3e4a397408e` | STRUCTURAL_RANGE_TOO_NARROW ; carnet et coûts conservés |
| HNT stop | 22:10:27 | `observation_340493efc7782edbb45c894657180828` | STRUCTURAL_STOP_TOO_WIDE ; carnet et coûts conservés |

Chaque cas de validation ci-dessus porte ses `episode_id`, `decision_id`, `signal_id` et `observation_id`. Ce dernier est l'identifiant repris sous le nom `execution_observation_id` dans le statut et le journal ; ce sont deux noms du même identifiant, pas deux observations différentes. `parent_decision_id=null` est normal pour la validation initiale.

Exemple STRK : bid 0,053573 €, ask 0,05365 €, âge 0,3544 s ; coûts aller-retour immédiats estimés 0,3222 / 0,6447 / 0,9678 € pour 50/100/150 €. Scénario adverse : 0,4221 / 0,8445 / 1,2676 €. Ce sont des estimations au carnet et aux frais hypothétiques, pas des résultats de trades.

Pour tous les cas contrôlés : `fill_status=NO_REAL_FILL_EVIDENCE`, `passive_fill_status=PASSIVE_FILL_UNKNOWN`, `c3_status=UNKNOWN/NO_AUTHORIZATION`. Une absence de carnet avant veto volume reste une absence ; le collecteur séparé ne prétend pas reconstruire ce carnet historique.

La fonction de capture intercepte ses erreurs et ne participe pas à la décision. Le test `test_observer_disk_failure_changes_neither_email_nor_buy_plan` confirme le même appel SMTP mocké et le même plan avec écriture disponible ou impossible. Aucun test n'a envoyé de mail ou placé d'ordre.

## Rattachement causal : acquis et limite

BUY STRK : `signal_6cd8df15f6bbf842e8e29d93bbdb7078` → `episode_b71889f857b20af201f884d37e01409e` → `decision_4e1c60df40e8e7ab4eb8e43c441b22db` → `observation_0c53d73754098b32df512730c2fa5e9e` → `alert_id=STRK-EUR:20:1791152423018`. Le journal `production_decision_journal.json` contient la ligne `BUY_SENT/DELIVERED` avec exactement ces IDs, cycle `2026-10-04T22:19:05.822148+00:00`.

Les quatre rejets échantillonnés ont leurs IDs propres dans les observations, sans rapprochement au ticker. Un BUY ne doit pas être artificiellement inséré dans le registre des rejets.

Registre : la capture `observation_ddc04b1a6fb26a356ae319340bce88c5` pointe explicitement vers `registry_episode_id=GTC-EUR|1791132050`, encore BLOCKED_BUT_ALIVE. Les trades publics et le nouveau carnet ont été observés vers 20:00:53. Ce lien capture → épisode registre est exact.

**Limite non masquée :** cet épisode a été créé à 16:40:50, avant #101. Ses IDs de décision/épisode production d'origine sont absents ; le parent reste `null`. Aucun épisode du registre conservé à la révision contrôlée ne possède encore `source_decision_id`. La chaîne complète vers un nouvel épisode de registre instrumenté n'est donc pas démontrée live. On ne rattache pas rétroactivement le rejet GTC de 18:11 au veto initial de 16:40 sur la seule égalité du ticker. Ce manque ne doit pas être déclaré résolu par les tests unitaires de propagation.

## Sources externes : erreurs réellement enregistrées

Les mêmes codes apparaissent dans les deux cycles. Ils ne sont pas des 5xx transitoires démontrés. Aucun code ne prouve à lui seul la disparition définitive du service.

| Source / endpoint | HTTP | Interprétation étayée | Impact / alternative |
|---|---|---|---|
| Binance official — `www.binance.com/bapi/composite/v1/public/cms/article/catalog/list/query` | 400 | Requête refusée ; contrat/paramètres ou politique de l'endpoint à examiner si cette source devient nécessaire. Cause fine non prouvée par le code seul. | Flux CMS absent ; page officielle et autres flux restent disponibles. |
| CryptoCompare — `min-api.cryptocompare.com/data/v2/news/` | 401 | Accès non authentifié refusé ; exigence d'authentification/politique de source. | Actualités agrégées absentes ; autres RSS déjà configurés. |
| Coinbase official — `www.coinbase.com/blog/rss.xml` | 403 | Accès refusé depuis le runner ; mécanisme exact non identifié. | RSS absent ; page Coinbase et autres sources déjà configurées. |
| External Binance — `api.binance.com/api/v3/ticker/price` | 451 | Restriction d'accès signalée par le serveur. | Confirmation externe manquante ; OKX/Kraken restent interrogés, Bitvavo autonome. |
| External Bybit — `api.bybit.com/v5/market/tickers` | 403 | Accès refusé depuis le runner. | Même dégradation partielle de corroboration externe. |

V3 a tout de même traité 426 marchés, 193 puis 197 candidats, sans `critical_error`. Les pages/flux alternatifs ne garantissent pas une couverture sémantique identique de chaque news ; aucune substitution de donnée n'a été inventée. Aucune correction de ces fournisseurs n'est indispensable au fonctionnement du cœur Bitvavo dans les cycles observés. Aucun changement d'architecture ni contournement d'accès n'est proposé pour supprimer ces warnings.

## Invariants et tests

`python scripts/run_all_tests.py` sur la révision actuelle contrôlée : **259 tests réussis** (193 unittest + 66 fonctions ; les tests ajoutés entre-temps sur main expliquent l'écart avec 255). Les assertions d'empreinte et d'AST de Phase C passent.

Diff depuis la base pré-#101 `e00281e` : aucune modification de `research/production_gate.py`, `research/risk.py`, detector, contexte, scoring, sizing ou autorisation BUY. Le sender ne diffère que par la télémétrie #101 déjà validée. Aucun nouvel ordre automatique, aucun TEST_ENTRY, aucune promotion C1/C2/C3.

À 22:33:31 : `incomplete_rejection_evaluations=0`, `incomplete_reentry_evaluations=0`, `stale_incomplete_evaluations=0`. Les erreurs de bougies des autres évaluateurs ne sont pas présentées comme une rechute de ce stock résolu.

## Encore ouvert et maturation

- Chaîne complète production → nouveau registre instrumenté à observer ; les parents historiques inconnus restent inconnus.
- Le dernier cycle a correctement exposé un C0 périmé (`UNKNOWN_STALE_CONTROL`). Il ne peut pas servir silencieusement de comparaison C0 contemporaine complète.
- La cadence de collecte GitHub reste irrégulière : après le cycle publié à 20:03, aucun nouveau run prospectif n'apparaissait dans l'inventaire à la reprise de 22:40. Le bon état d'un cycle exécuté ne démontre pas une collecte toutes les 30 minutes. Aucune cause supplémentaire du scheduler n'a été établie ici.
- Erreurs candles ICX/A/ONG/ONT dans les évaluateurs V3/V3.1/policies ; champs d'erreur conservés, pas de rendement imputé.

Mode : collecte, maturation et surveillance prospective. Horizon principal 4 h, sensibilité 24 h, environ 28 jours et au moins 100 épisodes matures suffisamment indépendants ; gagnants et perdants. PnL net, expectancy, drawdown, MAE, coûts, slippage, concentration et incertitude restent à évaluer selon le protocole. Ces deux cycles ne démontrent aucune rentabilité ni supériorité d'un challenger.

Pas de blocker empêchant de poursuivre la collecte descriptive identifié. Les trous de C0 et de provenance empêchent en revanche de déclarer dès maintenant une comparaison causale intégrale ou une promotion justifiée.
