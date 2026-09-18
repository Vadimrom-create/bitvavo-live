# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-18T01:47:40.535447+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : aucun candidat matériel
- **MEILLEUR_LATENT_ACCELERATOR** : aucun candidat matériel
- **MEILLEUR_PULLBACK_REENTRY** : DOT-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.138 | entrée 7.250 | trend 8.300 | rang 7.494
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. DOT-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.494
2. NEAR-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 6.453

## Accélération indépendante

- TREAD-EUR — CONFIRMED_ACCELERATION — score 6.861/10 — DETECTED_BUT_TOO_LATE
- LSK-EUR — BUILDING_ACCELERATION — score 6.043/10 — REQUIRES_V4_ENTRY_AND_EXECUTION_VALIDATION
- DRIFT-EUR — BUILDING_ACCELERATION — score 5.133/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- CNPY-EUR — MEMORY_24H — score mémoire 9.527/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- YB-EUR — ACTIVE_NOW — score mémoire 8.650/10 — sources V4 — WATCH_ONLY
- LDO-EUR — ACTIVE_NOW — score mémoire 8.350/10 — sources V4 — WATCH_ONLY
- ETHFI-EUR — ACTIVE_NOW — score mémoire 8.306/10 — sources V4 — WATCH_ONLY
- KAS-EUR — ACTIVE_NOW — score mémoire 8.194/10 — sources DECISION_LAYER, V4 — WATCH_ONLY
- ICP-EUR — ACTIVE_NOW — score mémoire 8.024/10 — sources V4 — WATCH_ONLY
- METIS-EUR — ACTIVE_NOW — score mémoire 8.014/10 — sources V4 — DETECTED_BUT_TOO_LATE
- ZRO-EUR — ACTIVE_NOW — score mémoire 7.995/10 — sources V4 — WATCH_ONLY
- FORM-EUR — ACTIVE_NOW — score mémoire 7.934/10 — sources V4 — WATCH_ONLY
- VET-EUR — ACTIVE_NOW — score mémoire 7.925/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY

## Audit des plus fortes hausses

- AVA-EUR +67.12% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- TREAD-EUR +42.08% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- DRIFT-EUR +42.06% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- CNPY-EUR +39.73% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- COTI-EUR +32.24% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- NEAR-EUR +22.65% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- CROSS-EUR +21.95% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- AGI-EUR +19.72% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- ARB-EUR +17.47% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- PEAQ-EUR +16.43% — DETECTED_EARLY — couche NONE — action INTERPRETATION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
