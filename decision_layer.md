# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-19T20:38:09.648071+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : SUI-EUR | action ACHETE_MAINTENANT | opportunité 8.038 | entrée 7.400 | trend 8.450 | rang 7.768
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : HYPE-EUR | action PLACE_LIMITE_PASSIVE | opportunité 7.765 | entrée 6.000 | trend 8.750 | rang 7.682
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : aucun candidat matériel
- **MEILLEUR_PULLBACK_REENTRY** : TAO-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 7.565 | entrée 7.150 | trend 7.950 | rang 7.424
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. SUI-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 7.768
2. HYPE-EUR — MEILLEURE_LIMITE_PASSIVE — PLACE_LIMITE_PASSIVE — rank 7.682
3. TAO-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.424

## Accélération indépendante

Aucune accélération indépendante confirmée ou en construction.

## Watchlist persistante 24–72 h

- DYDX-EUR — ACTIVE_NOW — score mémoire 8.341/10 — sources V4 — WATCH_ONLY
- IMX-EUR — ACTIVE_NOW — score mémoire 8.272/10 — sources V4 — DETECTED_BUT_TOO_LATE
- MIOTA-EUR — ACTIVE_NOW — score mémoire 8.158/10 — sources V4 — WATCH_ONLY
- AAVE-EUR — ACTIVE_NOW — score mémoire 8.047/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- NEO-EUR — ACTIVE_NOW — score mémoire 8.010/10 — sources V4 — WATCH_ONLY
- LPT-EUR — ACTIVE_NOW — score mémoire 7.934/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- PYTH-EUR — ACTIVE_NOW — score mémoire 7.918/10 — sources V4 — WATCH_ONLY
- COW-EUR — ACTIVE_NOW — score mémoire 7.896/10 — sources V4 — WATCH_ONLY
- ACH-EUR — ACTIVE_NOW — score mémoire 7.805/10 — sources DECISION_LAYER, V4 — WATCH_ONLY
- APT-EUR — ACTIVE_NOW — score mémoire 7.781/10 — sources DECISION_LAYER, V4 — WATCH_ONLY

## Audit des plus fortes hausses

- ZAMA-EUR +41.68% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- SYN-EUR +38.26% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- CELR-EUR +30.90% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- G-EUR +28.05% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- XTZ-EUR +27.39% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- EPIC-EUR +26.66% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ENA-EUR +22.88% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- INJ-EUR +19.66% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- EDGE-EUR +18.67% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- AVAX-EUR +17.25% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
