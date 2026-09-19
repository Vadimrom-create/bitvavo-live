# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-19T09:26:00.024411+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : ONDO-EUR | action ACHETE_MAINTENANT | opportunité 9.106 | entrée 7.850 | trend 7.650 | rang 8.038
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : aucun candidat matériel
- **MEILLEUR_LATENT_ACCELERATOR** : SOL-EUR | action LATENT_ACCELERATOR | opportunité 7.480 | entrée 4.500 | trend 8.250 | rang 7.174
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : AVAX-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 9.286 | entrée 7.300 | trend 8.450 | rang 7.960
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. ONDO-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.038
2. RAY-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.006
3. AVAX-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.960

## Accélération indépendante

- AVAX-EUR — BUILDING_ACCELERATION — score 4.916/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- RAY-EUR — ACTIVE_NOW — score mémoire 8.006/10 — sources ACCELERATION, DECISION_LAYER, V4 — BUYABLE_NOW
- TAO-EUR — ACTIVE_NOW — score mémoire 7.651/10 — sources ACCELERATION, DECISION_LAYER, V4 — BUYABLE_NOW
- AAVE-EUR — ACTIVE_NOW — score mémoire 8.360/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- JUP-EUR — ACTIVE_NOW — score mémoire 8.270/10 — sources V4 — WATCH_ONLY
- MET-EUR — ACTIVE_NOW — score mémoire 8.101/10 — sources V4 — DETECTED_BUT_TOO_LATE
- SYN-EUR — MEMORY_24H — score mémoire 8.094/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- LSK-EUR — MEMORY_24H — score mémoire 8.067/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- ARX-EUR — ACTIVE_NOW — score mémoire 8.060/10 — sources V4 — WATCH_ONLY
- PENDLE-EUR — ACTIVE_NOW — score mémoire 8.044/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- ONDO-EUR — ACTIVE_NOW — score mémoire 8.038/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY

## Audit des plus fortes hausses

- SYN-EUR +44.97% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- HEI-EUR +36.98% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ZAMA-EUR +36.32% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- EDGE-EUR +33.67% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- F-EUR +27.51% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- XTZ-EUR +26.70% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ZIG-EUR +25.17% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- SAGA-EUR +23.02% — DETECTED_TOO_LATE — couche NONE — action INTERPRETATION
- STRK-EUR +19.93% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- INJ-EUR +17.92% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
