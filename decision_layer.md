# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-30T22:56:36.650700+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : CRV-EUR | action ACHETE_MAINTENANT | opportunité 9.314 | entrée 7.050 | trend 8.400 | rang 8.295
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : RED-EUR | action PLACE_LIMITE_PASSIVE | opportunité 8.019 | entrée 6.000 | trend 9.200 | rang 7.846
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : MMT-EUR | action LATENT_ACCELERATOR | opportunité 7.753 | entrée 4.500 | trend 8.750 | rang 7.476
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : ALGO-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.864 | entrée 7.250 | trend 8.650 | rang 8.237
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Tous les achats immédiats

1. CRV-EUR — ACHETE_MAINTENANT — rank 8.295 — opportunité 9.314 — entrée 7.050 — trend 8.400
2. PLUME-EUR — ACHETE_MAINTENANT — rank 8.078 — opportunité 9.268 — entrée 7.450 — trend 8.200
3. XLM-EUR — ACHETE_MAINTENANT — rank 8.051 — opportunité 8.376 — entrée 7.400 — trend 8.700
4. VIRTUAL-EUR — ACHETE_MAINTENANT — rank 7.811 — opportunité 9.050 — entrée 7.150 — trend 7.550
5. DOT-EUR — ACHETE_MAINTENANT — rank 7.509 — opportunité 7.907 — entrée 6.850 — trend 7.950
6. PUMP-EUR — ACHETE_MAINTENANT — rank 7.446 — opportunité 8.033 — entrée 7.050 — trend 8.500
7. ADA-EUR — ACHETE_MAINTENANT — rank 7.362 — opportunité 8.404 — entrée 7.850 — trend 6.900

## Top cross-sectionnel — aperçu non exhaustif

Ce top est une vue courte multi-buckets. Il ne doit jamais être utilisé comme liste exhaustive des achats immédiats.
1. CRV-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.295
2. ALGO-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.237
3. PLUME-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.078

## Accélération indépendante

- CYBER-EUR — BUILDING_ACCELERATION — score 6.027/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- ETHFI-EUR — BUILDING_ACCELERATION — score 5.708/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- BLEND-EUR — BUILDING_ACCELERATION — score 5.606/10 — DETECTED_BUT_TOO_LATE
- A-EUR — BUILDING_ACCELERATION — score 5.160/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- ROBO-EUR — BUILDING_ACCELERATION — score 5.117/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- IOST-EUR — BUILDING_ACCELERATION — score 5.014/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- PLUME-EUR — ACTIVE_NOW — score mémoire 8.078/10 — sources ACCELERATION, DECISION_LAYER, V4 — BUYABLE_NOW
- LMWR-EUR — MEMORY_24H — score mémoire 9.685/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- CTR-EUR — MEMORY_24H — score mémoire 8.902/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- ARPA-EUR — MEMORY_24H — score mémoire 8.595/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- CVC-EUR — MEMORY_24H — score mémoire 8.565/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- HNT-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- PONKE-EUR — MEMORY_24H — score mémoire 8.400/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- CRV-EUR — ACTIVE_NOW — score mémoire 8.295/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- ALGO-EUR — ACTIVE_NOW — score mémoire 8.237/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- GWEI-EUR — MEMORY_24H — score mémoire 8.214/10 — sources ACCELERATION, V4 — MEMORY_ONLY

## Audit des plus fortes hausses

- MOVR-EUR +75.09% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- CT-EUR +48.05% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- SOON-EUR +22.25% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- GLMR-EUR +19.18% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- STX-EUR +18.44% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- CAP-EUR +14.39% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE
- SOMI-EUR +11.93% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- MON-EUR +10.87% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE
- WLD-EUR +10.72% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- AUDIO-EUR +10.66% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE

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
