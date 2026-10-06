# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-10-06T20:05:51.999064+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : STX-EUR | action PLACE_LIMITE_PASSIVE | opportunité 7.451 | entrée 6.700 | trend 8.150 | rang 7.138
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : ESP-EUR | action LATENT_ACCELERATOR | opportunité 7.565 | entrée 5.300 | trend 9.000 | rang 7.416
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : RENDER-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.123 | entrée 7.200 | trend 9.200 | rang 7.925
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Tous les achats immédiats

Aucun ACHETE_MAINTENANT dans le classement complet.

## Top cross-sectionnel — aperçu non exhaustif

Ce top est une vue courte multi-buckets. Il ne doit jamais être utilisé comme liste exhaustive des achats immédiats.
1. RENDER-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.925
2. ADA-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.529
3. ESP-EUR — MEILLEUR_LATENT_ACCELERATOR — LATENT_ACCELERATOR — rank 7.416

## Accélération indépendante

- TAI-EUR — CONFIRMED_ACCELERATION — score 6.926/10 — DETECTED_BUT_TOO_LATE
- POND-EUR — CONFIRMED_ACCELERATION — score 6.588/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- LIGHTER-EUR — BUILDING_ACCELERATION — score 6.426/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- INJ-EUR — BUILDING_ACCELERATION — score 5.534/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- PUMP-EUR — BUILDING_ACCELERATION — score 5.449/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- IMX-EUR — BUILDING_ACCELERATION — score 5.382/10 — DETECTED_BUT_TOO_LATE
- AI-EUR — BUILDING_ACCELERATION — score 4.949/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- FLUX-EUR — BUILDING_ACCELERATION — score 4.760/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- WELL-EUR — MEMORY_24H — score mémoire 10.000/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- UMA-EUR — MEMORY_24H — score mémoire 9.443/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- RENDER-EUR — ACTIVE_NOW — score mémoire 7.925/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- ICP-EUR — MEMORY_24H — score mémoire 7.875/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- ARX-EUR — MEMORY_DECAY_24_72H — score mémoire 7.755/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- WAL-EUR — ACTIVE_NOW — score mémoire 7.567/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- ADA-EUR — ACTIVE_NOW — score mémoire 7.529/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- YGG-EUR — MEMORY_24H — score mémoire 7.528/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- API3-EUR — MEMORY_24H — score mémoire 7.428/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- ESP-EUR — ACTIVE_NOW — score mémoire 7.416/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY

## Audit des plus fortes hausses

- ZEUS-EUR +47.95% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- NMR-EUR +37.02% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- ORCA-EUR +23.71% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- CAP-EUR +18.96% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- U-EUR +14.29% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- TRB-EUR +14.04% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- NPC-EUR +13.02% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- MET-EUR +10.30% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- ZRO-EUR +9.89% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE
- PARTI-EUR +9.82% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION

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
