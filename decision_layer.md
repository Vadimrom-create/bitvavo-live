# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-30T06:28:41.593494+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : CRV-EUR | action ACHETE_MAINTENANT | opportunité 8.172 | entrée 7.050 | trend 8.400 | rang 7.814
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : ICP-EUR | action PLACE_LIMITE_PASSIVE | opportunité 8.021 | entrée 6.400 | trend 9.200 | rang 7.977
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : TRB-EUR | action LATENT_ACCELERATOR | opportunité 7.501 | entrée 5.450 | trend 8.350 | rang 7.308
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : COMP-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.220 | entrée 6.000 | trend 9.200 | rang 8.043
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Tous les achats immédiats

1. CRV-EUR — ACHETE_MAINTENANT — rank 7.814 — opportunité 8.172 — entrée 7.050 — trend 8.400

## Top cross-sectionnel — aperçu non exhaustif

Ce top est une vue courte multi-buckets. Il ne doit jamais être utilisé comme liste exhaustive des achats immédiats.
1. COMP-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.043
2. ICP-EUR — MEILLEURE_LIMITE_PASSIVE — PLACE_LIMITE_PASSIVE — rank 7.977
3. AAVE-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.863

## Accélération indépendante

- ARK-EUR — CONFIRMED_ACCELERATION — score 9.883/10 — DETECTED_BUT_TOO_LATE
- GLMR-EUR — CONFIRMED_ACCELERATION — score 7.587/10 — DETECTED_BUT_TOO_LATE
- ICX-EUR — BUILDING_ACCELERATION — score 5.921/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- GWEI-EUR — BUILDING_ACCELERATION — score 5.843/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- 0G-EUR — BUILDING_ACCELERATION — score 5.333/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- SFP-EUR — BUILDING_ACCELERATION — score 5.233/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- MEW-EUR — BUILDING_ACCELERATION — score 5.198/10 — DETECTED_BUT_TOO_LATE
- BTT-EUR — BUILDING_ACCELERATION — score 4.908/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- TREAD-EUR — MEMORY_24H — score mémoire 9.983/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- ARK-EUR — ACTIVE_NOW — score mémoire 9.883/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- SWELL-EUR — MEMORY_24H — score mémoire 9.000/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- MOVR-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- AGI-EUR — MEMORY_24H — score mémoire 8.300/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- COMP-EUR — ACTIVE_NOW — score mémoire 8.043/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- SOLV-EUR — MEMORY_24H — score mémoire 8.017/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- ICP-EUR — ACTIVE_NOW — score mémoire 7.977/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- DOT-EUR — MEMORY_24H — score mémoire 7.899/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- GNS-EUR — MEMORY_24H — score mémoire 7.896/10 — sources ACCELERATION, V4 — MEMORY_ONLY

## Audit des plus fortes hausses

- MOVR-EUR +52.54% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- SOON-EUR +40.42% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- ZBCN-EUR +21.93% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- MEW-EUR +20.12% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- ZRO-EUR +19.35% — DETECTED_EARLY — couche NONE — action NONE
- QNT-EUR +18.32% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- PUMP-EUR +16.14% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- 0G-EUR +15.69% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- ARK-EUR +15.48% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- INIT-EUR +15.33% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE

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
