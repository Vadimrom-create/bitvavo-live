# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-10-06T20:38:13.185261+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : RAY-EUR | action PLACE_LIMITE_PASSIVE | opportunité 7.664 | entrée 6.200 | trend 8.650 | rang 7.562
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : ARPA-EUR | action LATENT_ACCELERATOR | opportunité 7.828 | entrée 5.200 | trend 9.000 | rang 7.645
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : RENDER-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.087 | entrée 7.150 | trend 9.200 | rang 8.064
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Tous les achats immédiats

Aucun ACHETE_MAINTENANT dans le classement complet.

## Top cross-sectionnel — aperçu non exhaustif

Ce top est une vue courte multi-buckets. Il ne doit jamais être utilisé comme liste exhaustive des achats immédiats.
1. RENDER-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.064
2. ADA-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.861
3. WAL-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.751

## Accélération indépendante

- SWEAT-EUR — CONFIRMED_ACCELERATION — score 6.951/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- SAGA-EUR — BUILDING_ACCELERATION — score 5.230/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- BTT-EUR — BUILDING_ACCELERATION — score 5.025/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- WELL-EUR — MEMORY_24H — score mémoire 10.000/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- UMA-EUR — MEMORY_24H — score mémoire 9.443/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- POND-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- RENDER-EUR — ACTIVE_NOW — score mémoire 8.064/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- RLC-EUR — MEMORY_24H — score mémoire 7.931/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- ICP-EUR — MEMORY_24H — score mémoire 7.875/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- ADA-EUR — ACTIVE_NOW — score mémoire 7.861/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- WAL-EUR — ACTIVE_NOW — score mémoire 7.751/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- ARX-EUR — MEMORY_DECAY_24_72H — score mémoire 7.664/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- ARPA-EUR — ACTIVE_NOW — score mémoire 7.645/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY

## Audit des plus fortes hausses

- ZEUS-EUR +53.29% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ORCA-EUR +32.25% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- NMR-EUR +31.71% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- CAP-EUR +18.96% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- RLC-EUR +14.23% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- MET-EUR +12.44% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- TRB-EUR +12.26% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- NPC-EUR +11.91% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- EDU-EUR +10.19% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- PARTI-EUR +8.88% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION

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
