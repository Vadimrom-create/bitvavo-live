# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-30T08:18:16.222134+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : ICP-EUR | action ACHETE_MAINTENANT | opportunité 8.500 | entrée 7.150 | trend 8.900 | rang 8.087
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : BIGTIME-EUR | action PLACE_LIMITE_PASSIVE | opportunité 8.281 | entrée 6.700 | trend 8.150 | rang 7.691
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : BONK-EUR | action LATENT_ACCELERATOR | opportunité 7.540 | entrée 5.650 | trend 8.050 | rang 7.271
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : PLUME-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 9.016 | entrée 7.200 | trend 7.950 | rang 7.880
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Tous les achats immédiats

1. ICP-EUR — ACHETE_MAINTENANT — rank 8.087 — opportunité 8.500 — entrée 7.150 — trend 8.900
2. XLM-EUR — ACHETE_MAINTENANT — rank 7.944 — opportunité 8.299 — entrée 7.450 — trend 8.500
3. HBAR-EUR — ACHETE_MAINTENANT — rank 7.786 — opportunité 7.969 — entrée 7.600 — trend 8.400

## Top cross-sectionnel — aperçu non exhaustif

Ce top est une vue courte multi-buckets. Il ne doit jamais être utilisé comme liste exhaustive des achats immédiats.
1. ICP-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.087
2. XLM-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 7.944
3. PLUME-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.880

## Accélération indépendante

- U-EUR — CONFIRMED_ACCELERATION — score 7.467/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- XDC-EUR — BUILDING_ACCELERATION — score 5.401/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- TOWNS-EUR — BUILDING_ACCELERATION — score 5.071/10 — DETECTED_BUT_TOO_LATE
- GLMR-EUR — BUILDING_ACCELERATION — score 5.056/10 — DETECTED_BUT_TOO_LATE
- FLOCK-EUR — BUILDING_ACCELERATION — score 5.037/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- MIRA-EUR — BUILDING_ACCELERATION — score 5.033/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- ZRC-EUR — BUILDING_ACCELERATION — score 4.910/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- TREAD-EUR — MEMORY_24H — score mémoire 9.983/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- SWELL-EUR — MEMORY_24H — score mémoire 9.000/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- GNS-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- MOVR-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- WMTX-EUR — MEMORY_24H — score mémoire 8.460/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- AGI-EUR — MEMORY_24H — score mémoire 8.300/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- ICP-EUR — ACTIVE_NOW — score mémoire 8.087/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- SOLV-EUR — MEMORY_24H — score mémoire 8.017/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- XLM-EUR — ACTIVE_NOW — score mémoire 7.944/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- PLUME-EUR — ACTIVE_NOW — score mémoire 7.880/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY

## Audit des plus fortes hausses

- MOVR-EUR +72.41% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- GTC-EUR +34.82% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- SOON-EUR +31.65% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- GLMR-EUR +22.49% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- GNS-EUR +16.67% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ZBCN-EUR +14.44% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- 0G-EUR +14.38% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- MEW-EUR +14.14% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- PUMP-EUR +13.94% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ZRO-EUR +13.39% — DETECTED_EARLY — couche NONE — action NONE

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
