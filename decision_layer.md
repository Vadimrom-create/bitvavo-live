# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-10-01T06:57:47.541631+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : W-EUR | action ACHETE_MAINTENANT | opportunité 8.821 | entrée 7.600 | trend 8.150 | rang 8.064
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : DEEP-EUR | action PLACE_LIMITE_PASSIVE | opportunité 7.713 | entrée 6.250 | trend 8.650 | rang 7.652
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : DIA-EUR | action LATENT_ACCELERATOR | opportunité 8.618 | entrée 5.600 | trend 8.500 | rang 7.880
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : KSM-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.690 | entrée 6.500 | trend 8.950 | rang 8.217
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Tous les achats immédiats

1. W-EUR — ACHETE_MAINTENANT — rank 8.064 — opportunité 8.821 — entrée 7.600 — trend 8.150
2. WLD-EUR — ACHETE_MAINTENANT — rank 8.046 — opportunité 8.459 — entrée 7.600 — trend 8.650
3. AAVE-EUR — ACHETE_MAINTENANT — rank 7.807 — opportunité 8.034 — entrée 7.150 — trend 8.700
4. FET-EUR — ACHETE_MAINTENANT — rank 7.750 — opportunité 8.957 — entrée 7.400 — trend 7.550
5. ENA-EUR — ACHETE_MAINTENANT — rank 7.723 — opportunité 8.110 — entrée 7.650 — trend 8.650
6. PUMP-EUR — ACHETE_MAINTENANT — rank 7.721 — opportunité 8.604 — entrée 7.400 — trend 8.250
7. TAO-EUR — ACHETE_MAINTENANT — rank 7.310 — opportunité 8.062 — entrée 7.600 — trend 7.050

## Top cross-sectionnel — aperçu non exhaustif

Ce top est une vue courte multi-buckets. Il ne doit jamais être utilisé comme liste exhaustive des achats immédiats.
1. KSM-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.217
2. AVAX-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.177
3. MERL-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.064

## Accélération indépendante

- MOVR-EUR — CONFIRMED_ACCELERATION — score 7.314/10 — DETECTED_BUT_TOO_LATE
- MOVE-EUR — CONFIRMED_ACCELERATION — score 7.093/10 — DETECTED_BUT_TOO_LATE
- STX-EUR — CONFIRMED_ACCELERATION — score 6.933/10 — DETECTED_BUT_TOO_LATE
- MERL-EUR — BUILDING_ACCELERATION — score 6.115/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- FET-EUR — BUILDING_ACCELERATION — score 5.884/10 — DETECTED_BUT_TOO_LATE
- ZRO-EUR — BUILDING_ACCELERATION — score 5.883/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- RE-EUR — BUILDING_ACCELERATION — score 5.631/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- MIOTA-EUR — BUILDING_ACCELERATION — score 5.184/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- XYO-EUR — BUILDING_ACCELERATION — score 4.931/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- FTT-EUR — BUILDING_ACCELERATION — score 4.842/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- CAP-EUR — MEMORY_24H — score mémoire 9.090/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- CTR-EUR — MEMORY_24H — score mémoire 8.902/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- ACU-EUR — MEMORY_24H — score mémoire 8.894/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- ARPA-EUR — MEMORY_24H — score mémoire 8.595/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- PONKE-EUR — MEMORY_24H — score mémoire 8.400/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- KSM-EUR — ACTIVE_NOW — score mémoire 8.217/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- AVAX-EUR — ACTIVE_NOW — score mémoire 8.177/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- CT-EUR — MEMORY_24H — score mémoire 8.105/10 — sources ACCELERATION — MEMORY_ONLY
- MERL-EUR — ACTIVE_NOW — score mémoire 8.064/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- W-EUR — ACTIVE_NOW — score mémoire 8.064/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY

## Audit des plus fortes hausses

- MOVR-EUR +88.40% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- CT-EUR +53.05% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- STX-EUR +33.21% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- MON-EUR +27.62% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- GLMR-EUR +22.60% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- CAP-EUR +21.43% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- TRAC-EUR +20.03% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- NOM-EUR +19.21% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- NOS-EUR +18.85% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- PLUME-EUR +15.44% — DETECTED_EARLY — couche NONE — action NONE

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
