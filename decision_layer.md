# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-10-01T04:24:51.037656+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : ALGO-EUR | action ACHETE_MAINTENANT | opportunité 9.314 | entrée 7.500 | trend 8.400 | rang 8.218
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : CELO-EUR | action PLACE_LIMITE_PASSIVE | opportunité 7.832 | entrée 5.850 | trend 8.400 | rang 7.429
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : KSM-EUR | action LATENT_ACCELERATOR | opportunité 7.873 | entrée 5.700 | trend 8.900 | rang 7.727
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : HUMA-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.347 | entrée 6.600 | trend 8.900 | rang 7.992
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Tous les achats immédiats

1. ALGO-EUR — ACHETE_MAINTENANT — rank 8.218 — opportunité 9.314 — entrée 7.500 — trend 8.400
2. AVAX-EUR — ACHETE_MAINTENANT — rank 8.042 — opportunité 8.280 — entrée 8.100 — trend 8.700
3. ENA-EUR — ACHETE_MAINTENANT — rank 7.757 — opportunité 8.209 — entrée 7.300 — trend 8.400
4. NEAR-EUR — ACHETE_MAINTENANT — rank 7.718 — opportunité 8.106 — entrée 7.400 — trend 8.250
5. RENDER-EUR — ACHETE_MAINTENANT — rank 7.550 — opportunité 8.644 — entrée 6.950 — trend 7.300
6. KAS-EUR — ACHETE_MAINTENANT — rank 7.457 — opportunité 8.085 — entrée 7.100 — trend 7.700
7. FET-EUR — ACHETE_MAINTENANT — rank 7.399 — opportunité 8.844 — entrée 7.450 — trend 6.550
8. ADA-EUR — ACHETE_MAINTENANT — rank 7.383 — opportunité 8.810 — entrée 7.850 — trend 6.350
9. PEPE-EUR — ACHETE_MAINTENANT — rank 7.265 — opportunité 8.758 — entrée 7.600 — trend 6.150
10. DOGE-EUR — ACHETE_MAINTENANT — rank 7.061 — opportunité 8.605 — entrée 7.600 — trend 5.600
11. SHIB-EUR — ACHETE_MAINTENANT — rank 6.470 — opportunité 8.225 — entrée 7.250 — trend 5.050

## Top cross-sectionnel — aperçu non exhaustif

Ce top est une vue courte multi-buckets. Il ne doit jamais être utilisé comme liste exhaustive des achats immédiats.
1. ALGO-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.218
2. AVAX-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.042
3. HUMA-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.992

## Accélération indépendante

- JTO-EUR — CONFIRMED_ACCELERATION — score 7.000/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- ZETA-EUR — BUILDING_ACCELERATION — score 6.086/10 — DETECTED_BUT_TOO_LATE
- AUDIO-EUR — BUILDING_ACCELERATION — score 5.481/10 — DETECTED_BUT_TOO_LATE
- CTSI-EUR — BUILDING_ACCELERATION — score 5.447/10 — DETECTED_BUT_TOO_LATE
- AMP-EUR — BUILDING_ACCELERATION — score 5.384/10 — DETECTED_BUT_TOO_LATE
- VSN-EUR — BUILDING_ACCELERATION — score 5.355/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- GNS-EUR — BUILDING_ACCELERATION — score 4.935/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- ALGO-EUR — ACTIVE_NOW — score mémoire 8.218/10 — sources ACCELERATION, DECISION_LAYER, V4 — BUYABLE_NOW
- AAVE-EUR — ACTIVE_NOW — score mémoire 7.731/10 — sources ACCELERATION, DECISION_LAYER, V4 — BUYABLE_NOW
- LMWR-EUR — MEMORY_24H — score mémoire 9.685/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- CT-EUR — MEMORY_24H — score mémoire 9.156/10 — sources ACCELERATION — MEMORY_ONLY
- LIGHTER-EUR — MEMORY_24H — score mémoire 9.020/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- CTR-EUR — MEMORY_24H — score mémoire 8.902/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- ACU-EUR — MEMORY_24H — score mémoire 8.894/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- ARPA-EUR — MEMORY_24H — score mémoire 8.595/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- GLMR-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- PONKE-EUR — MEMORY_24H — score mémoire 8.400/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY

## Audit des plus fortes hausses

- MOVR-EUR +85.68% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- CT-EUR +45.92% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- GLMR-EUR +36.76% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- STX-EUR +23.60% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- TRAC-EUR +22.77% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- MON-EUR +21.72% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- PLUME-EUR +18.51% — DETECTED_EARLY — couche NONE — action NONE
- CAP-EUR +16.67% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- SAFE-EUR +15.82% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- RED-EUR +13.47% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION

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
