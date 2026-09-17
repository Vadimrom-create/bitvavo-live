# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-17T13:54:39.599970+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : aucun candidat matériel
- **MEILLEUR_LATENT_ACCELERATOR** : aucun candidat matériel
- **MEILLEUR_PULLBACK_REENTRY** : NEAR-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 7.696 | entrée 7.600 | trend 8.100 | rang 6.851
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. NEAR-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 6.851
2. UNI-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 6.754

## Accélération indépendante

Aucune accélération indépendante confirmée ou en construction.

## Watchlist persistante 24–72 h

- ETHFI-EUR — ACTIVE_NOW — score mémoire 8.147/10 — sources V4 — WATCH_ONLY
- AERO-EUR — ACTIVE_NOW — score mémoire 8.127/10 — sources V4 — DETECTED_BUT_TOO_LATE
- XVG-EUR — ACTIVE_NOW — score mémoire 8.054/10 — sources V4 — WATCH_ONLY
- VTHO-EUR — ACTIVE_NOW — score mémoire 8.053/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- LDO-EUR — ACTIVE_NOW — score mémoire 7.913/10 — sources V4 — WATCH_ONLY
- ICP-EUR — ACTIVE_NOW — score mémoire 7.851/10 — sources V4 — WATCH_ONLY
- PROM-EUR — ACTIVE_NOW — score mémoire 7.737/10 — sources V4 — WATCH_ONLY
- VET-EUR — ACTIVE_NOW — score mémoire 7.706/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- INJ-EUR — ACTIVE_NOW — score mémoire 7.705/10 — sources DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- YGG-EUR — ACTIVE_NOW — score mémoire 7.686/10 — sources V4 — WATCH_ONLY

## Audit des plus fortes hausses

- AVA-EUR +85.14% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- AGI-EUR +24.38% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- FOLD-EUR +23.11% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- DGB-EUR +21.07% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- QUID-EUR +18.41% — DETECTED_TOO_LATE — couche NONE — action INTERPRETATION
- PEAQ-EUR +18.32% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- TREAD-EUR +17.47% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- LIGHTER-EUR +16.43% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- NEAR-EUR +16.08% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- EDEN-EUR +15.73% — DETECTED_EARLY — couche NONE — action INTERPRETATION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
