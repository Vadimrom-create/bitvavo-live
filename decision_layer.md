# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-20T10:05:58.529094+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : aucun candidat matériel
- **MEILLEUR_LATENT_ACCELERATOR** : aucun candidat matériel
- **MEILLEUR_PULLBACK_REENTRY** : INJ-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.497 | entrée 7.050 | trend 8.300 | rang 7.560
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. INJ-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.560
2. ENA-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.399
3. HYPE-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.360

## Accélération indépendante

- G-EUR — BUILDING_ACCELERATION — score 5.500/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- MERL-EUR — ACTIVE_NOW — score mémoire 8.021/10 — sources V4 — WATCH_ONLY
- SENT-EUR — ACTIVE_NOW — score mémoire 7.919/10 — sources V4 — WATCH_ONLY
- COTI-EUR — MEMORY_24H — score mémoire 7.904/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- KAS-EUR — ACTIVE_NOW — score mémoire 7.895/10 — sources DECISION_LAYER, V4 — WATCH_ONLY
- STX-EUR — ACTIVE_NOW — score mémoire 7.891/10 — sources DECISION_LAYER, V4 — WATCH_ONLY
- AERO-EUR — ACTIVE_NOW — score mémoire 7.821/10 — sources V4 — WATCH_ONLY
- PROVE-EUR — ACTIVE_NOW — score mémoire 7.802/10 — sources V4 — WATCH_ONLY
- AIOZ-EUR — ACTIVE_NOW — score mémoire 7.674/10 — sources V4 — WATCH_ONLY
- BIGTIME-EUR — MEMORY_24H — score mémoire 7.662/10 — sources V4 — MEMORY_ONLY
- COW-EUR — ACTIVE_NOW — score mémoire 7.610/10 — sources V4 — WATCH_ONLY

## Audit des plus fortes hausses

- CELR-EUR +77.76% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- ZIL-EUR +20.44% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- CTSI-EUR +17.28% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- SKL-EUR +17.10% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- C-EUR +11.73% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ZAMA-EUR +11.64% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- SOLV-EUR +11.52% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- JTO-EUR +11.06% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- EPIC-EUR +10.62% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- AVAX-EUR +9.59% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
