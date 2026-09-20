# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-20T23:46:19.661678+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : HBAR-EUR | action ACHETE_MAINTENANT | opportunité 8.839 | entrée 7.000 | trend 7.800 | rang 7.861
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : IOST-EUR | action PLACE_LIMITE_PASSIVE | opportunité 8.466 | entrée 6.000 | trend 7.850 | rang 7.642
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : LUNA2-EUR | action LATENT_ACCELERATOR | opportunité 7.509 | entrée 4.650 | trend 7.850 | rang 6.062
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : CAKE-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.410 | entrée 7.550 | trend 8.950 | rang 8.156
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. CAKE-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.156
2. COW-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.081
3. PHA-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.972

## Accélération indépendante

- KMNO-EUR — CONFIRMED_ACCELERATION — score 7.078/10 — DETECTED_BUT_TOO_LATE
- JUP-EUR — BUILDING_ACCELERATION — score 5.693/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- VVV-EUR — BUILDING_ACCELERATION — score 5.592/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- NPC-EUR — ACTIVE_NOW — score mémoire 7.617/10 — sources ACCELERATION, DECISION_LAYER, V4 — BUYABLE_NOW
- JUP-EUR — ACTIVE_NOW — score mémoire 7.541/10 — sources ACCELERATION, DECISION_LAYER, V4 — BUYABLE_NOW
- POL-EUR — ACTIVE_NOW — score mémoire 7.295/10 — sources ACCELERATION, DECISION_LAYER, V4 — BUYABLE_NOW
- ICX-EUR — MEMORY_24H — score mémoire 9.062/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- NES-EUR — MEMORY_24H — score mémoire 8.883/10 — sources ACCELERATION — MEMORY_ONLY
- NOS-EUR — MEMORY_24H — score mémoire 8.445/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- U-EUR — MEMORY_24H — score mémoire 8.376/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- FTT-EUR — MEMORY_24H — score mémoire 8.294/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- SENT-EUR — ACTIVE_NOW — score mémoire 8.183/10 — sources DECISION_LAYER, V4 — WATCH_ONLY
- CAKE-EUR — ACTIVE_NOW — score mémoire 8.156/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY

## Audit des plus fortes hausses

- SAGA-EUR +48.72% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- FTT-EUR +34.77% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- PTB-EUR +30.36% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- NIL-EUR +24.15% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- KMNO-EUR +22.61% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- EPIC-EUR +21.47% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- LUNA2-EUR +20.22% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- S-EUR +18.48% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- NEAR-EUR +16.92% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- CFG-EUR +15.32% — DETECTED_EARLY — couche NONE — action INTERPRETATION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
