# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-10-02T23:28:40.224213+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : SUPER-EUR | action ACHETE_MAINTENANT | opportunité 9.268 | entrée 7.650 | trend 8.200 | rang 8.202
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : SKY-EUR | action PLACE_LIMITE_PASSIVE | opportunité 7.594 | entrée 6.600 | trend 8.500 | rang 7.585
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : MAGIC-EUR | action LATENT_ACCELERATOR | opportunité 8.025 | entrée 5.700 | trend 8.650 | rang 7.687
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : AAVE-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.373 | entrée 6.250 | trend 9.200 | rang 8.154
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Tous les achats immédiats

1. SUPER-EUR — ACHETE_MAINTENANT — rank 8.202 — opportunité 9.268 — entrée 7.650 — trend 8.200
2. AXS-EUR — ACHETE_MAINTENANT — rank 7.731 — opportunité 9.013 — entrée 6.850 — trend 7.350
3. SYRUP-EUR — ACHETE_MAINTENANT — rank 7.725 — opportunité 8.459 — entrée 7.150 — trend 8.200
4. XLM-EUR — ACHETE_MAINTENANT — rank 6.721 — opportunité 8.022 — entrée 7.150 — trend 5.700
5. BCH-EUR — ACHETE_MAINTENANT — rank 6.658 — opportunité 7.765 — entrée 7.250 — trend 5.750

## Top cross-sectionnel — aperçu non exhaustif

Ce top est une vue courte multi-buckets. Il ne doit jamais être utilisé comme liste exhaustive des achats immédiats.
1. SUPER-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.202
2. AAVE-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.154
3. FLUID-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.046

## Accélération indépendante

- CNPY-EUR — CONFIRMED_ACCELERATION — score 9.238/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- TRIA-EUR — BUILDING_ACCELERATION — score 5.644/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- CHZ-EUR — BUILDING_ACCELERATION — score 5.640/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- CHR-EUR — BUILDING_ACCELERATION — score 5.026/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- BIRB-EUR — BUILDING_ACCELERATION — score 4.910/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- SLX-EUR — BUILDING_ACCELERATION — score 4.836/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- EDGE-EUR — MEMORY_24H — score mémoire 10.000/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- CNPY-EUR — ACTIVE_NOW — score mémoire 9.238/10 — sources ACCELERATION, V4 — WATCH_ONLY
- PEOPLE-EUR — MEMORY_24H — score mémoire 9.036/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- GNS-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- SUPER-EUR — ACTIVE_NOW — score mémoire 8.202/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- SOSO-EUR — MEMORY_24H — score mémoire 8.156/10 — sources ACCELERATION — MEMORY_ONLY
- AAVE-EUR — ACTIVE_NOW — score mémoire 8.154/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- FLUID-EUR — ACTIVE_NOW — score mémoire 8.046/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- CSPR-EUR — MEMORY_24H — score mémoire 7.942/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- HUMA-EUR — ACTIVE_NOW — score mémoire 7.935/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY

## Audit des plus fortes hausses

- SAND-EUR +47.56% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- GALA-EUR +15.90% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- ATH-EUR +12.91% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- MANA-EUR +12.21% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- ENJ-EUR +11.51% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- APE-EUR +10.69% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- SPK-EUR +9.19% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- INIT-EUR +8.90% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE
- WLD-EUR +8.35% — DETECTED_EARLY — couche NONE — action NONE
- NOS-EUR +8.08% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION

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
