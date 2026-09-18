# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-18T23:52:52.775773+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : aucun candidat matériel
- **MEILLEUR_LATENT_ACCELERATOR** : aucun candidat matériel
- **MEILLEUR_PULLBACK_REENTRY** : PEPE-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 7.902 | entrée 6.900 | trend 8.950 | rang 7.909
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. PEPE-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.909

## Accélération indépendante

Aucune accélération indépendante confirmée ou en construction.

## Watchlist persistante 24–72 h

- SYN-EUR — MEMORY_24H — score mémoire 8.311/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- VTHO-EUR — MEMORY_24H — score mémoire 8.268/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- GRT-EUR — ACTIVE_NOW — score mémoire 8.165/10 — sources V4 — WATCH_ONLY
- PYTH-EUR — ACTIVE_NOW — score mémoire 7.977/10 — sources V4 — WATCH_ONLY
- YB-EUR — MEMORY_24H — score mémoire 7.953/10 — sources V4 — MEMORY_ONLY
- AAVE-EUR — ACTIVE_NOW — score mémoire 7.928/10 — sources ACCELERATION, V4 — WATCH_ONLY
- PEPE-EUR — ACTIVE_NOW — score mémoire 7.909/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- ROSE-EUR — ACTIVE_NOW — score mémoire 7.892/10 — sources V4 — WATCH_ONLY
- AERO-EUR — MEMORY_24H — score mémoire 7.882/10 — sources V4 — MEMORY_ONLY
- FET-EUR — ACTIVE_NOW — score mémoire 7.847/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY

## Audit des plus fortes hausses

- F-EUR +60.39% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- G-EUR +56.70% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- STRK-EUR +53.54% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ARB-EUR +24.56% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- C-EUR +22.99% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- APT-EUR +22.46% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ZIG-EUR +21.84% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ZK-EUR +21.01% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE
- OP-EUR +20.18% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ZAMA-EUR +19.33% — DETECTED_EARLY — couche NONE — action INTERPRETATION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
