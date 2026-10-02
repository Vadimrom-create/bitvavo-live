# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-10-02T13:05:55.263693+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : PUMP-EUR | action ACHETE_MAINTENANT | opportunité 9.030 | entrée 7.400 | trend 7.800 | rang 7.855
  - V4 buy-ready with acceptable current entry; no structural veto. High extension/chase is retained as risk context, not an automatic veto.
- **MEILLEURE_LIMITE_PASSIVE** : RARE-EUR | action PLACE_LIMITE_PASSIVE | opportunité 8.536 | entrée 6.050 | trend 7.400 | rang 7.453
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : DYDX-EUR | action LATENT_ACCELERATOR | opportunité 7.820 | entrée 5.300 | trend 8.950 | rang 7.633
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : IMX-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 9.335 | entrée 6.400 | trend 8.650 | rang 8.076
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Tous les achats immédiats

1. PUMP-EUR — ACHETE_MAINTENANT — rank 7.855 — opportunité 9.030 — entrée 7.400 — trend 7.800
2. ZRO-EUR — ACHETE_MAINTENANT — rank 7.733 — opportunité 9.088 — entrée 6.900 — trend 8.800
3. AVAX-EUR — ACHETE_MAINTENANT — rank 7.425 — opportunité 8.677 — entrée 7.600 — trend 6.650
4. ADA-EUR — ACHETE_MAINTENANT — rank 7.248 — opportunité 8.034 — entrée 7.600 — trend 6.900
5. ONDO-EUR — ACHETE_MAINTENANT — rank 7.097 — opportunité 8.613 — entrée 7.500 — trend 6.150
6. SUI-EUR — ACHETE_MAINTENANT — rank 7.038 — opportunité 8.418 — entrée 7.650 — trend 6.150
7. ICP-EUR — ACHETE_MAINTENANT — rank 6.718 — opportunité 8.214 — entrée 7.300 — trend 6.500

## Top cross-sectionnel — aperçu non exhaustif

Ce top est une vue courte multi-buckets. Il ne doit jamais être utilisé comme liste exhaustive des achats immédiats.
1. IMX-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.076
2. STX-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.894
3. PUMP-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 7.855

## Accélération indépendante

- NOS-EUR — CONFIRMED_ACCELERATION — score 9.573/10 — DETECTED_BUT_TOO_LATE
- PUMP-EUR — CONFIRMED_ACCELERATION — score 7.928/10 — DETECTED_BUT_TOO_LATE
- GRASS-EUR — CONFIRMED_ACCELERATION — score 7.052/10 — DETECTED_BUT_TOO_LATE
- WLD-EUR — CONFIRMED_ACCELERATION — score 6.921/10 — DETECTED_BUT_TOO_LATE
- ZRO-EUR — CONFIRMED_ACCELERATION — score 6.752/10 — DETECTED_BUT_TOO_LATE
- ENS-EUR — CONFIRMED_ACCELERATION — score 6.717/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- GNS-EUR — CONFIRMED_ACCELERATION — score 6.709/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- SPK-EUR — CONFIRMED_ACCELERATION — score 6.646/10 — DETECTED_BUT_TOO_LATE
- GIGA-EUR — BUILDING_ACCELERATION — score 6.444/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- IKA-EUR — BUILDING_ACCELERATION — score 5.969/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- EDGE-EUR — MEMORY_24H — score mémoire 10.000/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- NOS-EUR — ACTIVE_NOW — score mémoire 9.573/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- TREAD-EUR — MEMORY_24H — score mémoire 9.258/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- PEOPLE-EUR — MEMORY_24H — score mémoire 9.036/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- U-EUR — MEMORY_24H — score mémoire 8.740/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- OSMO-EUR — MEMORY_DECAY_24_72H — score mémoire 8.262/10 — sources ACCELERATION — MEMORY_ONLY
- ZRC-EUR — MEMORY_24H — score mémoire 8.257/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- IMX-EUR — ACTIVE_NOW — score mémoire 8.076/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- SAND-EUR — MEMORY_24H — score mémoire 8.000/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- CSPR-EUR — MEMORY_24H — score mémoire 7.942/10 — sources ACCELERATION, V4 — MEMORY_ONLY

## Audit des plus fortes hausses

- SAND-EUR +60.17% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ENJ-EUR +26.92% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- GTC-EUR +24.20% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- GALA-EUR +19.58% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- SKY-EUR +18.20% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- MANA-EUR +17.55% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- SUPER-EUR +17.37% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- NOS-EUR +15.90% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- CT-EUR +15.23% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- MAGIC-EUR +14.59% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION

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
