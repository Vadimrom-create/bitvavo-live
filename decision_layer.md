# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-30T17:01:13.509350+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : RENDER-EUR | action ACHETE_MAINTENANT | opportunité 8.255 | entrée 7.150 | trend 8.400 | rang 7.859
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : COMP-EUR | action PLACE_LIMITE_PASSIVE | opportunité 8.278 | entrée 5.800 | trend 9.000 | rang 7.962
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : MIOTA-EUR | action LATENT_ACCELERATOR | opportunité 8.314 | entrée 5.550 | trend 8.900 | rang 7.869
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : ICP-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.488 | entrée 7.350 | trend 9.200 | rang 8.317
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Tous les achats immédiats

1. RENDER-EUR — ACHETE_MAINTENANT — rank 7.859 — opportunité 8.255 — entrée 7.150 — trend 8.400
2. SUI-EUR — ACHETE_MAINTENANT — rank 7.748 — opportunité 8.442 — entrée 7.250 — trend 8.150
3. NEAR-EUR — ACHETE_MAINTENANT — rank 7.732 — opportunité 8.875 — entrée 7.400 — trend 7.700
4. LINK-EUR — ACHETE_MAINTENANT — rank 7.722 — opportunité 8.024 — entrée 6.900 — trend 8.450
5. PUMP-EUR — ACHETE_MAINTENANT — rank 7.695 — opportunité 8.753 — entrée 7.500 — trend 8.500

## Top cross-sectionnel — aperçu non exhaustif

Ce top est une vue courte multi-buckets. Il ne doit jamais être utilisé comme liste exhaustive des achats immédiats.
1. ICP-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.317
2. PLUME-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.204
3. ZRO-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.191

## Accélération indépendante

- GLMR-EUR — CONFIRMED_ACCELERATION — score 9.015/10 — DETECTED_BUT_TOO_LATE
- PONKE-EUR — CONFIRMED_ACCELERATION — score 8.400/10 — DETECTED_BUT_TOO_LATE
- ZIG-EUR — BUILDING_ACCELERATION — score 6.397/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- SOLV-EUR — BUILDING_ACCELERATION — score 5.970/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- DEEP-EUR — BUILDING_ACCELERATION — score 5.948/10 — DETECTED_BUT_TOO_LATE
- PLUME-EUR — BUILDING_ACCELERATION — score 5.632/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- KAITO-EUR — BUILDING_ACCELERATION — score 4.957/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- AI-EUR — BUILDING_ACCELERATION — score 4.875/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- GAS-EUR — BUILDING_ACCELERATION — score 4.861/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- ZORA-EUR — BUILDING_ACCELERATION — score 4.766/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- SUI-EUR — ACTIVE_NOW — score mémoire 7.748/10 — sources ACCELERATION, DECISION_LAYER, V4 — BUYABLE_NOW
- EDGE-EUR — MEMORY_24H — score mémoire 9.861/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- GLMR-EUR — ACTIVE_NOW — score mémoire 9.015/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- CTR-EUR — MEMORY_24H — score mémoire 8.902/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- DGB-EUR — MEMORY_24H — score mémoire 8.670/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- MOVR-EUR — MEMORY_24H — score mémoire 8.615/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- ARPA-EUR — MEMORY_24H — score mémoire 8.595/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- CVC-EUR — MEMORY_24H — score mémoire 8.565/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- ICX-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- PONKE-EUR — ACTIVE_NOW — score mémoire 8.400/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE

## Audit des plus fortes hausses

- MOVR-EUR +65.14% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- CT-EUR +50.62% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- NOM-EUR +24.93% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- GLMR-EUR +23.07% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- QNT-EUR +21.61% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- SOON-EUR +15.09% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- RED-EUR +14.30% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- EPIC-EUR +14.14% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- MERL-EUR +13.41% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- DEEP-EUR +13.21% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION

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
