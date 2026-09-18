# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-18T03:46:27.108316+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : aucun candidat matériel
- **MEILLEUR_LATENT_ACCELERATOR** : aucun candidat matériel
- **MEILLEUR_PULLBACK_REENTRY** : TAO-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.434 | entrée 7.400 | trend 7.650 | rang 7.593
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. TAO-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.593
2. WLD-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.538
3. DOT-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.243

## Accélération indépendante

- RAY-EUR — CONFIRMED_ACCELERATION — score 6.543/10 — DETECTED_BUT_TOO_LATE
- UNI-EUR — BUILDING_ACCELERATION — score 5.831/10 — DETECTED_BUT_TOO_LATE
- DRIFT-EUR — BUILDING_ACCELERATION — score 5.512/10 — DETECTED_BUT_TOO_LATE
- WLD-EUR — BUILDING_ACCELERATION — score 5.260/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- CNPY-EUR — MEMORY_24H — score mémoire 9.527/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- ETHFI-EUR — ACTIVE_NOW — score mémoire 8.453/10 — sources V4 — DETECTED_BUT_TOO_LATE
- LDO-EUR — ACTIVE_NOW — score mémoire 8.268/10 — sources V4 — WATCH_ONLY
- VET-EUR — ACTIVE_NOW — score mémoire 8.244/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- YB-EUR — ACTIVE_NOW — score mémoire 8.057/10 — sources V4 — WATCH_ONLY
- ICP-EUR — ACTIVE_NOW — score mémoire 8.047/10 — sources V4 — WATCH_ONLY
- KAS-EUR — ACTIVE_NOW — score mémoire 8.028/10 — sources DECISION_LAYER, V4 — WATCH_ONLY
- VTHO-EUR — ACTIVE_NOW — score mémoire 8.004/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- XVG-EUR — ACTIVE_NOW — score mémoire 7.998/10 — sources V4 — WATCH_ONLY
- PROM-EUR — ACTIVE_NOW — score mémoire 7.980/10 — sources V4 — WATCH_ONLY

## Audit des plus fortes hausses

- TREAD-EUR +62.05% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- AVA-EUR +56.02% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- COTI-EUR +36.55% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ARB-EUR +34.00% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- DRIFT-EUR +31.33% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- CROSS-EUR +28.72% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- UNI-EUR +28.20% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- NEAR-EUR +26.35% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- APT-EUR +25.67% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- CNPY-EUR +23.95% — DETECTED_EARLY — couche NONE — action INTERPRETATION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
