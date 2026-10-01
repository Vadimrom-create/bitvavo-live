# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-10-01T02:57:23.278258+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : ICP-EUR | action ACHETE_MAINTENANT | opportunité 9.213 | entrée 7.350 | trend 8.700 | rang 8.316
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : SAFE-EUR | action PLACE_LIMITE_PASSIVE | opportunité 7.979 | entrée 5.900 | trend 7.550 | rang 7.106
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : HUMA-EUR | action LATENT_ACCELERATOR | opportunité 7.902 | entrée 5.550 | trend 8.900 | rang 7.745
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : ZRO-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.790 | entrée 5.750 | trend 8.400 | rang 7.997
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Tous les achats immédiats

1. ICP-EUR — ACHETE_MAINTENANT — rank 8.316 — opportunité 9.213 — entrée 7.350 — trend 8.700
2. AVAX-EUR — ACHETE_MAINTENANT — rank 8.092 — opportunité 9.215 — entrée 7.200 — trend 7.850
3. NEAR-EUR — ACHETE_MAINTENANT — rank 7.752 — opportunité 8.080 — entrée 7.200 — trend 8.250
4. AAVE-EUR — ACHETE_MAINTENANT — rank 7.689 — opportunité 8.175 — entrée 7.100 — trend 8.250
5. LINK-EUR — ACHETE_MAINTENANT — rank 7.306 — opportunité 7.963 — entrée 7.600 — trend 7.350
6. LTC-EUR — ACHETE_MAINTENANT — rank 7.128 — opportunité 8.649 — entrée 7.650 — trend 5.700

## Top cross-sectionnel — aperçu non exhaustif

Ce top est une vue courte multi-buckets. Il ne doit jamais être utilisé comme liste exhaustive des achats immédiats.
1. ICP-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.316
2. AVAX-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.092
3. ZRO-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.997

## Accélération indépendante

- MOVR-EUR — CONFIRMED_ACCELERATION — score 7.330/10 — DETECTED_BUT_TOO_LATE
- GLMR-EUR — CONFIRMED_ACCELERATION — score 7.073/10 — DETECTED_BUT_TOO_LATE
- PLUME-EUR — BUILDING_ACCELERATION — score 6.232/10 — DETECTED_BUT_TOO_LATE
- ESP-EUR — BUILDING_ACCELERATION — score 6.058/10 — DETECTED_BUT_TOO_LATE
- TRAC-EUR — BUILDING_ACCELERATION — score 5.991/10 — DETECTED_BUT_TOO_LATE
- TRUMP-EUR — BUILDING_ACCELERATION — score 5.570/10 — DETECTED_BUT_TOO_LATE
- JASMY-EUR — BUILDING_ACCELERATION — score 5.490/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- MIOTA-EUR — BUILDING_ACCELERATION — score 5.262/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- LMWR-EUR — MEMORY_24H — score mémoire 9.685/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- CT-EUR — MEMORY_24H — score mémoire 9.156/10 — sources ACCELERATION — MEMORY_ONLY
- CTR-EUR — MEMORY_24H — score mémoire 8.902/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- ACU-EUR — MEMORY_24H — score mémoire 8.894/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- ARPA-EUR — MEMORY_24H — score mémoire 8.595/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- PONKE-EUR — MEMORY_24H — score mémoire 8.400/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- ICP-EUR — ACTIVE_NOW — score mémoire 8.316/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- GWEI-EUR — MEMORY_24H — score mémoire 8.214/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- WIN-EUR — MEMORY_24H — score mémoire 8.130/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- AVAX-EUR — ACTIVE_NOW — score mémoire 8.092/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY

## Audit des plus fortes hausses

- MOVR-EUR +90.86% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- CT-EUR +48.84% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- TRAC-EUR +28.40% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- GLMR-EUR +26.95% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- STX-EUR +21.00% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- MON-EUR +19.55% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- PLUME-EUR +19.18% — DETECTED_EARLY — couche NONE — action NONE
- NOS-EUR +15.31% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- CAP-EUR +14.34% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE
- ICX-EUR +12.63% — DETECTED_EARLY — couche NONE — action INTERPRETATION

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
