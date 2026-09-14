# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-14T11:13:38.452655+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : aucun candidat matériel
- **MEILLEUR_LATENT_ACCELERATOR** : aucun candidat matériel
- **MEILLEUR_PULLBACK_REENTRY** : VTHO-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.334 | entrée 5.750 | trend 9.200 | rang 8.076
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. VTHO-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.076
2. WLD-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.319

## Accélération indépendante

- CPOOL-EUR — BUILDING_ACCELERATION — score 6.267/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- VTHO-EUR — ACTIVE_NOW — score mémoire 8.076/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- LAPTOP-EUR — MEMORY_24H — score mémoire 8.013/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- XPL-EUR — ACTIVE_NOW — score mémoire 7.997/10 — sources V4 — WATCH_ONLY
- LDO-EUR — ACTIVE_NOW — score mémoire 7.887/10 — sources V4 — WATCH_ONLY
- ETHFI-EUR — ACTIVE_NOW — score mémoire 7.803/10 — sources V4 — WATCH_ONLY
- RED-EUR — ACTIVE_NOW — score mémoire 7.781/10 — sources V4 — WATCH_ONLY
- NEO-EUR — MEMORY_24H — score mémoire 7.738/10 — sources V4 — MEMORY_ONLY
- FORM-EUR — ACTIVE_NOW — score mémoire 7.718/10 — sources V4 — WATCH_ONLY
- CAKE-EUR — ACTIVE_NOW — score mémoire 7.709/10 — sources V4 — WATCH_ONLY
- ENS-EUR — ACTIVE_NOW — score mémoire 7.665/10 — sources V4 — WATCH_ONLY

## Audit des plus fortes hausses

- CPOOL-EUR +65.44% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- CVC-EUR +32.58% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- T-EUR +30.62% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- FIL-EUR +23.69% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- REZ-EUR +22.93% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- CAP-EUR +15.17% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- IQ-EUR +12.09% — DETECTED_TOO_LATE — couche NONE — action INTERPRETATION
- CNPY-EUR +11.75% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- MIOTA-EUR +11.15% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE
- WAXP-EUR +10.26% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
