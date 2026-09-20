# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-20T23:32:03.166236+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : NPC-EUR | action ACHETE_MAINTENANT | opportunité 9.088 | entrée 7.400 | trend 8.250 | rang 8.145
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : SUPER-EUR | action PLACE_LIMITE_PASSIVE | opportunité 7.706 | entrée 6.100 | trend 8.650 | rang 7.590
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : JTO-EUR | action LATENT_ACCELERATOR | opportunité 8.984 | entrée 5.450 | trend 7.300 | rang 7.535
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : COW-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 9.397 | entrée 6.900 | trend 9.000 | rang 8.558
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. COW-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.558
2. NPC-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.145
3. CAKE-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.973

## Accélération indépendante

- U-EUR — CONFIRMED_ACCELERATION — score 8.376/10 — DETECTED_BUT_TOO_LATE
- TAI-EUR — CONFIRMED_ACCELERATION — score 6.862/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- EDGE-EUR — BUILDING_ACCELERATION — score 6.138/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- TAIKO-EUR — BUILDING_ACCELERATION — score 5.651/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- BCH-EUR — BUILDING_ACCELERATION — score 5.610/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- A-EUR — BUILDING_ACCELERATION — score 4.936/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- NPC-EUR — ACTIVE_NOW — score mémoire 8.145/10 — sources ACCELERATION, DECISION_LAYER, V4 — BUYABLE_NOW
- JUP-EUR — ACTIVE_NOW — score mémoire 7.442/10 — sources ACCELERATION, DECISION_LAYER, V4 — BUYABLE_NOW
- ICX-EUR — MEMORY_24H — score mémoire 9.062/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- NES-EUR — MEMORY_24H — score mémoire 8.883/10 — sources ACCELERATION — MEMORY_ONLY
- COW-EUR — ACTIVE_NOW — score mémoire 8.558/10 — sources DECISION_LAYER, V4 — WATCH_ONLY
- NOS-EUR — MEMORY_24H — score mémoire 8.445/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- U-EUR — ACTIVE_NOW — score mémoire 8.376/10 — sources ACCELERATION, V4 — DETECTED_BUT_TOO_LATE
- FTT-EUR — MEMORY_24H — score mémoire 8.294/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- UP-EUR — MEMORY_24H — score mémoire 8.113/10 — sources ACCELERATION — MEMORY_ONLY
- S-EUR — MEMORY_24H — score mémoire 8.013/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY

## Audit des plus fortes hausses

- SAGA-EUR +48.52% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- PTB-EUR +36.07% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- FTT-EUR +28.68% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- NIL-EUR +24.35% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- EPIC-EUR +20.27% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- KMNO-EUR +19.81% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- LUNA2-EUR +19.46% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- S-EUR +17.05% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- CFG-EUR +16.14% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- NEAR-EUR +15.08% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
