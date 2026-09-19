# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-19T01:08:59.016580+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : HYPE-EUR | action ACHETE_MAINTENANT | opportunité 9.180 | entrée 7.800 | trend 8.400 | rang 8.339
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : aucun candidat matériel
- **MEILLEUR_LATENT_ACCELERATOR** : aucun candidat matériel
- **MEILLEUR_PULLBACK_REENTRY** : FET-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 7.681 | entrée 6.400 | trend 8.650 | rang 7.655
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. HYPE-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.339
2. ONDO-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 7.720
3. FET-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.655

## Accélération indépendante

Aucune accélération indépendante confirmée ou en construction.

## Watchlist persistante 24–72 h

- PYTH-EUR — ACTIVE_NOW — score mémoire 8.689/10 — sources V4 — WATCH_ONLY
- HYPE-EUR — ACTIVE_NOW — score mémoire 8.339/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- AAVE-EUR — ACTIVE_NOW — score mémoire 8.311/10 — sources ACCELERATION, V4 — WATCH_ONLY
- SYN-EUR — MEMORY_24H — score mémoire 8.311/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- VTHO-EUR — MEMORY_24H — score mémoire 8.268/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- REZ-EUR — ACTIVE_NOW — score mémoire 8.105/10 — sources ACCELERATION, V4 — WATCH_ONLY
- ZRX-EUR — ACTIVE_NOW — score mémoire 8.048/10 — sources V4 — WATCH_ONLY
- YB-EUR — MEMORY_24H — score mémoire 7.953/10 — sources V4 — MEMORY_ONLY
- AVAX-EUR — ACTIVE_NOW — score mémoire 7.948/10 — sources ACCELERATION, V4 — WATCH_ONLY
- NPC-EUR — ACTIVE_NOW — score mémoire 7.837/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY

## Audit des plus fortes hausses

- F-EUR +60.04% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- G-EUR +50.85% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- STRK-EUR +48.36% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- SYN-EUR +24.30% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- ZAMA-EUR +24.08% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ZIG-EUR +21.77% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- APT-EUR +21.56% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- S-EUR +19.69% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- NEAR-EUR +19.27% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- SKY-EUR +19.23% — DETECTED_EARLY — couche NONE — action INTERPRETATION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
