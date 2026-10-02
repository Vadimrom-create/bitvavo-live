# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-10-02T09:18:19.060799+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : DYDX-EUR | action PLACE_LIMITE_PASSIVE | opportunité 7.690 | entrée 5.800 | trend 8.950 | rang 7.673
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : RUNE-EUR | action LATENT_ACCELERATOR | opportunité 7.570 | entrée 5.750 | trend 8.650 | rang 7.504
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : AAVE-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.337 | entrée 7.150 | trend 8.900 | rang 7.766
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Tous les achats immédiats

Aucun ACHETE_MAINTENANT dans le classement complet.

## Top cross-sectionnel — aperçu non exhaustif

Ce top est une vue courte multi-buckets. Il ne doit jamais être utilisé comme liste exhaustive des achats immédiats.
1. AAVE-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.766
2. STX-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.747
3. DYDX-EUR — MEILLEURE_LIMITE_PASSIVE — PLACE_LIMITE_PASSIVE — rank 7.673

## Accélération indépendante

- ENJ-EUR — CONFIRMED_ACCELERATION — score 8.797/10 — DETECTED_BUT_TOO_LATE
- SKY-EUR — CONFIRMED_ACCELERATION — score 8.514/10 — DETECTED_BUT_TOO_LATE
- GTC-EUR — CONFIRMED_ACCELERATION — score 7.154/10 — DETECTED_BUT_TOO_LATE
- NEX-EUR — CONFIRMED_ACCELERATION — score 7.118/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- MANA-EUR — CONFIRMED_ACCELERATION — score 6.838/10 — DETECTED_BUT_TOO_LATE
- SWEAT-EUR — BUILDING_ACCELERATION — score 5.397/10 — DETECTED_BUT_TOO_LATE
- CELR-EUR — BUILDING_ACCELERATION — score 5.280/10 — DETECTED_BUT_TOO_LATE
- SAND-EUR — BUILDING_ACCELERATION — score 5.034/10 — DETECTED_BUT_TOO_LATE
- TWT-EUR — BUILDING_ACCELERATION — score 4.946/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- BEAM-EUR — BUILDING_ACCELERATION — score 4.933/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- EDGE-EUR — MEMORY_24H — score mémoire 10.000/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- ICX-EUR — MEMORY_24H — score mémoire 9.403/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- TREAD-EUR — MEMORY_24H — score mémoire 9.258/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- OPEN-EUR — MEMORY_24H — score mémoire 9.112/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- PEOPLE-EUR — MEMORY_24H — score mémoire 9.036/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- ENJ-EUR — ACTIVE_NOW — score mémoire 8.797/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- SKY-EUR — ACTIVE_NOW — score mémoire 8.514/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- OSMO-EUR — MEMORY_24H — score mémoire 8.342/10 — sources ACCELERATION — MEMORY_ONLY
- ZRC-EUR — MEMORY_24H — score mémoire 8.257/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- HFT-EUR — MEMORY_24H — score mémoire 8.078/10 — sources ACCELERATION — MEMORY_ONLY

## Audit des plus fortes hausses

- SWEAT-EUR +184.38% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- SAND-EUR +48.02% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- CT-EUR +40.24% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- GTC-EUR +31.06% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- SCR-EUR +16.70% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- MANA-EUR +15.86% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- ENJ-EUR +15.60% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- MAGIC-EUR +14.15% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- SUPER-EUR +14.06% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- GALA-EUR +12.81% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION

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
