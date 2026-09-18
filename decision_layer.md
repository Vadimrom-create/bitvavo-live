# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-18T22:37:39.364801+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : aucun candidat matériel
- **MEILLEUR_LATENT_ACCELERATOR** : aucun candidat matériel
- **MEILLEUR_PULLBACK_REENTRY** : USELESS-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 7.619 | entrée 6.850 | trend 8.100 | rang 6.896
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. USELESS-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 6.896

## Accélération indépendante

- STRK-EUR — BUILDING_ACCELERATION — score 5.176/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- VTHO-EUR — ACTIVE_NOW — score mémoire 8.127/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- YB-EUR — ACTIVE_NOW — score mémoire 8.039/10 — sources V4 — WATCH_ONLY
- LDO-EUR — ACTIVE_NOW — score mémoire 8.003/10 — sources V4 — DETECTED_BUT_TOO_LATE
- XVG-EUR — ACTIVE_NOW — score mémoire 7.740/10 — sources V4 — WATCH_ONLY
- ICP-EUR — ACTIVE_NOW — score mémoire 7.736/10 — sources DECISION_LAYER, V4 — WATCH_ONLY
- VET-EUR — ACTIVE_NOW — score mémoire 7.689/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- SIGN-EUR — ACTIVE_NOW — score mémoire 7.633/10 — sources V4 — WATCH_ONLY
- CVX-EUR — MEMORY_24H — score mémoire 7.542/10 — sources V4 — MEMORY_ONLY
- METIS-EUR — ACTIVE_NOW — score mémoire 7.540/10 — sources V4 — WATCH_ONLY
- FORM-EUR — ACTIVE_NOW — score mémoire 7.540/10 — sources V4 — WATCH_ONLY

## Audit des plus fortes hausses

- F-EUR +72.80% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- STRK-EUR +53.14% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- G-EUR +47.64% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- ARB-EUR +24.65% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ZIG-EUR +23.88% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- APT-EUR +23.06% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- NEAR-EUR +22.40% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- ZAMA-EUR +21.73% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ZK-EUR +21.04% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE
- S-EUR +20.65% — DETECTED_EARLY — couche NONE — action INTERPRETATION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
