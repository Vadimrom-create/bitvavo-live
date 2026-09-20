# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-20T15:59:53.043292+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : HYPE-EUR | action ACHETE_MAINTENANT | opportunité 8.983 | entrée 7.700 | trend 8.250 | rang 8.213
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : aucun candidat matériel
- **MEILLEUR_LATENT_ACCELERATOR** : HBAR-EUR | action LATENT_ACCELERATOR | opportunité 7.431 | entrée 4.500 | trend 7.800 | rang 6.803
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : VVV-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.127 | entrée 6.450 | trend 8.450 | rang 7.524
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. HYPE-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.213
2. VVV-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.524
3. ENA-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.460

## Accélération indépendante

Aucune accélération indépendante confirmée ou en construction.

## Watchlist persistante 24–72 h

- HYPE-EUR — ACTIVE_NOW — score mémoire 8.213/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- INJ-EUR — ACTIVE_NOW — score mémoire 8.042/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- AERO-EUR — ACTIVE_NOW — score mémoire 7.926/10 — sources V4 — WATCH_ONLY
- MERL-EUR — ACTIVE_NOW — score mémoire 7.874/10 — sources V4 — WATCH_ONLY
- XTZ-EUR — ACTIVE_NOW — score mémoire 7.832/10 — sources DECISION_LAYER, V4 — WATCH_ONLY
- CELR-EUR — MEMORY_24H — score mémoire 7.831/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- PROVE-EUR — ACTIVE_NOW — score mémoire 7.821/10 — sources V4 — WATCH_ONLY
- ATH-EUR — ACTIVE_NOW — score mémoire 7.786/10 — sources V4 — WATCH_ONLY
- KMNO-EUR — ACTIVE_NOW — score mémoire 7.781/10 — sources V4 — WATCH_ONLY
- ARX-EUR — ACTIVE_NOW — score mémoire 7.751/10 — sources V4 — WATCH_ONLY

## Audit des plus fortes hausses

- CELR-EUR +60.39% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- SAGA-EUR +28.46% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- FTT-EUR +24.34% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE
- PTB-EUR +22.84% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- AVAX-EUR +20.16% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- EPIC-EUR +18.66% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- C-EUR +16.55% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- ALGO-EUR +12.01% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- CTSI-EUR +8.92% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- SKL-EUR +8.61% — DETECTED_EARLY — couche NONE — action INTERPRETATION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
