# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-29T10:02:50.839197+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : XLM-EUR | action ACHETE_MAINTENANT | opportunité 8.382 | entrée 7.800 | trend 8.750 | rang 7.990
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : ROSE-EUR | action PLACE_LIMITE_PASSIVE | opportunité 7.508 | entrée 5.850 | trend 7.950 | rang 7.075
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : MIOTA-EUR | action LATENT_ACCELERATOR | opportunité 7.916 | entrée 5.700 | trend 9.200 | rang 7.817
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : ENA-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 9.155 | entrée 7.250 | trend 7.900 | rang 8.131
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Tous les achats immédiats

1. XLM-EUR — ACHETE_MAINTENANT — rank 7.990 — opportunité 8.382 — entrée 7.800 — trend 8.750
2. LINK-EUR — ACHETE_MAINTENANT — rank 7.783 — opportunité 8.519 — entrée 7.200 — trend 9.200
3. POL-EUR — ACHETE_MAINTENANT — rank 7.757 — opportunité 8.704 — entrée 7.650 — trend 7.450
4. EIGEN-EUR — ACHETE_MAINTENANT — rank 7.172 — opportunité 8.193 — entrée 7.150 — trend 7.300

## Top cross-sectionnel — aperçu non exhaustif

Ce top est une vue courte multi-buckets. Il ne doit jamais être utilisé comme liste exhaustive des achats immédiats.
1. ENA-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.131
2. ALGO-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.049
3. XLM-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 7.990

## Accélération indépendante

- RPL-EUR — CONFIRMED_ACCELERATION — score 8.500/10 — DETECTED_BUT_TOO_LATE
- AMP-EUR — CONFIRMED_ACCELERATION — score 7.828/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- POND-EUR — CONFIRMED_ACCELERATION — score 7.229/10 — DETECTED_BUT_TOO_LATE
- CETUS-EUR — BUILDING_ACCELERATION — score 6.326/10 — DETECTED_BUT_TOO_LATE
- SUSHI-EUR — BUILDING_ACCELERATION — score 6.251/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- QNT-EUR — BUILDING_ACCELERATION — score 6.180/10 — DETECTED_BUT_TOO_LATE
- SKY-EUR — BUILDING_ACCELERATION — score 6.087/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- AZTEC-EUR — BUILDING_ACCELERATION — score 5.947/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- RSR-EUR — BUILDING_ACCELERATION — score 5.831/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- WIN-EUR — BUILDING_ACCELERATION — score 5.521/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- GIGA-EUR — MEMORY_24H — score mémoire 10.000/10 — sources ACCELERATION — MEMORY_ONLY
- ICX-EUR — MEMORY_24H — score mémoire 9.498/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- QUID-EUR — MEMORY_24H — score mémoire 9.062/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- SWELL-EUR — MEMORY_24H — score mémoire 9.000/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- DGB-EUR — MEMORY_24H — score mémoire 8.836/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- DYDX-EUR — MEMORY_24H — score mémoire 8.690/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- IMU-EUR — MEMORY_24H — score mémoire 8.632/10 — sources ACCELERATION — MEMORY_ONLY
- U-EUR — MEMORY_24H — score mémoire 8.582/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- RPL-EUR — ACTIVE_NOW — score mémoire 8.500/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- ENA-EUR — ACTIVE_NOW — score mémoire 8.131/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY

## Audit des plus fortes hausses

- POND-EUR +55.13% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- NMR-EUR +28.94% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- QNT-EUR +23.30% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- GRASS-EUR +23.12% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- CRV-EUR +21.40% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- SYRUP-EUR +20.25% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- 0G-EUR +18.83% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- CVX-EUR +16.68% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE
- INIT-EUR +15.92% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- SOON-EUR +15.59% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION

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
