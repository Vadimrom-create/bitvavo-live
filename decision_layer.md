# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-10-01T15:39:05.945610+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : AAVE-EUR | action ACHETE_MAINTENANT | opportunité 8.264 | entrée 6.950 | trend 8.900 | rang 7.966
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : TRB-EUR | action PLACE_LIMITE_PASSIVE | opportunité 7.470 | entrée 6.350 | trend 8.000 | rang 7.154
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : KSM-EUR | action LATENT_ACCELERATOR | opportunité 7.974 | entrée 4.750 | trend 8.900 | rang 7.658
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : PROM-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 9.344 | entrée 6.950 | trend 8.950 | rang 8.512
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Tous les achats immédiats

1. AAVE-EUR — ACHETE_MAINTENANT — rank 7.966 — opportunité 8.264 — entrée 6.950 — trend 8.900
2. STX-EUR — ACHETE_MAINTENANT — rank 7.648 — opportunité 8.620 — entrée 7.200 — trend 8.950

## Top cross-sectionnel — aperçu non exhaustif

Ce top est une vue courte multi-buckets. Il ne doit jamais être utilisé comme liste exhaustive des achats immédiats.
1. PROM-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.512
2. ZRO-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.179
3. AAVE-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 7.966

## Accélération indépendante

- MEGA-EUR — CONFIRMED_ACCELERATION — score 8.157/10 — DETECTED_BUT_TOO_LATE
- SOON-EUR — CONFIRMED_ACCELERATION — score 7.535/10 — DETECTED_BUT_TOO_LATE
- TAI-EUR — CONFIRMED_ACCELERATION — score 7.328/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- MOVR-EUR — CONFIRMED_ACCELERATION — score 7.053/10 — DETECTED_BUT_TOO_LATE
- ZRO-EUR — CONFIRMED_ACCELERATION — score 6.585/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- ZAMA-EUR — BUILDING_ACCELERATION — score 6.364/10 — DETECTED_BUT_TOO_LATE
- RE-EUR — BUILDING_ACCELERATION — score 6.300/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- OGN-EUR — BUILDING_ACCELERATION — score 5.997/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- PTB-EUR — BUILDING_ACCELERATION — score 5.900/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- SWEAT-EUR — BUILDING_ACCELERATION — score 5.500/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- AAVE-EUR — ACTIVE_NOW — score mémoire 7.966/10 — sources ACCELERATION, DECISION_LAYER, V4 — BUYABLE_NOW
- CPOOL-EUR — MEMORY_24H — score mémoire 10.000/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- XYO-EUR — MEMORY_24H — score mémoire 9.473/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- CT-EUR — MEMORY_24H — score mémoire 8.691/10 — sources ACCELERATION — MEMORY_ONLY
- ARPA-EUR — MEMORY_24H — score mémoire 8.595/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- PROM-EUR — ACTIVE_NOW — score mémoire 8.512/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- OSMO-EUR — MEMORY_24H — score mémoire 8.342/10 — sources ACCELERATION — MEMORY_ONLY
- ZRO-EUR — ACTIVE_NOW — score mémoire 8.179/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- MEGA-EUR — ACTIVE_NOW — score mémoire 8.157/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- KAIA-EUR — ACTIVE_NOW — score mémoire 7.833/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY

## Audit des plus fortes hausses

- SWEAT-EUR +105.43% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- MOVR-EUR +57.59% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- ALICE-EUR +31.45% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- CAP-EUR +31.38% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- CT-EUR +24.92% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- MON-EUR +19.11% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- NOS-EUR +18.86% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- MEGA-EUR +18.61% — DETECTED_EARLY — couche NONE — action NONE
- SYN-EUR +17.36% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- STX-EUR +14.26% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION

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
