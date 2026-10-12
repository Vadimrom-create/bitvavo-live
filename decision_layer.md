# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-10-12T17:33:32.495541+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : aucun candidat matériel
- **MEILLEUR_LATENT_ACCELERATOR** : CYBER-EUR | action LATENT_ACCELERATOR | opportunité 7.470 | entrée 4.800 | trend 8.950 | rang 7.170
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : TIA-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 7.330 | entrée 5.750 | trend 8.500 | rang 7.182
  - Trend remains strong; candidate retained for re-entry instead of discarded.

## Tous les achats immédiats

Aucun ACHETE_MAINTENANT dans le classement complet.

## Top cross-sectionnel — aperçu non exhaustif

Ce top est une vue courte multi-buckets. Il ne doit jamais être utilisé comme liste exhaustive des achats immédiats.
1. TIA-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.182
2. CYBER-EUR — MEILLEUR_LATENT_ACCELERATOR — LATENT_ACCELERATOR — rank 7.170
3. ZK-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 6.989

## Accélération indépendante

- STRK-EUR — CONFIRMED_ACCELERATION — score 8.881/10 — DETECTED_BUT_TOO_LATE
- CT-EUR — BUILDING_ACCELERATION — score 6.450/10 — DETECTED_BUT_TOO_LATE
- OGN-EUR — BUILDING_ACCELERATION — score 6.286/10 — DETECTED_BUT_TOO_LATE
- LINEA-EUR — BUILDING_ACCELERATION — score 5.397/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- ZRC-EUR — BUILDING_ACCELERATION — score 5.058/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- CTR-EUR — BUILDING_ACCELERATION — score 4.875/10 — DETECTED_BUT_TOO_LATE
- CHIP-EUR — BUILDING_ACCELERATION — score 4.786/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- RAD-EUR — MEMORY_24H — score mémoire 9.000/10 — sources ACCELERATION, DECISION_LAYER — MEMORY_ONLY
- STRK-EUR — ACTIVE_NOW — score mémoire 8.881/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- DBR-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION — MEMORY_ONLY
- SXT-EUR — MEMORY_24H — score mémoire 8.267/10 — sources ACCELERATION — MEMORY_ONLY
- OSMO-EUR — MEMORY_DECAY_24_72H — score mémoire 7.808/10 — sources ACCELERATION — MEMORY_ONLY
- RAY-EUR — MEMORY_24H — score mémoire 7.600/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- BEL-EUR — MEMORY_DECAY_24_72H — score mémoire 7.528/10 — sources ACCELERATION — MEMORY_ONLY
- AVNT-EUR — MEMORY_24H — score mémoire 7.410/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- EDU-EUR — MEMORY_24H — score mémoire 7.267/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- RON-EUR — MEMORY_DECAY_24_72H — score mémoire 7.243/10 — sources ACCELERATION — MEMORY_ONLY

## Audit des plus fortes hausses

- GTC-EUR +67.86% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- RSR-EUR +38.54% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- OSMO-EUR +36.61% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- CTK-EUR +30.34% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- W-EUR +12.79% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- SAFE-EUR +11.87% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- PYTH-EUR +10.88% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- CT-EUR +10.05% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- OGN-EUR +9.92% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- CYBER-EUR +9.53% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE

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
