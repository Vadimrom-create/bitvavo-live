# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-19T11:32:26.276777+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : PEPE-EUR | action ACHETE_MAINTENANT | opportunité 8.803 | entrée 7.450 | trend 7.450 | rang 7.773
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : aucun candidat matériel
- **MEILLEUR_LATENT_ACCELERATOR** : SOL-EUR | action LATENT_ACCELERATOR | opportunité 7.731 | entrée 4.500 | trend 8.250 | rang 7.285
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : HYPE-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.144 | entrée 6.900 | trend 8.750 | rang 7.964
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. HYPE-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.964
2. APT-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.920
3. PEPE-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 7.773

## Accélération indépendante

Aucune accélération indépendante confirmée ou en construction.

## Watchlist persistante 24–72 h

- SUI-EUR — ACTIVE_NOW — score mémoire 7.571/10 — sources ACCELERATION, DECISION_LAYER, V4 — BUYABLE_NOW
- ZAMA-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- WAL-EUR — ACTIVE_NOW — score mémoire 8.323/10 — sources V4 — WATCH_ONLY
- AERO-EUR — ACTIVE_NOW — score mémoire 8.189/10 — sources V4 — WATCH_ONLY
- PYTH-EUR — ACTIVE_NOW — score mémoire 8.112/10 — sources V4 — WATCH_ONLY
- LSK-EUR — MEMORY_24H — score mémoire 8.067/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- AAVE-EUR — ACTIVE_NOW — score mémoire 8.058/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- S-EUR — ACTIVE_NOW — score mémoire 8.054/10 — sources DECISION_LAYER, V4 — WATCH_ONLY
- HYPE-EUR — ACTIVE_NOW — score mémoire 7.964/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- POL-EUR — ACTIVE_NOW — score mémoire 7.934/10 — sources ACCELERATION, V4 — WATCH_ONLY

## Audit des plus fortes hausses

- SYN-EUR +41.27% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- ZAMA-EUR +39.88% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- STRK-EUR +35.59% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- EDGE-EUR +33.76% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- SAGA-EUR +32.33% — DETECTED_TOO_LATE — couche NONE — action INTERPRETATION
- HEI-EUR +28.72% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- F-EUR +28.26% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- EPIC-EUR +25.80% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ZIG-EUR +22.61% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- XTZ-EUR +22.56% — DETECTED_EARLY — couche NONE — action INTERPRETATION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
