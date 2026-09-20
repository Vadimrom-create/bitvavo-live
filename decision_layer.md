# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-20T09:22:21.350895+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : aucun candidat matériel
- **MEILLEUR_LATENT_ACCELERATOR** : aucun candidat matériel
- **MEILLEUR_PULLBACK_REENTRY** : ENA-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 9.089 | entrée 7.650 | trend 7.950 | rang 7.588
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. ENA-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.588
2. HYPE-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.369
3. INJ-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.314

## Accélération indépendante

- CELR-EUR — CONFIRMED_ACCELERATION — score 6.640/10 — DETECTED_BUT_TOO_LATE
- ENA-EUR — BUILDING_ACCELERATION — score 5.263/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- KAS-EUR — ACTIVE_NOW — score mémoire 7.954/10 — sources DECISION_LAYER, V4 — WATCH_ONLY
- AIOZ-EUR — ACTIVE_NOW — score mémoire 7.921/10 — sources V4 — WATCH_ONLY
- WAL-EUR — ACTIVE_NOW — score mémoire 7.858/10 — sources V4 — WATCH_ONLY
- COW-EUR — ACTIVE_NOW — score mémoire 7.741/10 — sources V4 — WATCH_ONLY
- AERO-EUR — ACTIVE_NOW — score mémoire 7.710/10 — sources V4 — WATCH_ONLY
- S-EUR — ACTIVE_NOW — score mémoire 7.662/10 — sources DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- BIGTIME-EUR — ACTIVE_NOW — score mémoire 7.662/10 — sources V4 — WATCH_ONLY
- W-EUR — ACTIVE_NOW — score mémoire 7.595/10 — sources V4 — WATCH_ONLY
- ENA-EUR — ACTIVE_NOW — score mémoire 7.588/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- SENT-EUR — ACTIVE_NOW — score mémoire 7.538/10 — sources V4 — WATCH_ONLY

## Audit des plus fortes hausses

- CELR-EUR +76.02% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- ZIL-EUR +25.11% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- CTSI-EUR +21.43% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- SKL-EUR +14.67% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- EPIC-EUR +14.39% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- JTO-EUR +12.60% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- T-EUR +11.08% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- STX-EUR +10.93% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- PHA-EUR +9.78% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ZAMA-EUR +9.53% — DETECTED_EARLY — couche NONE — action INTERPRETATION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
