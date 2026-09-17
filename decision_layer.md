# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-17T01:00:02.962422+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : aucun candidat matériel
- **MEILLEUR_LATENT_ACCELERATOR** : aucun candidat matériel
- **MEILLEUR_PULLBACK_REENTRY** : VTHO-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 9.000 | entrée 7.350 | trend 9.200 | rang 8.454
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. VTHO-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.454
2. NEAR-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.500

## Accélération indépendante

- LAPTOP-EUR — CONFIRMED_ACCELERATION — score 7.266/10 — REQUIRES_V4_ENTRY_AND_EXECUTION_VALIDATION
- VTHO-EUR — BUILDING_ACCELERATION — score 5.474/10 — REQUIRES_V4_ENTRY_AND_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- VTHO-EUR — ACTIVE_NOW — score mémoire 8.454/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- XVG-EUR — ACTIVE_NOW — score mémoire 8.386/10 — sources V4 — WATCH_ONLY
- LDO-EUR — ACTIVE_NOW — score mémoire 8.198/10 — sources V4 — WATCH_ONLY
- YB-EUR — ACTIVE_NOW — score mémoire 8.065/10 — sources V4 — WATCH_ONLY
- MASK-EUR — ACTIVE_NOW — score mémoire 8.054/10 — sources V4 — WATCH_ONLY
- ICP-EUR — ACTIVE_NOW — score mémoire 8.025/10 — sources V4 — WATCH_ONLY
- ETHFI-EUR — ACTIVE_NOW — score mémoire 8.024/10 — sources V4 — WATCH_ONLY
- ZRO-EUR — ACTIVE_NOW — score mémoire 8.007/10 — sources V4 — WATCH_ONLY
- INJ-EUR — ACTIVE_NOW — score mémoire 8.001/10 — sources DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- JUP-EUR — ACTIVE_NOW — score mémoire 7.842/10 — sources V4 — WATCH_ONLY

## Audit des plus fortes hausses

- SYN-EUR +75.43% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- LSK-EUR +31.12% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- DGB-EUR +23.99% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- FOLD-EUR +21.68% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- LIGHTER-EUR +17.70% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- AGI-EUR +15.23% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- IOST-EUR +15.15% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- TRAC-EUR +15.06% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE
- RAY-EUR +14.85% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- NEAR-EUR +14.57% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
