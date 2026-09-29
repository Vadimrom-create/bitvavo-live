# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-29T18:29:48.626665+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : PUMP-EUR | action ACHETE_MAINTENANT | opportunité 8.145 | entrée 7.100 | trend 8.650 | rang 7.816
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : JASMY-EUR | action PLACE_LIMITE_PASSIVE | opportunité 8.041 | entrée 6.150 | trend 8.700 | rang 7.786
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : ALICE-EUR | action LATENT_ACCELERATOR | opportunité 7.734 | entrée 5.000 | trend 8.850 | rang 6.973
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : SKY-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.509 | entrée 6.550 | trend 9.000 | rang 8.079
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Tous les achats immédiats

1. PUMP-EUR — ACHETE_MAINTENANT — rank 7.816 — opportunité 8.145 — entrée 7.100 — trend 8.650

## Top cross-sectionnel — aperçu non exhaustif

Ce top est une vue courte multi-buckets. Il ne doit jamais être utilisé comme liste exhaustive des achats immédiats.
1. SKY-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.079
2. ICP-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.935
3. PUMP-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 7.816

## Accélération indépendante

- NOM-EUR — BUILDING_ACCELERATION — score 6.103/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- NIL-EUR — BUILDING_ACCELERATION — score 5.952/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- EPIC-EUR — BUILDING_ACCELERATION — score 5.383/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- STRK-EUR — BUILDING_ACCELERATION — score 5.367/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- KMNO-EUR — BUILDING_ACCELERATION — score 5.235/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- GROVE-EUR — BUILDING_ACCELERATION — score 5.173/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- POND-EUR — BUILDING_ACCELERATION — score 5.018/10 — DETECTED_BUT_TOO_LATE
- NEAR-EUR — BUILDING_ACCELERATION — score 4.992/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- YFI-EUR — BUILDING_ACCELERATION — score 4.962/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- SOON-EUR — BUILDING_ACCELERATION — score 4.947/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- GIGA-EUR — MEMORY_24H — score mémoire 10.000/10 — sources ACCELERATION — MEMORY_ONLY
- QUID-EUR — MEMORY_24H — score mémoire 9.062/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- USELESS-EUR — MEMORY_24H — score mémoire 9.062/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- SWELL-EUR — MEMORY_24H — score mémoire 9.000/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- FUEL-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- WMTX-EUR — MEMORY_24H — score mémoire 8.145/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- SKY-EUR — ACTIVE_NOW — score mémoire 8.079/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- SOLV-EUR — MEMORY_24H — score mémoire 8.017/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- ZRC-EUR — MEMORY_24H — score mémoire 7.961/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- ICP-EUR — ACTIVE_NOW — score mémoire 7.935/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE

## Audit des plus fortes hausses

- POND-EUR +28.66% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- 0G-EUR +27.24% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- XDP-EUR +25.77% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- SOON-EUR +23.73% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- ZBCN-EUR +20.72% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- INIT-EUR +19.66% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- NMR-EUR +18.69% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- ALICE-EUR +13.74% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- PHA-EUR +13.45% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- GRASS-EUR +13.23% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION

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
