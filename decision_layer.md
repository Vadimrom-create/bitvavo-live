# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-10-05T13:06:40.793708+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : AAVE-EUR | action ACHETE_MAINTENANT | opportunité 9.383 | entrée 7.500 | trend 8.700 | rang 8.251
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : AKT-EUR | action PLACE_LIMITE_PASSIVE | opportunité 7.550 | entrée 6.250 | trend 8.400 | rang 7.487
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : MAGIC-EUR | action LATENT_ACCELERATOR | opportunité 7.725 | entrée 5.550 | trend 8.200 | rang 7.351
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : BAT-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.177 | entrée 5.850 | trend 8.900 | rang 7.907
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Tous les achats immédiats

1. AAVE-EUR — ACHETE_MAINTENANT — rank 8.251 — opportunité 9.383 — entrée 7.500 — trend 8.700
2. QNT-EUR — ACHETE_MAINTENANT — rank 7.508 — opportunité 8.733 — entrée 7.250 — trend 7.450

## Top cross-sectionnel — aperçu non exhaustif

Ce top est une vue courte multi-buckets. Il ne doit jamais être utilisé comme liste exhaustive des achats immédiats.
1. AAVE-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.251
2. BAT-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.907
3. FET-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.885

## Accélération indépendante

- EDU-EUR — CONFIRMED_ACCELERATION — score 9.962/10 — DETECTED_BUT_TOO_LATE
- MOCA-EUR — CONFIRMED_ACCELERATION — score 7.144/10 — DETECTED_BUT_TOO_LATE
- THQ-EUR — CONFIRMED_ACCELERATION — score 6.618/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- GNS-EUR — BUILDING_ACCELERATION — score 5.926/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- AAVE-EUR — BUILDING_ACCELERATION — score 5.391/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- GTC-EUR — BUILDING_ACCELERATION — score 5.148/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- QNT-EUR — ACTIVE_NOW — score mémoire 7.508/10 — sources ACCELERATION, DECISION_LAYER, V4 — BUYABLE_NOW
- EDU-EUR — ACTIVE_NOW — score mémoire 9.962/10 — sources ACCELERATION — DETECTED_BUT_TOO_LATE
- SWELL-EUR — MEMORY_24H — score mémoire 9.171/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- FIDA-EUR — MEMORY_DECAY_24_72H — score mémoire 9.053/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- ACT-EUR — MEMORY_24H — score mémoire 8.838/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- PLUME-EUR — MEMORY_24H — score mémoire 8.672/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- RLC-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- TREAD-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- UMA-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- PORTAL-EUR — MEMORY_24H — score mémoire 8.374/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY

## Audit des plus fortes hausses

- GTC-EUR +93.84% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- PNT-EUR +78.52% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE
- RLC-EUR +55.06% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- FLUID-EUR +27.32% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- SCR-EUR +19.29% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- EDU-EUR +17.22% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- CARV-EUR +15.96% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- NIL-EUR +12.70% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- ADA-EUR +12.07% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- UMA-EUR +11.63% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE

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
