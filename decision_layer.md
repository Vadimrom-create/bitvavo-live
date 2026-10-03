# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-10-03T02:01:39.714689+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : SYRUP-EUR | action ACHETE_MAINTENANT | opportunité 8.253 | entrée 7.400 | trend 8.150 | rang 7.747
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : HUMA-EUR | action PLACE_LIMITE_PASSIVE | opportunité 7.742 | entrée 6.200 | trend 8.650 | rang 7.614
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : FLUID-EUR | action LATENT_ACCELERATOR | opportunité 7.961 | entrée 5.750 | trend 9.000 | rang 7.832
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : AAVE-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.411 | entrée 6.350 | trend 8.900 | rang 8.008
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Tous les achats immédiats

1. SYRUP-EUR — ACHETE_MAINTENANT — rank 7.747 — opportunité 8.253 — entrée 7.400 — trend 8.150
2. WLD-EUR — ACHETE_MAINTENANT — rank 7.631 — opportunité 8.206 — entrée 7.350 — trend 8.700

## Top cross-sectionnel — aperçu non exhaustif

Ce top est une vue courte multi-buckets. Il ne doit jamais être utilisé comme liste exhaustive des achats immédiats.
1. AAVE-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.008
2. FLUID-EUR — MEILLEUR_LATENT_ACCELERATOR — LATENT_ACCELERATOR — rank 7.832
3. SYRUP-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 7.747

## Accélération indépendante

- NOS-EUR — CONFIRMED_ACCELERATION — score 6.984/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- TRAC-EUR — CONFIRMED_ACCELERATION — score 6.860/10 — DETECTED_BUT_TOO_LATE
- BRETT-EUR — BUILDING_ACCELERATION — score 5.764/10 — DETECTED_BUT_TOO_LATE
- MOVR-EUR — BUILDING_ACCELERATION — score 5.445/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- EDGE-EUR — MEMORY_24H — score mémoire 10.000/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- FOLD-EUR — MEMORY_24H — score mémoire 9.866/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- PEOPLE-EUR — MEMORY_24H — score mémoire 9.036/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- MOVE-EUR — MEMORY_24H — score mémoire 8.978/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- GNS-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- SOSO-EUR — MEMORY_24H — score mémoire 8.156/10 — sources ACCELERATION — MEMORY_ONLY
- AAVE-EUR — ACTIVE_NOW — score mémoire 8.008/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- CSPR-EUR — MEMORY_24H — score mémoire 7.942/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- FLUID-EUR — ACTIVE_NOW — score mémoire 7.832/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- SYRUP-EUR — ACTIVE_NOW — score mémoire 7.747/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY

## Audit des plus fortes hausses

- SAND-EUR +48.74% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ATH-EUR +15.01% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- GALA-EUR +14.90% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- ENJ-EUR +14.68% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- CT-EUR +12.57% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- WLD-EUR +10.59% — DETECTED_EARLY — couche NONE — action NONE
- NOS-EUR +9.62% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- MANA-EUR +9.40% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- APE-EUR +9.16% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- UP-EUR +8.64% — DETECTED_EARLY — couche NONE — action INTERPRETATION

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
