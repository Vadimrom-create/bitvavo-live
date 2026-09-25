# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-25T14:58:37.557436+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : CAKE-EUR | action ACHETE_MAINTENANT | opportunité 8.680 | entrée 7.250 | trend 8.950 | rang 8.292
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : ICP-EUR | action PLACE_LIMITE_PASSIVE | opportunité 8.182 | entrée 6.050 | trend 9.200 | rang 8.042
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : ENS-EUR | action LATENT_ACCELERATOR | opportunité 7.767 | entrée 5.750 | trend 8.450 | rang 7.545
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : AXS-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 9.345 | entrée 7.750 | trend 8.750 | rang 8.316
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. AXS-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.316
2. CAKE-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.292
3. OP-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.189

## Accélération indépendante

- GRASS-EUR — CONFIRMED_ACCELERATION — score 7.731/10 — DETECTED_BUT_TOO_LATE
- GTC-EUR — CONFIRMED_ACCELERATION — score 7.652/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- ICX-EUR — CONFIRMED_ACCELERATION — score 7.274/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- RARE-EUR — BUILDING_ACCELERATION — score 6.374/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- PLUME-EUR — BUILDING_ACCELERATION — score 5.743/10 — DETECTED_BUT_TOO_LATE
- MOVR-EUR — BUILDING_ACCELERATION — score 5.257/10 — DETECTED_BUT_TOO_LATE
- ENJ-EUR — BUILDING_ACCELERATION — score 5.249/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- WIN-EUR — BUILDING_ACCELERATION — score 5.181/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- HAEDAL-EUR — BUILDING_ACCELERATION — score 5.045/10 — DETECTED_BUT_TOO_LATE
- GLMR-EUR — BUILDING_ACCELERATION — score 4.987/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- AXS-EUR — ACTIVE_NOW — score mémoire 8.316/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- CAKE-EUR — ACTIVE_NOW — score mémoire 8.292/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- HFT-EUR — MEMORY_24H — score mémoire 8.258/10 — sources ACCELERATION — MEMORY_ONLY
- OP-EUR — ACTIVE_NOW — score mémoire 8.189/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- PYTH-EUR — ACTIVE_NOW — score mémoire 8.151/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- ICP-EUR — ACTIVE_NOW — score mémoire 8.042/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- INJ-EUR — ACTIVE_NOW — score mémoire 7.963/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- ADA-EUR — ACTIVE_NOW — score mémoire 7.949/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- JUP-EUR — ACTIVE_NOW — score mémoire 7.892/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- LDO-EUR — ACTIVE_NOW — score mémoire 7.852/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY

## Audit des plus fortes hausses

- PHA-EUR +57.48% — DETECTED_TOO_LATE — couche NONE — action INTERPRETATION
- TREAD-EUR +44.69% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ARK-EUR +26.76% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- KMNO-EUR +19.74% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- QNT-EUR +18.83% — DETECTED_EARLY — couche NONE — action NONE
- DBR-EUR +18.74% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- NIL-EUR +18.58% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- EDGE-EUR +17.56% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- XPL-EUR +16.69% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- GRASS-EUR +16.49% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
