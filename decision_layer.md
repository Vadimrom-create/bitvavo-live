# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-21T03:23:31.455269+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : TAO-EUR | action ACHETE_MAINTENANT | opportunité 7.821 | entrée 7.250 | trend 7.950 | rang 7.471
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : XTZ-EUR | action PLACE_LIMITE_PASSIVE | opportunité 7.479 | entrée 6.300 | trend 8.050 | rang 7.330
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : DEEP-EUR | action LATENT_ACCELERATOR | opportunité 7.895 | entrée 5.300 | trend 8.950 | rang 7.567
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : GRT-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 9.071 | entrée 6.250 | trend 8.700 | rang 7.991
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. GRT-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.991
2. MERL-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.944
3. STX-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.793

## Accélération indépendante

- ZETA-EUR — CONFIRMED_ACCELERATION — score 10.000/10 — DETECTED_BUT_TOO_LATE
- BOME-EUR — CONFIRMED_ACCELERATION — score 8.655/10 — DETECTED_BUT_TOO_LATE
- G-EUR — CONFIRMED_ACCELERATION — score 7.835/10 — DETECTED_BUT_TOO_LATE
- ZAMA-EUR — CONFIRMED_ACCELERATION — score 7.213/10 — DETECTED_BUT_TOO_LATE
- NEAR-EUR — BUILDING_ACCELERATION — score 6.074/10 — DETECTED_BUT_TOO_LATE
- VIRTUAL-EUR — BUILDING_ACCELERATION — score 6.027/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- SOMI-EUR — BUILDING_ACCELERATION — score 5.940/10 — DETECTED_BUT_TOO_LATE
- JUP-EUR — BUILDING_ACCELERATION — score 5.527/10 — DETECTED_BUT_TOO_LATE
- DOGS-EUR — BUILDING_ACCELERATION — score 5.517/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- POPCAT-EUR — BUILDING_ACCELERATION — score 5.515/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- FET-EUR — ACTIVE_NOW — score mémoire 6.668/10 — sources ACCELERATION, DECISION_LAYER, V4 — BUYABLE_NOW
- FTT-EUR — MEMORY_24H — score mémoire 10.000/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- ZETA-EUR — ACTIVE_NOW — score mémoire 10.000/10 — sources ACCELERATION, V4 — DETECTED_BUT_TOO_LATE
- ICX-EUR — MEMORY_24H — score mémoire 9.062/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- NES-EUR — MEMORY_24H — score mémoire 8.883/10 — sources ACCELERATION — MEMORY_ONLY
- BOME-EUR — ACTIVE_NOW — score mémoire 8.655/10 — sources ACCELERATION, V4 — DETECTED_BUT_TOO_LATE
- LSK-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- U-EUR — MEMORY_24H — score mémoire 8.376/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- UP-EUR — MEMORY_24H — score mémoire 8.113/10 — sources ACCELERATION — MEMORY_ONLY
- GRT-EUR — ACTIVE_NOW — score mémoire 7.991/10 — sources DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE

## Audit des plus fortes hausses

- PTB-EUR +89.15% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- FTT-EUR +40.44% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- SAGA-EUR +40.26% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- NIL-EUR +26.61% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- VVV-EUR +23.96% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- NEAR-EUR +22.08% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- KMNO-EUR +21.23% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- EPIC-EUR +20.49% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- TREAD-EUR +19.30% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- S-EUR +16.93% — DETECTED_EARLY — couche NONE — action INTERPRETATION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
