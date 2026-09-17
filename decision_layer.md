# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-17T20:22:30.303027+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : aucun candidat matériel
- **MEILLEUR_LATENT_ACCELERATOR** : aucun candidat matériel
- **MEILLEUR_PULLBACK_REENTRY** : VET-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.298 | entrée 7.250 | trend 8.650 | rang 8.010
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. VET-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.010

## Accélération indépendante

- COTI-EUR — BUILDING_ACCELERATION — score 6.061/10 — DETECTED_BUT_TOO_LATE
- AVA-EUR — BUILDING_ACCELERATION — score 5.014/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- CNPY-EUR — MEMORY_24H — score mémoire 9.527/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- METIS-EUR — ACTIVE_NOW — score mémoire 8.590/10 — sources V4 — DETECTED_BUT_TOO_LATE
- VTHO-EUR — ACTIVE_NOW — score mémoire 8.114/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- LDO-EUR — ACTIVE_NOW — score mémoire 8.040/10 — sources V4 — WATCH_ONLY
- ZRO-EUR — ACTIVE_NOW — score mémoire 8.019/10 — sources V4 — WATCH_ONLY
- INJ-EUR — ACTIVE_NOW — score mémoire 8.014/10 — sources DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- VET-EUR — ACTIVE_NOW — score mémoire 8.010/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- WLD-EUR — ACTIVE_NOW — score mémoire 7.961/10 — sources DECISION_LAYER, V4 — WATCH_ONLY
- CHILLGUY-EUR — ACTIVE_NOW — score mémoire 7.914/10 — sources V4 — DETECTED_BUT_TOO_LATE
- ICP-EUR — ACTIVE_NOW — score mémoire 7.878/10 — sources V4 — WATCH_ONLY

## Audit des plus fortes hausses

- AVA-EUR +80.41% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- CNPY-EUR +48.33% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- COTI-EUR +37.49% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- CROSS-EUR +36.84% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- TREAD-EUR +31.28% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- AGI-EUR +24.96% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- UNI-EUR +20.57% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- QUID-EUR +19.03% — DETECTED_TOO_LATE — couche NONE — action INTERPRETATION
- PEAQ-EUR +18.38% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- NEAR-EUR +18.12% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
