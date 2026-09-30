# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-30T22:39:09.136093+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : XLM-EUR | action ACHETE_MAINTENANT | opportunité 8.189 | entrée 7.450 | trend 8.700 | rang 8.012
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : MMT-EUR | action PLACE_LIMITE_PASSIVE | opportunité 7.783 | entrée 6.350 | trend 8.750 | rang 7.716
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : RED-EUR | action LATENT_ACCELERATOR | opportunité 7.774 | entrée 5.750 | trend 9.200 | rang 7.695
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : ALGO-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.947 | entrée 6.850 | trend 8.650 | rang 8.266
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Tous les achats immédiats

1. XLM-EUR — ACHETE_MAINTENANT — rank 8.012 — opportunité 8.189 — entrée 7.450 — trend 8.700
2. DOT-EUR — ACHETE_MAINTENANT — rank 7.745 — opportunité 8.450 — entrée 6.850 — trend 7.950
3. CRV-EUR — ACHETE_MAINTENANT — rank 7.724 — opportunité 8.059 — entrée 7.300 — trend 8.400
4. VIRTUAL-EUR — ACHETE_MAINTENANT — rank 7.512 — opportunité 8.294 — entrée 6.950 — trend 7.550
5. WLD-EUR — ACHETE_MAINTENANT — rank 7.503 — opportunité 8.259 — entrée 7.200 — trend 7.800

## Top cross-sectionnel — aperçu non exhaustif

Ce top est une vue courte multi-buckets. Il ne doit jamais être utilisé comme liste exhaustive des achats immédiats.
1. ALGO-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.266
2. SYRUP-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.241
3. XLM-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.012

## Accélération indépendante

- HNT-EUR — CONFIRMED_ACCELERATION — score 8.500/10 — DETECTED_BUT_TOO_LATE
- STX-EUR — CONFIRMED_ACCELERATION — score 7.100/10 — DETECTED_BUT_TOO_LATE
- AIOZ-EUR — CONFIRMED_ACCELERATION — score 6.616/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- MOVR-EUR — BUILDING_ACCELERATION — score 6.371/10 — DETECTED_BUT_TOO_LATE
- NIL-EUR — BUILDING_ACCELERATION — score 6.371/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- MON-EUR — BUILDING_ACCELERATION — score 6.362/10 — DETECTED_BUT_TOO_LATE
- ZBCN-EUR — BUILDING_ACCELERATION — score 6.136/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- VIRTUAL-EUR — BUILDING_ACCELERATION — score 6.091/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- DOT-EUR — BUILDING_ACCELERATION — score 5.960/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- MOVE-EUR — BUILDING_ACCELERATION — score 5.743/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- LMWR-EUR — MEMORY_24H — score mémoire 9.685/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- CTR-EUR — MEMORY_24H — score mémoire 8.902/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- ARPA-EUR — MEMORY_24H — score mémoire 8.595/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- CVC-EUR — MEMORY_24H — score mémoire 8.565/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- HNT-EUR — ACTIVE_NOW — score mémoire 8.500/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- PONKE-EUR — MEMORY_24H — score mémoire 8.400/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- ALGO-EUR — ACTIVE_NOW — score mémoire 8.266/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- SYRUP-EUR — ACTIVE_NOW — score mémoire 8.241/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- GWEI-EUR — MEMORY_24H — score mémoire 8.214/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- XLM-EUR — ACTIVE_NOW — score mémoire 8.012/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY

## Audit des plus fortes hausses

- MOVR-EUR +74.48% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- CT-EUR +48.59% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- SOON-EUR +21.61% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- GLMR-EUR +20.02% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- STX-EUR +17.63% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- CAP-EUR +14.69% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE
- NOS-EUR +12.86% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- SOMI-EUR +12.14% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- MON-EUR +11.47% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE
- NOM-EUR +11.44% — DETECTED_EARLY — couche NONE — action INTERPRETATION

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
