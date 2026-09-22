# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-22T06:24:16.506343+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : TAIKO-EUR | action ACHETE_MAINTENANT | opportunité 7.877 | entrée 6.900 | trend 8.700 | rang 7.814
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : SSV-EUR | action PLACE_LIMITE_PASSIVE | opportunité 7.417 | entrée 6.200 | trend 8.400 | rang 7.420
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : BAT-EUR | action LATENT_ACCELERATOR | opportunité 7.461 | entrée 5.650 | trend 8.150 | rang 7.284
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : SOL-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.174 | entrée 6.700 | trend 8.750 | rang 7.932
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. SOL-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.932
2. THE-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.883
3. INIT-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.816

## Accélération indépendante

- SAGA-EUR — CONFIRMED_ACCELERATION — score 9.632/10 — DETECTED_BUT_TOO_LATE
- ZRC-EUR — CONFIRMED_ACCELERATION — score 8.500/10 — DETECTED_BUT_TOO_LATE
- BTT-EUR — CONFIRMED_ACCELERATION — score 8.098/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- AVA-EUR — CONFIRMED_ACCELERATION — score 6.691/10 — DETECTED_BUT_TOO_LATE
- ICX-EUR — BUILDING_ACCELERATION — score 6.417/10 — DETECTED_BUT_TOO_LATE
- COTI-EUR — BUILDING_ACCELERATION — score 5.027/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- AGI-EUR — BUILDING_ACCELERATION — score 4.970/10 — DETECTED_BUT_TOO_LATE
- MLN-EUR — BUILDING_ACCELERATION — score 4.951/10 — DETECTED_BUT_TOO_LATE
- FTT-EUR — BUILDING_ACCELERATION — score 4.950/10 — DETECTED_BUT_TOO_LATE
- NIL-EUR — BUILDING_ACCELERATION — score 4.886/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- SAGA-EUR — ACTIVE_NOW — score mémoire 9.632/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- PHA-EUR — MEMORY_24H — score mémoire 9.177/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- GIGA-EUR — MEMORY_24H — score mémoire 9.062/10 — sources ACCELERATION — MEMORY_ONLY
- SWEAT-EUR — MEMORY_24H — score mémoire 9.062/10 — sources ACCELERATION — MEMORY_ONLY
- VELO-EUR — MEMORY_24H — score mémoire 9.000/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- ZEUS-EUR — MEMORY_24H — score mémoire 8.781/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- MEW-EUR — MEMORY_24H — score mémoire 8.523/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- ZRC-EUR — ACTIVE_NOW — score mémoire 8.500/10 — sources ACCELERATION — DETECTED_BUT_TOO_LATE
- XMN-EUR — MEMORY_24H — score mémoire 8.438/10 — sources ACCELERATION — MEMORY_ONLY
- BTT-EUR — ACTIVE_NOW — score mémoire 8.098/10 — sources ACCELERATION — WATCH_ONLY

## Audit des plus fortes hausses

- ZRC-EUR +110.07% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ICX-EUR +101.80% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- AIOZ-EUR +54.04% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- KERNEL-EUR +31.81% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- SAGA-EUR +26.99% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- PEPE-EUR +26.86% — DETECTED_EARLY — couche NONE — action NONE
- BONK-EUR +20.91% — DETECTED_TOO_LATE — couche NONE — action INTERPRETATION
- WIF-EUR +20.20% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- FORM-EUR +20.01% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- GRASS-EUR +19.76% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
