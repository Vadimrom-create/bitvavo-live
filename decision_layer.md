# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-10-12T18:07:27.716266+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : aucun candidat matériel
- **MEILLEUR_LATENT_ACCELERATOR** : aucun candidat matériel
- **MEILLEUR_PULLBACK_REENTRY** : ZK-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 7.646 | entrée 5.650 | trend 8.400 | rang 7.330
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Tous les achats immédiats

Aucun ACHETE_MAINTENANT dans le classement complet.

## Top cross-sectionnel — aperçu non exhaustif

Ce top est une vue courte multi-buckets. Il ne doit jamais être utilisé comme liste exhaustive des achats immédiats.
1. ZK-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.330
2. TIA-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.240
3. STX-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.169

## Accélération indépendante

- CTR-EUR — CONFIRMED_ACCELERATION — score 7.878/10 — DETECTED_BUT_TOO_LATE
- GRASS-EUR — CONFIRMED_ACCELERATION — score 7.726/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- OGN-EUR — CONFIRMED_ACCELERATION — score 7.091/10 — DETECTED_BUT_TOO_LATE
- SKL-EUR — BUILDING_ACCELERATION — score 6.235/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- S-EUR — BUILDING_ACCELERATION — score 4.868/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- RAD-EUR — MEMORY_24H — score mémoire 9.000/10 — sources ACCELERATION, DECISION_LAYER — MEMORY_ONLY
- STRK-EUR — MEMORY_24H — score mémoire 8.881/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- DBR-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION — MEMORY_ONLY
- SXT-EUR — MEMORY_24H — score mémoire 8.267/10 — sources ACCELERATION — MEMORY_ONLY
- CTR-EUR — ACTIVE_NOW — score mémoire 7.878/10 — sources ACCELERATION — DETECTED_BUT_TOO_LATE
- GRASS-EUR — ACTIVE_NOW — score mémoire 7.726/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- OSMO-EUR — MEMORY_DECAY_24_72H — score mémoire 7.708/10 — sources ACCELERATION — MEMORY_ONLY
- EDU-EUR — ACTIVE_NOW — score mémoire 7.625/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- RAY-EUR — MEMORY_24H — score mémoire 7.600/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- BEL-EUR — MEMORY_DECAY_24_72H — score mémoire 7.432/10 — sources ACCELERATION — MEMORY_ONLY

## Audit des plus fortes hausses

- GTC-EUR +76.45% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- RSR-EUR +42.28% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- OSMO-EUR +32.41% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- CTK-EUR +17.94% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- OGN-EUR +14.01% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- SAFE-EUR +12.63% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- SKL-EUR +11.04% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- W-EUR +9.63% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- PYTH-EUR +9.14% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- CYBER-EUR +8.63% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE

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
