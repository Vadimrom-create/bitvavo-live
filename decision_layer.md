# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-22T11:30:09.756974+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : INIT-EUR | action PLACE_LIMITE_PASSIVE | opportunité 7.582 | entrée 6.650 | trend 8.600 | rang 7.561
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : BAT-EUR | action LATENT_ACCELERATOR | opportunité 7.739 | entrée 5.350 | trend 7.950 | rang 7.304
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : NEAR-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.666 | entrée 8.250 | trend 8.100 | rang 8.010
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. NEAR-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.010
2. AVAX-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.872
3. COW-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.848

## Accélération indépendante

- AUDIO-EUR — CONFIRMED_ACCELERATION — score 9.640/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- BTT-EUR — CONFIRMED_ACCELERATION — score 8.500/10 — DETECTED_BUT_TOO_LATE
- PONKE-EUR — CONFIRMED_ACCELERATION — score 6.922/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- MLN-EUR — CONFIRMED_ACCELERATION — score 6.706/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- ZK-EUR — BUILDING_ACCELERATION — score 6.291/10 — DETECTED_BUT_TOO_LATE
- THQ-EUR — BUILDING_ACCELERATION — score 5.317/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- WIF-EUR — BUILDING_ACCELERATION — score 4.890/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- AUDIO-EUR — ACTIVE_NOW — score mémoire 9.640/10 — sources ACCELERATION — WATCH_ONLY
- SWEAT-EUR — MEMORY_24H — score mémoire 9.062/10 — sources ACCELERATION — MEMORY_ONLY
- HFT-EUR — MEMORY_24H — score mémoire 8.783/10 — sources ACCELERATION — MEMORY_ONLY
- BTT-EUR — ACTIVE_NOW — score mémoire 8.500/10 — sources ACCELERATION — DETECTED_BUT_TOO_LATE
- GIGA-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION — MEMORY_ONLY
- U-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- NEAR-EUR — ACTIVE_NOW — score mémoire 8.010/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- AVAX-EUR — ACTIVE_NOW — score mémoire 7.872/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- COW-EUR — ACTIVE_NOW — score mémoire 7.848/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- HYPE-EUR — ACTIVE_NOW — score mémoire 7.782/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY

## Audit des plus fortes hausses

- ICX-EUR +95.90% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- ZRC-EUR +84.40% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- KERNEL-EUR +31.36% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- AIOZ-EUR +31.02% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- BTT-EUR +30.07% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- NIL-EUR +21.11% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- FORM-EUR +20.32% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- GRASS-EUR +19.67% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- PEPE-EUR +17.05% — DETECTED_EARLY — couche NONE — action NONE
- WIF-EUR +16.04% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
