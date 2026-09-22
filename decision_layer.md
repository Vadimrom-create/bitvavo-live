# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-22T21:54:12.982847+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : QNT-EUR | action ACHETE_MAINTENANT | opportunité 8.667 | entrée 7.400 | trend 7.100 | rang 7.478
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : 0G-EUR | action PLACE_LIMITE_PASSIVE | opportunité 7.697 | entrée 6.450 | trend 8.600 | rang 7.624
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : RUNE-EUR | action LATENT_ACCELERATOR | opportunité 8.511 | entrée 5.600 | trend 8.850 | rang 7.773
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : NEO-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 9.154 | entrée 6.550 | trend 8.200 | rang 8.146
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. NEO-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.146
2. SOL-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.940
3. SUPER-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.921

## Accélération indépendante

- HNT-EUR — CONFIRMED_ACCELERATION — score 9.544/10 — DETECTED_BUT_TOO_LATE
- KERNEL-EUR — CONFIRMED_ACCELERATION — score 9.430/10 — DETECTED_BUT_TOO_LATE
- NES-EUR — CONFIRMED_ACCELERATION — score 8.853/10 — DETECTED_BUT_TOO_LATE
- PONKE-EUR — CONFIRMED_ACCELERATION — score 6.698/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- ADX-EUR — CONFIRMED_ACCELERATION — score 6.666/10 — DETECTED_BUT_TOO_LATE
- NEO-EUR — BUILDING_ACCELERATION — score 5.541/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- COTI-EUR — BUILDING_ACCELERATION — score 5.221/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- MLN-EUR — BUILDING_ACCELERATION — score 5.147/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- WCT-EUR — BUILDING_ACCELERATION — score 4.972/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- AXS-EUR — BUILDING_ACCELERATION — score 4.852/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- QNT-EUR — ACTIVE_NOW — score mémoire 7.478/10 — sources ACCELERATION, DECISION_LAYER, V4 — BUYABLE_NOW
- HNT-EUR — ACTIVE_NOW — score mémoire 9.544/10 — sources ACCELERATION, V4 — DETECTED_BUT_TOO_LATE
- TREAD-EUR — MEMORY_24H — score mémoire 9.440/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- KERNEL-EUR — ACTIVE_NOW — score mémoire 9.430/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- NES-EUR — ACTIVE_NOW — score mémoire 8.853/10 — sources ACCELERATION, V4 — DETECTED_BUT_TOO_LATE
- LUNA2-EUR — MEMORY_24H — score mémoire 8.762/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- DEGEN-EUR — MEMORY_24H — score mémoire 8.739/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- AUDIO-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION — MEMORY_ONLY
- LAPTOP-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- NEO-EUR — ACTIVE_NOW — score mémoire 8.146/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY

## Audit des plus fortes hausses

- DRIFT-EUR +35.94% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- BCH-EUR +27.55% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- CHR-EUR +27.53% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- KERNEL-EUR +27.49% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- USELESS-EUR +23.04% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- FLOCK-EUR +17.68% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- NIL-EUR +17.52% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- KITE-EUR +17.49% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- PENGU-EUR +15.14% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ZRO-EUR +14.96% — DETECTED_EARLY — couche NONE — action INTERPRETATION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
