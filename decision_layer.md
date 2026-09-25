# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-25T12:26:09.508141+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : CAKE-EUR | action ACHETE_MAINTENANT | opportunité 9.441 | entrée 6.850 | trend 8.950 | rang 8.342
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : GRT-EUR | action PLACE_LIMITE_PASSIVE | opportunité 8.298 | entrée 6.650 | trend 8.850 | rang 7.782
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : BONK-EUR | action LATENT_ACCELERATOR | opportunité 7.927 | entrée 5.500 | trend 8.450 | rang 7.564
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : ENS-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.100 | entrée 6.700 | trend 8.750 | rang 7.875
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. CAKE-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.342
2. INJ-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.113
3. SENT-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.047

## Accélération indépendante

- PIXEL-EUR — CONFIRMED_ACCELERATION — score 9.575/10 — DETECTED_BUT_TOO_LATE
- PHA-EUR — CONFIRMED_ACCELERATION — score 8.218/10 — DETECTED_BUT_TOO_LATE
- ICX-EUR — BUILDING_ACCELERATION — score 5.647/10 — DETECTED_BUT_TOO_LATE
- AVA-EUR — BUILDING_ACCELERATION — score 4.886/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- CAKE-EUR — ACTIVE_NOW — score mémoire 8.342/10 — sources ACCELERATION, DECISION_LAYER, V4 — BUYABLE_NOW
- XRP-EUR — ACTIVE_NOW — score mémoire 7.411/10 — sources ACCELERATION, DECISION_LAYER, V4 — BUYABLE_NOW
- UNI-EUR — ACTIVE_NOW — score mémoire 7.275/10 — sources ACCELERATION, DECISION_LAYER, V4 — BUYABLE_NOW
- PIXEL-EUR — ACTIVE_NOW — score mémoire 9.575/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- SCR-EUR — MEMORY_24H — score mémoire 9.062/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- GLMR-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- TAI-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- CSPR-EUR — MEMORY_24H — score mémoire 8.374/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- HFT-EUR — MEMORY_24H — score mémoire 8.258/10 — sources ACCELERATION — MEMORY_ONLY
- PHA-EUR — ACTIVE_NOW — score mémoire 8.218/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE

## Audit des plus fortes hausses

- TREAD-EUR +33.43% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ARK-EUR +32.21% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- QNT-EUR +30.44% — DETECTED_EARLY — couche NONE — action NONE
- PHA-EUR +28.94% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- XPL-EUR +26.88% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- FET-EUR +20.01% — DETECTED_EARLY — couche NONE — action NONE
- PIXEL-EUR +19.62% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ONDO-EUR +19.20% — DETECTED_EARLY — couche NONE — action NONE
- PEAQ-EUR +19.06% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- DEEP-EUR +18.89% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
