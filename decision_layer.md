# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-19T02:18:19.159983+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : aucun candidat matériel
- **MEILLEUR_LATENT_ACCELERATOR** : aucun candidat matériel
- **MEILLEUR_PULLBACK_REENTRY** : ONDO-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.835 | entrée 7.200 | trend 7.650 | rang 7.732
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. ONDO-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.732
2. HYPE-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.695
3. SOL-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.258

## Accélération indépendante

- SYN-EUR — CONFIRMED_ACCELERATION — score 8.620/10 — DETECTED_BUT_TOO_LATE
- ONDO-EUR — BUILDING_ACCELERATION — score 5.472/10 — REQUIRES_V4_ENTRY_AND_EXECUTION_VALIDATION
- STRK-EUR — BUILDING_ACCELERATION — score 5.015/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- SYN-EUR — ACTIVE_NOW — score mémoire 8.620/10 — sources ACCELERATION, V4 — DETECTED_BUT_TOO_LATE
- PROVE-EUR — ACTIVE_NOW — score mémoire 8.397/10 — sources V4 — DETECTED_BUT_TOO_LATE
- VTHO-EUR — MEMORY_24H — score mémoire 8.268/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- PEPE-EUR — MEMORY_24H — score mémoire 8.255/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- ROSE-EUR — ACTIVE_NOW — score mémoire 8.079/10 — sources V4 — WATCH_ONLY
- AAVE-EUR — ACTIVE_NOW — score mémoire 7.973/10 — sources ACCELERATION, V4 — WATCH_ONLY
- KMNO-EUR — ACTIVE_NOW — score mémoire 7.915/10 — sources V4 — WATCH_ONLY
- PYTH-EUR — ACTIVE_NOW — score mémoire 7.836/10 — sources V4 — WATCH_ONLY
- BEAM-EUR — ACTIVE_NOW — score mémoire 7.816/10 — sources V4 — WATCH_ONLY
- COW-EUR — MEMORY_24H — score mémoire 7.799/10 — sources V4 — MEMORY_ONLY

## Audit des plus fortes hausses

- G-EUR +52.44% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- STRK-EUR +46.60% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- F-EUR +35.56% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- SYN-EUR +29.85% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- ZAMA-EUR +26.21% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- XTZ-EUR +22.17% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- S-EUR +21.46% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ZIG-EUR +21.37% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- APT-EUR +19.77% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ZK-EUR +19.63% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
