# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-19T06:42:43.217668+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : AAVE-EUR | action ACHETE_MAINTENANT | opportunité 8.469 | entrée 7.100 | trend 8.950 | rang 8.163
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : APT-EUR | action PLACE_LIMITE_PASSIVE | opportunité 7.692 | entrée 6.500 | trend 8.450 | rang 7.402
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : ONDO-EUR | action LATENT_ACCELERATOR | opportunité 7.450 | entrée 4.500 | trend 7.650 | rang 6.961
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : HYPE-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.028 | entrée 6.900 | trend 8.500 | rang 7.814
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. AAVE-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.163
2. HYPE-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.814
3. SOL-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.585

## Accélération indépendante

- G-EUR — BUILDING_ACCELERATION — score 5.500/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- PENDLE-EUR — ACTIVE_NOW — score mémoire 8.209/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- AIOZ-EUR — ACTIVE_NOW — score mémoire 8.177/10 — sources V4 — DETECTED_BUT_TOO_LATE
- AAVE-EUR — ACTIVE_NOW — score mémoire 8.163/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- KAS-EUR — ACTIVE_NOW — score mémoire 8.059/10 — sources DECISION_LAYER, V4 — WATCH_ONLY
- RED-EUR — ACTIVE_NOW — score mémoire 7.989/10 — sources V4 — WATCH_ONLY
- ARX-EUR — ACTIVE_NOW — score mémoire 7.902/10 — sources V4 — DETECTED_BUT_TOO_LATE
- UNI-EUR — ACTIVE_NOW — score mémoire 7.881/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- AERO-EUR — ACTIVE_NOW — score mémoire 7.879/10 — sources V4 — WATCH_ONLY
- MIOTA-EUR — ACTIVE_NOW — score mémoire 7.845/10 — sources V4 — WATCH_ONLY
- SSV-EUR — MEMORY_24H — score mémoire 7.845/10 — sources V4 — MEMORY_ONLY

## Audit des plus fortes hausses

- EDGE-EUR +76.50% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- G-EUR +46.08% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- STRK-EUR +32.20% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- F-EUR +27.48% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- SYN-EUR +26.36% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- XTZ-EUR +25.40% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- INJ-EUR +22.25% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- ZAMA-EUR +22.06% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- EPIC-EUR +20.67% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ZIG-EUR +20.39% — DETECTED_EARLY — couche NONE — action INTERPRETATION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
