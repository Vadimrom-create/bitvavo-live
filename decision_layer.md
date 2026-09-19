# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-19T16:00:12.971896+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : HYPE-EUR | action ACHETE_MAINTENANT | opportunité 8.516 | entrée 8.150 | trend 8.750 | rang 8.249
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : VET-EUR | action PLACE_LIMITE_PASSIVE | opportunité 8.045 | entrée 5.950 | trend 8.700 | rang 7.711
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : UNI-EUR | action LATENT_ACCELERATOR | opportunité 7.436 | entrée 4.500 | trend 8.150 | rang 6.895
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : TAO-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 7.627 | entrée 7.350 | trend 8.300 | rang 7.545
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. HYPE-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.249
2. PEPE-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.164
3. VET-EUR — MEILLEURE_LIMITE_PASSIVE — PLACE_LIMITE_PASSIVE — rank 7.711

## Accélération indépendante

- G-EUR — CONFIRMED_ACCELERATION — score 8.990/10 — DETECTED_BUT_TOO_LATE
- F-EUR — BUILDING_ACCELERATION — score 5.880/10 — REQUIRES_V4_ENTRY_AND_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- G-EUR — ACTIVE_NOW — score mémoire 8.990/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- HYPE-EUR — ACTIVE_NOW — score mémoire 8.249/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- PEPE-EUR — ACTIVE_NOW — score mémoire 8.164/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- AAVE-EUR — ACTIVE_NOW — score mémoire 8.040/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- MIOTA-EUR — ACTIVE_NOW — score mémoire 7.956/10 — sources V4 — WATCH_ONLY
- IMX-EUR — ACTIVE_NOW — score mémoire 7.940/10 — sources V4 — WATCH_ONLY
- W-EUR — ACTIVE_NOW — score mémoire 7.938/10 — sources V4 — WATCH_ONLY
- TIA-EUR — MEMORY_24H — score mémoire 7.871/10 — sources V4 — MEMORY_ONLY
- AERO-EUR — ACTIVE_NOW — score mémoire 7.846/10 — sources V4 — WATCH_ONLY
- WAL-EUR — ACTIVE_NOW — score mémoire 7.819/10 — sources V4 — WATCH_ONLY

## Audit des plus fortes hausses

- ZAMA-EUR +47.89% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- XTZ-EUR +36.50% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- SYN-EUR +31.17% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- EPIC-EUR +28.37% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- SAGA-EUR +22.69% — DETECTED_TOO_LATE — couche NONE — action INTERPRETATION
- AIOZ-EUR +19.87% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ENA-EUR +19.14% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- STRK-EUR +18.89% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- G-EUR +18.24% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- EDGE-EUR +17.91% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
