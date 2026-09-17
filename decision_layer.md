# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-17T17:27:25.667579+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : aucun candidat matériel
- **MEILLEUR_LATENT_ACCELERATOR** : aucun candidat matériel
- **MEILLEUR_PULLBACK_REENTRY** : FET-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.210 | entrée 7.650 | trend 7.650 | rang 7.229
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. FET-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.229
2. NEAR-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 6.692

## Accélération indépendante

- CNPY-EUR — CONFIRMED_ACCELERATION — score 9.527/10 — REQUIRES_V4_ENTRY_AND_EXECUTION_VALIDATION
- DRIFT-EUR — BUILDING_ACCELERATION — score 5.269/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- CNPY-EUR — ACTIVE_NOW — score mémoire 9.527/10 — sources ACCELERATION, V4 — WATCH_ONLY
- VET-EUR — ACTIVE_NOW — score mémoire 8.353/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- LDO-EUR — ACTIVE_NOW — score mémoire 8.270/10 — sources V4 — WATCH_ONLY
- YB-EUR — ACTIVE_NOW — score mémoire 8.114/10 — sources V4 — WATCH_ONLY
- ICP-EUR — ACTIVE_NOW — score mémoire 8.015/10 — sources V4 — WATCH_ONLY
- ZIL-EUR — ACTIVE_NOW — score mémoire 7.914/10 — sources DECISION_LAYER, V4 — WATCH_ONLY
- ETHFI-EUR — ACTIVE_NOW — score mémoire 7.914/10 — sources V4 — WATCH_ONLY
- XVG-EUR — ACTIVE_NOW — score mémoire 7.891/10 — sources V4 — WATCH_ONLY
- ZRO-EUR — ACTIVE_NOW — score mémoire 7.879/10 — sources V4 — WATCH_ONLY
- KAS-EUR — ACTIVE_NOW — score mémoire 7.873/10 — sources DECISION_LAYER, V4 — WATCH_ONLY

## Audit des plus fortes hausses

- AVA-EUR +96.01% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- KSM-EUR +32.21% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- AGI-EUR +31.99% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- UNI-EUR +25.44% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- CROSS-EUR +23.80% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- NEAR-EUR +22.61% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- PEAQ-EUR +20.12% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- FOLD-EUR +19.89% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- GALA-EUR +18.65% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- ROSE-EUR +16.90% — DETECTED_EARLY — couche NONE — action INTERPRETATION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
