# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-16T20:56:14.241292+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : aucun candidat matériel
- **MEILLEUR_LATENT_ACCELERATOR** : aucun candidat matériel
- **MEILLEUR_PULLBACK_REENTRY** : VET-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 9.301 | entrée 7.050 | trend 8.650 | rang 8.338
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. VET-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.338
2. USELESS-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.331
3. TAO-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.269

## Accélération indépendante

Aucune accélération indépendante confirmée ou en construction.

## Watchlist persistante 24–72 h

- VET-EUR — ACTIVE_NOW — score mémoire 8.338/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- VTHO-EUR — ACTIVE_NOW — score mémoire 8.154/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- GRT-EUR — ACTIVE_NOW — score mémoire 8.067/10 — sources V4 — WATCH_ONLY
- FET-EUR — ACTIVE_NOW — score mémoire 8.013/10 — sources DECISION_LAYER, V4 — WATCH_ONLY
- LDO-EUR — ACTIVE_NOW — score mémoire 7.991/10 — sources V4 — WATCH_ONLY
- PHA-EUR — ACTIVE_NOW — score mémoire 7.924/10 — sources V4 — WATCH_ONLY
- ICP-EUR — ACTIVE_NOW — score mémoire 7.921/10 — sources V4 — WATCH_ONLY
- ETHFI-EUR — ACTIVE_NOW — score mémoire 7.896/10 — sources V4 — WATCH_ONLY
- PROM-EUR — ACTIVE_NOW — score mémoire 7.888/10 — sources V4 — WATCH_ONLY
- SOMI-EUR — ACTIVE_NOW — score mémoire 7.736/10 — sources V4 — WATCH_ONLY

## Audit des plus fortes hausses

- SYN-EUR +129.21% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- LSK-EUR +85.70% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- HEI-EUR +30.16% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- HNT-EUR +20.99% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- FOLD-EUR +19.82% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- RAY-EUR +14.42% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- IOST-EUR +14.17% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- LIGHTER-EUR +12.27% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ARB-EUR +11.78% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- NEAR-EUR +11.53% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
