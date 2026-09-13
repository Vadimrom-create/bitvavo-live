# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-13T23:32:44.705211+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : aucun candidat matériel
- **MEILLEUR_LATENT_ACCELERATOR** : VTHO-EUR | action LATENT_ACCELERATOR | opportunité 7.679 | entrée 4.950 | trend 9.200 | rang 6.898
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : FET-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 7.091 | entrée 6.000 | trend 7.650 | rang 6.856
  - Trend remains strong; candidate retained for re-entry instead of discarded.

## Top cross-sectionnel

1. VTHO-EUR — MEILLEUR_LATENT_ACCELERATOR — LATENT_ACCELERATOR — rank 6.898
2. FET-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 6.856

## Accélération indépendante

Aucune accélération indépendante confirmée ou en construction.

## Watchlist persistante 24–72 h

- LDO-EUR — ACTIVE_NOW — score mémoire 7.977/10 — sources V4 — WATCH_ONLY
- YB-EUR — ACTIVE_NOW — score mémoire 7.867/10 — sources V4 — WATCH_ONLY
- ICP-EUR — ACTIVE_NOW — score mémoire 7.743/10 — sources V4 — WATCH_ONLY
- APT-EUR — MEMORY_24H — score mémoire 7.715/10 — sources V4 — MEMORY_ONLY
- VET-EUR — ACTIVE_NOW — score mémoire 7.672/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- ETHFI-EUR — ACTIVE_NOW — score mémoire 7.591/10 — sources V4 — WATCH_ONLY
- ZIG-EUR — MEMORY_24H — score mémoire 7.576/10 — sources V4 — MEMORY_ONLY
- XVG-EUR — ACTIVE_NOW — score mémoire 7.473/10 — sources V4 — WATCH_ONLY
- TREE-EUR — MEMORY_24H — score mémoire 7.466/10 — sources V4 — MEMORY_ONLY
- NEAR-EUR — ACTIVE_NOW — score mémoire 7.454/10 — sources DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE

## Audit des plus fortes hausses

- LSK-EUR +125.11% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- CVC-EUR +36.48% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- ZKJ-EUR +22.83% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- FIL-EUR +17.10% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- VTHO-EUR +16.44% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- SOLV-EUR +14.47% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- IQ-EUR +13.58% — DETECTED_TOO_LATE — couche NONE — action INTERPRETATION
- BIRB-EUR +11.52% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE
- ZIL-EUR +8.85% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- POWR-EUR +8.26% — DETECTED_EARLY — couche NONE — action INTERPRETATION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
