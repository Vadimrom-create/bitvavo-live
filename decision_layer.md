# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-21T00:49:44.526560+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : PYTH-EUR | action ACHETE_MAINTENANT | opportunité 9.318 | entrée 7.500 | trend 8.500 | rang 8.333
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : PROVE-EUR | action PLACE_LIMITE_PASSIVE | opportunité 8.187 | entrée 6.100 | trend 8.350 | rang 7.608
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : ZK-EUR | action LATENT_ACCELERATOR | opportunité 8.015 | entrée 5.750 | trend 8.400 | rang 7.628
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : WAL-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.838 | entrée 5.850 | trend 9.200 | rang 8.191
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. PYTH-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.333
2. HYPE-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.240
3. WAL-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.191

## Accélération indépendante

- PUFFER-EUR — CONFIRMED_ACCELERATION — score 8.500/10 — DETECTED_BUT_TOO_LATE
- ACX-EUR — CONFIRMED_ACCELERATION — score 7.062/10 — DETECTED_BUT_TOO_LATE
- NOS-EUR — CONFIRMED_ACCELERATION — score 6.907/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- FARTCOIN-EUR — CONFIRMED_ACCELERATION — score 6.549/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- VELO-EUR — BUILDING_ACCELERATION — score 5.847/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- MOVE-EUR — BUILDING_ACCELERATION — score 5.401/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- KERNEL-EUR — BUILDING_ACCELERATION — score 5.367/10 — DETECTED_BUT_TOO_LATE
- IRYS-EUR — BUILDING_ACCELERATION — score 5.323/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- TRAC-EUR — BUILDING_ACCELERATION — score 4.806/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- PUMP-EUR — BUILDING_ACCELERATION — score 4.765/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- AERO-EUR — ACTIVE_NOW — score mémoire 7.684/10 — sources DECISION_LAYER, V4 — BUYABLE_NOW
- ICX-EUR — MEMORY_24H — score mémoire 9.062/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- NES-EUR — MEMORY_24H — score mémoire 8.883/10 — sources ACCELERATION — MEMORY_ONLY
- PUFFER-EUR — ACTIVE_NOW — score mémoire 8.500/10 — sources ACCELERATION, V4 — DETECTED_BUT_TOO_LATE
- U-EUR — MEMORY_24H — score mémoire 8.376/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- PYTH-EUR — ACTIVE_NOW — score mémoire 8.333/10 — sources DECISION_LAYER, V4 — WATCH_ONLY
- HYPE-EUR — ACTIVE_NOW — score mémoire 8.240/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- WAL-EUR — ACTIVE_NOW — score mémoire 8.191/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- UP-EUR — MEMORY_24H — score mémoire 8.113/10 — sources ACCELERATION — MEMORY_ONLY
- VET-EUR — ACTIVE_NOW — score mémoire 7.943/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY

## Audit des plus fortes hausses

- SAGA-EUR +50.68% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- PTB-EUR +33.19% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- FTT-EUR +29.55% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- EPIC-EUR +27.43% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- NIL-EUR +24.30% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- NEAR-EUR +20.99% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- S-EUR +20.01% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- CFG-EUR +19.55% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- KMNO-EUR +19.38% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- LUNA2-EUR +14.36% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
