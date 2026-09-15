# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-15T10:03:25.698160+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : aucun candidat matériel
- **MEILLEUR_LATENT_ACCELERATOR** : aucun candidat matériel
- **MEILLEUR_PULLBACK_REENTRY** : UNI-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 7.492 | entrée 7.250 | trend 7.750 | rang 7.212
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. UNI-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.212
2. USELESS-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.150
3. TAO-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 6.998

## Accélération indépendante

Aucune accélération indépendante confirmée ou en construction.

## Watchlist persistante 24–72 h

- CAP-EUR — MEMORY_24H — score mémoire 8.685/10 — sources ACCELERATION — MEMORY_ONLY
- LAPTOP-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- SOMI-EUR — ACTIVE_NOW — score mémoire 8.194/10 — sources V4 — WATCH_ONLY
- VTHO-EUR — MEMORY_24H — score mémoire 8.054/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- ETHFI-EUR — ACTIVE_NOW — score mémoire 7.914/10 — sources V4 — WATCH_ONLY
- KAS-EUR — ACTIVE_NOW — score mémoire 7.785/10 — sources V4 — WATCH_ONLY
- LDO-EUR — ACTIVE_NOW — score mémoire 7.782/10 — sources V4 — WATCH_ONLY
- AIOZ-EUR — ACTIVE_NOW — score mémoire 7.657/10 — sources V4 — WATCH_ONLY
- PHA-EUR — ACTIVE_NOW — score mémoire 7.601/10 — sources V4 — WATCH_ONLY
- YB-EUR — ACTIVE_NOW — score mémoire 7.596/10 — sources V4 — WATCH_ONLY

## Audit des plus fortes hausses

- CAP-EUR +30.90% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- CNPY-EUR +27.81% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- PUFFER-EUR +25.85% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- SAGA-EUR +21.31% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- ASTR-EUR +14.70% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ACX-EUR +11.82% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- LAPTOP-EUR +9.30% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- CROSS-EUR +8.85% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- ACE-EUR +8.80% — DETECTED_TOO_LATE — couche NONE — action INTERPRETATION
- COTI-EUR +7.09% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
