# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-18T03:28:55.391560+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : aucun candidat matériel
- **MEILLEUR_LATENT_ACCELERATOR** : aucun candidat matériel
- **MEILLEUR_PULLBACK_REENTRY** : TAO-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.097 | entrée 7.400 | trend 7.650 | rang 7.381
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. TAO-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.381
2. DOT-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.233

## Accélération indépendante

- RAY-EUR — CONFIRMED_ACCELERATION — score 8.687/10 — DETECTED_BUT_TOO_LATE
- UNI-EUR — CONFIRMED_ACCELERATION — score 8.669/10 — DETECTED_BUT_TOO_LATE
- ARB-EUR — CONFIRMED_ACCELERATION — score 7.703/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- CNPY-EUR — MEMORY_24H — score mémoire 9.527/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- RAY-EUR — ACTIVE_NOW — score mémoire 8.687/10 — sources ACCELERATION, V4 — DETECTED_BUT_TOO_LATE
- UNI-EUR — ACTIVE_NOW — score mémoire 8.669/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- ICP-EUR — ACTIVE_NOW — score mémoire 8.531/10 — sources V4 — WATCH_ONLY
- VET-EUR — ACTIVE_NOW — score mémoire 8.314/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- LDO-EUR — ACTIVE_NOW — score mémoire 8.218/10 — sources V4 — WATCH_ONLY
- ETHFI-EUR — ACTIVE_NOW — score mémoire 8.205/10 — sources V4 — WATCH_ONLY
- INJ-EUR — ACTIVE_NOW — score mémoire 8.189/10 — sources DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- YB-EUR — ACTIVE_NOW — score mémoire 8.186/10 — sources V4 — WATCH_ONLY
- KAS-EUR — ACTIVE_NOW — score mémoire 8.098/10 — sources DECISION_LAYER, V4 — WATCH_ONLY

## Audit des plus fortes hausses

- TREAD-EUR +58.89% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- AVA-EUR +50.92% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- COTI-EUR +34.39% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ARB-EUR +32.44% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- CROSS-EUR +31.23% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- DRIFT-EUR +28.42% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- NEAR-EUR +27.65% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- CNPY-EUR +26.53% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- UNI-EUR +24.81% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- APT-EUR +24.33% — DETECTED_EARLY — couche NONE — action INTERPRETATION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
