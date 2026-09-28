# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-28T08:39:12.936836+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : GRAM-EUR | action ACHETE_MAINTENANT | opportunité 8.289 | entrée 7.000 | trend 8.700 | rang 7.921
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : CC-EUR | action PLACE_LIMITE_PASSIVE | opportunité 7.525 | entrée 6.100 | trend 8.700 | rang 7.515
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : IMX-EUR | action LATENT_ACCELERATOR | opportunité 7.532 | entrée 5.650 | trend 8.400 | rang 7.318
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : HBAR-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.004 | entrée 6.350 | trend 8.950 | rang 7.773
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Tous les achats immédiats

1. GRAM-EUR — ACHETE_MAINTENANT — rank 7.921 — opportunité 8.289 — entrée 7.000 — trend 8.700
2. ALGO-EUR — ACHETE_MAINTENANT — rank 7.536 — opportunité 8.079 — entrée 7.050 — trend 8.150

## Top cross-sectionnel — aperçu non exhaustif

Ce top est une vue courte multi-buckets. Il ne doit jamais être utilisé comme liste exhaustive des achats immédiats.
1. GRAM-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 7.921
2. HBAR-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.773
3. W-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.759

## Accélération indépendante

- DGB-EUR — CONFIRMED_ACCELERATION — score 8.403/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- ZRO-EUR — CONFIRMED_ACCELERATION — score 7.073/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- GRAM-EUR — ACTIVE_NOW — score mémoire 7.921/10 — sources ACCELERATION, DECISION_LAYER, V4 — BUYABLE_NOW
- ALGO-EUR — ACTIVE_NOW — score mémoire 7.536/10 — sources ACCELERATION, DECISION_LAYER, V4 — BUYABLE_NOW
- ZRC-EUR — MEMORY_24H — score mémoire 8.779/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- FUEL-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- XMN-EUR — MEMORY_24H — score mémoire 8.447/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- DGB-EUR — ACTIVE_NOW — score mémoire 8.403/10 — sources ACCELERATION, V4 — WATCH_ONLY
- FRAX-EUR — MEMORY_24H — score mémoire 8.380/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- WMTX-EUR — MEMORY_24H — score mémoire 8.187/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- ACX-EUR — MEMORY_24H — score mémoire 8.120/10 — sources ACCELERATION — MEMORY_ONLY
- CAP-EUR — MEMORY_24H — score mémoire 7.967/10 — sources ACCELERATION, V4 — MEMORY_ONLY

## Audit des plus fortes hausses

- QNT-EUR +44.76% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- TREAD-EUR +36.94% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- AUDIO-EUR +19.33% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- GRT-EUR +15.14% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- XDC-EUR +12.31% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- HBAR-EUR +9.84% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE
- PUMP-EUR +9.80% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- SOSO-EUR +7.91% — NOT_DETECTED — couche SCANNER_COVERAGE — action NOT_APPLICABLE
- AZTEC-EUR +7.75% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- GRASS-EUR +7.01% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
