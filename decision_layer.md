# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-19T16:20:25.259996+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : PEPE-EUR | action ACHETE_MAINTENANT | opportunité 9.227 | entrée 8.400 | trend 7.900 | rang 8.085
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : aucun candidat matériel
- **MEILLEUR_LATENT_ACCELERATOR** : UNI-EUR | action LATENT_ACCELERATOR | opportunité 7.405 | entrée 4.500 | trend 8.150 | rang 6.880
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : INJ-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.149 | entrée 6.750 | trend 8.550 | rang 7.253
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. PEPE-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.085
2. HYPE-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.024
3. INJ-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.253

## Accélération indépendante

- C-EUR — BUILDING_ACCELERATION — score 5.701/10 — REQUIRES_V4_ENTRY_AND_EXECUTION_VALIDATION
- PEPE-EUR — BUILDING_ACCELERATION — score 4.852/10 — REQUIRES_V4_ENTRY_AND_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- G-EUR — MEMORY_24H — score mémoire 8.990/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- PEPE-EUR — ACTIVE_NOW — score mémoire 8.085/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- SENT-EUR — ACTIVE_NOW — score mémoire 8.050/10 — sources V4 — WATCH_ONLY
- HYPE-EUR — ACTIVE_NOW — score mémoire 8.024/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- ROSE-EUR — ACTIVE_NOW — score mémoire 7.982/10 — sources V4 — WATCH_ONLY
- IMX-EUR — ACTIVE_NOW — score mémoire 7.901/10 — sources V4 — WATCH_ONLY
- AAVE-EUR — ACTIVE_NOW — score mémoire 7.899/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- VET-EUR — ACTIVE_NOW — score mémoire 7.888/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- VVV-EUR — ACTIVE_NOW — score mémoire 7.815/10 — sources DECISION_LAYER, V4 — WATCH_ONLY
- WAL-EUR — ACTIVE_NOW — score mémoire 7.804/10 — sources V4 — WATCH_ONLY

## Audit des plus fortes hausses

- ZAMA-EUR +40.85% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- XTZ-EUR +33.31% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- SYN-EUR +30.19% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- EPIC-EUR +28.55% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- G-EUR +23.46% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- SAGA-EUR +21.62% — DETECTED_TOO_LATE — couche NONE — action INTERPRETATION
- EDGE-EUR +21.56% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- ENA-EUR +20.90% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- STRK-EUR +18.66% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- AVAX-EUR +17.96% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
