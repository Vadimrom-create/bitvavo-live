# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-20T02:40:38.120588+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : ENA-EUR | action PLACE_LIMITE_PASSIVE | opportunité 7.510 | entrée 5.800 | trend 8.250 | rang 6.577
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : INJ-EUR | action LATENT_ACCELERATOR | opportunité 7.551 | entrée 4.450 | trend 8.600 | rang 6.568
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : HYPE-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 7.510 | entrée 6.250 | trend 8.250 | rang 7.415
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. HYPE-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.415
2. SOL-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.308
3. ENA-EUR — MEILLEURE_LIMITE_PASSIVE — PLACE_LIMITE_PASSIVE — rank 6.577

## Accélération indépendante

Aucune accélération indépendante confirmée ou en construction.

## Watchlist persistante 24–72 h

- CELR-EUR — MEMORY_24H — score mémoire 8.548/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- PENDLE-EUR — ACTIVE_NOW — score mémoire 8.170/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- VVV-EUR — ACTIVE_NOW — score mémoire 8.092/10 — sources DECISION_LAYER, V4 — WATCH_ONLY
- ZAMA-EUR — MEMORY_24H — score mémoire 7.949/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- G-EUR — MEMORY_24H — score mémoire 7.898/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- PROVE-EUR — ACTIVE_NOW — score mémoire 7.853/10 — sources V4 — WATCH_ONLY
- COW-EUR — ACTIVE_NOW — score mémoire 7.832/10 — sources V4 — WATCH_ONLY
- DOT-EUR — MEMORY_24H — score mémoire 7.831/10 — sources DECISION_LAYER, V4 — MEMORY_ONLY
- WAL-EUR — ACTIVE_NOW — score mémoire 7.802/10 — sources V4 — WATCH_ONLY
- ETC-EUR — MEMORY_24H — score mémoire 7.770/10 — sources V4 — MEMORY_ONLY

## Audit des plus fortes hausses

- CELR-EUR +103.12% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- G-EUR +55.46% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- ZAMA-EUR +32.37% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ZIL-EUR +19.49% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- AGLD-EUR +18.45% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE
- SOLV-EUR +17.40% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ENA-EUR +16.50% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- INJ-EUR +16.37% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- SKL-EUR +15.36% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- HEI-EUR +14.58% — DETECTED_EARLY — couche NONE — action INTERPRETATION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
