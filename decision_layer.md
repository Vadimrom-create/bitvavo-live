# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-16T20:41:09.214369+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : aucun candidat matériel
- **MEILLEUR_LATENT_ACCELERATOR** : aucun candidat matériel
- **MEILLEUR_PULLBACK_REENTRY** : VET-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 9.372 | entrée 7.250 | trend 8.650 | rang 8.427
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. VET-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.427
2. INJ-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.238
3. TAO-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.212

## Accélération indépendante

- HEI-EUR — CONFIRMED_ACCELERATION — score 7.513/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- VET-EUR — ACTIVE_NOW — score mémoire 8.427/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- LDO-EUR — ACTIVE_NOW — score mémoire 8.234/10 — sources V4 — WATCH_ONLY
- VTHO-EUR — ACTIVE_NOW — score mémoire 8.060/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- W-EUR — ACTIVE_NOW — score mémoire 8.036/10 — sources V4 — WATCH_ONLY
- PROM-EUR — ACTIVE_NOW — score mémoire 8.016/10 — sources V4 — WATCH_ONLY
- FET-EUR — ACTIVE_NOW — score mémoire 7.925/10 — sources DECISION_LAYER, V4 — WATCH_ONLY
- DOT-EUR — ACTIVE_NOW — score mémoire 7.920/10 — sources DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- ETHFI-EUR — ACTIVE_NOW — score mémoire 7.916/10 — sources V4 — WATCH_ONLY
- ICP-EUR — ACTIVE_NOW — score mémoire 7.877/10 — sources V4 — WATCH_ONLY
- FORM-EUR — ACTIVE_NOW — score mémoire 7.761/10 — sources V4 — WATCH_ONLY

## Audit des plus fortes hausses

- SYN-EUR +137.20% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- LSK-EUR +80.05% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- HEI-EUR +30.50% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- FOLD-EUR +21.96% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- HNT-EUR +20.49% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- IOST-EUR +13.18% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- RAY-EUR +12.74% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- CNPY-EUR +12.66% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- LIGHTER-EUR +12.61% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- NEAR-EUR +11.31% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
