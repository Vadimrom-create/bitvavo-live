# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-25T23:20:16.461023+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : ONDO-EUR | action ACHETE_MAINTENANT | opportunité 9.429 | entrée 8.150 | trend 8.850 | rang 8.366
  - V4 buy-ready with acceptable current entry; no structural veto. High extension/chase is retained as risk context, not an automatic veto.
- **MEILLEURE_LIMITE_PASSIVE** : ALT-EUR | action PLACE_LIMITE_PASSIVE | opportunité 8.158 | entrée 5.950 | trend 8.750 | rang 7.778
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : MOVR-EUR | action LATENT_ACCELERATOR | opportunité 8.090 | entrée 5.650 | trend 8.950 | rang 7.740
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : ZK-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 9.103 | entrée 6.500 | trend 8.950 | rang 8.306
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. ONDO-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.366
2. LINK-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.342
3. ZK-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.306

## Accélération indépendante

- CETUS-EUR — CONFIRMED_ACCELERATION — score 8.024/10 — DETECTED_BUT_TOO_LATE
- THQ-EUR — CONFIRMED_ACCELERATION — score 6.564/10 — DETECTED_BUT_TOO_LATE
- CRO-EUR — BUILDING_ACCELERATION — score 5.800/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- CATI-EUR — BUILDING_ACCELERATION — score 5.524/10 — DETECTED_BUT_TOO_LATE
- SPX-EUR — BUILDING_ACCELERATION — score 5.524/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- INJ-EUR — BUILDING_ACCELERATION — score 5.455/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- AXL-EUR — BUILDING_ACCELERATION — score 5.393/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- WLD-EUR — BUILDING_ACCELERATION — score 5.208/10 — DETECTED_BUT_TOO_LATE
- TAO-EUR — BUILDING_ACCELERATION — score 5.187/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- XPL-EUR — BUILDING_ACCELERATION — score 4.934/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- XPL-EUR — ACTIVE_NOW — score mémoire 8.114/10 — sources ACCELERATION, DECISION_LAYER, V4 — BUYABLE_NOW
- ARB-EUR — ACTIVE_NOW — score mémoire 6.984/10 — sources ACCELERATION, DECISION_LAYER, V4 — BUYABLE_NOW
- PHA-EUR — MEMORY_24H — score mémoire 10.000/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- PONKE-EUR — MEMORY_24H — score mémoire 9.578/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- CTC-EUR — MEMORY_24H — score mémoire 8.874/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- NIL-EUR — MEMORY_24H — score mémoire 8.667/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- ARK-EUR — MEMORY_24H — score mémoire 8.526/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- ONDO-EUR — ACTIVE_NOW — score mémoire 8.366/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- LINK-EUR — ACTIVE_NOW — score mémoire 8.342/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- ZK-EUR — ACTIVE_NOW — score mémoire 8.306/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY

## Audit des plus fortes hausses

- PHA-EUR +64.32% — DETECTED_TOO_LATE — couche NONE — action INTERPRETATION
- ARK-EUR +29.13% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- RARE-EUR +21.84% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- AERO-EUR +21.47% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- SEI-EUR +19.82% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- ENA-EUR +19.20% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- TREAD-EUR +19.19% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- SUI-EUR +19.06% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- DEEP-EUR +18.63% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE
- GRASS-EUR +18.31% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
