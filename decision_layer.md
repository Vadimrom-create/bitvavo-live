# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-28T21:17:44.636743+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : VIRTUAL-EUR | action ACHETE_MAINTENANT | opportunité 9.281 | entrée 7.300 | trend 9.000 | rang 8.475
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : AZTEC-EUR | action PLACE_LIMITE_PASSIVE | opportunité 7.983 | entrée 5.800 | trend 8.900 | rang 7.786
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : ARX-EUR | action LATENT_ACCELERATOR | opportunité 8.034 | entrée 5.200 | trend 7.900 | rang 7.102
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : HUMA-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 9.288 | entrée 6.900 | trend 8.450 | rang 8.289
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Tous les achats immédiats

1. VIRTUAL-EUR — ACHETE_MAINTENANT — rank 8.475 — opportunité 9.281 — entrée 7.300 — trend 9.000
2. XLM-EUR — ACHETE_MAINTENANT — rank 7.709 — opportunité 7.668 — entrée 7.600 — trend 8.450

## Top cross-sectionnel — aperçu non exhaustif

Ce top est une vue courte multi-buckets. Il ne doit jamais être utilisé comme liste exhaustive des achats immédiats.
1. VIRTUAL-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.475
2. HUMA-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.289
3. LINK-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.985

## Accélération indépendante

- 0G-EUR — CONFIRMED_ACCELERATION — score 7.200/10 — DETECTED_BUT_TOO_LATE
- APT-EUR — BUILDING_ACCELERATION — score 6.233/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- PEOPLE-EUR — BUILDING_ACCELERATION — score 6.170/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- PONKE-EUR — BUILDING_ACCELERATION — score 5.807/10 — DETECTED_BUT_TOO_LATE
- SAGA-EUR — BUILDING_ACCELERATION — score 5.493/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- BTT-EUR — BUILDING_ACCELERATION — score 5.456/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- NOM-EUR — BUILDING_ACCELERATION — score 5.240/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- ZRC-EUR — BUILDING_ACCELERATION — score 5.238/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- FUEL-EUR — BUILDING_ACCELERATION — score 5.119/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- SOON-EUR — BUILDING_ACCELERATION — score 5.113/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- VIRTUAL-EUR — ACTIVE_NOW — score mémoire 8.475/10 — sources ACCELERATION, DECISION_LAYER, V4 — BUYABLE_NOW
- HFT-EUR — MEMORY_24H — score mémoire 10.000/10 — sources ACCELERATION — MEMORY_ONLY
- PUFFER-EUR — MEMORY_24H — score mémoire 9.062/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- ZEUS-EUR — MEMORY_24H — score mémoire 8.844/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- HUMA-EUR — ACTIVE_NOW — score mémoire 8.289/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- LINK-EUR — ACTIVE_NOW — score mémoire 7.985/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- DGB-EUR — MEMORY_24H — score mémoire 7.972/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- RUNE-EUR — ACTIVE_NOW — score mémoire 7.915/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- ACX-EUR — MEMORY_DECAY_24_72H — score mémoire 7.892/10 — sources ACCELERATION — MEMORY_ONLY
- AZTEC-EUR — ACTIVE_NOW — score mémoire 7.786/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY

## Audit des plus fortes hausses

- HBAR-EUR +28.31% — DETECTED_EARLY — couche NONE — action NONE
- QNT-EUR +25.60% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- NMR-EUR +15.18% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- ALGO-EUR +13.64% — DETECTED_EARLY — couche NONE — action NONE
- MIOTA-EUR +9.46% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- IKA-EUR +9.29% — DETECTED_TOO_LATE — couche NONE — action INTERPRETATION
- LINK-EUR +8.74% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- TREAD-EUR +7.32% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- SOON-EUR +6.43% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- 0G-EUR +6.28% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION

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
