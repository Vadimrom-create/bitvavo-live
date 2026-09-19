# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-19T12:24:02.140184+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : FET-EUR | action ACHETE_MAINTENANT | opportunité 9.044 | entrée 7.200 | trend 8.100 | rang 8.025
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : aucun candidat matériel
- **MEILLEUR_LATENT_ACCELERATOR** : AVAX-EUR | action LATENT_ACCELERATOR | opportunité 7.452 | entrée 4.500 | trend 8.050 | rang 6.503
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : AAVE-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 7.785 | entrée 6.100 | trend 8.950 | rang 7.775
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. FET-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.025
2. HYPE-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 7.989
3. ONDO-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 7.835

## Accélération indépendante

- STRK-EUR — CONFIRMED_ACCELERATION — score 6.880/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- ZAMA-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- IMX-EUR — ACTIVE_NOW — score mémoire 8.421/10 — sources V4 — WATCH_ONLY
- W-EUR — ACTIVE_NOW — score mémoire 8.281/10 — sources V4 — WATCH_ONLY
- LSK-EUR — MEMORY_24H — score mémoire 8.067/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- ZIL-EUR — ACTIVE_NOW — score mémoire 8.060/10 — sources DECISION_LAYER, V4 — WATCH_ONLY
- AIOZ-EUR — ACTIVE_NOW — score mémoire 8.034/10 — sources V4 — DETECTED_BUT_TOO_LATE
- KMNO-EUR — ACTIVE_NOW — score mémoire 8.028/10 — sources V4 — WATCH_ONLY
- FET-EUR — ACTIVE_NOW — score mémoire 8.025/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- GALA-EUR — ACTIVE_NOW — score mémoire 8.023/10 — sources V4 — WATCH_ONLY
- SENT-EUR — ACTIVE_NOW — score mémoire 8.004/10 — sources V4 — WATCH_ONLY

## Audit des plus fortes hausses

- SYN-EUR +39.64% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- STRK-EUR +37.46% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- EDGE-EUR +34.15% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- ZAMA-EUR +33.96% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- CAP-EUR +30.85% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- SAGA-EUR +29.18% — DETECTED_TOO_LATE — couche NONE — action INTERPRETATION
- HEI-EUR +27.71% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- F-EUR +26.12% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- EPIC-EUR +23.13% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- XTZ-EUR +22.28% — DETECTED_EARLY — couche NONE — action INTERPRETATION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
