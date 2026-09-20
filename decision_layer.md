# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-20T16:50:13.594690+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : SOL-EUR | action ACHETE_MAINTENANT | opportunité 9.168 | entrée 7.850 | trend 7.700 | rang 8.015
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : ALGO-EUR | action PLACE_LIMITE_PASSIVE | opportunité 7.598 | entrée 6.750 | trend 8.200 | rang 6.874
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : HBAR-EUR | action LATENT_ACCELERATOR | opportunité 7.678 | entrée 4.500 | trend 7.800 | rang 6.902
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : INJ-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.034 | entrée 6.350 | trend 8.300 | rang 7.295
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. SOL-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.015
2. HYPE-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 7.816
3. ONDO-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 7.361

## Accélération indépendante

- SUI-EUR — CONFIRMED_ACCELERATION — score 9.126/10 — DETECTED_BUT_TOO_LATE
- ADA-EUR — CONFIRMED_ACCELERATION — score 6.576/10 — REQUIRES_V4_ENTRY_AND_EXECUTION_VALIDATION
- VET-EUR — BUILDING_ACCELERATION — score 6.152/10 — REQUIRES_V4_ENTRY_AND_EXECUTION_VALIDATION
- FET-EUR — BUILDING_ACCELERATION — score 5.844/10 — REQUIRES_V4_ENTRY_AND_EXECUTION_VALIDATION
- C-EUR — BUILDING_ACCELERATION — score 5.744/10 — DETECTED_BUT_TOO_LATE
- G-EUR — BUILDING_ACCELERATION — score 5.102/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- ONDO-EUR — ACTIVE_NOW — score mémoire 7.361/10 — sources ACCELERATION, DECISION_LAYER, V4 — BUYABLE_NOW
- ADA-EUR — ACTIVE_NOW — score mémoire 6.998/10 — sources ACCELERATION, DECISION_LAYER, V4 — BUYABLE_NOW
- SUI-EUR — ACTIVE_NOW — score mémoire 9.126/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- STX-EUR — ACTIVE_NOW — score mémoire 8.171/10 — sources DECISION_LAYER, V4 — WATCH_ONLY
- ZIL-EUR — ACTIVE_NOW — score mémoire 8.018/10 — sources DECISION_LAYER, V4 — WATCH_ONLY
- SOL-EUR — ACTIVE_NOW — score mémoire 8.015/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- SENT-EUR — ACTIVE_NOW — score mémoire 7.987/10 — sources V4 — WATCH_ONLY
- PENDLE-EUR — ACTIVE_NOW — score mémoire 7.977/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- MERL-EUR — ACTIVE_NOW — score mémoire 7.966/10 — sources V4 — WATCH_ONLY
- PROVE-EUR — ACTIVE_NOW — score mémoire 7.943/10 — sources V4 — WATCH_ONLY

## Audit des plus fortes hausses

- CELR-EUR +48.70% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- LUNA2-EUR +26.69% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- PTB-EUR +24.51% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- EPIC-EUR +23.32% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- SAGA-EUR +21.57% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- FTT-EUR +21.17% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- NEAR-EUR +17.35% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- AVAX-EUR +16.07% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- KMNO-EUR +11.66% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- S-EUR +11.41% — DETECTED_EARLY — couche NONE — action INTERPRETATION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
