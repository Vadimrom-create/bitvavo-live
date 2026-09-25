# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-25T16:12:04.129846+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : LDO-EUR | action ACHETE_MAINTENANT | opportunité 8.966 | entrée 6.800 | trend 8.750 | rang 8.218
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : OP-EUR | action PLACE_LIMITE_PASSIVE | opportunité 7.789 | entrée 6.050 | trend 8.400 | rang 7.573
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : MOVR-EUR | action LATENT_ACCELERATOR | opportunité 8.351 | entrée 5.500 | trend 8.950 | rang 7.841
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : IMX-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 9.243 | entrée 6.550 | trend 8.500 | rang 8.338
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. IMX-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.338
2. ZK-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.295
3. LDO-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.218

## Accélération indépendante

- CTC-EUR — CONFIRMED_ACCELERATION — score 8.874/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- WMTX-EUR — CONFIRMED_ACCELERATION — score 7.948/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- ICX-EUR — CONFIRMED_ACCELERATION — score 7.741/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- ENJ-EUR — CONFIRMED_ACCELERATION — score 7.319/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- ZK-EUR — CONFIRMED_ACCELERATION — score 7.315/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- AI-EUR — CONFIRMED_ACCELERATION — score 6.776/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- WIN-EUR — BUILDING_ACCELERATION — score 6.130/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- DUSK-EUR — BUILDING_ACCELERATION — score 6.019/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- BILL-EUR — BUILDING_ACCELERATION — score 5.838/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- USELESS-EUR — BUILDING_ACCELERATION — score 5.713/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- LDO-EUR — ACTIVE_NOW — score mémoire 8.218/10 — sources ACCELERATION, DECISION_LAYER, V4 — BUYABLE_NOW
- JUP-EUR — ACTIVE_NOW — score mémoire 7.984/10 — sources ACCELERATION, DECISION_LAYER, V4 — BUYABLE_NOW
- CTC-EUR — ACTIVE_NOW — score mémoire 8.874/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- IMX-EUR — ACTIVE_NOW — score mémoire 8.338/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- ZK-EUR — ACTIVE_NOW — score mémoire 8.295/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- TIA-EUR — ACTIVE_NOW — score mémoire 8.162/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- HFT-EUR — MEMORY_DECAY_24_72H — score mémoire 8.120/10 — sources ACCELERATION — MEMORY_ONLY
- INJ-EUR — ACTIVE_NOW — score mémoire 8.099/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- RENDER-EUR — ACTIVE_NOW — score mémoire 8.097/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- REQ-EUR — MEMORY_24H — score mémoire 8.033/10 — sources ACCELERATION, V4 — MEMORY_ONLY

## Audit des plus fortes hausses

- PHA-EUR +46.48% — DETECTED_TOO_LATE — couche NONE — action INTERPRETATION
- ARK-EUR +29.33% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- TREAD-EUR +27.81% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- RARE-EUR +21.15% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ENA-EUR +18.30% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- EDGE-EUR +17.46% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- DBR-EUR +16.75% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- KMNO-EUR +16.09% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- GRASS-EUR +16.09% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- QNT-EUR +15.79% — DETECTED_EARLY — couche NONE — action NONE

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
