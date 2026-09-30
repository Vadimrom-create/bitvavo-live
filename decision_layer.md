# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-30T19:05:30.812174+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : XLM-EUR | action ACHETE_MAINTENANT | opportunité 9.202 | entrée 8.050 | trend 8.700 | rang 8.501
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : RENDER-EUR | action PLACE_LIMITE_PASSIVE | opportunité 7.734 | entrée 6.550 | trend 8.200 | rang 7.536
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : KSM-EUR | action LATENT_ACCELERATOR | opportunité 7.840 | entrée 5.200 | trend 9.200 | rang 7.656
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : XVG-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 9.131 | entrée 6.900 | trend 7.950 | rang 8.130
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Tous les achats immédiats

1. XLM-EUR — ACHETE_MAINTENANT — rank 8.501 — opportunité 9.202 — entrée 8.050 — trend 8.700
2. PUMP-EUR — ACHETE_MAINTENANT — rank 7.675 — opportunité 8.096 — entrée 7.250 — trend 8.500

## Top cross-sectionnel — aperçu non exhaustif

Ce top est une vue courte multi-buckets. Il ne doit jamais être utilisé comme liste exhaustive des achats immédiats.
1. XLM-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.501
2. XVG-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.130
3. SUSHI-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.848

## Accélération indépendante

- CT-EUR — CONFIRMED_ACCELERATION — score 9.221/10 — DETECTED_BUT_TOO_LATE
- CAP-EUR — CONFIRMED_ACCELERATION — score 6.656/10 — DETECTED_BUT_TOO_LATE
- TRAC-EUR — CONFIRMED_ACCELERATION — score 6.553/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- UP-EUR — BUILDING_ACCELERATION — score 6.496/10 — DETECTED_BUT_TOO_LATE
- WELL-EUR — BUILDING_ACCELERATION — score 5.533/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- MOVR-EUR — BUILDING_ACCELERATION — score 5.261/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- EDGE-EUR — MEMORY_24H — score mémoire 9.861/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- CT-EUR — ACTIVE_NOW — score mémoire 9.221/10 — sources ACCELERATION — DETECTED_BUT_TOO_LATE
- CTR-EUR — MEMORY_24H — score mémoire 8.902/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- DGB-EUR — MEMORY_24H — score mémoire 8.670/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- ARPA-EUR — MEMORY_24H — score mémoire 8.595/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- CVC-EUR — MEMORY_24H — score mémoire 8.565/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- XLM-EUR — ACTIVE_NOW — score mémoire 8.501/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- PONKE-EUR — MEMORY_24H — score mémoire 8.400/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- GWEI-EUR — MEMORY_24H — score mémoire 8.214/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- GNS-EUR — MEMORY_24H — score mémoire 8.190/10 — sources ACCELERATION, V4 — MEMORY_ONLY

## Audit des plus fortes hausses

- MOVR-EUR +54.91% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- CT-EUR +52.60% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- SOON-EUR +21.39% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- UP-EUR +19.37% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- GLMR-EUR +17.55% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- PHA-EUR +15.40% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- TRAC-EUR +14.40% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- SOMI-EUR +12.06% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- MERL-EUR +11.96% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- CAP-EUR +11.92% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE

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
