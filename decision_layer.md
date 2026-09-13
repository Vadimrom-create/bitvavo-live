# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-13T23:17:09.587329+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : aucun candidat matériel
- **MEILLEUR_LATENT_ACCELERATOR** : aucun candidat matériel
- **MEILLEUR_PULLBACK_REENTRY** : VET-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 7.542 | entrée 6.350 | trend 8.650 | rang 7.585
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. VET-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.585
2. VTHO-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.004

## Accélération indépendante

- LAPTOP-EUR — BUILDING_ACCELERATION — score 6.437/10 — REQUIRES_V4_ENTRY_AND_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- LDO-EUR — ACTIVE_NOW — score mémoire 7.978/10 — sources V4 — WATCH_ONLY
- YB-EUR — ACTIVE_NOW — score mémoire 7.770/10 — sources V4 — WATCH_ONLY
- APT-EUR — MEMORY_24H — score mémoire 7.715/10 — sources V4 — MEMORY_ONLY
- ICP-EUR — ACTIVE_NOW — score mémoire 7.659/10 — sources V4 — WATCH_ONLY
- ETHFI-EUR — ACTIVE_NOW — score mémoire 7.608/10 — sources V4 — WATCH_ONLY
- VET-EUR — ACTIVE_NOW — score mémoire 7.585/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- ZIG-EUR — MEMORY_24H — score mémoire 7.576/10 — sources V4 — MEMORY_ONLY
- XVG-EUR — ACTIVE_NOW — score mémoire 7.510/10 — sources V4 — WATCH_ONLY
- CATI-EUR — ACTIVE_NOW — score mémoire 7.480/10 — sources V4 — WATCH_ONLY
- TREE-EUR — MEMORY_24H — score mémoire 7.466/10 — sources V4 — MEMORY_ONLY

## Audit des plus fortes hausses

- LSK-EUR +199.27% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- CVC-EUR +40.46% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- ZKJ-EUR +25.17% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- FIL-EUR +16.88% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- VTHO-EUR +16.45% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- SOLV-EUR +14.78% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- IQ-EUR +14.45% — DETECTED_TOO_LATE — couche NONE — action INTERPRETATION
- POWR-EUR +9.75% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- BIRB-EUR +9.36% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE
- ZIL-EUR +8.70% — DETECTED_EARLY — couche NONE — action INTERPRETATION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
