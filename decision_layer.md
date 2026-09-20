# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-20T01:20:38.932993+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : TAO-EUR | action ACHETE_MAINTENANT | opportunité 8.939 | entrée 7.050 | trend 7.700 | rang 7.928
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : aucun candidat matériel
- **MEILLEUR_LATENT_ACCELERATOR** : aucun candidat matériel
- **MEILLEUR_PULLBACK_REENTRY** : VET-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 7.762 | entrée 7.150 | trend 8.450 | rang 7.387
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. TAO-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 7.928
2. VET-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.387
3. SOL-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.009

## Accélération indépendante

- G-EUR — CONFIRMED_ACCELERATION — score 6.500/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- NPC-EUR — ACTIVE_NOW — score mémoire 8.159/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- WAL-EUR — ACTIVE_NOW — score mémoire 7.965/10 — sources V4 — WATCH_ONLY
- TAO-EUR — ACTIVE_NOW — score mémoire 7.928/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- CELR-EUR — MEMORY_24H — score mémoire 7.906/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- DOT-EUR — MEMORY_24H — score mémoire 7.831/10 — sources DECISION_LAYER, V4 — MEMORY_ONLY
- ZK-EUR — ACTIVE_NOW — score mémoire 7.801/10 — sources V4 — WATCH_ONLY
- ETC-EUR — MEMORY_24H — score mémoire 7.770/10 — sources V4 — MEMORY_ONLY
- STX-EUR — ACTIVE_NOW — score mémoire 7.749/10 — sources V4 — DETECTED_BUT_TOO_LATE
- PROVE-EUR — ACTIVE_NOW — score mémoire 7.737/10 — sources V4 — WATCH_ONLY
- ONDO-EUR — MEMORY_24H — score mémoire 7.735/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY

## Audit des plus fortes hausses

- CELR-EUR +81.40% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- G-EUR +53.56% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ZAMA-EUR +28.91% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ENA-EUR +23.05% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- EDGE-EUR +20.48% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- AVAX-EUR +20.13% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- ZIL-EUR +20.05% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- SKL-EUR +19.93% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- INJ-EUR +19.60% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- XTZ-EUR +17.76% — DETECTED_EARLY — couche NONE — action INTERPRETATION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
