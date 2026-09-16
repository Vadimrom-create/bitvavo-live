# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-16T08:40:12.231823+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : aucun candidat matériel
- **MEILLEUR_LATENT_ACCELERATOR** : aucun candidat matériel
- **MEILLEUR_PULLBACK_REENTRY** : VTHO-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.368 | entrée 6.350 | trend 9.200 | rang 8.163
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. VTHO-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.163
2. TAO-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 6.814

## Accélération indépendante

- ALIGN-EUR — CONFIRMED_ACCELERATION — score 7.116/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- VTHO-EUR — ACTIVE_NOW — score mémoire 8.163/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- ICP-EUR — ACTIVE_NOW — score mémoire 7.875/10 — sources V4 — WATCH_ONLY
- VET-EUR — ACTIVE_NOW — score mémoire 7.805/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- CVC-EUR — MEMORY_24H — score mémoire 7.734/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- YB-EUR — ACTIVE_NOW — score mémoire 7.730/10 — sources V4 — WATCH_ONLY
- AIOZ-EUR — ACTIVE_NOW — score mémoire 7.676/10 — sources V4 — WATCH_ONLY
- LDO-EUR — ACTIVE_NOW — score mémoire 7.631/10 — sources V4 — WATCH_ONLY
- ALGO-EUR — MEMORY_24H — score mémoire 7.613/10 — sources V4 — MEMORY_ONLY
- ETHFI-EUR — ACTIVE_NOW — score mémoire 7.584/10 — sources V4 — WATCH_ONLY
- ZIL-EUR — ACTIVE_NOW — score mémoire 7.529/10 — sources DECISION_LAYER, V4 — WATCH_ONLY

## Audit des plus fortes hausses

- SYN-EUR +114.74% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- LMWR-EUR +24.16% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- USELESS-EUR +19.43% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- LSK-EUR +18.30% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- ARB-EUR +16.01% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- TLM-EUR +13.76% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE
- CNPY-EUR +12.46% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ALIGN-EUR +11.37% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- FOLD-EUR +10.07% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- GLMR-EUR +8.31% — DETECTED_EARLY — couche NONE — action INTERPRETATION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
