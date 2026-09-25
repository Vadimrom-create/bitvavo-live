# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-25T17:42:03.607423+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : RENDER-EUR | action ACHETE_MAINTENANT | opportunité 8.486 | entrée 7.600 | trend 9.000 | rang 8.296
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : GALA-EUR | action PLACE_LIMITE_PASSIVE | opportunité 8.987 | entrée 6.300 | trend 7.400 | rang 7.648
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : ALGO-EUR | action LATENT_ACCELERATOR | opportunité 8.893 | entrée 5.750 | trend 8.750 | rang 8.171
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : VET-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.895 | entrée 6.950 | trend 8.150 | rang 8.100
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. RENDER-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.296
2. ALGO-EUR — MEILLEUR_LATENT_ACCELERATOR — LATENT_ACCELERATOR — rank 8.171
3. VET-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.100

## Accélération indépendante

- TAI-EUR — CONFIRMED_ACCELERATION — score 8.500/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- NOS-EUR — CONFIRMED_ACCELERATION — score 7.922/10 — DETECTED_BUT_TOO_LATE
- ICX-EUR — CONFIRMED_ACCELERATION — score 7.202/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- GRASS-EUR — CONFIRMED_ACCELERATION — score 6.902/10 — DETECTED_BUT_TOO_LATE
- WMTX-EUR — CONFIRMED_ACCELERATION — score 6.732/10 — DETECTED_BUT_TOO_LATE
- DODO-EUR — BUILDING_ACCELERATION — score 5.507/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- QNT-EUR — ACTIVE_NOW — score mémoire 6.108/10 — sources ACCELERATION, DECISION_LAYER, V4 — BUYABLE_NOW
- SWELL-EUR — MEMORY_24H — score mémoire 8.882/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- CTC-EUR — MEMORY_24H — score mémoire 8.874/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- FUEL-EUR — MEMORY_24H — score mémoire 8.650/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- TAI-EUR — ACTIVE_NOW — score mémoire 8.500/10 — sources ACCELERATION, V4 — WATCH_ONLY
- RENDER-EUR — ACTIVE_NOW — score mémoire 8.296/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- RED-EUR — ACTIVE_NOW — score mémoire 8.215/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- ALGO-EUR — ACTIVE_NOW — score mémoire 8.171/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- VET-EUR — ACTIVE_NOW — score mémoire 8.100/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- REQ-EUR — MEMORY_24H — score mémoire 8.033/10 — sources ACCELERATION, V4 — MEMORY_ONLY

## Audit des plus fortes hausses

- PHA-EUR +63.48% — DETECTED_TOO_LATE — couche NONE — action INTERPRETATION
- WMTX-EUR +42.27% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ARK-EUR +28.26% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- GRASS-EUR +26.66% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- RARE-EUR +24.04% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- AERO-EUR +20.94% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- ENA-EUR +19.96% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- EDGE-EUR +18.62% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- TREAD-EUR +17.15% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- SPK-EUR +16.74% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
