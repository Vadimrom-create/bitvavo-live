# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-30T10:01:43.364995+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : SYRUP-EUR | action ACHETE_MAINTENANT | opportunité 9.278 | entrée 7.400 | trend 8.450 | rang 8.376
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : COMP-EUR | action PLACE_LIMITE_PASSIVE | opportunité 8.310 | entrée 6.000 | trend 9.200 | rang 8.095
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : COW-EUR | action LATENT_ACCELERATOR | opportunité 7.521 | entrée 4.500 | trend 8.650 | rang 7.354
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : MANA-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 9.009 | entrée 6.850 | trend 8.050 | rang 7.981
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Tous les achats immédiats

1. SYRUP-EUR — ACHETE_MAINTENANT — rank 8.376 — opportunité 9.278 — entrée 7.400 — trend 8.450
2. XLM-EUR — ACHETE_MAINTENANT — rank 8.176 — opportunité 8.743 — entrée 7.600 — trend 8.700
3. CRV-EUR — ACHETE_MAINTENANT — rank 8.143 — opportunité 9.232 — entrée 6.900 — trend 8.650
4. LDO-EUR — ACHETE_MAINTENANT — rank 7.703 — opportunité 8.571 — entrée 7.000 — trend 7.800
5. DOT-EUR — ACHETE_MAINTENANT — rank 7.510 — opportunité 8.052 — entrée 7.000 — trend 8.150
6. PEPE-EUR — ACHETE_MAINTENANT — rank 6.946 — opportunité 8.615 — entrée 7.500 — trend 5.650

## Top cross-sectionnel — aperçu non exhaustif

Ce top est une vue courte multi-buckets. Il ne doit jamais être utilisé comme liste exhaustive des achats immédiats.
1. SYRUP-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.376
2. XLM-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.176
3. CRV-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.143

## Accélération indépendante

- CTR-EUR — CONFIRMED_ACCELERATION — score 8.902/10 — DETECTED_BUT_TOO_LATE
- TRAC-EUR — CONFIRMED_ACCELERATION — score 8.678/10 — DETECTED_BUT_TOO_LATE
- SWELL-EUR — CONFIRMED_ACCELERATION — score 7.664/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- PEOPLE-EUR — CONFIRMED_ACCELERATION — score 7.447/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- CPOOL-EUR — CONFIRMED_ACCELERATION — score 7.283/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- ACX-EUR — CONFIRMED_ACCELERATION — score 6.781/10 — DETECTED_BUT_TOO_LATE
- GNS-EUR — BUILDING_ACCELERATION — score 6.480/10 — DETECTED_BUT_TOO_LATE
- NOS-EUR — BUILDING_ACCELERATION — score 6.236/10 — DETECTED_BUT_TOO_LATE
- PEAQ-EUR — BUILDING_ACCELERATION — score 6.206/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- ONT-EUR — BUILDING_ACCELERATION — score 5.856/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- CRV-EUR — ACTIVE_NOW — score mémoire 8.143/10 — sources ACCELERATION, DECISION_LAYER, V4 — BUYABLE_NOW
- DOT-EUR — ACTIVE_NOW — score mémoire 7.510/10 — sources ACCELERATION, DECISION_LAYER, V4 — BUYABLE_NOW
- TREAD-EUR — MEMORY_24H — score mémoire 9.983/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- CTR-EUR — ACTIVE_NOW — score mémoire 8.902/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- GWEI-EUR — MEMORY_24H — score mémoire 8.731/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- TRAC-EUR — ACTIVE_NOW — score mémoire 8.678/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- WMTX-EUR — MEMORY_24H — score mémoire 8.460/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- SYRUP-EUR — ACTIVE_NOW — score mémoire 8.376/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- LRC-EUR — MEMORY_24H — score mémoire 8.342/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- AGI-EUR — MEMORY_24H — score mémoire 8.300/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY

## Audit des plus fortes hausses

- MOVR-EUR +79.52% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- GTC-EUR +31.06% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- SOON-EUR +29.16% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- GLMR-EUR +29.10% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- PHA-EUR +22.41% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- ARK-EUR +19.47% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- TRAC-EUR +15.35% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- GWEI-EUR +15.04% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- PUMP-EUR +14.29% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- GNS-EUR +14.23% — DETECTED_EARLY — couche NONE — action INTERPRETATION

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
