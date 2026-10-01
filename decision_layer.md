# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-10-01T04:00:26.244753+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : AVAX-EUR | action ACHETE_MAINTENANT | opportunité 8.597 | entrée 7.450 | trend 8.700 | rang 8.087
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : HUMA-EUR | action PLACE_LIMITE_PASSIVE | opportunité 8.127 | entrée 6.000 | trend 8.900 | rang 7.862
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : WOO-EUR | action LATENT_ACCELERATOR | opportunité 8.041 | entrée 5.250 | trend 8.500 | rang 7.629
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : AVNT-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 9.308 | entrée 6.350 | trend 8.450 | rang 8.178
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Tous les achats immédiats

1. AVAX-EUR — ACHETE_MAINTENANT — rank 8.087 — opportunité 8.597 — entrée 7.450 — trend 8.700
2. ENA-EUR — ACHETE_MAINTENANT — rank 8.081 — opportunité 8.786 — entrée 7.450 — trend 8.400
3. KAS-EUR — ACHETE_MAINTENANT — rank 7.993 — opportunité 9.042 — entrée 7.450 — trend 7.700
4. AAVE-EUR — ACHETE_MAINTENANT — rank 7.852 — opportunité 8.378 — entrée 7.000 — trend 8.700
5. ALGO-EUR — ACHETE_MAINTENANT — rank 7.772 — opportunité 8.683 — entrée 6.800 — trend 8.400
6. NEAR-EUR — ACHETE_MAINTENANT — rank 7.653 — opportunité 8.148 — entrée 7.150 — trend 8.250
7. RENDER-EUR — ACHETE_MAINTENANT — rank 7.502 — opportunité 8.711 — entrée 7.050 — trend 7.300
8. PEPE-EUR — ACHETE_MAINTENANT — rank 7.298 — opportunité 8.812 — entrée 7.650 — trend 6.150
9. WIF-EUR — ACHETE_MAINTENANT — rank 7.274 — opportunité 8.265 — entrée 7.000 — trend 7.150
10. VIRTUAL-EUR — ACHETE_MAINTENANT — rank 7.104 — opportunité 8.982 — entrée 6.950 — trend 7.300
11. ETH-EUR — ACHETE_MAINTENANT — rank 6.465 — opportunité 8.454 — entrée 7.600 — trend 4.800

## Top cross-sectionnel — aperçu non exhaustif

Ce top est une vue courte multi-buckets. Il ne doit jamais être utilisé comme liste exhaustive des achats immédiats.
1. AVNT-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.178
2. HBAR-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.159
3. MMT-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.102

## Accélération indépendante

- KAIA-EUR — CONFIRMED_ACCELERATION — score 9.710/10 — DETECTED_BUT_TOO_LATE
- MON-EUR — CONFIRMED_ACCELERATION — score 6.776/10 — DETECTED_BUT_TOO_LATE
- DUSK-EUR — CONFIRMED_ACCELERATION — score 6.717/10 — DETECTED_BUT_TOO_LATE
- DYDX-EUR — CONFIRMED_ACCELERATION — score 6.571/10 — DETECTED_BUT_TOO_LATE
- IMX-EUR — CONFIRMED_ACCELERATION — score 6.568/10 — DETECTED_BUT_TOO_LATE
- PEOPLE-EUR — BUILDING_ACCELERATION — score 5.805/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- CAT-EUR — BUILDING_ACCELERATION — score 5.553/10 — DETECTED_BUT_TOO_LATE
- 1INCH-EUR — BUILDING_ACCELERATION — score 5.549/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- EGLD-EUR — BUILDING_ACCELERATION — score 5.427/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- LINEA-EUR — BUILDING_ACCELERATION — score 5.423/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- ALGO-EUR — ACTIVE_NOW — score mémoire 7.772/10 — sources ACCELERATION, DECISION_LAYER, V4 — BUYABLE_NOW
- KAIA-EUR — ACTIVE_NOW — score mémoire 9.710/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- LMWR-EUR — MEMORY_24H — score mémoire 9.685/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- CT-EUR — MEMORY_24H — score mémoire 9.156/10 — sources ACCELERATION — MEMORY_ONLY
- LIGHTER-EUR — MEMORY_24H — score mémoire 9.020/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- CTR-EUR — MEMORY_24H — score mémoire 8.902/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- ACU-EUR — MEMORY_24H — score mémoire 8.894/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- ARPA-EUR — MEMORY_24H — score mémoire 8.595/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- GLMR-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- PONKE-EUR — MEMORY_24H — score mémoire 8.400/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY

## Audit des plus fortes hausses

- MOVR-EUR +88.09% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- CT-EUR +47.49% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- GLMR-EUR +37.55% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- TRAC-EUR +25.64% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- MON-EUR +23.79% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- STX-EUR +23.77% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- PLUME-EUR +17.55% — DETECTED_EARLY — couche NONE — action NONE
- NOS-EUR +14.41% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- KAIA-EUR +13.71% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- SOON-EUR +13.66% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION

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
