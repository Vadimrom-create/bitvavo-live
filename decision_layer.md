# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-29T11:01:41.190172+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : LINK-EUR | action ACHETE_MAINTENANT | opportunité 8.231 | entrée 7.600 | trend 9.200 | rang 7.986
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : LDO-EUR | action PLACE_LIMITE_PASSIVE | opportunité 8.106 | entrée 6.150 | trend 7.500 | rang 7.266
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : ROSE-EUR | action LATENT_ACCELERATOR | opportunité 8.575 | entrée 5.700 | trend 8.500 | rang 7.751
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : PLUME-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 9.189 | entrée 7.000 | trend 8.200 | rang 8.089
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Tous les achats immédiats

1. LINK-EUR — ACHETE_MAINTENANT — rank 7.986 — opportunité 8.231 — entrée 7.600 — trend 9.200

## Top cross-sectionnel — aperçu non exhaustif

Ce top est une vue courte multi-buckets. Il ne doit jamais être utilisé comme liste exhaustive des achats immédiats.
1. PLUME-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.089
2. CFG-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.011
3. LINK-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 7.986

## Accélération indépendante

- CELO-EUR — CONFIRMED_ACCELERATION — score 9.029/10 — DETECTED_BUT_TOO_LATE
- UP-EUR — CONFIRMED_ACCELERATION — score 7.034/10 — DETECTED_BUT_TOO_LATE
- MTL-EUR — CONFIRMED_ACCELERATION — score 6.776/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- LISTA-EUR — CONFIRMED_ACCELERATION — score 6.571/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- SOMI-EUR — BUILDING_ACCELERATION — score 5.740/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- SENT-EUR — BUILDING_ACCELERATION — score 5.517/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- CROSS-EUR — BUILDING_ACCELERATION — score 5.067/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- SIGN-EUR — BUILDING_ACCELERATION — score 5.032/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- POND-EUR — BUILDING_ACCELERATION — score 4.801/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- AMP-EUR — MEMORY_24H — score mémoire 10.000/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- GIGA-EUR — MEMORY_24H — score mémoire 10.000/10 — sources ACCELERATION — MEMORY_ONLY
- ICX-EUR — MEMORY_24H — score mémoire 9.498/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- BTT-EUR — MEMORY_24H — score mémoire 9.062/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- QUID-EUR — MEMORY_24H — score mémoire 9.062/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- CELO-EUR — ACTIVE_NOW — score mémoire 9.029/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- SWELL-EUR — MEMORY_24H — score mémoire 9.000/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- DGB-EUR — MEMORY_24H — score mémoire 8.836/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- DYDX-EUR — MEMORY_24H — score mémoire 8.690/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- IMU-EUR — MEMORY_24H — score mémoire 8.632/10 — sources ACCELERATION — MEMORY_ONLY

## Audit des plus fortes hausses

- POND-EUR +51.08% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- CELO-EUR +28.23% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- GRASS-EUR +24.20% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- NMR-EUR +23.48% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- 0G-EUR +21.52% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- CRV-EUR +19.65% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- SYRUP-EUR +19.28% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ZBCN-EUR +18.72% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- CVX-EUR +16.87% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE
- INIT-EUR +14.78% — DETECTED_EARLY — couche NONE — action INTERPRETATION

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
