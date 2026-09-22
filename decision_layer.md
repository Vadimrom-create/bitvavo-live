# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-22T11:12:17.141603+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : QNT-EUR | action ACHETE_MAINTENANT | opportunité 7.561 | entrée 7.550 | trend 5.650 | rang 6.485
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : SOL-EUR | action PLACE_LIMITE_PASSIVE | opportunité 7.623 | entrée 6.450 | trend 8.450 | rang 7.562
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : AVNT-EUR | action LATENT_ACCELERATOR | opportunité 8.993 | entrée 5.200 | trend 7.350 | rang 7.467
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : COW-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.265 | entrée 6.400 | trend 8.700 | rang 7.920
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. COW-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.920
2. NEAR-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.893
3. TAIKO-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.838

## Accélération indépendante

- HFT-EUR — CONFIRMED_ACCELERATION — score 8.783/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- TREAD-EUR — CONFIRMED_ACCELERATION — score 7.642/10 — DETECTED_BUT_TOO_LATE
- FLOCK-EUR — CONFIRMED_ACCELERATION — score 7.561/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- HOT-EUR — CONFIRMED_ACCELERATION — score 7.500/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- NOS-EUR — BUILDING_ACCELERATION — score 6.163/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- BTT-EUR — BUILDING_ACCELERATION — score 6.145/10 — DETECTED_BUT_TOO_LATE
- WIN-EUR — BUILDING_ACCELERATION — score 5.856/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- SWELL-EUR — BUILDING_ACCELERATION — score 5.191/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- SWEAT-EUR — MEMORY_24H — score mémoire 9.062/10 — sources ACCELERATION — MEMORY_ONLY
- HFT-EUR — ACTIVE_NOW — score mémoire 8.783/10 — sources ACCELERATION — WATCH_ONLY
- GIGA-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION — MEMORY_ONLY
- U-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- AVA-EUR — MEMORY_24H — score mémoire 8.261/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- COW-EUR — ACTIVE_NOW — score mémoire 7.920/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- NEAR-EUR — ACTIVE_NOW — score mémoire 7.893/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- TAIKO-EUR — ACTIVE_NOW — score mémoire 7.838/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- HYPE-EUR — ACTIVE_NOW — score mémoire 7.682/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- TREAD-EUR — ACTIVE_NOW — score mémoire 7.642/10 — sources ACCELERATION, V4 — DETECTED_BUT_TOO_LATE

## Audit des plus fortes hausses

- ICX-EUR +98.56% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- ZRC-EUR +84.03% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- AIOZ-EUR +35.78% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- KERNEL-EUR +25.78% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- NIL-EUR +23.40% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- FORM-EUR +22.76% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- U-EUR +20.70% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- TREAD-EUR +19.41% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- GRASS-EUR +19.18% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- PEPE-EUR +17.79% — DETECTED_EARLY — couche NONE — action NONE

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
