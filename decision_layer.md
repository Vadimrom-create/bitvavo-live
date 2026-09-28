# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-28T09:20:31.896598+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : GRAM-EUR | action ACHETE_MAINTENANT | opportunité 8.383 | entrée 7.200 | trend 8.700 | rang 7.997
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : SEI-EUR | action PLACE_LIMITE_PASSIVE | opportunité 7.654 | entrée 6.450 | trend 8.850 | rang 7.440
  - Strong structure but imperfect current entry; prefer passive execution. High extension/chase reduces rank but does not erase the setup.
- **MEILLEUR_LATENT_ACCELERATOR** : IMX-EUR | action LATENT_ACCELERATOR | opportunité 7.426 | entrée 4.750 | trend 8.400 | rang 7.250
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : CC-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.045 | entrée 7.250 | trend 8.700 | rang 7.913
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Tous les achats immédiats

1. GRAM-EUR — ACHETE_MAINTENANT — rank 7.997 — opportunité 8.383 — entrée 7.200 — trend 8.700

## Top cross-sectionnel — aperçu non exhaustif

Ce top est une vue courte multi-buckets. Il ne doit jamais être utilisé comme liste exhaustive des achats immédiats.
1. GRAM-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 7.997
2. CC-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.913
3. KAS-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.564

## Accélération indépendante

- HBAR-EUR — CONFIRMED_ACCELERATION — score 8.500/10 — DETECTED_BUT_TOO_LATE
- PARTI-EUR — CONFIRMED_ACCELERATION — score 7.672/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- ALGO-EUR — CONFIRMED_ACCELERATION — score 7.344/10 — DETECTED_BUT_TOO_LATE
- ZEUS-EUR — BUILDING_ACCELERATION — score 6.249/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- AGI-EUR — BUILDING_ACCELERATION — score 5.891/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- GRT-EUR — BUILDING_ACCELERATION — score 5.316/10 — DETECTED_BUT_TOO_LATE
- CPOOL-EUR — BUILDING_ACCELERATION — score 5.226/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- ATH-EUR — BUILDING_ACCELERATION — score 5.149/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- GRAM-EUR — BUILDING_ACCELERATION — score 4.810/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- GRAM-EUR — ACTIVE_NOW — score mémoire 7.997/10 — sources ACCELERATION, DECISION_LAYER, V4 — BUYABLE_NOW
- ZRC-EUR — MEMORY_24H — score mémoire 8.779/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- FUEL-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- HBAR-EUR — ACTIVE_NOW — score mémoire 8.500/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- XMN-EUR — MEMORY_24H — score mémoire 8.447/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- FRAX-EUR — MEMORY_24H — score mémoire 8.380/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- WMTX-EUR — MEMORY_24H — score mémoire 8.187/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- ACX-EUR — MEMORY_24H — score mémoire 8.120/10 — sources ACCELERATION — MEMORY_ONLY
- CAP-EUR — MEMORY_24H — score mémoire 7.967/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- SAFE-EUR — MEMORY_24H — score mémoire 7.933/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY

## Audit des plus fortes hausses

- TREAD-EUR +32.97% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- QNT-EUR +29.28% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- HBAR-EUR +19.61% — DETECTED_EARLY — couche NONE — action NONE
- GRT-EUR +16.38% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- AUDIO-EUR +14.07% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- AZTEC-EUR +12.15% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- PUMP-EUR +11.24% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- XDC-EUR +9.48% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- ALGO-EUR +7.64% — DETECTED_EARLY — couche NONE — action NONE
- MON-EUR +6.84% — DETECTED_EARLY — couche NONE — action INTERPRETATION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
