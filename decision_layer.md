# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-18T00:39:35.532709+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : aucun candidat matériel
- **MEILLEUR_LATENT_ACCELERATOR** : aucun candidat matériel
- **MEILLEUR_PULLBACK_REENTRY** : LSK-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 7.768 | entrée 5.950 | trend 8.400 | rang 7.212
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. LSK-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.212
2. PHA-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.025
3. UNI-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 6.464

## Accélération indépendante

- LSK-EUR — CONFIRMED_ACCELERATION — score 7.747/10 — REQUIRES_V4_ENTRY_AND_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- CNPY-EUR — MEMORY_24H — score mémoire 9.527/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- YB-EUR — ACTIVE_NOW — score mémoire 8.186/10 — sources V4 — WATCH_ONLY
- XVG-EUR — ACTIVE_NOW — score mémoire 8.113/10 — sources V4 — WATCH_ONLY
- VTHO-EUR — ACTIVE_NOW — score mémoire 7.976/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- ETHFI-EUR — ACTIVE_NOW — score mémoire 7.938/10 — sources V4 — WATCH_ONLY
- LDO-EUR — ACTIVE_NOW — score mémoire 7.937/10 — sources V4 — WATCH_ONLY
- ICP-EUR — ACTIVE_NOW — score mémoire 7.764/10 — sources V4 — WATCH_ONLY
- LSK-EUR — ACTIVE_NOW — score mémoire 7.747/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- FET-EUR — ACTIVE_NOW — score mémoire 7.722/10 — sources DECISION_LAYER, V4 — WATCH_ONLY
- SOMI-EUR — ACTIVE_NOW — score mémoire 7.666/10 — sources V4 — WATCH_ONLY

## Audit des plus fortes hausses

- AVA-EUR +73.39% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- TREAD-EUR +53.49% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- COTI-EUR +44.77% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- CNPY-EUR +42.70% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- CROSS-EUR +36.24% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- DRIFT-EUR +25.77% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- AGI-EUR +21.36% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- BABY-EUR +19.58% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE
- PEAQ-EUR +15.63% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- FOLD-EUR +15.33% — DETECTED_EARLY — couche NONE — action INTERPRETATION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
