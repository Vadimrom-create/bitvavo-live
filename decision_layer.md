# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-21T03:42:57.795789+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : KAS-EUR | action ACHETE_MAINTENANT | opportunité 9.010 | entrée 7.050 | trend 8.700 | rang 8.341
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : PORTAL-EUR | action PLACE_LIMITE_PASSIVE | opportunité 7.701 | entrée 6.650 | trend 8.000 | rang 7.332
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : PENDLE-EUR | action LATENT_ACCELERATOR | opportunité 8.097 | entrée 5.650 | trend 8.650 | rang 7.567
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : MERL-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.289 | entrée 6.950 | trend 8.900 | rang 7.962
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. KAS-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.341
2. MERL-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.962
3. GRT-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.934

## Accélération indépendante

- USELESS-EUR — CONFIRMED_ACCELERATION — score 8.481/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- ZK-EUR — CONFIRMED_ACCELERATION — score 7.929/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- BICO-EUR — BUILDING_ACCELERATION — score 5.862/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- CRO-EUR — BUILDING_ACCELERATION — score 5.704/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- EGLD-EUR — BUILDING_ACCELERATION — score 5.695/10 — DETECTED_BUT_TOO_LATE
- WIN-EUR — BUILDING_ACCELERATION — score 5.533/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- XAI-EUR — BUILDING_ACCELERATION — score 5.480/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- SCR-EUR — BUILDING_ACCELERATION — score 5.361/10 — DETECTED_BUT_TOO_LATE
- VANA-EUR — BUILDING_ACCELERATION — score 5.295/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- CELO-EUR — BUILDING_ACCELERATION — score 5.019/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- FTT-EUR — MEMORY_24H — score mémoire 10.000/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- ZETA-EUR — MEMORY_24H — score mémoire 10.000/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- ICX-EUR — MEMORY_24H — score mémoire 9.062/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- NES-EUR — MEMORY_24H — score mémoire 8.883/10 — sources ACCELERATION — MEMORY_ONLY
- BOME-EUR — MEMORY_24H — score mémoire 8.655/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- LSK-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- USELESS-EUR — ACTIVE_NOW — score mémoire 8.481/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- U-EUR — MEMORY_24H — score mémoire 8.376/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- KAS-EUR — ACTIVE_NOW — score mémoire 8.341/10 — sources DECISION_LAYER, V4 — WATCH_ONLY
- UP-EUR — MEMORY_24H — score mémoire 8.113/10 — sources ACCELERATION — MEMORY_ONLY

## Audit des plus fortes hausses

- PTB-EUR +90.83% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- SAGA-EUR +36.55% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- FTT-EUR +36.53% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- NIL-EUR +27.03% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- KMNO-EUR +25.27% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- NEAR-EUR +23.24% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- VVV-EUR +22.35% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- EPIC-EUR +21.08% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- TREAD-EUR +19.57% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- PEAQ-EUR +18.74% — DETECTED_EARLY — couche NONE — action INTERPRETATION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
