# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-18T22:51:32.032469+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : aucun candidat matériel
- **MEILLEUR_LATENT_ACCELERATOR** : aucun candidat matériel
- **MEILLEUR_PULLBACK_REENTRY** : WLD-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 7.406 | entrée 6.300 | trend 8.150 | rang 6.883
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. WLD-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 6.883

## Accélération indépendante

- TREAD-EUR — BUILDING_ACCELERATION — score 6.420/10 — REQUIRES_V4_ENTRY_AND_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- VTHO-EUR — ACTIVE_NOW — score mémoire 8.161/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- XVG-EUR — ACTIVE_NOW — score mémoire 7.960/10 — sources V4 — WATCH_ONLY
- LDO-EUR — ACTIVE_NOW — score mémoire 7.948/10 — sources V4 — DETECTED_BUT_TOO_LATE
- YB-EUR — ACTIVE_NOW — score mémoire 7.882/10 — sources V4 — WATCH_ONLY
- SIGN-EUR — ACTIVE_NOW — score mémoire 7.812/10 — sources V4 — WATCH_ONLY
- VET-EUR — ACTIVE_NOW — score mémoire 7.715/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- ICP-EUR — ACTIVE_NOW — score mémoire 7.707/10 — sources DECISION_LAYER, V4 — WATCH_ONLY
- METIS-EUR — ACTIVE_NOW — score mémoire 7.683/10 — sources V4 — WATCH_ONLY
- CVX-EUR — MEMORY_24H — score mémoire 7.542/10 — sources V4 — MEMORY_ONLY
- ZIL-EUR — ACTIVE_NOW — score mémoire 7.509/10 — sources DECISION_LAYER, V4 — WATCH_ONLY

## Audit des plus fortes hausses

- F-EUR +68.99% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- STRK-EUR +54.67% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- G-EUR +52.50% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- ZIG-EUR +23.83% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ARB-EUR +23.16% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- APT-EUR +21.51% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ZK-EUR +21.50% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE
- C-EUR +20.79% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- NEAR-EUR +20.69% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- ZAMA-EUR +20.09% — DETECTED_EARLY — couche NONE — action INTERPRETATION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
