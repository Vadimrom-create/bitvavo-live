# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-28T07:54:57.441318+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : GRAM-EUR | action ACHETE_MAINTENANT | opportunité 8.170 | entrée 6.850 | trend 8.200 | rang 7.647
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : SKY-EUR | action PLACE_LIMITE_PASSIVE | opportunité 7.625 | entrée 6.000 | trend 8.750 | rang 7.617
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : AZTEC-EUR | action LATENT_ACCELERATOR | opportunité 8.029 | entrée 5.300 | trend 8.650 | rang 7.436
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : WLD-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.021 | entrée 6.700 | trend 8.650 | rang 7.848
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Tous les achats immédiats

1. GRAM-EUR — ACHETE_MAINTENANT — rank 7.647 — opportunité 8.170 — entrée 6.850 — trend 8.200

## Top cross-sectionnel — aperçu non exhaustif

Ce top est une vue courte multi-buckets. Il ne doit jamais être utilisé comme liste exhaustive des achats immédiats.
1. WLD-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.848
2. ONDO-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.798
3. CC-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.793

## Accélération indépendante

- MON-EUR — CONFIRMED_ACCELERATION — score 6.512/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- GRAM-EUR — BUILDING_ACCELERATION — score 5.886/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- AVA-EUR — BUILDING_ACCELERATION — score 5.679/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- XDC-EUR — BUILDING_ACCELERATION — score 5.215/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- ROBO-EUR — BUILDING_ACCELERATION — score 5.213/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- REQ-EUR — BUILDING_ACCELERATION — score 5.140/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- DGB-EUR — MEMORY_24H — score mémoire 10.000/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- ZRC-EUR — MEMORY_24H — score mémoire 8.779/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- FUEL-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- XMN-EUR — MEMORY_24H — score mémoire 8.447/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- FRAX-EUR — MEMORY_24H — score mémoire 8.380/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- WMTX-EUR — MEMORY_24H — score mémoire 8.187/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- ACX-EUR — MEMORY_24H — score mémoire 8.120/10 — sources ACCELERATION — MEMORY_ONLY
- CAP-EUR — MEMORY_24H — score mémoire 7.967/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- SAFE-EUR — MEMORY_24H — score mémoire 7.933/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- TOSHI-EUR — MEMORY_24H — score mémoire 7.894/10 — sources ACCELERATION, V4 — MEMORY_ONLY

## Audit des plus fortes hausses

- QNT-EUR +60.24% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- TREAD-EUR +30.53% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- AUDIO-EUR +19.39% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- GRT-EUR +12.99% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- XDC-EUR +10.70% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- PUMP-EUR +9.18% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- AZTEC-EUR +9.09% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- SOSO-EUR +6.37% — NOT_DETECTED — couche SCANNER_COVERAGE — action NOT_APPLICABLE
- MON-EUR +6.36% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ARX-EUR +6.14% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
