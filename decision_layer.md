# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-30T07:56:38.118559+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : HBAR-EUR | action ACHETE_MAINTENANT | opportunité 9.342 | entrée 7.800 | trend 8.400 | rang 8.343
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : WOO-EUR | action PLACE_LIMITE_PASSIVE | opportunité 8.243 | entrée 6.150 | trend 8.200 | rang 7.573
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : MOCA-EUR | action LATENT_ACCELERATOR | opportunité 8.056 | entrée 5.450 | trend 8.250 | rang 7.436
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : PLUME-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 9.151 | entrée 7.000 | trend 7.950 | rang 7.992
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Tous les achats immédiats

1. HBAR-EUR — ACHETE_MAINTENANT — rank 8.343 — opportunité 9.342 — entrée 7.800 — trend 8.400
2. XLM-EUR — ACHETE_MAINTENANT — rank 8.333 — opportunité 9.190 — entrée 7.650 — trend 8.500
3. ICP-EUR — ACHETE_MAINTENANT — rank 8.120 — opportunité 8.522 — entrée 7.150 — trend 8.900
4. SYRUP-EUR — ACHETE_MAINTENANT — rank 8.029 — opportunité 8.601 — entrée 6.800 — trend 8.700
5. BABY-EUR — ACHETE_MAINTENANT — rank 7.740 — opportunité 8.025 — entrée 6.900 — trend 8.450

## Top cross-sectionnel — aperçu non exhaustif

Ce top est une vue courte multi-buckets. Il ne doit jamais être utilisé comme liste exhaustive des achats immédiats.
1. HBAR-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.343
2. XLM-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.333
3. ICP-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.120

## Accélération indépendante

- GNS-EUR — CONFIRMED_ACCELERATION — score 8.500/10 — DETECTED_BUT_TOO_LATE
- MOVR-EUR — CONFIRMED_ACCELERATION — score 8.500/10 — DETECTED_BUT_TOO_LATE
- TRAC-EUR — CONFIRMED_ACCELERATION — score 8.317/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- TOWNS-EUR — CONFIRMED_ACCELERATION — score 7.754/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- RON-EUR — CONFIRMED_ACCELERATION — score 7.199/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- ICX-EUR — CONFIRMED_ACCELERATION — score 7.069/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- SCR-EUR — CONFIRMED_ACCELERATION — score 6.570/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- ONG-EUR — BUILDING_ACCELERATION — score 6.493/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- RED-EUR — BUILDING_ACCELERATION — score 6.448/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- SYRUP-EUR — BUILDING_ACCELERATION — score 6.414/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- SYRUP-EUR — ACTIVE_NOW — score mémoire 8.029/10 — sources ACCELERATION, DECISION_LAYER, V4 — BUYABLE_NOW
- BABY-EUR — ACTIVE_NOW — score mémoire 7.740/10 — sources ACCELERATION, DECISION_LAYER, V4 — BUYABLE_NOW
- TREAD-EUR — MEMORY_24H — score mémoire 9.983/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- SWELL-EUR — MEMORY_24H — score mémoire 9.000/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- GNS-EUR — ACTIVE_NOW — score mémoire 8.500/10 — sources ACCELERATION, V4 — DETECTED_BUT_TOO_LATE
- MOVR-EUR — ACTIVE_NOW — score mémoire 8.500/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- WMTX-EUR — MEMORY_24H — score mémoire 8.460/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- HBAR-EUR — ACTIVE_NOW — score mémoire 8.343/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- XLM-EUR — ACTIVE_NOW — score mémoire 8.333/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- TRAC-EUR — ACTIVE_NOW — score mémoire 8.317/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY

## Audit des plus fortes hausses

- MOVR-EUR +73.00% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- SOON-EUR +37.42% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- GTC-EUR +36.54% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- GNS-EUR +22.49% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- GLMR-EUR +18.84% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- 0G-EUR +17.34% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- ZBCN-EUR +16.62% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ZRO-EUR +15.93% — DETECTED_EARLY — couche NONE — action NONE
- PUMP-EUR +15.00% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- PHA-EUR +14.64% — DETECTED_EARLY — couche NONE — action INTERPRETATION

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
