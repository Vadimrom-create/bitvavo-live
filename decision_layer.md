# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-10-26T23:29:21.748158+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : INIT-EUR | action PLACE_LIMITE_PASSIVE | opportunité 7.412 | entrée 6.300 | trend 8.550 | rang 7.185
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : ELSA-EUR | action LATENT_ACCELERATOR | opportunité 7.578 | entrée 5.550 | trend 8.650 | rang 6.953
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : DODO-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 7.579 | entrée 5.750 | trend 8.650 | rang 7.159
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Tous les achats immédiats

Aucun ACHETE_MAINTENANT dans le classement complet.

## Top cross-sectionnel — aperçu non exhaustif

Ce top est une vue courte multi-buckets. Il ne doit jamais être utilisé comme liste exhaustive des achats immédiats.
1. INIT-EUR — MEILLEURE_LIMITE_PASSIVE — PLACE_LIMITE_PASSIVE — rank 7.185
2. DODO-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.159
3. ELSA-EUR — MEILLEUR_LATENT_ACCELERATOR — LATENT_ACCELERATOR — rank 6.953

## Accélération indépendante

- MLN-EUR — BUILDING_ACCELERATION — score 6.271/10 — DETECTED_BUT_TOO_LATE
- OSMO-EUR — BUILDING_ACCELERATION — score 5.832/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- SOLV-EUR — BUILDING_ACCELERATION — score 4.798/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- PTB-EUR — MEMORY_24H — score mémoire 8.912/10 — sources ACCELERATION — MEMORY_ONLY
- GROVE-EUR — MEMORY_24H — score mémoire 8.703/10 — sources ACCELERATION — MEMORY_ONLY
- WHUF-EUR — MEMORY_DECAY_24_72H — score mémoire 8.598/10 — sources ACCELERATION — MEMORY_ONLY
- PROMPT-EUR — MEMORY_24H — score mémoire 8.512/10 — sources ACCELERATION — MEMORY_ONLY
- PHA-EUR — MEMORY_24H — score mémoire 7.246/10 — sources ACCELERATION, DECISION_LAYER — MEMORY_ONLY
- IMU-EUR — MEMORY_24H — score mémoire 7.235/10 — sources ACCELERATION — MEMORY_ONLY
- INIT-EUR — ACTIVE_NOW — score mémoire 7.185/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- WIN-EUR — ACTIVE_NOW — score mémoire 7.162/10 — sources DECISION_LAYER, V4 — WATCH_ONLY
- DODO-EUR — ACTIVE_NOW — score mémoire 7.159/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- HAEDAL-EUR — MEMORY_24H — score mémoire 7.035/10 — sources ACCELERATION — MEMORY_ONLY

## Audit des plus fortes hausses

- ZRC-EUR +39.22% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- NEX-EUR +23.14% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- CHIP-EUR +17.40% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- PARTI-EUR +16.58% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- SYN-EUR +16.11% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- VERONA-EUR +14.89% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- HAEDAL-EUR +12.57% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE
- BEAM-EUR +12.29% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- KAT-EUR +10.51% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- SOON-EUR +9.94% — DETECTED_EARLY — couche NONE — action INTERPRETATION

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
