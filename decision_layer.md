# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-30T11:59:46.155094+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : CRV-EUR | action ACHETE_MAINTENANT | opportunité 9.307 | entrée 7.100 | trend 8.650 | rang 8.408
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : ZRO-EUR | action PLACE_LIMITE_PASSIVE | opportunité 7.907 | entrée 5.850 | trend 8.950 | rang 7.514
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : SPK-EUR | action LATENT_ACCELERATOR | opportunité 8.919 | entrée 5.500 | trend 7.700 | rang 7.473
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : AAVE-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 9.281 | entrée 7.250 | trend 8.450 | rang 8.393
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Tous les achats immédiats

1. CRV-EUR — ACHETE_MAINTENANT — rank 8.408 — opportunité 9.307 — entrée 7.100 — trend 8.650
2. POL-EUR — ACHETE_MAINTENANT — rank 8.175 — opportunité 9.151 — entrée 7.200 — trend 7.950
3. XLM-EUR — ACHETE_MAINTENANT — rank 7.942 — opportunité 8.269 — entrée 7.350 — trend 8.700
4. HBAR-EUR — ACHETE_MAINTENANT — rank 7.892 — opportunité 8.645 — entrée 6.900 — trend 8.400
5. RENDER-EUR — ACHETE_MAINTENANT — rank 7.885 — opportunité 8.423 — entrée 7.400 — trend 8.150
6. LTC-EUR — ACHETE_MAINTENANT — rank 7.776 — opportunité 8.594 — entrée 7.400 — trend 7.700
7. LDO-EUR — ACHETE_MAINTENANT — rank 7.739 — opportunité 8.628 — entrée 6.950 — trend 7.800
8. TAO-EUR — ACHETE_MAINTENANT — rank 7.059 — opportunité 7.992 — entrée 7.000 — trend 6.850

## Top cross-sectionnel — aperçu non exhaustif

Ce top est une vue courte multi-buckets. Il ne doit jamais être utilisé comme liste exhaustive des achats immédiats.
1. CRV-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.408
2. AAVE-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.393
3. SYRUP-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.259

## Accélération indépendante

- ZEN-EUR — CONFIRMED_ACCELERATION — score 9.021/10 — DETECTED_BUT_TOO_LATE
- CVC-EUR — CONFIRMED_ACCELERATION — score 8.565/10 — DETECTED_BUT_TOO_LATE
- SPK-EUR — CONFIRMED_ACCELERATION — score 7.692/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- NOM-EUR — CONFIRMED_ACCELERATION — score 6.860/10 — DETECTED_BUT_TOO_LATE
- PEOPLE-EUR — CONFIRMED_ACCELERATION — score 6.639/10 — DETECTED_BUT_TOO_LATE
- AIOZ-EUR — BUILDING_ACCELERATION — score 5.623/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- NIL-EUR — BUILDING_ACCELERATION — score 5.556/10 — DETECTED_BUT_TOO_LATE
- MLN-EUR — BUILDING_ACCELERATION — score 5.376/10 — DETECTED_BUT_TOO_LATE
- FET-EUR — BUILDING_ACCELERATION — score 5.115/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- BIO-EUR — BUILDING_ACCELERATION — score 4.973/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- HBAR-EUR — ACTIVE_NOW — score mémoire 7.892/10 — sources ACCELERATION, DECISION_LAYER, V4 — BUYABLE_NOW
- ZEN-EUR — ACTIVE_NOW — score mémoire 9.021/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- BTT-EUR — MEMORY_24H — score mémoire 8.963/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- CTR-EUR — MEMORY_24H — score mémoire 8.902/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- GWEI-EUR — MEMORY_24H — score mémoire 8.731/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- DGB-EUR — MEMORY_24H — score mémoire 8.670/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- CVC-EUR — ACTIVE_NOW — score mémoire 8.565/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- PUNDIX-EUR — MEMORY_24H — score mémoire 8.561/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- WMTX-EUR — MEMORY_24H — score mémoire 8.460/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- CRV-EUR — ACTIVE_NOW — score mémoire 8.408/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY

## Audit des plus fortes hausses

- MOVR-EUR +58.95% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- ARK-EUR +53.43% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- CT-EUR +52.33% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- SOON-EUR +33.90% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- QNT-EUR +26.35% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- GLMR-EUR +21.21% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- GTC-EUR +17.13% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- PHA-EUR +16.62% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- NIL-EUR +14.86% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- NOM-EUR +13.02% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION

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
