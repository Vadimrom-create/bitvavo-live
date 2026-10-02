# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-10-02T15:58:50.273957+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : ALGO-EUR | action ACHETE_MAINTENANT | opportunité 9.016 | entrée 7.250 | trend 8.650 | rang 8.316
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : NMR-EUR | action PLACE_LIMITE_PASSIVE | opportunité 7.571 | entrée 6.150 | trend 7.900 | rang 7.223
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : ILV-EUR | action LATENT_ACCELERATOR | opportunité 7.701 | entrée 5.650 | trend 8.700 | rang 7.571
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : DYDX-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 9.295 | entrée 6.250 | trend 8.950 | rang 8.463
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Tous les achats immédiats

1. ALGO-EUR — ACHETE_MAINTENANT — rank 8.316 — opportunité 9.016 — entrée 7.250 — trend 8.650
2. AAVE-EUR — ACHETE_MAINTENANT — rank 8.099 — opportunité 8.627 — entrée 7.000 — trend 8.900

## Top cross-sectionnel — aperçu non exhaustif

Ce top est une vue courte multi-buckets. Il ne doit jamais être utilisé comme liste exhaustive des achats immédiats.
1. DYDX-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.463
2. ALGO-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.316
3. AAVE-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.099

## Accélération indépendante

- CAP-EUR — CONFIRMED_ACCELERATION — score 8.954/10 — DETECTED_BUT_TOO_LATE
- REQ-EUR — CONFIRMED_ACCELERATION — score 7.500/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- SPK-EUR — BUILDING_ACCELERATION — score 6.220/10 — DETECTED_BUT_TOO_LATE
- BTT-EUR — BUILDING_ACCELERATION — score 5.863/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- WIN-EUR — BUILDING_ACCELERATION — score 5.500/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- LISTA-EUR — BUILDING_ACCELERATION — score 5.095/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- NMR-EUR — BUILDING_ACCELERATION — score 4.796/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- EDGE-EUR — MEMORY_24H — score mémoire 10.000/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- TREAD-EUR — MEMORY_24H — score mémoire 9.258/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- PEOPLE-EUR — MEMORY_24H — score mémoire 9.036/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- CAP-EUR — ACTIVE_NOW — score mémoire 8.954/10 — sources ACCELERATION, V4 — DETECTED_BUT_TOO_LATE
- AIOZ-EUR — MEMORY_24H — score mémoire 8.925/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- U-EUR — MEMORY_24H — score mémoire 8.740/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- AGI-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- ZRC-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- DYDX-EUR — ACTIVE_NOW — score mémoire 8.463/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- ALGO-EUR — ACTIVE_NOW — score mémoire 8.316/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY

## Audit des plus fortes hausses

- SAND-EUR +39.64% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- GTC-EUR +23.15% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- WLD-EUR +17.23% — DETECTED_EARLY — couche NONE — action NONE
- SKY-EUR +16.80% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- APE-EUR +15.53% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- GALA-EUR +14.74% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- SPK-EUR +14.50% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ZRO-EUR +12.69% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- ATH-EUR +12.41% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE
- NOS-EUR +12.17% — DETECTED_EARLY — couche NONE — action INTERPRETATION

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
