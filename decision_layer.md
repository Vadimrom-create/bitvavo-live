# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-19T08:00:11.153389+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : AVAX-EUR | action ACHETE_MAINTENANT | opportunité 8.839 | entrée 7.600 | trend 8.450 | rang 8.178
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : SOL-EUR | action PLACE_LIMITE_PASSIVE | opportunité 7.620 | entrée 6.700 | trend 8.250 | rang 7.504
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : aucun candidat matériel
- **MEILLEUR_PULLBACK_REENTRY** : INJ-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 7.389 | entrée 5.750 | trend 7.900 | rang 5.929
  - Trend remains strong; candidate retained for re-entry instead of discarded.

## Top cross-sectionnel

1. AVAX-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.178
2. HYPE-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 7.662
3. SOL-EUR — MEILLEURE_LIMITE_PASSIVE — PLACE_LIMITE_PASSIVE — rank 7.504

## Accélération indépendante

- SYN-EUR — CONFIRMED_ACCELERATION — score 7.534/10 — DETECTED_BUT_TOO_LATE
- G-EUR — CONFIRMED_ACCELERATION — score 6.764/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- RAY-EUR — ACTIVE_NOW — score mémoire 8.407/10 — sources ACCELERATION, V4 — WATCH_ONLY
- PENDLE-EUR — ACTIVE_NOW — score mémoire 8.191/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- AVAX-EUR — ACTIVE_NOW — score mémoire 8.178/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- AIOZ-EUR — ACTIVE_NOW — score mémoire 8.108/10 — sources V4 — WATCH_ONLY
- AAVE-EUR — ACTIVE_NOW — score mémoire 8.090/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- LSK-EUR — MEMORY_24H — score mémoire 8.067/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- PROVE-EUR — ACTIVE_NOW — score mémoire 8.054/10 — sources V4 — WATCH_ONLY
- ACH-EUR — ACTIVE_NOW — score mémoire 8.010/10 — sources V4 — DETECTED_BUT_TOO_LATE
- SUPER-EUR — ACTIVE_NOW — score mémoire 7.983/10 — sources V4 — DETECTED_BUT_TOO_LATE
- VVV-EUR — ACTIVE_NOW — score mémoire 7.923/10 — sources DECISION_LAYER, V4 — WATCH_ONLY

## Audit des plus fortes hausses

- EDGE-EUR +51.81% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- F-EUR +31.87% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- XTZ-EUR +31.57% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- SYN-EUR +30.36% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- HEI-EUR +28.22% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ZIG-EUR +25.81% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- INJ-EUR +22.97% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- EPIC-EUR +19.63% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- STRK-EUR +19.43% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- SAGA-EUR +18.46% — DETECTED_TOO_LATE — couche NONE — action INTERPRETATION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
