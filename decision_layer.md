# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-30T09:43:56.907951+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : XLM-EUR | action ACHETE_MAINTENANT | opportunité 9.365 | entrée 8.050 | trend 8.500 | rang 8.418
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : ENJ-EUR | action PLACE_LIMITE_PASSIVE | opportunité 8.993 | entrée 6.250 | trend 7.500 | rang 7.801
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : C-EUR | action LATENT_ACCELERATOR | opportunité 7.823 | entrée 4.500 | trend 8.450 | rang 7.419
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : W-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 9.210 | entrée 7.250 | trend 8.150 | rang 8.253
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Tous les achats immédiats

1. XLM-EUR — ACHETE_MAINTENANT — rank 8.418 — opportunité 9.365 — entrée 8.050 — trend 8.500
2. CRV-EUR — ACHETE_MAINTENANT — rank 8.181 — opportunité 9.329 — entrée 7.250 — trend 8.400
3. LDO-EUR — ACHETE_MAINTENANT — rank 8.050 — opportunité 9.012 — entrée 7.500 — trend 8.150
4. DOT-EUR — ACHETE_MAINTENANT — rank 7.883 — opportunité 8.925 — entrée 7.000 — trend 7.950
5. RENDER-EUR — ACHETE_MAINTENANT — rank 7.653 — opportunité 8.034 — entrée 7.050 — trend 8.150
6. ADA-EUR — ACHETE_MAINTENANT — rank 7.423 — opportunité 8.857 — entrée 7.850 — trend 6.550
7. SOL-EUR — ACHETE_MAINTENANT — rank 7.229 — opportunité 8.695 — entrée 7.400 — trend 6.450
8. ETH-EUR — ACHETE_MAINTENANT — rank 6.470 — opportunité 8.331 — entrée 7.850 — trend 4.650

## Top cross-sectionnel — aperçu non exhaustif

Ce top est une vue courte multi-buckets. Il ne doit jamais être utilisé comme liste exhaustive des achats immédiats.
1. XLM-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.418
2. W-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.253
3. CRV-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.181

## Accélération indépendante

- GWEI-EUR — CONFIRMED_ACCELERATION — score 8.731/10 — DETECTED_BUT_TOO_LATE
- LRC-EUR — CONFIRMED_ACCELERATION — score 8.342/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- SUSHI-EUR — CONFIRMED_ACCELERATION — score 7.132/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- MOVR-EUR — CONFIRMED_ACCELERATION — score 6.670/10 — DETECTED_BUT_TOO_LATE
- ATH-EUR — BUILDING_ACCELERATION — score 6.427/10 — DETECTED_BUT_TOO_LATE
- KSM-EUR — BUILDING_ACCELERATION — score 6.128/10 — DETECTED_BUT_TOO_LATE
- ENJ-EUR — BUILDING_ACCELERATION — score 5.874/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- EGLD-EUR — BUILDING_ACCELERATION — score 5.720/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- DUSK-EUR — BUILDING_ACCELERATION — score 5.505/10 — DETECTED_BUT_TOO_LATE
- LAYER-EUR — BUILDING_ACCELERATION — score 5.341/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- CRV-EUR — ACTIVE_NOW — score mémoire 8.181/10 — sources ACCELERATION, DECISION_LAYER, V4 — BUYABLE_NOW
- DOT-EUR — ACTIVE_NOW — score mémoire 7.883/10 — sources ACCELERATION, DECISION_LAYER, V4 — BUYABLE_NOW
- TREAD-EUR — MEMORY_24H — score mémoire 9.983/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- GWEI-EUR — ACTIVE_NOW — score mémoire 8.731/10 — sources ACCELERATION, V4 — DETECTED_BUT_TOO_LATE
- WMTX-EUR — MEMORY_24H — score mémoire 8.460/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- XLM-EUR — ACTIVE_NOW — score mémoire 8.418/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- LRC-EUR — ACTIVE_NOW — score mémoire 8.342/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- AGI-EUR — MEMORY_24H — score mémoire 8.300/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- W-EUR — ACTIVE_NOW — score mémoire 8.253/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- DYDX-EUR — MEMORY_24H — score mémoire 8.239/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY

## Audit des plus fortes hausses

- MOVR-EUR +100.09% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- GTC-EUR +33.74% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- GLMR-EUR +32.49% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- SOON-EUR +31.17% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- PHA-EUR +25.13% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- ARK-EUR +21.41% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- 0G-EUR +13.71% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- GWEI-EUR +13.15% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ZRO-EUR +12.60% — DETECTED_EARLY — couche NONE — action NONE
- MEW-EUR +12.42% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE

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
