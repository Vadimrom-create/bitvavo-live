# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-26T04:27:51.071180+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : KAS-EUR | action ACHETE_MAINTENANT | opportunité 9.421 | entrée 7.150 | trend 8.950 | rang 8.551
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : W-EUR | action PLACE_LIMITE_PASSIVE | opportunité 7.708 | entrée 5.850 | trend 8.500 | rang 7.536
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : WAL-EUR | action LATENT_ACCELERATOR | opportunité 7.855 | entrée 5.600 | trend 8.450 | rang 7.542
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : COMP-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 9.280 | entrée 7.050 | trend 8.750 | rang 8.505
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. KAS-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.551
2. COMP-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.505
3. APT-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.236

## Accélération indépendante

- ICX-EUR — CONFIRMED_ACCELERATION — score 9.118/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- PROM-EUR — CONFIRMED_ACCELERATION — score 8.723/10 — DETECTED_BUT_TOO_LATE
- PUFFER-EUR — CONFIRMED_ACCELERATION — score 8.207/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- CFG-EUR — CONFIRMED_ACCELERATION — score 6.993/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- KAS-EUR — BUILDING_ACCELERATION — score 6.006/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- WAXP-EUR — BUILDING_ACCELERATION — score 5.837/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- PHA-EUR — BUILDING_ACCELERATION — score 5.492/10 — DETECTED_BUT_TOO_LATE
- CPOOL-EUR — BUILDING_ACCELERATION — score 4.989/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- PONKE-EUR — MEMORY_24H — score mémoire 9.578/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- ICX-EUR — ACTIVE_NOW — score mémoire 9.118/10 — sources ACCELERATION, V4 — WATCH_ONLY
- XMN-EUR — MEMORY_24H — score mémoire 8.896/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- CTC-EUR — MEMORY_24H — score mémoire 8.874/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- ONT-EUR — MEMORY_24H — score mémoire 8.859/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- PROM-EUR — ACTIVE_NOW — score mémoire 8.723/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- WIN-EUR — MEMORY_24H — score mémoire 8.694/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- KAS-EUR — ACTIVE_NOW — score mémoire 8.551/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- COMP-EUR — ACTIVE_NOW — score mémoire 8.505/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- APT-EUR — ACTIVE_NOW — score mémoire 8.236/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY

## Audit des plus fortes hausses

- POND-EUR +93.24% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- PHA-EUR +67.59% — DETECTED_TOO_LATE — couche NONE — action INTERPRETATION
- ARK-EUR +36.58% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- SAGA-EUR +30.65% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- AERO-EUR +27.09% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- ENA-EUR +21.68% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- RARE-EUR +19.75% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- SEI-EUR +18.67% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- WMTX-EUR +17.01% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- JTO-EUR +16.46% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
