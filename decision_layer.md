# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-20T20:24:29.896402+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : JUP-EUR | action ACHETE_MAINTENANT | opportunité 8.635 | entrée 6.950 | trend 8.450 | rang 8.012
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : SUPER-EUR | action PLACE_LIMITE_PASSIVE | opportunité 7.961 | entrée 5.850 | trend 8.400 | rang 7.476
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : SIGN-EUR | action LATENT_ACCELERATOR | opportunité 7.486 | entrée 4.500 | trend 8.950 | rang 7.424
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : MERL-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 9.280 | entrée 6.850 | trend 8.700 | rang 8.428
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. MERL-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.428
2. CAKE-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.142
3. COW-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.109

## Accélération indépendante

- NOS-EUR — CONFIRMED_ACCELERATION — score 8.445/10 — DETECTED_BUT_TOO_LATE
- MEGA-EUR — CONFIRMED_ACCELERATION — score 7.345/10 — DETECTED_BUT_TOO_LATE
- QUID-EUR — CONFIRMED_ACCELERATION — score 6.877/10 — DETECTED_BUT_TOO_LATE
- ZAMA-EUR — CONFIRMED_ACCELERATION — score 6.570/10 — DETECTED_BUT_TOO_LATE
- PUMP-EUR — BUILDING_ACCELERATION — score 5.402/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- NIL-EUR — BUILDING_ACCELERATION — score 5.140/10 — DETECTED_BUT_TOO_LATE
- EDEN-EUR — BUILDING_ACCELERATION — score 4.990/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- ARPA-EUR — BUILDING_ACCELERATION — score 4.970/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- MET-EUR — BUILDING_ACCELERATION — score 4.905/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- PUMP-EUR — ACTIVE_NOW — score mémoire 6.946/10 — sources ACCELERATION, DECISION_LAYER, V4 — BUYABLE_NOW
- NES-EUR — MEMORY_24H — score mémoire 8.883/10 — sources ACCELERATION — MEMORY_ONLY
- PTB-EUR — MEMORY_24H — score mémoire 8.518/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- NOS-EUR — ACTIVE_NOW — score mémoire 8.445/10 — sources ACCELERATION, V4 — DETECTED_BUT_TOO_LATE
- MERL-EUR — ACTIVE_NOW — score mémoire 8.428/10 — sources DECISION_LAYER, V4 — WATCH_ONLY
- FTT-EUR — MEMORY_24H — score mémoire 8.388/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- CAKE-EUR — ACTIVE_NOW — score mémoire 8.142/10 — sources DECISION_LAYER, V4 — WATCH_ONLY
- COW-EUR — ACTIVE_NOW — score mémoire 8.109/10 — sources DECISION_LAYER, V4 — WATCH_ONLY
- STX-EUR — ACTIVE_NOW — score mémoire 8.103/10 — sources DECISION_LAYER, V4 — WATCH_ONLY
- PHA-EUR — ACTIVE_NOW — score mémoire 8.062/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE

## Audit des plus fortes hausses

- SAGA-EUR +58.73% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- FTT-EUR +40.03% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- PTB-EUR +29.53% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- S-EUR +25.43% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- NIL-EUR +23.14% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- CELR-EUR +22.68% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- STRK-EUR +17.72% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- AVAX-EUR +16.94% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- NEAR-EUR +16.37% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- KMNO-EUR +16.27% — DETECTED_EARLY — couche NONE — action INTERPRETATION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
