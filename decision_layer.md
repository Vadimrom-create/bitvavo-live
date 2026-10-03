# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-10-03T01:30:16.003219+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : AAVE-EUR | action ACHETE_MAINTENANT | opportunité 9.397 | entrée 7.000 | trend 8.900 | rang 8.443
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : FLUID-EUR | action PLACE_LIMITE_PASSIVE | opportunité 7.773 | entrée 6.050 | trend 9.000 | rang 7.719
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : IMX-EUR | action LATENT_ACCELERATOR | opportunité 8.305 | entrée 5.600 | trend 8.700 | rang 7.599
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : ALGO-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 9.024 | entrée 6.650 | trend 8.450 | rang 8.080
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Tous les achats immédiats

1. AAVE-EUR — ACHETE_MAINTENANT — rank 8.443 — opportunité 9.397 — entrée 7.000 — trend 8.900
2. SYRUP-EUR — ACHETE_MAINTENANT — rank 8.122 — opportunité 9.252 — entrée 7.150 — trend 8.150
3. SUPER-EUR — ACHETE_MAINTENANT — rank 7.835 — opportunité 8.238 — entrée 7.700 — trend 8.550
4. WLD-EUR — ACHETE_MAINTENANT — rank 7.636 — opportunité 8.406 — entrée 7.250 — trend 8.700
5. SUI-EUR — ACHETE_MAINTENANT — rank 7.232 — opportunité 8.546 — entrée 7.400 — trend 6.900

## Top cross-sectionnel — aperçu non exhaustif

Ce top est une vue courte multi-buckets. Il ne doit jamais être utilisé comme liste exhaustive des achats immédiats.
1. AAVE-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.443
2. SYRUP-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.122
3. ALGO-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.080

## Accélération indépendante

- TREAD-EUR — CONFIRMED_ACCELERATION — score 8.776/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- ENJ-EUR — CONFIRMED_ACCELERATION — score 6.984/10 — DETECTED_BUT_TOO_LATE
- MOCA-EUR — BUILDING_ACCELERATION — score 6.255/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- AGI-EUR — BUILDING_ACCELERATION — score 6.083/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- CTK-EUR — BUILDING_ACCELERATION — score 5.988/10 — DETECTED_BUT_TOO_LATE
- ME-EUR — BUILDING_ACCELERATION — score 5.496/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- BAT-EUR — BUILDING_ACCELERATION — score 5.491/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- PUFFER-EUR — BUILDING_ACCELERATION — score 5.012/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- SUI-EUR — ACTIVE_NOW — score mémoire 7.232/10 — sources ACCELERATION, DECISION_LAYER, V4 — BUYABLE_NOW
- EDGE-EUR — MEMORY_24H — score mémoire 10.000/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- FOLD-EUR — MEMORY_24H — score mémoire 9.866/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- UP-EUR — MEMORY_24H — score mémoire 9.062/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- PEOPLE-EUR — MEMORY_24H — score mémoire 9.036/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- MOVE-EUR — MEMORY_24H — score mémoire 8.978/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- TREAD-EUR — ACTIVE_NOW — score mémoire 8.776/10 — sources ACCELERATION, V4 — WATCH_ONLY
- GNS-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- AAVE-EUR — ACTIVE_NOW — score mémoire 8.443/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- SOSO-EUR — MEMORY_24H — score mémoire 8.156/10 — sources ACCELERATION — MEMORY_ONLY

## Audit des plus fortes hausses

- SAND-EUR +57.31% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ENJ-EUR +20.38% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- GALA-EUR +17.62% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- ATH-EUR +13.96% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- CT-EUR +13.74% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- MANA-EUR +12.39% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- WLD-EUR +11.21% — DETECTED_EARLY — couche NONE — action NONE
- APE-EUR +10.51% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- SPK-EUR +8.79% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- NOS-EUR +8.38% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION

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
