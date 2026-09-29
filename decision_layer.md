# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-29T11:23:21.262849+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : ALGO-EUR | action ACHETE_MAINTENANT | opportunité 8.437 | entrée 7.000 | trend 8.900 | rang 8.091
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : JTO-EUR | action PLACE_LIMITE_PASSIVE | opportunité 9.010 | entrée 6.300 | trend 7.500 | rang 7.772
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : JASMY-EUR | action LATENT_ACCELERATOR | opportunité 7.509 | entrée 4.500 | trend 8.400 | rang 7.256
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : W-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.461 | entrée 6.450 | trend 8.650 | rang 7.955
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Tous les achats immédiats

1. ALGO-EUR — ACHETE_MAINTENANT — rank 8.091 — opportunité 8.437 — entrée 7.000 — trend 8.900
2. LINK-EUR — ACHETE_MAINTENANT — rank 8.056 — opportunité 8.333 — entrée 7.400 — trend 9.200
3. XLM-EUR — ACHETE_MAINTENANT — rank 8.040 — opportunité 8.394 — entrée 7.850 — trend 8.650
4. XDC-EUR — ACHETE_MAINTENANT — rank 7.856 — opportunité 8.485 — entrée 6.900 — trend 8.750
5. GALA-EUR — ACHETE_MAINTENANT — rank 7.749 — opportunité 8.156 — entrée 7.100 — trend 8.450

## Top cross-sectionnel — aperçu non exhaustif

Ce top est une vue courte multi-buckets. Il ne doit jamais être utilisé comme liste exhaustive des achats immédiats.
1. ALGO-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.091
2. LINK-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.056
3. XLM-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.040

## Accélération indépendante

- 0G-EUR — CONFIRMED_ACCELERATION — score 9.156/10 — DETECTED_BUT_TOO_LATE
- ZBCN-EUR — CONFIRMED_ACCELERATION — score 8.500/10 — DETECTED_BUT_TOO_LATE
- W-EUR — CONFIRMED_ACCELERATION — score 8.219/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- OSMO-EUR — CONFIRMED_ACCELERATION — score 6.533/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- ARX-EUR — BUILDING_ACCELERATION — score 5.983/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- REQ-EUR — BUILDING_ACCELERATION — score 5.767/10 — DETECTED_BUT_TOO_LATE
- CTC-EUR — BUILDING_ACCELERATION — score 5.437/10 — DETECTED_BUT_TOO_LATE
- CRO-EUR — BUILDING_ACCELERATION — score 5.081/10 — DETECTED_BUT_TOO_LATE
- SUSHI-EUR — BUILDING_ACCELERATION — score 4.964/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- AMP-EUR — MEMORY_24H — score mémoire 10.000/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- GIGA-EUR — MEMORY_24H — score mémoire 10.000/10 — sources ACCELERATION — MEMORY_ONLY
- ICX-EUR — MEMORY_24H — score mémoire 9.498/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- 0G-EUR — ACTIVE_NOW — score mémoire 9.156/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- BTT-EUR — MEMORY_24H — score mémoire 9.062/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- QUID-EUR — MEMORY_24H — score mémoire 9.062/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- SWELL-EUR — MEMORY_24H — score mémoire 9.000/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- DGB-EUR — MEMORY_24H — score mémoire 8.836/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- DYDX-EUR — MEMORY_24H — score mémoire 8.690/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- IMU-EUR — MEMORY_24H — score mémoire 8.632/10 — sources ACCELERATION — MEMORY_ONLY

## Audit des plus fortes hausses

- POND-EUR +44.75% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- ZBCN-EUR +28.62% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- 0G-EUR +26.42% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- CELO-EUR +25.79% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- NMR-EUR +22.83% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- GRASS-EUR +21.87% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- SYRUP-EUR +20.61% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- CRV-EUR +19.05% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- INIT-EUR +15.68% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- CVX-EUR +14.81% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE

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
