# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-16T14:21:27.451020+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : aucun candidat matériel
- **MEILLEUR_LATENT_ACCELERATOR** : aucun candidat matériel
- **MEILLEUR_PULLBACK_REENTRY** : NEAR-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 7.482 | entrée 7.450 | trend 8.100 | rang 7.492
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. NEAR-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.492
2. TAO-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 6.938

## Accélération indépendante

Aucune accélération indépendante confirmée ou en construction.

## Watchlist persistante 24–72 h

- ZORA-EUR — ACTIVE_NOW — score mémoire 7.801/10 — sources V4 — WATCH_ONLY
- ICP-EUR — ACTIVE_NOW — score mémoire 7.752/10 — sources V4 — WATCH_ONLY
- LDO-EUR — ACTIVE_NOW — score mémoire 7.735/10 — sources V4 — WATCH_ONLY
- ETHFI-EUR — ACTIVE_NOW — score mémoire 7.722/10 — sources V4 — WATCH_ONLY
- SOMI-EUR — ACTIVE_NOW — score mémoire 7.672/10 — sources V4 — WATCH_ONLY
- UNI-EUR — MEMORY_24H — score mémoire 7.629/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- VTHO-EUR — ACTIVE_NOW — score mémoire 7.619/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- ALGO-EUR — MEMORY_24H — score mémoire 7.613/10 — sources V4 — MEMORY_ONLY
- AVAX-EUR — MEMORY_24H — score mémoire 7.587/10 — sources V4 — MEMORY_ONLY
- ZEN-EUR — MEMORY_24H — score mémoire 7.586/10 — sources V4 — MEMORY_ONLY

## Audit des plus fortes hausses

- SYN-EUR +115.02% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- LSK-EUR +45.43% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- FOLD-EUR +19.59% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- HEI-EUR +16.45% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- ARB-EUR +15.93% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- TAI-EUR +15.21% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- USELESS-EUR +13.94% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- IOST-EUR +12.88% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- CNPY-EUR +10.70% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- ZKJ-EUR +6.82% — DETECTED_EARLY — couche NONE — action INTERPRETATION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
