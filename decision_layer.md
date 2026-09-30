# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-30T18:23:47.023738+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : STX-EUR | action ACHETE_MAINTENANT | opportunité 8.208 | entrée 6.950 | trend 8.950 | rang 7.435
  - V4 buy-ready with acceptable current entry; no structural veto. High extension/chase is retained as risk context, not an automatic veto.
- **MEILLEURE_LIMITE_PASSIVE** : FLUX-EUR | action PLACE_LIMITE_PASSIVE | opportunité 7.621 | entrée 6.200 | trend 8.500 | rang 7.498
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : ZRO-EUR | action LATENT_ACCELERATOR | opportunité 7.725 | entrée 5.150 | trend 9.200 | rang 7.632
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : TRB-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 9.283 | entrée 6.650 | trend 8.350 | rang 8.204
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Tous les achats immédiats

1. STX-EUR — ACHETE_MAINTENANT — rank 7.435 — opportunité 8.208 — entrée 6.950 — trend 8.950

## Top cross-sectionnel — aperçu non exhaustif

Ce top est une vue courte multi-buckets. Il ne doit jamais être utilisé comme liste exhaustive des achats immédiats.
1. TRB-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.204
2. ALGO-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.183
3. XLM-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.053

## Accélération indépendante

- ARK-EUR — CONFIRMED_ACCELERATION — score 6.500/10 — DETECTED_BUT_TOO_LATE
- ICX-EUR — BUILDING_ACCELERATION — score 6.443/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- BTT-EUR — BUILDING_ACCELERATION — score 6.382/10 — DETECTED_BUT_TOO_LATE
- LMWR-EUR — BUILDING_ACCELERATION — score 5.217/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- S-EUR — BUILDING_ACCELERATION — score 5.194/10 — DETECTED_BUT_TOO_LATE
- NOS-EUR — BUILDING_ACCELERATION — score 4.785/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- EDGE-EUR — MEMORY_24H — score mémoire 9.861/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- CTR-EUR — MEMORY_24H — score mémoire 8.902/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- DGB-EUR — MEMORY_24H — score mémoire 8.670/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- ARPA-EUR — MEMORY_24H — score mémoire 8.595/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- CVC-EUR — MEMORY_24H — score mémoire 8.565/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- PONKE-EUR — MEMORY_24H — score mémoire 8.400/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- LRC-EUR — MEMORY_24H — score mémoire 8.342/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- GWEI-EUR — MEMORY_24H — score mémoire 8.214/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- TRB-EUR — ACTIVE_NOW — score mémoire 8.204/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- GNS-EUR — MEMORY_24H — score mémoire 8.190/10 — sources ACCELERATION, V4 — MEMORY_ONLY

## Audit des plus fortes hausses

- MOVR-EUR +60.15% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- CT-EUR +43.78% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- UP-EUR +26.29% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- SOON-EUR +23.37% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- GLMR-EUR +22.29% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- QNT-EUR +15.54% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- NOM-EUR +14.91% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- MERL-EUR +14.43% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- STX-EUR +12.66% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- NOS-EUR +12.37% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION

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
