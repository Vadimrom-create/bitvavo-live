# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-25T22:50:53.435009+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : ADA-EUR | action ACHETE_MAINTENANT | opportunité 9.296 | entrée 8.050 | trend 8.200 | rang 8.331
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : ZK-EUR | action PLACE_LIMITE_PASSIVE | opportunité 8.307 | entrée 5.850 | trend 8.950 | rang 7.921
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : SIGN-EUR | action LATENT_ACCELERATOR | opportunité 7.905 | entrée 4.500 | trend 8.950 | rang 7.625
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : FET-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.860 | entrée 8.250 | trend 8.850 | rang 8.330
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. ADA-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.331
2. FET-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.330
3. PYTH-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.319

## Accélération indépendante

- ARK-EUR — CONFIRMED_ACCELERATION — score 8.994/10 — DETECTED_BUT_TOO_LATE
- ARKM-EUR — CONFIRMED_ACCELERATION — score 7.889/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- OP-EUR — CONFIRMED_ACCELERATION — score 6.531/10 — DETECTED_BUT_TOO_LATE
- VELO-EUR — CONFIRMED_ACCELERATION — score 6.509/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- A-EUR — BUILDING_ACCELERATION — score 5.723/10 — DETECTED_BUT_TOO_LATE
- NEIRO-EUR — BUILDING_ACCELERATION — score 5.687/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- RAY-EUR — BUILDING_ACCELERATION — score 5.324/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- BICO-EUR — BUILDING_ACCELERATION — score 4.927/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- LPT-EUR — BUILDING_ACCELERATION — score 4.785/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- ZEUS-EUR — BUILDING_ACCELERATION — score 4.781/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- LTC-EUR — ACTIVE_NOW — score mémoire 7.913/10 — sources ACCELERATION, DECISION_LAYER, V4 — BUYABLE_NOW
- VIRTUAL-EUR — ACTIVE_NOW — score mémoire 7.394/10 — sources ACCELERATION, DECISION_LAYER, V4 — BUYABLE_NOW
- ARB-EUR — ACTIVE_NOW — score mémoire 6.684/10 — sources ACCELERATION, DECISION_LAYER, V4 — BUYABLE_NOW
- PHA-EUR — MEMORY_24H — score mémoire 10.000/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- ARK-EUR — ACTIVE_NOW — score mémoire 8.994/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- CTC-EUR — MEMORY_24H — score mémoire 8.874/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- NIL-EUR — MEMORY_24H — score mémoire 8.667/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- ADA-EUR — ACTIVE_NOW — score mémoire 8.331/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- FET-EUR — ACTIVE_NOW — score mémoire 8.330/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- PYTH-EUR — ACTIVE_NOW — score mémoire 8.319/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE

## Audit des plus fortes hausses

- PHA-EUR +80.60% — DETECTED_TOO_LATE — couche NONE — action INTERPRETATION
- ARK-EUR +32.94% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- RARE-EUR +22.62% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- AERO-EUR +21.13% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- SEI-EUR +20.15% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- ENA-EUR +19.26% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- DEEP-EUR +18.24% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE
- SUI-EUR +17.93% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- GRASS-EUR +17.58% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- JTO-EUR +15.60% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
