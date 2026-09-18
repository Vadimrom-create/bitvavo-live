# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-18T03:10:29.084868+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : aucun candidat matériel
- **MEILLEUR_LATENT_ACCELERATOR** : aucun candidat matériel
- **MEILLEUR_PULLBACK_REENTRY** : TAO-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.309 | entrée 7.850 | trend 7.650 | rang 7.565
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. TAO-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.565
2. DOT-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.274

## Accélération indépendante

- ARB-EUR — CONFIRMED_ACCELERATION — score 9.889/10 — DETECTED_BUT_TOO_LATE
- NEAR-EUR — CONFIRMED_ACCELERATION — score 8.018/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- ARB-EUR — ACTIVE_NOW — score mémoire 9.889/10 — sources ACCELERATION, V4 — DETECTED_BUT_TOO_LATE
- CNPY-EUR — MEMORY_24H — score mémoire 9.527/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- LDO-EUR — ACTIVE_NOW — score mémoire 8.318/10 — sources V4 — WATCH_ONLY
- YB-EUR — ACTIVE_NOW — score mémoire 8.275/10 — sources V4 — WATCH_ONLY
- ICP-EUR — ACTIVE_NOW — score mémoire 8.182/10 — sources V4 — WATCH_ONLY
- VET-EUR — ACTIVE_NOW — score mémoire 8.075/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- METIS-EUR — ACTIVE_NOW — score mémoire 8.050/10 — sources V4 — DETECTED_BUT_TOO_LATE
- ETHFI-EUR — ACTIVE_NOW — score mémoire 8.042/10 — sources V4 — WATCH_ONLY
- KAS-EUR — ACTIVE_NOW — score mémoire 8.031/10 — sources DECISION_LAYER, V4 — WATCH_ONLY
- NEAR-EUR — ACTIVE_NOW — score mémoire 8.018/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE

## Audit des plus fortes hausses

- TREAD-EUR +66.22% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- AVA-EUR +56.97% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- DRIFT-EUR +41.69% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- COTI-EUR +35.95% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- CNPY-EUR +33.38% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ARB-EUR +29.84% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- NEAR-EUR +28.58% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- CROSS-EUR +25.03% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- UNI-EUR +18.65% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- APT-EUR +18.49% — DETECTED_EARLY — couche NONE — action INTERPRETATION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
