# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-25T19:45:26.261256+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : LINK-EUR | action ACHETE_MAINTENANT | opportunité 8.299 | entrée 7.150 | trend 9.000 | rang 8.155
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : PYTH-EUR | action PLACE_LIMITE_PASSIVE | opportunité 7.978 | entrée 5.800 | trend 9.200 | rang 7.913
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : MANA-EUR | action LATENT_ACCELERATOR | opportunité 7.946 | entrée 5.250 | trend 9.000 | rang 7.765
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : ONDO-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.538 | entrée 8.000 | trend 8.850 | rang 8.285
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. ONDO-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.285
2. AXS-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.184
3. LINK-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.155

## Accélération indépendante

- WMTX-EUR — BUILDING_ACCELERATION — score 5.844/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- RUNE-EUR — BUILDING_ACCELERATION — score 4.951/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- REQ-EUR — BUILDING_ACCELERATION — score 4.873/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- FOLD-EUR — BUILDING_ACCELERATION — score 4.855/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- ICX-EUR — MEMORY_24H — score mémoire 9.081/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- SWELL-EUR — MEMORY_24H — score mémoire 8.882/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- CTC-EUR — MEMORY_24H — score mémoire 8.874/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- NIL-EUR — MEMORY_24H — score mémoire 8.667/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- ONDO-EUR — ACTIVE_NOW — score mémoire 8.285/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- AXS-EUR — ACTIVE_NOW — score mémoire 8.184/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- LINK-EUR — ACTIVE_NOW — score mémoire 8.155/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- HFT-EUR — MEMORY_24H — score mémoire 8.111/10 — sources ACCELERATION — MEMORY_ONLY
- FET-EUR — ACTIVE_NOW — score mémoire 8.103/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- RPL-EUR — ACTIVE_NOW — score mémoire 8.086/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY

## Audit des plus fortes hausses

- PHA-EUR +67.13% — DETECTED_TOO_LATE — couche NONE — action INTERPRETATION
- ARK-EUR +28.36% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- RARE-EUR +27.65% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- GRASS-EUR +22.46% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- EDGE-EUR +20.99% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ENA-EUR +18.40% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- AERO-EUR +18.18% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- SEI-EUR +16.55% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- WMTX-EUR +16.06% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- CC-EUR +15.29% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
