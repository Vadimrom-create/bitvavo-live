# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-10-02T15:16:50.023518+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : DYDX-EUR | action PLACE_LIMITE_PASSIVE | opportunité 7.734 | entrée 5.800 | trend 8.950 | rang 7.691
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : ZIG-EUR | action LATENT_ACCELERATOR | opportunité 7.836 | entrée 5.350 | trend 8.950 | rang 7.709
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : NOM-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.470 | entrée 6.900 | trend 8.650 | rang 7.957
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Tous les achats immédiats

Aucun ACHETE_MAINTENANT dans le classement complet.

## Top cross-sectionnel — aperçu non exhaustif

Ce top est une vue courte multi-buckets. Il ne doit jamais être utilisé comme liste exhaustive des achats immédiats.
1. NOM-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.957
2. MON-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.836
3. AAVE-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.768

## Accélération indépendante

- MAGIC-EUR — CONFIRMED_ACCELERATION — score 9.974/10 — DETECTED_BUT_TOO_LATE
- AGI-EUR — CONFIRMED_ACCELERATION — score 8.500/10 — DETECTED_BUT_TOO_LATE
- DBR-EUR — CONFIRMED_ACCELERATION — score 8.273/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- INIT-EUR — CONFIRMED_ACCELERATION — score 8.255/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- THQ-EUR — CONFIRMED_ACCELERATION — score 7.472/10 — DETECTED_BUT_TOO_LATE
- SCR-EUR — BUILDING_ACCELERATION — score 5.917/10 — DETECTED_BUT_TOO_LATE
- SHELL-EUR — BUILDING_ACCELERATION — score 5.725/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- SOON-EUR — BUILDING_ACCELERATION — score 5.513/10 — DETECTED_BUT_TOO_LATE
- XYO-EUR — BUILDING_ACCELERATION — score 5.094/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- ZEUS-EUR — BUILDING_ACCELERATION — score 5.016/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- EDGE-EUR — MEMORY_24H — score mémoire 10.000/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- MAGIC-EUR — ACTIVE_NOW — score mémoire 9.974/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- TREAD-EUR — MEMORY_24H — score mémoire 9.258/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- PEOPLE-EUR — MEMORY_24H — score mémoire 9.036/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- AIOZ-EUR — MEMORY_24H — score mémoire 8.925/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- U-EUR — MEMORY_24H — score mémoire 8.740/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- AGI-EUR — ACTIVE_NOW — score mémoire 8.500/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- ZRC-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- DBR-EUR — ACTIVE_NOW — score mémoire 8.273/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- INIT-EUR — ACTIVE_NOW — score mémoire 8.255/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY

## Audit des plus fortes hausses

- SAND-EUR +45.77% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- MAGIC-EUR +25.88% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- GTC-EUR +19.68% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- NOS-EUR +18.78% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ZRO-EUR +17.75% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- SKY-EUR +16.70% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- APE-EUR +14.90% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- WLD-EUR +14.07% — DETECTED_EARLY — couche NONE — action NONE
- GALA-EUR +13.82% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- ATH-EUR +13.29% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE

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
