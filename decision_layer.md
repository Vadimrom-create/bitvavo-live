# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-27T23:32:49.485761+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : RENDER-EUR | action ACHETE_MAINTENANT | opportunité 8.812 | entrée 7.300 | trend 9.200 | rang 8.384
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : ATH-EUR | action PLACE_LIMITE_PASSIVE | opportunité 8.187 | entrée 5.850 | trend 9.200 | rang 7.965
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : BRETT-EUR | action LATENT_ACCELERATOR | opportunité 8.331 | entrée 5.250 | trend 9.000 | rang 7.883
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : FIL-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.906 | entrée 6.250 | trend 8.650 | rang 8.139
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Tous les achats immédiats

1. RENDER-EUR — ACHETE_MAINTENANT — rank 8.384 — opportunité 8.812 — entrée 7.300 — trend 9.200
2. ONDO-EUR — ACHETE_MAINTENANT — rank 8.160 — opportunité 8.567 — entrée 7.650 — trend 8.850
3. OP-EUR — ACHETE_MAINTENANT — rank 8.152 — opportunité 8.520 — entrée 7.000 — trend 8.950
4. AAVE-EUR — ACHETE_MAINTENANT — rank 8.137 — opportunité 8.284 — entrée 7.050 — trend 9.000
5. EIGEN-EUR — ACHETE_MAINTENANT — rank 8.038 — opportunité 8.264 — entrée 6.900 — trend 8.900
6. GRAM-EUR — ACHETE_MAINTENANT — rank 7.922 — opportunité 8.119 — entrée 6.850 — trend 8.700
7. SUI-EUR — ACHETE_MAINTENANT — rank 7.711 — opportunité 8.226 — entrée 7.150 — trend 8.850

## Top cross-sectionnel — aperçu non exhaustif

Ce top est une vue courte multi-buckets. Il ne doit jamais être utilisé comme liste exhaustive des achats immédiats.
1. RENDER-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.384
2. ONDO-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.160
3. OP-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.152

## Accélération indépendante

- XDC-EUR — CONFIRMED_ACCELERATION — score 7.376/10 — DETECTED_BUT_TOO_LATE
- DGB-EUR — CONFIRMED_ACCELERATION — score 6.989/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- NOS-EUR — CONFIRMED_ACCELERATION — score 6.582/10 — DETECTED_BUT_TOO_LATE
- STRK-EUR — BUILDING_ACCELERATION — score 6.471/10 — DETECTED_BUT_TOO_LATE
- KMNO-EUR — BUILDING_ACCELERATION — score 5.811/10 — DETECTED_BUT_TOO_LATE
- PEAQ-EUR — BUILDING_ACCELERATION — score 5.797/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- T-EUR — BUILDING_ACCELERATION — score 5.368/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- ONDO-EUR — BUILDING_ACCELERATION — score 5.327/10 — DETECTED_BUT_TOO_LATE
- TREAD-EUR — BUILDING_ACCELERATION — score 5.313/10 — DETECTED_BUT_TOO_LATE
- IMU-EUR — BUILDING_ACCELERATION — score 4.980/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- YB-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- QNT-EUR — MEMORY_24H — score mémoire 8.429/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- RENDER-EUR — ACTIVE_NOW — score mémoire 8.384/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- FRAX-EUR — MEMORY_24H — score mémoire 8.380/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- ONDO-EUR — ACTIVE_NOW — score mémoire 8.160/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- OP-EUR — ACTIVE_NOW — score mémoire 8.152/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- FIL-EUR — ACTIVE_NOW — score mémoire 8.139/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- AAVE-EUR — ACTIVE_NOW — score mémoire 8.137/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- APE-EUR — ACTIVE_NOW — score mémoire 8.122/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- ACX-EUR — MEMORY_24H — score mémoire 8.120/10 — sources ACCELERATION — MEMORY_ONLY

## Audit des plus fortes hausses

- QNT-EUR +89.37% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- SOON-EUR +43.13% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- INX-EUR +32.25% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- GRT-EUR +27.73% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- TREAD-EUR +23.31% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- W-EUR +20.22% — DETECTED_EARLY — couche NONE — action NONE
- PUMP-EUR +16.28% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- XDC-EUR +15.27% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE
- IMX-EUR +14.16% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- AUDIO-EUR +12.90% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
