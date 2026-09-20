# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-20T12:34:46.411367+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : SAGA-EUR | action PLACE_LIMITE_PASSIVE | opportunité 7.628 | entrée 6.550 | trend 7.800 | rang 7.037
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : aucun candidat matériel
- **MEILLEUR_PULLBACK_REENTRY** : AVAX-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.522 | entrée 7.800 | trend 8.150 | rang 7.472
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. AVAX-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.472
2. EPIC-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.264
3. NEAR-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.224

## Accélération indépendante

- ENSO-EUR — CONFIRMED_ACCELERATION — score 7.724/10 — DETECTED_BUT_TOO_LATE
- ZAMA-EUR — CONFIRMED_ACCELERATION — score 6.611/10 — REQUIRES_V4_ENTRY_AND_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- AIOZ-EUR — ACTIVE_NOW — score mémoire 7.990/10 — sources V4 — WATCH_ONLY
- ENA-EUR — MEMORY_24H — score mémoire 7.976/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- COTI-EUR — MEMORY_24H — score mémoire 7.904/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- ENSO-EUR — ACTIVE_NOW — score mémoire 7.724/10 — sources ACCELERATION, V4 — DETECTED_BUT_TOO_LATE
- OP-EUR — ACTIVE_NOW — score mémoire 7.715/10 — sources DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- PHA-EUR — ACTIVE_NOW — score mémoire 7.692/10 — sources DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- BIGTIME-EUR — MEMORY_24H — score mémoire 7.662/10 — sources V4 — MEMORY_ONLY
- ACH-EUR — ACTIVE_NOW — score mémoire 7.654/10 — sources DECISION_LAYER, V4 — WATCH_ONLY
- T-EUR — MEMORY_24H — score mémoire 7.592/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- MERL-EUR — ACTIVE_NOW — score mémoire 7.586/10 — sources V4 — WATCH_ONLY

## Audit des plus fortes hausses

- CELR-EUR +77.15% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- PTB-EUR +22.30% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- ENSO-EUR +18.30% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- ZAMA-EUR +14.88% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- CTSI-EUR +12.52% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- AVAX-EUR +11.47% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- C-EUR +10.42% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- S-EUR +10.38% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- SAGA-EUR +9.58% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ZIL-EUR +9.41% — DETECTED_EARLY — couche NONE — action INTERPRETATION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
