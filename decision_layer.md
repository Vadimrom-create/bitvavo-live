# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-25T10:18:00.115961+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : VET-EUR | action ACHETE_MAINTENANT | opportunité 9.327 | entrée 7.250 | trend 8.400 | rang 8.403
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : MERL-EUR | action PLACE_LIMITE_PASSIVE | opportunité 7.752 | entrée 5.950 | trend 8.150 | rang 7.352
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : RED-EUR | action LATENT_ACCELERATOR | opportunité 7.790 | entrée 5.450 | trend 8.950 | rang 7.604
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : BONK-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 9.209 | entrée 7.000 | trend 8.200 | rang 8.215
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. VET-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.403
2. BONK-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.215
3. CAKE-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.953

## Accélération indépendante

- ZRC-EUR — CONFIRMED_ACCELERATION — score 8.253/10 — DETECTED_BUT_TOO_LATE
- SAGA-EUR — CONFIRMED_ACCELERATION — score 7.667/10 — DETECTED_BUT_TOO_LATE
- BTT-EUR — CONFIRMED_ACCELERATION — score 7.470/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- IRYS-EUR — CONFIRMED_ACCELERATION — score 6.857/10 — DETECTED_BUT_TOO_LATE
- ZKP-EUR — CONFIRMED_ACCELERATION — score 6.606/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- ARK-EUR — BUILDING_ACCELERATION — score 5.963/10 — DETECTED_BUT_TOO_LATE
- OSMO-EUR — BUILDING_ACCELERATION — score 5.819/10 — DETECTED_BUT_TOO_LATE
- ZETA-EUR — BUILDING_ACCELERATION — score 5.498/10 — DETECTED_BUT_TOO_LATE
- TOSHI-EUR — BUILDING_ACCELERATION — score 5.422/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- MOVR-EUR — BUILDING_ACCELERATION — score 5.295/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- SENT-EUR — ACTIVE_NOW — score mémoire 7.947/10 — sources ACCELERATION, DECISION_LAYER, V4 — BUYABLE_NOW
- GLMR-EUR — MEMORY_24H — score mémoire 9.062/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- DYDX-EUR — MEMORY_24H — score mémoire 9.010/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- TAI-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- VET-EUR — ACTIVE_NOW — score mémoire 8.403/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- CSPR-EUR — MEMORY_24H — score mémoire 8.374/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- HFT-EUR — MEMORY_24H — score mémoire 8.258/10 — sources ACCELERATION — MEMORY_ONLY
- ZRC-EUR — ACTIVE_NOW — score mémoire 8.253/10 — sources ACCELERATION, V4 — DETECTED_BUT_TOO_LATE
- BONK-EUR — ACTIVE_NOW — score mémoire 8.215/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- CAKE-EUR — ACTIVE_NOW — score mémoire 7.953/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY

## Audit des plus fortes hausses

- TREAD-EUR +45.83% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- QNT-EUR +40.00% — DETECTED_EARLY — couche NONE — action NONE
- ONDO-EUR +31.51% — DETECTED_EARLY — couche NONE — action NONE
- XPL-EUR +29.65% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- ARK-EUR +27.67% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- PHA-EUR +25.60% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- FET-EUR +22.33% — DETECTED_EARLY — couche NONE — action NONE
- PEAQ-EUR +21.87% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- EDGE-EUR +18.70% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- CHIP-EUR +17.67% — DETECTED_EARLY — couche NONE — action INTERPRETATION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
