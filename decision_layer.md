# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-20T10:52:40.681294+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : aucun candidat matériel
- **MEILLEUR_LATENT_ACCELERATOR** : aucun candidat matériel
- **MEILLEUR_PULLBACK_REENTRY** : ENA-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.109 | entrée 6.350 | trend 8.500 | rang 7.360
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. ENA-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.360
2. VET-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.209
3. INJ-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.175

## Accélération indépendante

- ENSO-EUR — CONFIRMED_ACCELERATION — score 8.500/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- ENSO-EUR — ACTIVE_NOW — score mémoire 8.500/10 — sources ACCELERATION, V4 — DETECTED_BUT_TOO_LATE
- PENDLE-EUR — ACTIVE_NOW — score mémoire 8.009/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- COTI-EUR — MEMORY_24H — score mémoire 7.904/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- STX-EUR — ACTIVE_NOW — score mémoire 7.840/10 — sources DECISION_LAYER, V4 — WATCH_ONLY
- WAL-EUR — ACTIVE_NOW — score mémoire 7.809/10 — sources V4 — WATCH_ONLY
- MERL-EUR — ACTIVE_NOW — score mémoire 7.769/10 — sources V4 — WATCH_ONLY
- KAS-EUR — ACTIVE_NOW — score mémoire 7.722/10 — sources DECISION_LAYER, V4 — WATCH_ONLY
- BIGTIME-EUR — MEMORY_24H — score mémoire 7.662/10 — sources V4 — MEMORY_ONLY
- PROVE-EUR — ACTIVE_NOW — score mémoire 7.648/10 — sources V4 — WATCH_ONLY
- AIOZ-EUR — ACTIVE_NOW — score mémoire 7.574/10 — sources V4 — WATCH_ONLY

## Audit des plus fortes hausses

- CELR-EUR +78.57% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- ZIL-EUR +19.53% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- SKL-EUR +18.92% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ALLO-EUR +16.28% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- C-EUR +11.16% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- CTSI-EUR +10.06% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- T-EUR +9.20% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- ENSO-EUR +8.93% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- JTO-EUR +8.16% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ONG-EUR +7.73% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
