# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-10-11T23:59:10.189524+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : AERO-EUR | action PLACE_LIMITE_PASSIVE | opportunité 7.710 | entrée 6.550 | trend 8.850 | rang 7.579
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : aucun candidat matériel
- **MEILLEUR_PULLBACK_REENTRY** : ZK-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 7.965 | entrée 6.350 | trend 8.950 | rang 7.630
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Tous les achats immédiats

Aucun ACHETE_MAINTENANT dans le classement complet.

## Top cross-sectionnel — aperçu non exhaustif

Ce top est une vue courte multi-buckets. Il ne doit jamais être utilisé comme liste exhaustive des achats immédiats.
1. ZK-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.630
2. FIL-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.602
3. AERO-EUR — MEILLEURE_LIMITE_PASSIVE — PLACE_LIMITE_PASSIVE — rank 7.579

## Accélération indépendante

- STRK-EUR — CONFIRMED_ACCELERATION — score 8.918/10 — DETECTED_BUT_TOO_LATE
- ZEUS-EUR — CONFIRMED_ACCELERATION — score 8.500/10 — DETECTED_BUT_TOO_LATE
- PHA-EUR — BUILDING_ACCELERATION — score 5.160/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- STRK-EUR — ACTIVE_NOW — score mémoire 8.918/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- TREAD-EUR — MEMORY_DECAY_24_72H — score mémoire 8.907/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- IO-EUR — MEMORY_24H — score mémoire 8.545/10 — sources ACCELERATION — MEMORY_ONLY
- OSMO-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION — MEMORY_ONLY
- ZEUS-EUR — ACTIVE_NOW — score mémoire 8.500/10 — sources ACCELERATION, V4 — DETECTED_BUT_TOO_LATE
- BEL-EUR — MEMORY_24H — score mémoire 8.196/10 — sources ACCELERATION — MEMORY_ONLY
- RON-EUR — MEMORY_24H — score mémoire 8.054/10 — sources ACCELERATION — MEMORY_ONLY
- MANTA-EUR — MEMORY_24H — score mémoire 7.990/10 — sources ACCELERATION — MEMORY_ONLY
- LRC-EUR — MEMORY_24H — score mémoire 7.831/10 — sources ACCELERATION — MEMORY_ONLY
- ZK-EUR — ACTIVE_NOW — score mémoire 7.630/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY

## Audit des plus fortes hausses

- ZEUS-EUR +57.67% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ZRC-EUR +55.63% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- MAGIC-EUR +42.93% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- S-EUR +28.95% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- GRASS-EUR +24.85% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- W-EUR +24.08% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- LUMIA-EUR +23.79% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- PLUME-EUR +20.63% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- STRK-EUR +19.45% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- DYM-EUR +15.52% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE

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
