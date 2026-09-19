# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-19T21:50:10.567117+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : ONDO-EUR | action PLACE_LIMITE_PASSIVE | opportunité 7.499 | entrée 6.250 | trend 8.450 | rang 7.481
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : aucun candidat matériel
- **MEILLEUR_PULLBACK_REENTRY** : HYPE-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.078 | entrée 6.250 | trend 8.750 | rang 7.856
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. HYPE-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.856
2. SUI-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.596
3. TAO-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.485

## Accélération indépendante

- CELR-EUR — CONFIRMED_ACCELERATION — score 7.685/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- AAVE-EUR — ACTIVE_NOW — score mémoire 8.515/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- S-EUR — ACTIVE_NOW — score mémoire 8.032/10 — sources DECISION_LAYER, V4 — WATCH_ONLY
- SENT-EUR — ACTIVE_NOW — score mémoire 8.011/10 — sources V4 — WATCH_ONLY
- APT-EUR — ACTIVE_NOW — score mémoire 7.947/10 — sources DECISION_LAYER, V4 — WATCH_ONLY
- PROVE-EUR — ACTIVE_NOW — score mémoire 7.901/10 — sources V4 — WATCH_ONLY
- PENDLE-EUR — ACTIVE_NOW — score mémoire 7.870/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- HYPE-EUR — ACTIVE_NOW — score mémoire 7.856/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- XVG-EUR — ACTIVE_NOW — score mémoire 7.829/10 — sources V4 — WATCH_ONLY
- WAL-EUR — ACTIVE_NOW — score mémoire 7.815/10 — sources V4 — WATCH_ONLY
- JUP-EUR — ACTIVE_NOW — score mémoire 7.733/10 — sources DECISION_LAYER, V4 — WATCH_ONLY

## Audit des plus fortes hausses

- CELR-EUR +43.16% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- ZAMA-EUR +35.50% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- G-EUR +26.37% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- XTZ-EUR +24.33% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- EDGE-EUR +21.33% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- INJ-EUR +20.36% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- SOLV-EUR +18.04% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- CROSS-EUR +17.88% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ENA-EUR +17.76% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- AVAX-EUR +16.99% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
