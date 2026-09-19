# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-19T00:53:09.126187+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : FET-EUR | action ACHETE_MAINTENANT | opportunité 7.748 | entrée 6.800 | trend 8.650 | rang 7.709
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : aucun candidat matériel
- **MEILLEUR_LATENT_ACCELERATOR** : aucun candidat matériel
- **MEILLEUR_PULLBACK_REENTRY** : HYPE-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.180 | entrée 7.600 | trend 8.400 | rang 7.844
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. HYPE-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.844
2. FET-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 7.709
3. ONDO-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 7.506

## Accélération indépendante

- F-EUR — BUILDING_ACCELERATION — score 6.380/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- AAVE-EUR — ACTIVE_NOW — score mémoire 8.373/10 — sources ACCELERATION, V4 — DETECTED_BUT_TOO_LATE
- SYN-EUR — MEMORY_24H — score mémoire 8.311/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- VTHO-EUR — MEMORY_24H — score mémoire 8.268/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- LTC-EUR — ACTIVE_NOW — score mémoire 8.012/10 — sources DECISION_LAYER, V4 — WATCH_ONLY
- ZRX-EUR — ACTIVE_NOW — score mémoire 7.986/10 — sources V4 — WATCH_ONLY
- PEPE-EUR — ACTIVE_NOW — score mémoire 7.985/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- YB-EUR — MEMORY_24H — score mémoire 7.953/10 — sources V4 — MEMORY_ONLY
- SSV-EUR — ACTIVE_NOW — score mémoire 7.913/10 — sources V4 — WATCH_ONLY
- AVAX-EUR — ACTIVE_NOW — score mémoire 7.895/10 — sources ACCELERATION, V4 — WATCH_ONLY
- PYTH-EUR — ACTIVE_NOW — score mémoire 7.860/10 — sources V4 — WATCH_ONLY

## Audit des plus fortes hausses

- F-EUR +59.63% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- G-EUR +53.76% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- STRK-EUR +46.71% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ZAMA-EUR +23.55% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- APT-EUR +23.40% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ARB-EUR +22.69% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ZIG-EUR +21.95% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- C-EUR +21.42% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- SYN-EUR +20.64% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- S-EUR +19.42% — DETECTED_EARLY — couche NONE — action INTERPRETATION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
