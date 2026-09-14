# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-14T06:15:35.313998+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : aucun candidat matériel
- **MEILLEUR_LATENT_ACCELERATOR** : aucun candidat matériel
- **MEILLEUR_PULLBACK_REENTRY** : VTHO-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.650 | entrée 6.300 | trend 9.200 | rang 7.998
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. VTHO-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.998
2. USELESS-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.398

## Accélération indépendante

- POWR-EUR — CONFIRMED_ACCELERATION — score 7.575/10 — DETECTED_BUT_TOO_LATE
- LSK-EUR — BUILDING_ACCELERATION — score 6.399/10 — REQUIRES_V4_ENTRY_AND_EXECUTION_VALIDATION
- SUI-EUR — BUILDING_ACCELERATION — score 4.826/10 — REQUIRES_V4_ENTRY_AND_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- LDO-EUR — ACTIVE_NOW — score mémoire 8.608/10 — sources V4 — WATCH_ONLY
- PHA-EUR — ACTIVE_NOW — score mémoire 8.225/10 — sources V4 — WATCH_ONLY
- WLD-EUR — ACTIVE_NOW — score mémoire 8.142/10 — sources DECISION_LAYER, V4 — WATCH_ONLY
- CVC-EUR — MEMORY_24H — score mémoire 8.123/10 — sources ACCELERATION — MEMORY_ONLY
- ZETA-EUR — ACTIVE_NOW — score mémoire 8.055/10 — sources V4 — WATCH_ONLY
- LAPTOP-EUR — MEMORY_24H — score mémoire 8.013/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- VTHO-EUR — ACTIVE_NOW — score mémoire 7.998/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- FET-EUR — ACTIVE_NOW — score mémoire 7.998/10 — sources DECISION_LAYER, V4 — WATCH_ONLY
- VET-EUR — ACTIVE_NOW — score mémoire 7.977/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- NEAR-EUR — ACTIVE_NOW — score mémoire 7.966/10 — sources DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE

## Audit des plus fortes hausses

- CVC-EUR +35.77% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- REZ-EUR +34.65% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- ARK-EUR +26.10% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- FIL-EUR +22.05% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- MTL-EUR +21.82% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- CPOOL-EUR +21.68% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- IQ-EUR +14.74% — DETECTED_TOO_LATE — couche NONE — action INTERPRETATION
- ZKJ-EUR +12.32% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- CNPY-EUR +11.24% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- BABY-EUR +10.47% — DETECTED_EARLY — couche NONE — action INTERPRETATION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
