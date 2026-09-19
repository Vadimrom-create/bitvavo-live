# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-19T15:00:15.077109+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : HYPE-EUR | action ACHETE_MAINTENANT | opportunité 8.408 | entrée 7.950 | trend 8.750 | rang 8.168
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : VET-EUR | action PLACE_LIMITE_PASSIVE | opportunité 7.903 | entrée 5.950 | trend 8.700 | rang 7.599
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : NPC-EUR | action LATENT_ACCELERATOR | opportunité 7.551 | entrée 4.500 | trend 8.250 | rang 7.108
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : TAO-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.473 | entrée 7.650 | trend 8.300 | rang 7.954
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. HYPE-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.168
2. TAO-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.954
3. LPT-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.857

## Accélération indépendante

- G-EUR — BUILDING_ACCELERATION — score 6.063/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- USELESS-EUR — ACTIVE_NOW — score mémoire 7.595/10 — sources ACCELERATION, DECISION_LAYER, V4 — BUYABLE_NOW
- ZAMA-EUR — MEMORY_24H — score mémoire 8.324/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- JUP-EUR — ACTIVE_NOW — score mémoire 8.209/10 — sources DECISION_LAYER, V4 — WATCH_ONLY
- HYPE-EUR — ACTIVE_NOW — score mémoire 8.168/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- VVV-EUR — ACTIVE_NOW — score mémoire 8.104/10 — sources DECISION_LAYER, V4 — WATCH_ONLY
- AAVE-EUR — ACTIVE_NOW — score mémoire 8.051/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- PROVE-EUR — ACTIVE_NOW — score mémoire 8.027/10 — sources V4 — WATCH_ONLY
- PYTH-EUR — ACTIVE_NOW — score mémoire 8.015/10 — sources V4 — WATCH_ONLY
- MIOTA-EUR — ACTIVE_NOW — score mémoire 8.010/10 — sources V4 — WATCH_ONLY
- ATH-EUR — ACTIVE_NOW — score mémoire 8.002/10 — sources V4 — WATCH_ONLY

## Audit des plus fortes hausses

- ZAMA-EUR +44.90% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- XTZ-EUR +37.91% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- SYN-EUR +35.00% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- SAGA-EUR +25.76% — DETECTED_TOO_LATE — couche NONE — action INTERPRETATION
- STRK-EUR +25.05% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- EPIC-EUR +24.10% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- AIOZ-EUR +22.56% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- F-EUR +22.31% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- EDGE-EUR +21.66% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- ENA-EUR +20.61% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
