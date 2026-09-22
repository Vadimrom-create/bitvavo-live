# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-22T10:54:21.307369+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : QNT-EUR | action ACHETE_MAINTENANT | opportunité 8.489 | entrée 7.550 | trend 5.650 | rang 6.886
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : TAIKO-EUR | action PLACE_LIMITE_PASSIVE | opportunité 7.633 | entrée 6.250 | trend 8.700 | rang 7.633
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : BAT-EUR | action LATENT_ACCELERATOR | opportunité 7.779 | entrée 5.350 | trend 7.950 | rang 7.322
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : COW-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 7.948 | entrée 6.400 | trend 8.700 | rang 7.758
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. COW-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.758
2. TAIKO-EUR — MEILLEURE_LIMITE_PASSIVE — PLACE_LIMITE_PASSIVE — rank 7.633
3. SOL-EUR — MEILLEURE_LIMITE_PASSIVE — PLACE_LIMITE_PASSIVE — rank 7.607

## Accélération indépendante

- U-EUR — CONFIRMED_ACCELERATION — score 8.500/10 — DETECTED_BUT_TOO_LATE
- AVA-EUR — CONFIRMED_ACCELERATION — score 8.261/10 — DETECTED_BUT_TOO_LATE
- WIF-EUR — CONFIRMED_ACCELERATION — score 7.519/10 — DETECTED_BUT_TOO_LATE
- ZAMA-EUR — CONFIRMED_ACCELERATION — score 7.299/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- XMN-EUR — CONFIRMED_ACCELERATION — score 6.662/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- HUMA-EUR — BUILDING_ACCELERATION — score 6.037/10 — DETECTED_BUT_TOO_LATE
- TREAD-EUR — BUILDING_ACCELERATION — score 6.006/10 — DETECTED_BUT_TOO_LATE
- PUNDIX-EUR — BUILDING_ACCELERATION — score 5.559/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- FORM-EUR — BUILDING_ACCELERATION — score 5.031/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- SWEAT-EUR — MEMORY_24H — score mémoire 9.062/10 — sources ACCELERATION — MEMORY_ONLY
- GIGA-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION — MEMORY_ONLY
- U-EUR — ACTIVE_NOW — score mémoire 8.500/10 — sources ACCELERATION, V4 — DETECTED_BUT_TOO_LATE
- AVA-EUR — ACTIVE_NOW — score mémoire 8.261/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- PONKE-EUR — MEMORY_24H — score mémoire 8.130/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- COW-EUR — ACTIVE_NOW — score mémoire 7.758/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- TAIKO-EUR — ACTIVE_NOW — score mémoire 7.633/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- SOL-EUR — ACTIVE_NOW — score mémoire 7.607/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- NEAR-EUR — ACTIVE_NOW — score mémoire 7.554/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- INIT-EUR — ACTIVE_NOW — score mémoire 7.531/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY

## Audit des plus fortes hausses

- ICX-EUR +103.11% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- ZRC-EUR +87.19% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- AIOZ-EUR +36.96% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- U-EUR +34.83% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- KERNEL-EUR +30.89% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- FORM-EUR +24.28% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- WIF-EUR +21.08% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- GRASS-EUR +19.15% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- NIL-EUR +19.06% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- PEPE-EUR +17.81% — DETECTED_EARLY — couche NONE — action NONE

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
