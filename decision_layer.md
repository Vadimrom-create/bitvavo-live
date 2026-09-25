# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-25T23:29:20.695386+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : LINK-EUR | action ACHETE_MAINTENANT | opportunité 8.760 | entrée 7.950 | trend 9.000 | rang 8.416
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : MOVR-EUR | action PLACE_LIMITE_PASSIVE | opportunité 8.207 | entrée 5.950 | trend 8.950 | rang 7.819
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : SIGN-EUR | action LATENT_ACCELERATOR | opportunité 7.781 | entrée 4.500 | trend 8.950 | rang 7.546
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : FET-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 9.176 | entrée 8.450 | trend 8.850 | rang 8.520
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. FET-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.520
2. LINK-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.416
3. ZK-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.401

## Accélération indépendante

- THQ-EUR — CONFIRMED_ACCELERATION — score 8.272/10 — DETECTED_BUT_TOO_LATE
- CETUS-EUR — CONFIRMED_ACCELERATION — score 7.119/10 — DETECTED_BUT_TOO_LATE
- POND-EUR — CONFIRMED_ACCELERATION — score 6.692/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- WLD-EUR — BUILDING_ACCELERATION — score 6.305/10 — DETECTED_BUT_TOO_LATE
- CAT-EUR — BUILDING_ACCELERATION — score 5.346/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- CRO-EUR — BUILDING_ACCELERATION — score 5.081/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- APT-EUR — BUILDING_ACCELERATION — score 4.943/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- CVC-EUR — BUILDING_ACCELERATION — score 4.819/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- XPL-EUR — ACTIVE_NOW — score mémoire 8.114/10 — sources ACCELERATION, DECISION_LAYER, V4 — BUYABLE_NOW
- ARB-EUR — ACTIVE_NOW — score mémoire 6.984/10 — sources ACCELERATION, DECISION_LAYER, V4 — BUYABLE_NOW
- PHA-EUR — MEMORY_24H — score mémoire 10.000/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- PONKE-EUR — MEMORY_24H — score mémoire 9.578/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- CTC-EUR — MEMORY_24H — score mémoire 8.874/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- NIL-EUR — MEMORY_24H — score mémoire 8.667/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- ARK-EUR — MEMORY_24H — score mémoire 8.526/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- FET-EUR — ACTIVE_NOW — score mémoire 8.520/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- LINK-EUR — ACTIVE_NOW — score mémoire 8.416/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- ZK-EUR — ACTIVE_NOW — score mémoire 8.401/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY

## Audit des plus fortes hausses

- PHA-EUR +64.80% — DETECTED_TOO_LATE — couche NONE — action INTERPRETATION
- ARK-EUR +30.89% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- RARE-EUR +22.19% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- AERO-EUR +20.79% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- TREAD-EUR +19.78% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- SEI-EUR +19.75% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- ENA-EUR +19.52% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- GRASS-EUR +19.09% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- SUI-EUR +18.39% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- DEEP-EUR +18.04% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
