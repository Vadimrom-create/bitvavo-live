# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-18T06:41:14.053778+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : aucun candidat matériel
- **MEILLEUR_LATENT_ACCELERATOR** : COTI-EUR | action LATENT_ACCELERATOR | opportunité 7.663 | entrée 5.150 | trend 8.300 | rang 5.705
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : WLD-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.058 | entrée 7.450 | trend 8.150 | rang 7.232
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. WLD-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.232
2. USELESS-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.124
3. DOT-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.102

## Accélération indépendante

- DRIFT-EUR — BUILDING_ACCELERATION — score 6.269/10 — DETECTED_BUT_TOO_LATE
- RAY-EUR — BUILDING_ACCELERATION — score 5.262/10 — DETECTED_BUT_TOO_LATE
- COTI-EUR — BUILDING_ACCELERATION — score 5.260/10 — DETECTED_BUT_TOO_LATE
- ENA-EUR — BUILDING_ACCELERATION — score 5.027/10 — REQUIRES_V4_ENTRY_AND_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- KAS-EUR — ACTIVE_NOW — score mémoire 8.495/10 — sources DECISION_LAYER, V4 — WATCH_ONLY
- TREAD-EUR — MEMORY_24H — score mémoire 8.374/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- ATOM-EUR — ACTIVE_NOW — score mémoire 8.285/10 — sources V4 — DETECTED_BUT_TOO_LATE
- LDO-EUR — ACTIVE_NOW — score mémoire 8.130/10 — sources V4 — WATCH_ONLY
- VET-EUR — ACTIVE_NOW — score mémoire 8.024/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- VTHO-EUR — ACTIVE_NOW — score mémoire 7.964/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- ETHFI-EUR — ACTIVE_NOW — score mémoire 7.860/10 — sources V4 — WATCH_ONLY
- VELO-EUR — ACTIVE_NOW — score mémoire 7.846/10 — sources V4 — WATCH_ONLY
- SOMI-EUR — ACTIVE_NOW — score mémoire 7.780/10 — sources V4 — WATCH_ONLY
- ICP-EUR — ACTIVE_NOW — score mémoire 7.751/10 — sources V4 — WATCH_ONLY

## Audit des plus fortes hausses

- DRIFT-EUR +40.92% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- COTI-EUR +35.03% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- CNPY-EUR +28.97% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- NEAR-EUR +28.21% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- ARB-EUR +28.03% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- CROSS-EUR +27.40% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- UNI-EUR +26.29% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- MET-EUR +21.18% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE
- RAY-EUR +21.05% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- G-EUR +20.96% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
