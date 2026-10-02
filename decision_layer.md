# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-10-02T16:43:55.185052+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : RENDER-EUR | action ACHETE_MAINTENANT | opportunité 6.986 | entrée 6.850 | trend 6.400 | rang 6.406
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : AZTEC-EUR | action PLACE_LIMITE_PASSIVE | opportunité 9.160 | entrée 5.950 | trend 8.150 | rang 7.982
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : FLUID-EUR | action LATENT_ACCELERATOR | opportunité 7.666 | entrée 5.350 | trend 8.800 | rang 7.220
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : AAVE-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.806 | entrée 6.600 | trend 8.650 | rang 8.012
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Tous les achats immédiats

1. RENDER-EUR — ACHETE_MAINTENANT — rank 6.406 — opportunité 6.986 — entrée 6.850 — trend 6.400

## Top cross-sectionnel — aperçu non exhaustif

Ce top est une vue courte multi-buckets. Il ne doit jamais être utilisé comme liste exhaustive des achats immédiats.
1. AAVE-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.012
2. HUMA-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.009
3. AZTEC-EUR — MEILLEURE_LIMITE_PASSIVE — PLACE_LIMITE_PASSIVE — rank 7.982

## Accélération indépendante

- U-EUR — CONFIRMED_ACCELERATION — score 8.145/10 — DETECTED_BUT_TOO_LATE
- GTC-EUR — BUILDING_ACCELERATION — score 5.941/10 — DETECTED_BUT_TOO_LATE
- HFT-EUR — BUILDING_ACCELERATION — score 5.558/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- KSM-EUR — BUILDING_ACCELERATION — score 5.269/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- WIN-EUR — BUILDING_ACCELERATION — score 5.023/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- ADX-EUR — BUILDING_ACCELERATION — score 4.777/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- EDGE-EUR — MEMORY_24H — score mémoire 10.000/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- TREAD-EUR — MEMORY_24H — score mémoire 9.258/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- PEOPLE-EUR — MEMORY_24H — score mémoire 9.036/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- CAP-EUR — MEMORY_24H — score mémoire 8.954/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- ZRC-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- AGI-EUR — MEMORY_24H — score mémoire 8.283/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- U-EUR — ACTIVE_NOW — score mémoire 8.145/10 — sources ACCELERATION, V4 — DETECTED_BUT_TOO_LATE
- AAVE-EUR — ACTIVE_NOW — score mémoire 8.012/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- ALGO-EUR — MEMORY_24H — score mémoire 8.010/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- HUMA-EUR — ACTIVE_NOW — score mémoire 8.009/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY

## Audit des plus fortes hausses

- SAND-EUR +44.05% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- GTC-EUR +32.96% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- SKY-EUR +16.29% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- ATH-EUR +15.73% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- GALA-EUR +15.66% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- WLD-EUR +15.59% — DETECTED_EARLY — couche NONE — action NONE
- SUPER-EUR +14.29% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- NOS-EUR +13.45% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- MANA-EUR +12.73% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- ZRO-EUR +12.43% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION

## Gestion des positions détenues

Policy : STAGED_10_20_RUNNER_V1
- +10% : prise partielle 35%.
- +20% : seconde prise 35%.
- Runner conservé : 30%.
- Revue coût d'opportunité après 72 h ; sortie seulement avant la première partielle, proche/sous le PRU et avec momentum 15m affaibli.
- Pas de stop serré mécaniquement après une petite hausse ; le stop reste lié à l'invalidation structurelle.

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
