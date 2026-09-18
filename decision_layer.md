# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-18T06:46:39.902324+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : SYRUP-EUR | action PLACE_LIMITE_PASSIVE | opportunité 7.505 | entrée 6.700 | trend 7.950 | rang 7.293
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : aucun candidat matériel
- **MEILLEUR_PULLBACK_REENTRY** : DOT-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 7.802 | entrée 7.000 | trend 8.300 | rang 7.074
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. SYRUP-EUR — MEILLEURE_LIMITE_PASSIVE — PLACE_LIMITE_PASSIVE — rank 7.293
2. DOT-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.074
3. WLD-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.011

## Accélération indépendante

Aucune accélération indépendante confirmée ou en construction.

## Watchlist persistante 24–72 h

- TREAD-EUR — MEMORY_24H — score mémoire 8.374/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- KAS-EUR — ACTIVE_NOW — score mémoire 8.346/10 — sources DECISION_LAYER, V4 — WATCH_ONLY
- LDO-EUR — ACTIVE_NOW — score mémoire 8.308/10 — sources V4 — WATCH_ONLY
- VTHO-EUR — ACTIVE_NOW — score mémoire 8.137/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- ATOM-EUR — ACTIVE_NOW — score mémoire 8.106/10 — sources V4 — DETECTED_BUT_TOO_LATE
- ETHFI-EUR — ACTIVE_NOW — score mémoire 8.056/10 — sources V4 — WATCH_ONLY
- VET-EUR — ACTIVE_NOW — score mémoire 8.008/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- SOMI-EUR — ACTIVE_NOW — score mémoire 7.843/10 — sources V4 — WATCH_ONLY
- METIS-EUR — ACTIVE_NOW — score mémoire 7.787/10 — sources V4 — DETECTED_BUT_TOO_LATE
- ARB-EUR — MEMORY_24H — score mémoire 7.749/10 — sources ACCELERATION, V4 — MEMORY_ONLY

## Audit des plus fortes hausses

- DRIFT-EUR +42.17% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- COTI-EUR +31.73% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- CNPY-EUR +29.89% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ARB-EUR +28.90% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- NEAR-EUR +28.60% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- CROSS-EUR +27.76% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- UNI-EUR +26.72% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- G-EUR +25.64% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- MET-EUR +21.18% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE
- AGI-EUR +20.00% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
