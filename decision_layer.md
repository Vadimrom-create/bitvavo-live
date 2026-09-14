# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-14T17:47:29.387802+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : aucun candidat matériel
- **MEILLEUR_LATENT_ACCELERATOR** : aucun candidat matériel
- **MEILLEUR_PULLBACK_REENTRY** : VTHO-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 7.851 | entrée 5.350 | trend 9.200 | rang 7.806
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. VTHO-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.806
2. TAO-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.294
3. NEAR-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.032

## Accélération indépendante

Aucune accélération indépendante confirmée ou en construction.

## Watchlist persistante 24–72 h

- ETHFI-EUR — ACTIVE_NOW — score mémoire 8.527/10 — sources V4 — WATCH_ONLY
- SOMI-EUR — ACTIVE_NOW — score mémoire 8.262/10 — sources V4 — WATCH_ONLY
- VET-EUR — ACTIVE_NOW — score mémoire 8.091/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- LDO-EUR — ACTIVE_NOW — score mémoire 8.073/10 — sources V4 — WATCH_ONLY
- ZIL-EUR — ACTIVE_NOW — score mémoire 8.059/10 — sources DECISION_LAYER, V4 — WATCH_ONLY
- WLD-EUR — ACTIVE_NOW — score mémoire 8.042/10 — sources DECISION_LAYER, V4 — WATCH_ONLY
- GRT-EUR — ACTIVE_NOW — score mémoire 7.949/10 — sources V4 — WATCH_ONLY
- STRK-EUR — ACTIVE_NOW — score mémoire 7.830/10 — sources V4 — WATCH_ONLY
- ICP-EUR — ACTIVE_NOW — score mémoire 7.807/10 — sources V4 — WATCH_ONLY
- VTHO-EUR — ACTIVE_NOW — score mémoire 7.806/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY

## Audit des plus fortes hausses

- CNPY-EUR +34.76% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- CPOOL-EUR +32.97% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- CAP-EUR +21.59% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- QKC-EUR +17.14% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- MTL-EUR +15.17% — DETECTED_TOO_LATE — couche NONE — action INTERPRETATION
- SENT-EUR +13.71% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ARK-EUR +12.71% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- NPC-EUR +10.61% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- T-EUR +10.54% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- PENDLE-EUR +9.84% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
