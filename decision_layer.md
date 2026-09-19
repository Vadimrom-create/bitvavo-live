# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-19T15:47:03.135794+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : HYPE-EUR | action ACHETE_MAINTENANT | opportunité 8.149 | entrée 7.450 | trend 8.750 | rang 7.991
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : aucun candidat matériel
- **MEILLEUR_LATENT_ACCELERATOR** : UNI-EUR | action LATENT_ACCELERATOR | opportunité 7.480 | entrée 4.500 | trend 8.150 | rang 6.915
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : TAO-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 7.904 | entrée 7.350 | trend 8.300 | rang 7.660
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. HYPE-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 7.991
2. PEPE-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 7.925
3. TAO-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.660

## Accélération indépendante

- G-EUR — CONFIRMED_ACCELERATION — score 10.000/10 — DETECTED_BUT_TOO_LATE
- INJ-EUR — BUILDING_ACCELERATION — score 6.147/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- G-EUR — ACTIVE_NOW — score mémoire 10.000/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- PYTH-EUR — ACTIVE_NOW — score mémoire 8.396/10 — sources V4 — WATCH_ONLY
- KSM-EUR — ACTIVE_NOW — score mémoire 8.144/10 — sources V4 — WATCH_ONLY
- VVV-EUR — ACTIVE_NOW — score mémoire 8.037/10 — sources DECISION_LAYER, V4 — WATCH_ONLY
- HYPE-EUR — ACTIVE_NOW — score mémoire 7.991/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- AAVE-EUR — ACTIVE_NOW — score mémoire 7.986/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- W-EUR — ACTIVE_NOW — score mémoire 7.955/10 — sources V4 — WATCH_ONLY
- PEPE-EUR — ACTIVE_NOW — score mémoire 7.925/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- SENT-EUR — ACTIVE_NOW — score mémoire 7.911/10 — sources V4 — WATCH_ONLY
- MIOTA-EUR — ACTIVE_NOW — score mémoire 7.893/10 — sources V4 — WATCH_ONLY

## Audit des plus fortes hausses

- ZAMA-EUR +42.34% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- XTZ-EUR +33.92% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- SYN-EUR +32.50% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- EPIC-EUR +28.60% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- SAGA-EUR +23.90% — DETECTED_TOO_LATE — couche NONE — action INTERPRETATION
- EDGE-EUR +22.48% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- AIOZ-EUR +21.19% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ENA-EUR +21.09% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- STRK-EUR +20.75% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- NOS-EUR +16.67% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
