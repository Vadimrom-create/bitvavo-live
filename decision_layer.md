# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-10-11T13:34:36.839972+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : AERO-EUR | action PLACE_LIMITE_PASSIVE | opportunité 7.928 | entrée 6.000 | trend 8.850 | rang 7.567
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : BAND-EUR | action LATENT_ACCELERATOR | opportunité 7.605 | entrée 5.450 | trend 8.700 | rang 7.500
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : AVNT-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.105 | entrée 6.450 | trend 8.750 | rang 7.814
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Tous les achats immédiats

Aucun ACHETE_MAINTENANT dans le classement complet.

## Top cross-sectionnel — aperçu non exhaustif

Ce top est une vue courte multi-buckets. Il ne doit jamais être utilisé comme liste exhaustive des achats immédiats.
1. AVNT-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.814
2. AERO-EUR — MEILLEURE_LIMITE_PASSIVE — PLACE_LIMITE_PASSIVE — rank 7.567
3. W-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.559

## Accélération indépendante

- OSMO-EUR — CONFIRMED_ACCELERATION — score 9.247/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- NIL-EUR — CONFIRMED_ACCELERATION — score 7.994/10 — DETECTED_BUT_TOO_LATE
- NEO-EUR — BUILDING_ACCELERATION — score 6.073/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- LRC-EUR — BUILDING_ACCELERATION — score 6.042/10 — DETECTED_BUT_TOO_LATE
- BEL-EUR — BUILDING_ACCELERATION — score 6.030/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- ZRC-EUR — BUILDING_ACCELERATION — score 6.015/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- TAI-EUR — BUILDING_ACCELERATION — score 5.760/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- VET-EUR — BUILDING_ACCELERATION — score 5.577/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- VELO-EUR — BUILDING_ACCELERATION — score 5.454/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- ZRX-EUR — BUILDING_ACCELERATION — score 5.287/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- GTC-EUR — MEMORY_DECAY_24_72H — score mémoire 9.465/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- OSMO-EUR — ACTIVE_NOW — score mémoire 9.247/10 — sources ACCELERATION — WATCH_ONLY
- TREAD-EUR — MEMORY_24H — score mémoire 8.918/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- IO-EUR — MEMORY_24H — score mémoire 8.545/10 — sources ACCELERATION — MEMORY_ONLY
- RON-EUR — MEMORY_24H — score mémoire 8.054/10 — sources ACCELERATION — MEMORY_ONLY
- NIL-EUR — ACTIVE_NOW — score mémoire 7.994/10 — sources ACCELERATION — DETECTED_BUT_TOO_LATE
- AVNT-EUR — ACTIVE_NOW — score mémoire 7.814/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- AERO-EUR — ACTIVE_NOW — score mémoire 7.567/10 — sources DECISION_LAYER, V4 — WATCH_ONLY
- W-EUR — ACTIVE_NOW — score mémoire 7.559/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- BAND-EUR — ACTIVE_NOW — score mémoire 7.500/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY

## Audit des plus fortes hausses

- ZEUS-EUR +54.28% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- STRK-EUR +50.67% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- CHIP-EUR +28.53% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- LUMIA-EUR +24.75% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- TIA-EUR +18.68% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- MAGIC-EUR +16.85% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- GRASS-EUR +15.49% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- S-EUR +15.14% — DETECTED_TOO_LATE — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- SENT-EUR +13.82% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- ZK-EUR +12.58% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION

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
