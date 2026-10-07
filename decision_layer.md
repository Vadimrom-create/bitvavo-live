# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-10-07T00:33:47.307128+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : ESP-EUR | action PLACE_LIMITE_PASSIVE | opportunité 7.627 | entrée 5.950 | trend 8.650 | rang 7.341
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : PARTI-EUR | action LATENT_ACCELERATOR | opportunité 7.695 | entrée 5.400 | trend 8.900 | rang 7.418
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : RENDER-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 7.657 | entrée 7.600 | trend 8.700 | rang 7.545
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Tous les achats immédiats

Aucun ACHETE_MAINTENANT dans le classement complet.

## Top cross-sectionnel — aperçu non exhaustif

Ce top est une vue courte multi-buckets. Il ne doit jamais être utilisé comme liste exhaustive des achats immédiats.
1. RENDER-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.545
2. WAL-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.488
3. PARTI-EUR — MEILLEUR_LATENT_ACCELERATOR — LATENT_ACCELERATOR — rank 7.418

## Accélération indépendante

- POND-EUR — CONFIRMED_ACCELERATION — score 10.000/10 — DETECTED_BUT_TOO_LATE
- LUMIA-EUR — CONFIRMED_ACCELERATION — score 7.176/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- EDGE-EUR — CONFIRMED_ACCELERATION — score 6.786/10 — DETECTED_BUT_TOO_LATE
- ZEUS-EUR — BUILDING_ACCELERATION — score 6.033/10 — DETECTED_BUT_TOO_LATE
- GTC-EUR — BUILDING_ACCELERATION — score 5.839/10 — DETECTED_BUT_TOO_LATE
- UP-EUR — BUILDING_ACCELERATION — score 5.765/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- SWELL-EUR — BUILDING_ACCELERATION — score 5.595/10 — DETECTED_BUT_TOO_LATE
- DATAIP-EUR — BUILDING_ACCELERATION — score 5.410/10 — DETECTED_BUT_TOO_LATE
- METIS-EUR — BUILDING_ACCELERATION — score 4.788/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- POND-EUR — ACTIVE_NOW — score mémoire 10.000/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- UMA-EUR — MEMORY_24H — score mémoire 9.443/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- CHIP-EUR — MEMORY_24H — score mémoire 8.278/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- SOSO-EUR — MEMORY_24H — score mémoire 7.615/10 — sources ACCELERATION — MEMORY_ONLY
- ICP-EUR — MEMORY_DECAY_24_72H — score mémoire 7.546/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- RENDER-EUR — ACTIVE_NOW — score mémoire 7.545/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- WAL-EUR — ACTIVE_NOW — score mémoire 7.488/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- PARTI-EUR — ACTIVE_NOW — score mémoire 7.418/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- STX-EUR — MEMORY_24H — score mémoire 7.361/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- ESP-EUR — ACTIVE_NOW — score mémoire 7.341/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY

## Audit des plus fortes hausses

- ZEUS-EUR +92.94% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ORCA-EUR +38.79% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- NMR-EUR +34.05% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- CAP-EUR +21.37% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- POND-EUR +19.58% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- MAGIC-EUR +15.35% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- MET-EUR +12.73% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- TRB-EUR +12.08% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- WELL-EUR +11.73% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- NPC-EUR +11.68% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE

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
