# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-25T13:04:13.386320+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : ADA-EUR | action ACHETE_MAINTENANT | opportunité 8.308 | entrée 7.850 | trend 8.500 | rang 7.954
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : RAY-EUR | action PLACE_LIMITE_PASSIVE | opportunité 7.826 | entrée 6.000 | trend 8.550 | rang 7.558
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : ZK-EUR | action LATENT_ACCELERATOR | opportunité 8.568 | entrée 5.700 | trend 7.950 | rang 7.537
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : GMT-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.524 | entrée 7.550 | trend 8.250 | rang 7.998
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. GMT-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.998
2. ADA-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 7.954
3. SENT-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.920

## Accélération indépendante

- BIO-EUR — CONFIRMED_ACCELERATION — score 7.275/10 — DETECTED_BUT_TOO_LATE
- FTT-EUR — BUILDING_ACCELERATION — score 5.976/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- SAGA-EUR — BUILDING_ACCELERATION — score 5.784/10 — DETECTED_BUT_TOO_LATE
- AGLD-EUR — BUILDING_ACCELERATION — score 5.579/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- HNT-EUR — BUILDING_ACCELERATION — score 5.247/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- POND-EUR — BUILDING_ACCELERATION — score 5.003/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- HUMA-EUR — MEMORY_24H — score mémoire 10.000/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- SCR-EUR — MEMORY_24H — score mémoire 9.062/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- GLMR-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- CSPR-EUR — MEMORY_24H — score mémoire 8.374/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- HFT-EUR — MEMORY_24H — score mémoire 8.258/10 — sources ACCELERATION — MEMORY_ONLY
- PHA-EUR — MEMORY_24H — score mémoire 8.218/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- GMT-EUR — ACTIVE_NOW — score mémoire 7.998/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- ADA-EUR — ACTIVE_NOW — score mémoire 7.954/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- SENT-EUR — ACTIVE_NOW — score mémoire 7.920/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- ENS-EUR — ACTIVE_NOW — score mémoire 7.869/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY

## Audit des plus fortes hausses

- PHA-EUR +40.47% — DETECTED_TOO_LATE — couche NONE — action INTERPRETATION
- TREAD-EUR +33.76% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ARK-EUR +28.10% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- XPL-EUR +27.98% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- QNT-EUR +25.35% — DETECTED_EARLY — couche NONE — action NONE
- FET-EUR +20.59% — DETECTED_EARLY — couche NONE — action NONE
- ONDO-EUR +20.34% — DETECTED_EARLY — couche NONE — action NONE
- PIXEL-EUR +19.54% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- KMNO-EUR +18.92% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- SUI-EUR +18.14% — DETECTED_EARLY — couche NONE — action INTERPRETATION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
