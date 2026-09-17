# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-17T21:54:55.706850+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : aucun candidat matériel
- **MEILLEUR_LATENT_ACCELERATOR** : aucun candidat matériel
- **MEILLEUR_PULLBACK_REENTRY** : LSK-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 7.898 | entrée 5.500 | trend 8.400 | rang 7.413
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. LSK-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.413
2. NEAR-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 6.477

## Accélération indépendante

- TREAD-EUR — BUILDING_ACCELERATION — score 6.107/10 — DETECTED_BUT_TOO_LATE
- COTI-EUR — BUILDING_ACCELERATION — score 5.229/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- CNPY-EUR — MEMORY_24H — score mémoire 9.527/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- VTHO-EUR — ACTIVE_NOW — score mémoire 8.189/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- AKT-EUR — ACTIVE_NOW — score mémoire 7.972/10 — sources DECISION_LAYER, V4 — WATCH_ONLY
- LDO-EUR — ACTIVE_NOW — score mémoire 7.923/10 — sources V4 — WATCH_ONLY
- METIS-EUR — ACTIVE_NOW — score mémoire 7.872/10 — sources V4 — WATCH_ONLY
- XVG-EUR — ACTIVE_NOW — score mémoire 7.841/10 — sources V4 — WATCH_ONLY
- ETHFI-EUR — ACTIVE_NOW — score mémoire 7.782/10 — sources V4 — WATCH_ONLY
- SOMI-EUR — ACTIVE_NOW — score mémoire 7.697/10 — sources V4 — WATCH_ONLY
- ATOM-EUR — ACTIVE_NOW — score mémoire 7.664/10 — sources V4 — WATCH_ONLY
- VET-EUR — ACTIVE_NOW — score mémoire 7.644/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY

## Audit des plus fortes hausses

- AVA-EUR +80.76% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- COTI-EUR +44.29% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- CROSS-EUR +42.34% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- CNPY-EUR +41.18% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- TREAD-EUR +39.54% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- AGI-EUR +26.76% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- G-EUR +23.80% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- PEAQ-EUR +20.61% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- UNI-EUR +19.91% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- DRIFT-EUR +18.66% — DETECTED_EARLY — couche NONE — action INTERPRETATION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
