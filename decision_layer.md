# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-10-03T03:19:23.661499+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : WLD-EUR | action ACHETE_MAINTENANT | opportunité 8.360 | entrée 7.700 | trend 8.700 | rang 7.845
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : AXS-EUR | action PLACE_LIMITE_PASSIVE | opportunité 8.613 | entrée 6.000 | trend 9.000 | rang 7.979
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : INIT-EUR | action LATENT_ACCELERATOR | opportunité 7.725 | entrée 5.550 | trend 8.500 | rang 7.452
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : ORCA-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.424 | entrée 6.650 | trend 8.750 | rang 7.936
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Tous les achats immédiats

1. WLD-EUR — ACHETE_MAINTENANT — rank 7.845 — opportunité 8.360 — entrée 7.700 — trend 8.700

## Top cross-sectionnel — aperçu non exhaustif

Ce top est une vue courte multi-buckets. Il ne doit jamais être utilisé comme liste exhaustive des achats immédiats.
1. AXS-EUR — MEILLEURE_LIMITE_PASSIVE — PLACE_LIMITE_PASSIVE — rank 7.979
2. ORCA-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.936
3. FLUID-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.907

## Accélération indépendante

- SWEAT-EUR — CONFIRMED_ACCELERATION — score 6.930/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- AIOZ-EUR — BUILDING_ACCELERATION — score 6.483/10 — DETECTED_BUT_TOO_LATE
- CT-EUR — BUILDING_ACCELERATION — score 5.594/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- CHZ-EUR — BUILDING_ACCELERATION — score 5.368/10 — DETECTED_BUT_TOO_LATE
- YGG-EUR — BUILDING_ACCELERATION — score 5.289/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- SAND-EUR — BUILDING_ACCELERATION — score 5.077/10 — DETECTED_BUT_TOO_LATE
- SLP-EUR — BUILDING_ACCELERATION — score 4.881/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- EDGE-EUR — MEMORY_24H — score mémoire 10.000/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- PEOPLE-EUR — MEMORY_24H — score mémoire 9.036/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- MOVE-EUR — MEMORY_24H — score mémoire 8.978/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- GNS-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- SOSO-EUR — MEMORY_24H — score mémoire 8.156/10 — sources ACCELERATION — MEMORY_ONLY
- AXS-EUR — ACTIVE_NOW — score mémoire 7.979/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- CSPR-EUR — MEMORY_24H — score mémoire 7.942/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- ORCA-EUR — ACTIVE_NOW — score mémoire 7.936/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- FLUID-EUR — ACTIVE_NOW — score mémoire 7.907/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- AAVE-EUR — ACTIVE_NOW — score mémoire 7.854/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY

## Audit des plus fortes hausses

- SAND-EUR +69.42% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ENJ-EUR +20.75% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- MANA-EUR +18.32% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- GALA-EUR +16.59% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- ATH-EUR +14.20% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- BAT-EUR +11.65% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE
- APE-EUR +10.84% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- TREAD-EUR +10.72% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- WLD-EUR +10.62% — DETECTED_EARLY — couche NONE — action NONE
- AGI-EUR +9.68% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE

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
