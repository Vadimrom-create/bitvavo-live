# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-30T05:01:25.382909+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : ICP-EUR | action ACHETE_MAINTENANT | opportunité 9.240 | entrée 7.400 | trend 8.900 | rang 8.492
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : ALICE-EUR | action PLACE_LIMITE_PASSIVE | opportunité 7.980 | entrée 6.100 | trend 8.550 | rang 7.638
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : SPK-EUR | action LATENT_ACCELERATOR | opportunité 8.656 | entrée 5.650 | trend 7.700 | rang 7.535
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : HUMA-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 9.354 | entrée 6.950 | trend 8.650 | rang 8.449
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Tous les achats immédiats

1. ICP-EUR — ACHETE_MAINTENANT — rank 8.492 — opportunité 9.240 — entrée 7.400 — trend 8.900
2. RENDER-EUR — ACHETE_MAINTENANT — rank 8.208 — opportunité 9.226 — entrée 7.700 — trend 7.950
3. SUI-EUR — ACHETE_MAINTENANT — rank 8.178 — opportunité 9.167 — entrée 7.600 — trend 7.900

## Top cross-sectionnel — aperçu non exhaustif

Ce top est une vue courte multi-buckets. Il ne doit jamais être utilisé comme liste exhaustive des achats immédiats.
1. ICP-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.492
2. HUMA-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.449
3. RENDER-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.208

## Accélération indépendante

- 0G-EUR — BUILDING_ACCELERATION — score 5.608/10 — DETECTED_BUT_TOO_LATE
- ROBO-EUR — BUILDING_ACCELERATION — score 5.599/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- MOVR-EUR — BUILDING_ACCELERATION — score 4.909/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- DEEP-EUR — MEMORY_24H — score mémoire 10.000/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- ICX-EUR — MEMORY_24H — score mémoire 9.062/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- SWELL-EUR — MEMORY_24H — score mémoire 9.000/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- IMU-EUR — MEMORY_24H — score mémoire 8.866/10 — sources ACCELERATION — MEMORY_ONLY
- QUID-EUR — MEMORY_24H — score mémoire 8.702/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- POND-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- ICP-EUR — ACTIVE_NOW — score mémoire 8.492/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- HUMA-EUR — ACTIVE_NOW — score mémoire 8.449/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- RENDER-EUR — ACTIVE_NOW — score mémoire 8.208/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- SUI-EUR — ACTIVE_NOW — score mémoire 8.178/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY

## Audit des plus fortes hausses

- SOON-EUR +43.05% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- MOVR-EUR +37.13% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- POND-EUR +32.48% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- ZBCN-EUR +29.69% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ZRO-EUR +23.37% — DETECTED_EARLY — couche NONE — action NONE
- MEW-EUR +20.73% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- PHA-EUR +19.49% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- PUMP-EUR +17.62% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- QNT-EUR +16.82% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- INIT-EUR +16.38% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE

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
