# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-19T11:45:49.873061+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : HYPE-EUR | action ACHETE_MAINTENANT | opportunité 8.142 | entrée 7.150 | trend 8.750 | rang 7.976
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : ENA-EUR | action PLACE_LIMITE_PASSIVE | opportunité 7.598 | entrée 5.900 | trend 8.350 | rang 6.656
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : SOL-EUR | action LATENT_ACCELERATOR | opportunité 7.861 | entrée 4.500 | trend 8.250 | rang 7.347
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : APT-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.468 | entrée 5.700 | trend 8.750 | rang 7.655
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. HYPE-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 7.976
2. PEPE-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 7.955
3. FET-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 7.814

## Accélération indépendante

Aucune accélération indépendante confirmée ou en construction.

## Watchlist persistante 24–72 h

- ZAMA-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- WAL-EUR — ACTIVE_NOW — score mémoire 8.483/10 — sources V4 — DETECTED_BUT_TOO_LATE
- PYTH-EUR — ACTIVE_NOW — score mémoire 8.391/10 — sources V4 — WATCH_ONLY
- AAVE-EUR — ACTIVE_NOW — score mémoire 8.141/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- LSK-EUR — MEMORY_24H — score mémoire 8.067/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- AERO-EUR — ACTIVE_NOW — score mémoire 8.034/10 — sources V4 — WATCH_ONLY
- GRT-EUR — ACTIVE_NOW — score mémoire 8.018/10 — sources V4 — WATCH_ONLY
- HYPE-EUR — ACTIVE_NOW — score mémoire 7.976/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- PEPE-EUR — ACTIVE_NOW — score mémoire 7.955/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- RED-EUR — ACTIVE_NOW — score mémoire 7.918/10 — sources V4 — WATCH_ONLY

## Audit des plus fortes hausses

- ZAMA-EUR +41.98% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- SYN-EUR +39.05% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- EDGE-EUR +36.38% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- STRK-EUR +35.94% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- SAGA-EUR +33.18% — DETECTED_TOO_LATE — couche NONE — action INTERPRETATION
- F-EUR +28.40% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- HEI-EUR +27.77% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- EPIC-EUR +23.92% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- XTZ-EUR +23.78% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ZIG-EUR +18.27% — DETECTED_EARLY — couche NONE — action INTERPRETATION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
