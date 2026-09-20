# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-20T23:24:21.369505+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : NPC-EUR | action ACHETE_MAINTENANT | opportunité 8.540 | entrée 7.400 | trend 8.250 | rang 7.945
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : SUPER-EUR | action PLACE_LIMITE_PASSIVE | opportunité 7.706 | entrée 6.100 | trend 8.650 | rang 7.585
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : GRT-EUR | action LATENT_ACCELERATOR | opportunité 7.654 | entrée 5.400 | trend 8.450 | rang 7.373
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : COW-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.571 | entrée 6.700 | trend 9.000 | rang 8.142
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. COW-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.142
2. CAKE-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.964
3. NPC-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 7.945

## Accélération indépendante

- LUNA2-EUR — CONFIRMED_ACCELERATION — score 8.476/10 — DETECTED_BUT_TOO_LATE
- DRIFT-EUR — CONFIRMED_ACCELERATION — score 7.962/10 — DETECTED_BUT_TOO_LATE
- TAI-EUR — CONFIRMED_ACCELERATION — score 7.712/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- AGI-EUR — CONFIRMED_ACCELERATION — score 6.894/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- C-EUR — CONFIRMED_ACCELERATION — score 6.833/10 — DETECTED_BUT_TOO_LATE
- EDGE-EUR — CONFIRMED_ACCELERATION — score 6.510/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- PTB-EUR — BUILDING_ACCELERATION — score 5.927/10 — DETECTED_BUT_TOO_LATE
- CFG-EUR — BUILDING_ACCELERATION — score 5.803/10 — DETECTED_BUT_TOO_LATE
- ARB-EUR — BUILDING_ACCELERATION — score 5.440/10 — DETECTED_BUT_TOO_LATE
- OSMO-EUR — BUILDING_ACCELERATION — score 4.937/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- NPC-EUR — ACTIVE_NOW — score mémoire 7.945/10 — sources ACCELERATION, DECISION_LAYER, V4 — BUYABLE_NOW
- JUP-EUR — ACTIVE_NOW — score mémoire 7.643/10 — sources ACCELERATION, DECISION_LAYER, V4 — BUYABLE_NOW
- ICX-EUR — MEMORY_24H — score mémoire 9.062/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- NES-EUR — MEMORY_24H — score mémoire 8.883/10 — sources ACCELERATION — MEMORY_ONLY
- LUNA2-EUR — ACTIVE_NOW — score mémoire 8.476/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- NOS-EUR — MEMORY_24H — score mémoire 8.445/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- FTT-EUR — MEMORY_24H — score mémoire 8.294/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- COW-EUR — ACTIVE_NOW — score mémoire 8.142/10 — sources DECISION_LAYER, V4 — WATCH_ONLY
- UP-EUR — MEMORY_24H — score mémoire 8.113/10 — sources ACCELERATION — MEMORY_ONLY
- S-EUR — MEMORY_24H — score mémoire 8.013/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY

## Audit des plus fortes hausses

- SAGA-EUR +50.24% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- PTB-EUR +35.81% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- FTT-EUR +30.03% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- NIL-EUR +23.01% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- LUNA2-EUR +20.78% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- EPIC-EUR +20.60% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- KMNO-EUR +20.10% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- S-EUR +17.65% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- NEAR-EUR +15.56% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- AVAX-EUR +15.48% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
