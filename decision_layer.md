# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-22T16:22:16.725708+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : AVNT-EUR | action ACHETE_MAINTENANT | opportunité 8.593 | entrée 7.000 | trend 7.350 | rang 7.524
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : BREV-EUR | action PLACE_LIMITE_PASSIVE | opportunité 7.701 | entrée 6.000 | trend 8.450 | rang 7.476
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : ZIL-EUR | action LATENT_ACCELERATOR | opportunité 7.599 | entrée 5.650 | trend 8.100 | rang 7.029
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : THE-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.600 | entrée 6.700 | trend 8.700 | rang 8.034
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. THE-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.034
2. FLUX-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.002
3. MERL-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.768

## Accélération indépendante

- CHR-EUR — CONFIRMED_ACCELERATION — score 10.000/10 — DETECTED_BUT_TOO_LATE
- MAGIC-EUR — CONFIRMED_ACCELERATION — score 8.394/10 — DETECTED_BUT_TOO_LATE
- SHELL-EUR — CONFIRMED_ACCELERATION — score 8.203/10 — DETECTED_BUT_TOO_LATE
- ZRO-EUR — CONFIRMED_ACCELERATION — score 7.663/10 — DETECTED_BUT_TOO_LATE
- ALICE-EUR — CONFIRMED_ACCELERATION — score 7.402/10 — DETECTED_BUT_TOO_LATE
- ACX-EUR — CONFIRMED_ACCELERATION — score 6.948/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- BEL-EUR — CONFIRMED_ACCELERATION — score 6.789/10 — DETECTED_BUT_TOO_LATE
- BAND-EUR — CONFIRMED_ACCELERATION — score 6.680/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- BTT-EUR — BUILDING_ACCELERATION — score 5.443/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- CHR-EUR — ACTIVE_NOW — score mémoire 10.000/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- MLN-EUR — MEMORY_24H — score mémoire 9.132/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- DEGEN-EUR — MEMORY_24H — score mémoire 8.739/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- AUDIO-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION — MEMORY_ONLY
- U-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- MAGIC-EUR — ACTIVE_NOW — score mémoire 8.394/10 — sources ACCELERATION, V4 — DETECTED_BUT_TOO_LATE
- SHELL-EUR — ACTIVE_NOW — score mémoire 8.203/10 — sources ACCELERATION, V4 — DETECTED_BUT_TOO_LATE
- THE-EUR — ACTIVE_NOW — score mémoire 8.034/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- FLUX-EUR — ACTIVE_NOW — score mémoire 8.002/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- PEAQ-EUR — MEMORY_24H — score mémoire 7.834/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY

## Audit des plus fortes hausses

- CHR-EUR +46.14% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- NIL-EUR +26.65% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- FLOCK-EUR +24.80% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- BCH-EUR +22.29% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- KERNEL-EUR +20.28% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- TREAD-EUR +15.53% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- KITE-EUR +15.35% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- GRASS-EUR +14.08% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- ZRO-EUR +11.62% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- AVA-EUR +11.24% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
