# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-28T11:58:39.282230+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : SEI-EUR | action ACHETE_MAINTENANT | opportunité 8.734 | entrée 8.000 | trend 8.600 | rang 7.978
  - V4 buy-ready with acceptable current entry; no structural veto. High extension/chase is retained as risk context, not an automatic veto.
- **MEILLEURE_LIMITE_PASSIVE** : XVG-EUR | action PLACE_LIMITE_PASSIVE | opportunité 8.574 | entrée 5.950 | trend 7.350 | rang 7.410
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : AZTEC-EUR | action LATENT_ACCELERATOR | opportunité 7.785 | entrée 5.550 | trend 8.450 | rang 7.461
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : EIGEN-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 9.083 | entrée 7.000 | trend 7.600 | rang 7.874
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Tous les achats immédiats

1. SEI-EUR — ACHETE_MAINTENANT — rank 7.978 — opportunité 8.734 — entrée 8.000 — trend 8.600
2. LINK-EUR — ACHETE_MAINTENANT — rank 7.129 — opportunité 7.762 — entrée 7.650 — trend 7.250
3. HYPE-EUR — ACHETE_MAINTENANT — rank 6.266 — opportunité 7.797 — entrée 7.150 — trend 4.850

## Top cross-sectionnel — aperçu non exhaustif

Ce top est une vue courte multi-buckets. Il ne doit jamais être utilisé comme liste exhaustive des achats immédiats.
1. SEI-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 7.978
2. EIGEN-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.874
3. XDC-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.819

## Accélération indépendante

- WMTX-EUR — CONFIRMED_ACCELERATION — score 9.914/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- SAGA-EUR — CONFIRMED_ACCELERATION — score 8.221/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- EDGE-EUR — BUILDING_ACCELERATION — score 6.367/10 — DETECTED_BUT_TOO_LATE
- LSK-EUR — BUILDING_ACCELERATION — score 5.209/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- XDC-EUR — BUILDING_ACCELERATION — score 4.964/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- NPC-EUR — BUILDING_ACCELERATION — score 4.823/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- LINK-EUR — ACTIVE_NOW — score mémoire 7.129/10 — sources ACCELERATION, DECISION_LAYER, V4 — BUYABLE_NOW
- PUMP-EUR — ACTIVE_NOW — score mémoire 5.876/10 — sources ACCELERATION, DECISION_LAYER, V4 — BUYABLE_NOW
- WMTX-EUR — ACTIVE_NOW — score mémoire 9.914/10 — sources ACCELERATION, V4 — WATCH_ONLY
- NMR-EUR — MEMORY_24H — score mémoire 9.777/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- BTT-EUR — MEMORY_24H — score mémoire 9.434/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- ZRC-EUR — MEMORY_24H — score mémoire 8.779/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- FUEL-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- XMN-EUR — MEMORY_24H — score mémoire 8.447/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- FRAX-EUR — MEMORY_DECAY_24_72H — score mémoire 8.346/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- SAGA-EUR — ACTIVE_NOW — score mémoire 8.221/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY

## Audit des plus fortes hausses

- QNT-EUR +42.14% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- HBAR-EUR +23.90% — DETECTED_EARLY — couche NONE — action NONE
- NMR-EUR +15.38% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- GRT-EUR +14.59% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- IKA-EUR +13.42% — DETECTED_TOO_LATE — couche NONE — action INTERPRETATION
- AUDIO-EUR +12.18% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- SOON-EUR +12.12% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ALGO-EUR +12.04% — DETECTED_EARLY — couche NONE — action NONE
- PUMP-EUR +11.11% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- SEI-EUR +7.63% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
