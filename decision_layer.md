# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-10-11T12:29:30.389034+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : AERO-EUR | action PLACE_LIMITE_PASSIVE | opportunité 7.688 | entrée 6.750 | trend 8.850 | rang 7.393
  - Strong structure but imperfect current entry; prefer passive execution. High extension/chase reduces rank but does not erase the setup.
- **MEILLEUR_LATENT_ACCELERATOR** : BOME-EUR | action LATENT_ACCELERATOR | opportunité 8.026 | entrée 5.550 | trend 8.450 | rang 7.442
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : C98-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 7.598 | entrée 5.400 | trend 8.650 | rang 7.415
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Tous les achats immédiats

Aucun ACHETE_MAINTENANT dans le classement complet.

## Top cross-sectionnel — aperçu non exhaustif

Ce top est une vue courte multi-buckets. Il ne doit jamais être utilisé comme liste exhaustive des achats immédiats.
1. BOME-EUR — MEILLEUR_LATENT_ACCELERATOR — LATENT_ACCELERATOR — rank 7.442
2. C98-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.415
3. AERO-EUR — MEILLEURE_LIMITE_PASSIVE — PLACE_LIMITE_PASSIVE — rank 7.393

## Accélération indépendante

- S-EUR — BUILDING_ACCELERATION — score 6.131/10 — DETECTED_BUT_TOO_LATE
- IO-EUR — BUILDING_ACCELERATION — score 5.013/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- RLC-EUR — BUILDING_ACCELERATION — score 5.008/10 — DETECTED_BUT_TOO_LATE
- BEAM-EUR — BUILDING_ACCELERATION — score 4.793/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- GTC-EUR — MEMORY_24H — score mémoire 9.580/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- TREAD-EUR — MEMORY_24H — score mémoire 8.918/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- BRETT-EUR — MEMORY_24H — score mémoire 8.610/10 — sources ACCELERATION — MEMORY_ONLY
- LRC-EUR — MEMORY_DECAY_24_72H — score mémoire 7.521/10 — sources ACCELERATION — MEMORY_ONLY
- BOME-EUR — ACTIVE_NOW — score mémoire 7.442/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- SENT-EUR — MEMORY_24H — score mémoire 7.432/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- C98-EUR — ACTIVE_NOW — score mémoire 7.415/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- AERO-EUR — ACTIVE_NOW — score mémoire 7.393/10 — sources DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- JUP-EUR — ACTIVE_NOW — score mémoire 7.338/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- AVNT-EUR — ACTIVE_NOW — score mémoire 7.335/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY

## Audit des plus fortes hausses

- ZEUS-EUR +62.40% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- STRK-EUR +58.94% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- LUMIA-EUR +29.54% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- CHIP-EUR +26.97% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- TIA-EUR +18.19% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- SENT-EUR +18.01% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- S-EUR +14.50% — DETECTED_TOO_LATE — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- ZK-EUR +11.60% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- RLC-EUR +11.45% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- PNT-EUR +11.28% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE

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
