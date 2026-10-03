# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-10-03T03:44:34.306121+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : ORCA-EUR | action ACHETE_MAINTENANT | opportunité 8.388 | entrée 6.900 | trend 8.750 | rang 7.965
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : SUPER-EUR | action PLACE_LIMITE_PASSIVE | opportunité 7.518 | entrée 6.650 | trend 8.550 | rang 7.574
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : NMR-EUR | action LATENT_ACCELERATOR | opportunité 7.544 | entrée 5.450 | trend 8.200 | rang 7.256
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : ALICE-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 9.093 | entrée 6.650 | trend 8.400 | rang 8.043
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Tous les achats immédiats

1. ORCA-EUR — ACHETE_MAINTENANT — rank 7.965 — opportunité 8.388 — entrée 6.900 — trend 8.750
2. WLD-EUR — ACHETE_MAINTENANT — rank 7.777 — opportunité 8.096 — entrée 7.600 — trend 8.700

## Top cross-sectionnel — aperçu non exhaustif

Ce top est une vue courte multi-buckets. Il ne doit jamais être utilisé comme liste exhaustive des achats immédiats.
1. ALICE-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.043
2. ORCA-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 7.965
3. FLUID-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.947

## Accélération indépendante

- SPK-EUR — CONFIRMED_ACCELERATION — score 7.453/10 — DETECTED_BUT_TOO_LATE
- HFT-EUR — CONFIRMED_ACCELERATION — score 7.397/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- BIGTIME-EUR — CONFIRMED_ACCELERATION — score 7.333/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- TOWNS-EUR — CONFIRMED_ACCELERATION — score 6.611/10 — DETECTED_BUT_TOO_LATE
- TLM-EUR — BUILDING_ACCELERATION — score 6.191/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- SOLV-EUR — BUILDING_ACCELERATION — score 5.891/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- EDU-EUR — BUILDING_ACCELERATION — score 5.817/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- AEVO-EUR — BUILDING_ACCELERATION — score 5.684/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- AXS-EUR — BUILDING_ACCELERATION — score 5.564/10 — DETECTED_BUT_TOO_LATE
- CHZ-EUR — BUILDING_ACCELERATION — score 5.485/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- EDGE-EUR — MEMORY_24H — score mémoire 10.000/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- PEOPLE-EUR — MEMORY_24H — score mémoire 9.036/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- MOVE-EUR — MEMORY_24H — score mémoire 8.978/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- GNS-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- SOSO-EUR — MEMORY_24H — score mémoire 8.156/10 — sources ACCELERATION — MEMORY_ONLY
- ALICE-EUR — ACTIVE_NOW — score mémoire 8.043/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- ORCA-EUR — ACTIVE_NOW — score mémoire 7.965/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- FLUID-EUR — ACTIVE_NOW — score mémoire 7.947/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- CSPR-EUR — MEMORY_24H — score mémoire 7.942/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- AAVE-EUR — ACTIVE_NOW — score mémoire 7.805/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY

## Audit des plus fortes hausses

- SAND-EUR +80.05% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- MANA-EUR +21.01% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- ENJ-EUR +18.16% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ATH-EUR +13.15% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- GALA-EUR +13.12% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- CT-EUR +13.07% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- APE-EUR +12.58% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- AXS-EUR +12.17% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- BAT-EUR +11.24% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE
- WLD-EUR +10.54% — DETECTED_EARLY — couche NONE — action NONE

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
