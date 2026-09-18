# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-18T05:08:27.252561+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : aucun candidat matériel
- **MEILLEUR_LATENT_ACCELERATOR** : aucun candidat matériel
- **MEILLEUR_PULLBACK_REENTRY** : DOT-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.449 | entrée 7.250 | trend 8.300 | rang 7.506
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. DOT-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.506
2. USELESS-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.342
3. SYRUP-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.301

## Accélération indépendante

- PUMP-EUR — CONFIRMED_ACCELERATION — score 8.449/10 — DETECTED_BUT_TOO_LATE
- TREAD-EUR — CONFIRMED_ACCELERATION — score 6.693/10 — DETECTED_BUT_TOO_LATE
- RAY-EUR — BUILDING_ACCELERATION — score 4.870/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- PUMP-EUR — ACTIVE_NOW — score mémoire 8.449/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- ENS-EUR — ACTIVE_NOW — score mémoire 8.248/10 — sources V4 — WATCH_ONLY
- ICP-EUR — ACTIVE_NOW — score mémoire 8.133/10 — sources V4 — WATCH_ONLY
- LDO-EUR — ACTIVE_NOW — score mémoire 8.087/10 — sources V4 — WATCH_ONLY
- ETHFI-EUR — ACTIVE_NOW — score mémoire 8.055/10 — sources V4 — WATCH_ONLY
- VET-EUR — ACTIVE_NOW — score mémoire 7.836/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- XVG-EUR — ACTIVE_NOW — score mémoire 7.832/10 — sources V4 — WATCH_ONLY
- KAS-EUR — ACTIVE_NOW — score mémoire 7.827/10 — sources DECISION_LAYER, V4 — WATCH_ONLY
- VTHO-EUR — ACTIVE_NOW — score mémoire 7.824/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- SOMI-EUR — ACTIVE_NOW — score mémoire 7.819/10 — sources V4 — WATCH_ONLY

## Audit des plus fortes hausses

- AVA-EUR +39.69% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- NEAR-EUR +31.88% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- COTI-EUR +29.89% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- CNPY-EUR +29.57% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- DRIFT-EUR +27.66% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- TREAD-EUR +26.59% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- CROSS-EUR +25.62% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- UNI-EUR +23.32% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ARB-EUR +23.30% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- AGI-EUR +21.31% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
