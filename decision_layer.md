# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-10-08T21:21:58.983955+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : W-EUR | action PLACE_LIMITE_PASSIVE | opportunité 7.762 | entrée 6.450 | trend 8.650 | rang 7.519
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : MAGIC-EUR | action LATENT_ACCELERATOR | opportunité 7.713 | entrée 5.250 | trend 8.650 | rang 6.975
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : NMR-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 7.490 | entrée 6.650 | trend 8.650 | rang 7.384
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Tous les achats immédiats

Aucun ACHETE_MAINTENANT dans le classement complet.

## Top cross-sectionnel — aperçu non exhaustif

Ce top est une vue courte multi-buckets. Il ne doit jamais être utilisé comme liste exhaustive des achats immédiats.
1. W-EUR — MEILLEURE_LIMITE_PASSIVE — PLACE_LIMITE_PASSIVE — rank 7.519
2. NMR-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.384
3. RAY-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.301

## Accélération indépendante

- MAGIC-EUR — CONFIRMED_ACCELERATION — score 8.875/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- QUID-EUR — CONFIRMED_ACCELERATION — score 7.798/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- EDU-EUR — CONFIRMED_ACCELERATION — score 7.708/10 — DETECTED_BUT_TOO_LATE
- TAIKO-EUR — BUILDING_ACCELERATION — score 5.850/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- 0G-EUR — BUILDING_ACCELERATION — score 5.450/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- ZBCN-EUR — BUILDING_ACCELERATION — score 4.925/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- AEVO-EUR — BUILDING_ACCELERATION — score 4.897/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- HAEDAL-EUR — BUILDING_ACCELERATION — score 4.824/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- GNS-EUR — MEMORY_24H — score mémoire 10.000/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- RLC-EUR — MEMORY_24H — score mémoire 10.000/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- MAGIC-EUR — ACTIVE_NOW — score mémoire 8.875/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- ZRC-EUR — MEMORY_24H — score mémoire 8.533/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- GTC-EUR — MEMORY_24H — score mémoire 8.274/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- NOS-EUR — MEMORY_24H — score mémoire 8.214/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- QUID-EUR — ACTIVE_NOW — score mémoire 7.798/10 — sources ACCELERATION — WATCH_ONLY
- SWELL-EUR — MEMORY_DECAY_24_72H — score mémoire 7.791/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- EDU-EUR — ACTIVE_NOW — score mémoire 7.708/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- CTSI-EUR — MEMORY_24H — score mémoire 7.656/10 — sources ACCELERATION — MEMORY_ONLY

## Audit des plus fortes hausses

- OGN-EUR +111.94% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- ZRC-EUR +56.92% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- RLC-EUR +28.89% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- GTC-EUR +20.58% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- SKL-EUR +18.47% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- DRV-EUR +17.71% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- QUID-EUR +16.72% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- PYTH-EUR +16.24% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- CTSI-EUR +16.22% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- TIA-EUR +14.22% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE

## Gestion des positions détenues

Policy : STAGED_10_20_RUNNER_V1
- +10% : prise partielle 35%.
- +20% : seconde prise 35%.
- Runner conservé : 30%.
- Revue coût d'opportunité après 72 h ; sortie seulement avant la première partielle, proche/sous le PRU et avec momentum 15m affaibli.
- Pas de stop serré mécaniquement après une petite hausse ; le stop reste lié à l'invalidation structurelle.

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
