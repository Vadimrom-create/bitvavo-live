# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-16T01:22:41.164320+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : aucun candidat matériel
- **MEILLEUR_LATENT_ACCELERATOR** : aucun candidat matériel
- **MEILLEUR_PULLBACK_REENTRY** : LSK-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 7.452 | entrée 4.950 | trend 8.400 | rang 6.676
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. LSK-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 6.676

## Accélération indépendante

Aucune accélération indépendante confirmée ou en construction.

## Watchlist persistante 24–72 h

- SOMI-EUR — ACTIVE_NOW — score mémoire 8.010/10 — sources V4 — WATCH_ONLY
- ICP-EUR — ACTIVE_NOW — score mémoire 7.850/10 — sources V4 — WATCH_ONLY
- XVG-EUR — ACTIVE_NOW — score mémoire 7.804/10 — sources V4 — WATCH_ONLY
- VET-EUR — ACTIVE_NOW — score mémoire 7.732/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- NEAR-EUR — ACTIVE_NOW — score mémoire 7.729/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- LDO-EUR — ACTIVE_NOW — score mémoire 7.648/10 — sources V4 — WATCH_ONLY
- RED-EUR — ACTIVE_NOW — score mémoire 7.646/10 — sources V4 — WATCH_ONLY
- WLD-EUR — ACTIVE_NOW — score mémoire 7.602/10 — sources DECISION_LAYER, V4 — WATCH_ONLY
- ETHFI-EUR — ACTIVE_NOW — score mémoire 7.598/10 — sources V4 — WATCH_ONLY
- YB-EUR — ACTIVE_NOW — score mémoire 7.573/10 — sources V4 — WATCH_ONLY

## Audit des plus fortes hausses

- PUFFER-EUR +34.81% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- ALIGN-EUR +30.27% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- SAGA-EUR +25.35% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- LAPTOP-EUR +20.93% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- VTHO-EUR +19.12% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- CNPY-EUR +18.33% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- SYN-EUR +16.62% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- CROSS-EUR +15.69% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- ARB-EUR +12.51% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- G-EUR +11.19% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
