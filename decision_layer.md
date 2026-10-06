# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-10-06T20:01:28.577718+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : STX-EUR | action PLACE_LIMITE_PASSIVE | opportunité 7.442 | entrée 6.700 | trend 8.150 | rang 7.134
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : ESP-EUR | action LATENT_ACCELERATOR | opportunité 7.565 | entrée 5.300 | trend 9.000 | rang 7.416
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : RENDER-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.069 | entrée 7.200 | trend 9.200 | rang 7.897
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Tous les achats immédiats

Aucun ACHETE_MAINTENANT dans le classement complet.

## Top cross-sectionnel — aperçu non exhaustif

Ce top est une vue courte multi-buckets. Il ne doit jamais être utilisé comme liste exhaustive des achats immédiats.
1. RENDER-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.897
2. ADA-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.547
3. API3-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.428

## Accélération indépendante

- U-EUR — CONFIRMED_ACCELERATION — score 7.236/10 — DETECTED_BUT_TOO_LATE
- CSPR-EUR — CONFIRMED_ACCELERATION — score 6.845/10 — DETECTED_BUT_TOO_LATE
- LIGHTER-EUR — BUILDING_ACCELERATION — score 5.593/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- PENGU-EUR — BUILDING_ACCELERATION — score 5.251/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- NPC-EUR — BUILDING_ACCELERATION — score 5.001/10 — DETECTED_BUT_TOO_LATE
- TAI-EUR — BUILDING_ACCELERATION — score 4.887/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- WELL-EUR — MEMORY_24H — score mémoire 10.000/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- UMA-EUR — MEMORY_24H — score mémoire 9.443/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- RENDER-EUR — ACTIVE_NOW — score mémoire 7.897/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- ICP-EUR — MEMORY_24H — score mémoire 7.875/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- ARX-EUR — MEMORY_DECAY_24_72H — score mémoire 7.768/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- WAL-EUR — ACTIVE_NOW — score mémoire 7.552/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- ADA-EUR — ACTIVE_NOW — score mémoire 7.547/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- YGG-EUR — MEMORY_24H — score mémoire 7.528/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- API3-EUR — ACTIVE_NOW — score mémoire 7.428/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- ESP-EUR — ACTIVE_NOW — score mémoire 7.416/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY

## Audit des plus fortes hausses

- NMR-EUR +37.25% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- ZEUS-EUR +33.51% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ORCA-EUR +27.12% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- CAP-EUR +19.44% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- TRB-EUR +13.43% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- U-EUR +13.00% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- NPC-EUR +12.61% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- MET-EUR +10.81% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- VTHO-EUR +9.61% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- API3-EUR +9.18% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE

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
