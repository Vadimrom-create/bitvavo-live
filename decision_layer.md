# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-20T13:24:30.600281+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : HBAR-EUR | action ACHETE_MAINTENANT | opportunité 7.942 | entrée 7.300 | trend 6.550 | rang 6.951
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : ENSO-EUR | action PLACE_LIMITE_PASSIVE | opportunité 7.736 | entrée 6.250 | trend 8.750 | rang 7.579
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : aucun candidat matériel
- **MEILLEUR_PULLBACK_REENTRY** : WAL-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 7.484 | entrée 5.050 | trend 8.700 | rang 7.421
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. ENSO-EUR — MEILLEURE_LIMITE_PASSIVE — PLACE_LIMITE_PASSIVE — rank 7.579
2. WAL-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.421
3. INJ-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.380

## Accélération indépendante

- ZAMA-EUR — CONFIRMED_ACCELERATION — score 7.094/10 — DETECTED_BUT_TOO_LATE
- CELR-EUR — BUILDING_ACCELERATION — score 5.861/10 — DETECTED_BUT_TOO_LATE
- C-EUR — BUILDING_ACCELERATION — score 5.856/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- AIOZ-EUR — MEMORY_24H — score mémoire 8.123/10 — sources V4 — MEMORY_ONLY
- SENT-EUR — ACTIVE_NOW — score mémoire 8.040/10 — sources V4 — WATCH_ONLY
- COTI-EUR — MEMORY_24H — score mémoire 7.904/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- PROVE-EUR — ACTIVE_NOW — score mémoire 7.849/10 — sources V4 — WATCH_ONLY
- BIGTIME-EUR — MEMORY_24H — score mémoire 7.662/10 — sources V4 — MEMORY_ONLY
- CAKE-EUR — ACTIVE_NOW — score mémoire 7.661/10 — sources DECISION_LAYER, V4 — WATCH_ONLY
- ENA-EUR — ACTIVE_NOW — score mémoire 7.610/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- ACH-EUR — ACTIVE_NOW — score mémoire 7.605/10 — sources DECISION_LAYER, V4 — WATCH_ONLY
- MERL-EUR — ACTIVE_NOW — score mémoire 7.592/10 — sources V4 — WATCH_ONLY
- AERO-EUR — ACTIVE_NOW — score mémoire 7.590/10 — sources V4 — WATCH_ONLY

## Audit des plus fortes hausses

- CELR-EUR +71.42% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- ZAMA-EUR +22.39% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- PTB-EUR +15.18% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- AVAX-EUR +15.12% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- C-EUR +14.72% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- CTSI-EUR +10.74% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- SKL-EUR +8.71% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- SAGA-EUR +7.84% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- S-EUR +7.07% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- VELO-EUR +6.85% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
