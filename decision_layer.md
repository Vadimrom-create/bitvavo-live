# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-20T14:29:02.022092+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : ALGO-EUR | action PLACE_LIMITE_PASSIVE | opportunité 7.525 | entrée 6.650 | trend 8.100 | rang 7.195
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : aucun candidat matériel
- **MEILLEUR_PULLBACK_REENTRY** : WAL-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 9.269 | entrée 5.350 | trend 8.700 | rang 8.278
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. WAL-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.278
2. HYPE-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.301
3. SAGA-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.257

## Accélération indépendante

- SYN-EUR — CONFIRMED_ACCELERATION — score 8.488/10 — DETECTED_BUT_TOO_LATE
- EPIC-EUR — CONFIRMED_ACCELERATION — score 6.573/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- SYN-EUR — ACTIVE_NOW — score mémoire 8.488/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- WAL-EUR — ACTIVE_NOW — score mémoire 8.278/10 — sources DECISION_LAYER, V4 — WATCH_ONLY
- PHA-EUR — ACTIVE_NOW — score mémoire 8.218/10 — sources DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- CAKE-EUR — MEMORY_24H — score mémoire 8.134/10 — sources DECISION_LAYER, V4 — MEMORY_ONLY
- SIGN-EUR — ACTIVE_NOW — score mémoire 8.043/10 — sources V4 — WATCH_ONLY
- CELR-EUR — MEMORY_24H — score mémoire 7.831/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- STX-EUR — ACTIVE_NOW — score mémoire 7.774/10 — sources DECISION_LAYER, V4 — WATCH_ONLY
- AERO-EUR — ACTIVE_NOW — score mémoire 7.674/10 — sources V4 — WATCH_ONLY
- BIGTIME-EUR — MEMORY_24H — score mémoire 7.662/10 — sources V4 — MEMORY_ONLY
- ENSO-EUR — MEMORY_24H — score mémoire 7.642/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY

## Audit des plus fortes hausses

- CELR-EUR +88.77% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- EPIC-EUR +26.36% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- C-EUR +17.26% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- AVAX-EUR +13.49% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- PTB-EUR +11.52% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- CTSI-EUR +10.84% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- S-EUR +9.42% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ZAMA-EUR +9.18% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ACE-EUR +7.69% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- SAGA-EUR +7.35% — DETECTED_EARLY — couche NONE — action INTERPRETATION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
