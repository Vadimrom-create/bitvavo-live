# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-17T12:15:33.783578+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : aucun candidat matériel
- **MEILLEUR_LATENT_ACCELERATOR** : aucun candidat matériel
- **MEILLEUR_PULLBACK_REENTRY** : TAO-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 7.719 | entrée 6.850 | trend 7.650 | rang 7.307
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. TAO-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.307
2. NEAR-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.005

## Accélération indépendante

- TREAD-EUR — BUILDING_ACCELERATION — score 5.739/10 — REQUIRES_V4_ENTRY_AND_EXECUTION_VALIDATION
- SYN-EUR — BUILDING_ACCELERATION — score 5.711/10 — REQUIRES_V4_ENTRY_AND_EXECUTION_VALIDATION
- UNI-EUR — BUILDING_ACCELERATION — score 4.829/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- AIOZ-EUR — ACTIVE_NOW — score mémoire 8.132/10 — sources V4 — WATCH_ONLY
- AVA-EUR — MEMORY_24H — score mémoire 8.087/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- FET-EUR — ACTIVE_NOW — score mémoire 8.069/10 — sources DECISION_LAYER, V4 — WATCH_ONLY
- ETHFI-EUR — ACTIVE_NOW — score mémoire 8.040/10 — sources V4 — WATCH_ONLY
- AERO-EUR — ACTIVE_NOW — score mémoire 7.935/10 — sources V4 — WATCH_ONLY
- LDO-EUR — ACTIVE_NOW — score mémoire 7.877/10 — sources V4 — WATCH_ONLY
- FORM-EUR — ACTIVE_NOW — score mémoire 7.858/10 — sources V4 — WATCH_ONLY
- VET-EUR — ACTIVE_NOW — score mémoire 7.816/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- ICP-EUR — ACTIVE_NOW — score mémoire 7.812/10 — sources V4 — WATCH_ONLY
- PHA-EUR — ACTIVE_NOW — score mémoire 7.810/10 — sources V4 — WATCH_ONLY

## Audit des plus fortes hausses

- AVA-EUR +89.51% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- QUID-EUR +25.59% — DETECTED_TOO_LATE — couche NONE — action INTERPRETATION
- FOLD-EUR +18.09% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- GLMR-EUR +17.60% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- NEAR-EUR +17.54% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- PEAQ-EUR +17.01% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- DGB-EUR +16.93% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- LIGHTER-EUR +14.56% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- HNT-EUR +14.10% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- USELESS-EUR +12.62% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
