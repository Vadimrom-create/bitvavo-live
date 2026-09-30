# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-30T01:27:45.498425+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : SUI-EUR | action ACHETE_MAINTENANT | opportunité 9.167 | entrée 8.050 | trend 7.900 | rang 8.159
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : HUMA-EUR | action PLACE_LIMITE_PASSIVE | opportunité 8.082 | entrée 5.800 | trend 8.650 | rang 7.726
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : BIO-EUR | action LATENT_ACCELERATOR | opportunité 8.381 | entrée 5.250 | trend 8.200 | rang 7.416
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : ALGO-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 9.325 | entrée 7.000 | trend 8.650 | rang 8.400
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Tous les achats immédiats

1. SUI-EUR — ACHETE_MAINTENANT — rank 8.159 — opportunité 9.167 — entrée 8.050 — trend 7.900
2. ICP-EUR — ACHETE_MAINTENANT — rank 7.954 — opportunité 8.775 — entrée 7.100 — trend 9.200
3. RENDER-EUR — ACHETE_MAINTENANT — rank 7.574 — opportunité 8.148 — entrée 7.200 — trend 8.150
4. RAY-EUR — ACHETE_MAINTENANT — rank 7.032 — opportunité 8.682 — entrée 7.450 — trend 5.650

## Top cross-sectionnel — aperçu non exhaustif

Ce top est une vue courte multi-buckets. Il ne doit jamais être utilisé comme liste exhaustive des achats immédiats.
1. ALGO-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.400
2. SUI-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.159
3. ICP-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 7.954

## Accélération indépendante

- COMP-EUR — CONFIRMED_ACCELERATION — score 9.636/10 — DETECTED_BUT_TOO_LATE
- BLUR-EUR — CONFIRMED_ACCELERATION — score 6.627/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- XAN-EUR — BUILDING_ACCELERATION — score 6.399/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- RECALL-EUR — BUILDING_ACCELERATION — score 5.949/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- 0G-EUR — BUILDING_ACCELERATION — score 5.943/10 — DETECTED_BUT_TOO_LATE
- MET-EUR — BUILDING_ACCELERATION — score 5.882/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- PNUT-EUR — BUILDING_ACCELERATION — score 5.864/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- COW-EUR — BUILDING_ACCELERATION — score 5.739/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- GIGA-EUR — BUILDING_ACCELERATION — score 5.604/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- SNX-EUR — BUILDING_ACCELERATION — score 5.559/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- RAY-EUR — ACTIVE_NOW — score mémoire 7.032/10 — sources ACCELERATION, DECISION_LAYER, V4 — BUYABLE_NOW
- COMP-EUR — ACTIVE_NOW — score mémoire 9.636/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- QUID-EUR — MEMORY_24H — score mémoire 9.062/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- SWELL-EUR — MEMORY_24H — score mémoire 9.000/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- IMU-EUR — MEMORY_24H — score mémoire 8.866/10 — sources ACCELERATION — MEMORY_ONLY
- EDGE-EUR — MEMORY_24H — score mémoire 8.544/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- ALGO-EUR — ACTIVE_NOW — score mémoire 8.400/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- SUI-EUR — ACTIVE_NOW — score mémoire 8.159/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- SOLV-EUR — MEMORY_24H — score mémoire 8.017/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- ICP-EUR — ACTIVE_NOW — score mémoire 7.954/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE

## Audit des plus fortes hausses

- SOON-EUR +46.44% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- MOVR-EUR +36.96% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- POND-EUR +30.47% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- GRASS-EUR +26.33% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- PUMP-EUR +24.21% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- QNT-EUR +23.46% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- 0G-EUR +22.18% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- MEW-EUR +18.16% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- ZRO-EUR +17.29% — DETECTED_EARLY — couche NONE — action NONE
- ZBCN-EUR +16.70% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE

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
