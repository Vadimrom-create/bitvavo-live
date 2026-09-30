# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-30T12:58:10.398014+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : XLM-EUR | action ACHETE_MAINTENANT | opportunité 9.411 | entrée 7.800 | trend 8.700 | rang 8.504
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : VIRTUAL-EUR | action PLACE_LIMITE_PASSIVE | opportunité 8.774 | entrée 6.750 | trend 7.550 | rang 7.519
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : COMP-EUR | action LATENT_ACCELERATOR | opportunité 8.102 | entrée 4.500 | trend 9.000 | rang 7.747
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : ICP-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.645 | entrée 7.250 | trend 9.200 | rang 8.261
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Tous les achats immédiats

1. XLM-EUR — ACHETE_MAINTENANT — rank 8.504 — opportunité 9.411 — entrée 7.800 — trend 8.700
2. LINK-EUR — ACHETE_MAINTENANT — rank 8.488 — opportunité 9.411 — entrée 7.800 — trend 8.700
3. ETHFI-EUR — ACHETE_MAINTENANT — rank 8.408 — opportunité 9.292 — entrée 7.600 — trend 8.650
4. AVAX-EUR — ACHETE_MAINTENANT — rank 8.374 — opportunité 9.293 — entrée 7.550 — trend 8.450
5. RENDER-EUR — ACHETE_MAINTENANT — rank 8.372 — opportunité 9.282 — entrée 8.050 — trend 8.400
6. AAVE-EUR — ACHETE_MAINTENANT — rank 8.180 — opportunité 9.444 — entrée 7.850 — trend 8.900
7. ONDO-EUR — ACHETE_MAINTENANT — rank 8.052 — opportunité 9.155 — entrée 7.850 — trend 7.900
8. ZRO-EUR — ACHETE_MAINTENANT — rank 8.049 — opportunité 8.574 — entrée 6.850 — trend 8.950
9. SEI-EUR — ACHETE_MAINTENANT — rank 8.041 — opportunité 9.117 — entrée 7.650 — trend 7.800
10. SYRUP-EUR — ACHETE_MAINTENANT — rank 8.024 — opportunité 8.736 — entrée 7.200 — trend 8.450
11. TAO-EUR — ACHETE_MAINTENANT — rank 7.894 — opportunité 9.048 — entrée 8.050 — trend 7.700
12. FET-EUR — ACHETE_MAINTENANT — rank 7.874 — opportunité 9.194 — entrée 7.550 — trend 7.900
13. SUI-EUR — ACHETE_MAINTENANT — rank 7.814 — opportunité 9.167 — entrée 7.800 — trend 7.900
14. CFG-EUR — ACHETE_MAINTENANT — rank 7.782 — opportunité 9.054 — entrée 7.400 — trend 7.550
15. POL-EUR — ACHETE_MAINTENANT — rank 7.644 — opportunité 8.345 — entrée 6.900 — trend 7.950
16. ADA-EUR — ACHETE_MAINTENANT — rank 7.614 — opportunité 8.983 — entrée 7.850 — trend 7.100
17. WIF-EUR — ACHETE_MAINTENANT — rank 7.585 — opportunité 8.208 — entrée 7.400 — trend 7.800
18. ENA-EUR — ACHETE_MAINTENANT — rank 7.543 — opportunité 8.780 — entrée 7.500 — trend 7.550
19. NEAR-EUR — ACHETE_MAINTENANT — rank 7.535 — opportunité 8.443 — entrée 7.850 — trend 7.750
20. ETC-EUR — ACHETE_MAINTENANT — rank 7.390 — opportunité 8.766 — entrée 7.400 — trend 6.950
21. SHIB-EUR — ACHETE_MAINTENANT — rank 7.322 — opportunité 8.900 — entrée 7.200 — trend 6.600
22. SOL-EUR — ACHETE_MAINTENANT — rank 7.120 — opportunité 8.914 — entrée 7.850 — trend 6.800
23. PENGU-EUR — ACHETE_MAINTENANT — rank 6.919 — opportunité 8.399 — entrée 6.900 — trend 6.350
24. PEPE-EUR — ACHETE_MAINTENANT — rank 6.845 — opportunité 8.637 — entrée 7.400 — trend 5.650
25. ETH-EUR — ACHETE_MAINTENANT — rank 6.823 — opportunité 8.640 — entrée 7.600 — trend 5.350
26. VET-EUR — ACHETE_MAINTENANT — rank 6.728 — opportunité 8.509 — entrée 6.950 — trend 5.700
27. BTC-EUR — ACHETE_MAINTENANT — rank 6.269 — opportunité 8.523 — entrée 7.850 — trend 5.100

## Top cross-sectionnel — aperçu non exhaustif

Ce top est une vue courte multi-buckets. Il ne doit jamais être utilisé comme liste exhaustive des achats immédiats.
1. XLM-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.504
2. LINK-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.488
3. ETHFI-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.408

## Accélération indépendante

- ZBCN-EUR — CONFIRMED_ACCELERATION — score 8.872/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- AIOZ-EUR — CONFIRMED_ACCELERATION — score 8.688/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- EGLD-EUR — CONFIRMED_ACCELERATION — score 8.340/10 — DETECTED_BUT_TOO_LATE
- SPX-EUR — CONFIRMED_ACCELERATION — score 8.198/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- RAY-EUR — CONFIRMED_ACCELERATION — score 8.020/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- EDGE-EUR — CONFIRMED_ACCELERATION — score 7.755/10 — DETECTED_BUT_TOO_LATE
- NPC-EUR — CONFIRMED_ACCELERATION — score 7.542/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- SOMI-EUR — CONFIRMED_ACCELERATION — score 7.525/10 — DETECTED_BUT_TOO_LATE
- STX-EUR — CONFIRMED_ACCELERATION — score 7.232/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- KITE-EUR — CONFIRMED_ACCELERATION — score 7.185/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- RENDER-EUR — ACTIVE_NOW — score mémoire 8.372/10 — sources ACCELERATION, DECISION_LAYER, V4 — BUYABLE_NOW
- FET-EUR — ACTIVE_NOW — score mémoire 7.874/10 — sources ACCELERATION, DECISION_LAYER, V4 — BUYABLE_NOW
- SUI-EUR — ACTIVE_NOW — score mémoire 7.814/10 — sources ACCELERATION, DECISION_LAYER, V4 — BUYABLE_NOW
- BTT-EUR — MEMORY_24H — score mémoire 9.062/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- ZEN-EUR — MEMORY_24H — score mémoire 9.021/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- CTR-EUR — MEMORY_24H — score mémoire 8.902/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- ZBCN-EUR — ACTIVE_NOW — score mémoire 8.872/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- GWEI-EUR — MEMORY_24H — score mémoire 8.731/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- AIOZ-EUR — ACTIVE_NOW — score mémoire 8.688/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- DGB-EUR — MEMORY_24H — score mémoire 8.670/10 — sources ACCELERATION, V4 — MEMORY_ONLY

## Audit des plus fortes hausses

- ARK-EUR +57.99% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- MOVR-EUR +52.71% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- CT-EUR +38.41% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- SOON-EUR +35.05% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- QNT-EUR +21.20% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- SOMI-EUR +20.24% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- GLMR-EUR +19.14% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- NIL-EUR +15.03% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- GTC-EUR +14.93% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- PHA-EUR +13.17% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE

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
