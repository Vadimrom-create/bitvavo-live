# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-10-01T06:32:56.513470+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : AAVE-EUR | action ACHETE_MAINTENANT | opportunité 8.293 | entrée 7.150 | trend 8.700 | rang 7.884
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : PROM-EUR | action PLACE_LIMITE_PASSIVE | opportunité 7.601 | entrée 6.200 | trend 8.400 | rang 7.472
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : ETHFI-EUR | action LATENT_ACCELERATOR | opportunité 8.124 | entrée 5.750 | trend 8.650 | rang 7.781
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : ZIG-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 9.046 | entrée 7.000 | trend 8.500 | rang 8.095
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Tous les achats immédiats

1. AAVE-EUR — ACHETE_MAINTENANT — rank 7.884 — opportunité 8.293 — entrée 7.150 — trend 8.700
2. XVG-EUR — ACHETE_MAINTENANT — rank 7.838 — opportunité 8.519 — entrée 6.950 — trend 8.200
3. NEAR-EUR — ACHETE_MAINTENANT — rank 7.607 — opportunité 8.084 — entrée 8.150 — trend 8.300
4. ENA-EUR — ACHETE_MAINTENANT — rank 7.479 — opportunité 8.164 — entrée 7.250 — trend 8.650

## Top cross-sectionnel — aperçu non exhaustif

Ce top est une vue courte multi-buckets. Il ne doit jamais être utilisé comme liste exhaustive des achats immédiats.
1. ZIG-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.095
2. AVAX-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.912
3. AAVE-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 7.884

## Accélération indépendante

- CT-EUR — CONFIRMED_ACCELERATION — score 8.105/10 — DETECTED_BUT_TOO_LATE
- GTC-EUR — BUILDING_ACCELERATION — score 6.344/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- ORCA-EUR — BUILDING_ACCELERATION — score 5.446/10 — DETECTED_BUT_TOO_LATE
- WIN-EUR — BUILDING_ACCELERATION — score 4.967/10 — DETECTED_BUT_TOO_LATE
- MEGA-EUR — BUILDING_ACCELERATION — score 4.936/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- PTB-EUR — BUILDING_ACCELERATION — score 4.930/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- PUMP-EUR — BUILDING_ACCELERATION — score 4.903/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- CAP-EUR — MEMORY_24H — score mémoire 9.090/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- CTR-EUR — MEMORY_24H — score mémoire 8.902/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- ACU-EUR — MEMORY_24H — score mémoire 8.894/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- ARPA-EUR — MEMORY_24H — score mémoire 8.595/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- PONKE-EUR — MEMORY_24H — score mémoire 8.400/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- MOVR-EUR — MEMORY_24H — score mémoire 8.346/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- CT-EUR — ACTIVE_NOW — score mémoire 8.105/10 — sources ACCELERATION — DETECTED_BUT_TOO_LATE
- ZIG-EUR — ACTIVE_NOW — score mémoire 8.095/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- AVAX-EUR — ACTIVE_NOW — score mémoire 7.912/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- AAVE-EUR — ACTIVE_NOW — score mémoire 7.884/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY

## Audit des plus fortes hausses

- MOVR-EUR +74.76% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- CT-EUR +53.95% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- STX-EUR +28.26% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- TRAC-EUR +27.37% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- MON-EUR +27.28% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- GLMR-EUR +23.82% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- NOM-EUR +19.83% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- CAP-EUR +18.69% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- NOS-EUR +16.45% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- PLUME-EUR +16.32% — DETECTED_EARLY — couche NONE — action NONE

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
