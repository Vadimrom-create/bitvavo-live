# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-10-27T19:33:08.102313+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : aucun candidat matériel
- **MEILLEUR_LATENT_ACCELERATOR** : aucun candidat matériel
- **MEILLEUR_PULLBACK_REENTRY** : CAP-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 6.808 | entrée 7.350 | trend 7.900 | rang 6.806
  - Trend remains strong; candidate retained for re-entry instead of discarded.

## Tous les achats immédiats

Aucun ACHETE_MAINTENANT dans le classement complet.

## Top cross-sectionnel — aperçu non exhaustif

Ce top est une vue courte multi-buckets. Il ne doit jamais être utilisé comme liste exhaustive des achats immédiats.
1. CAP-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 6.806
2. BABY-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 6.780
3. CHIP-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 6.726

## Accélération indépendante

- MAGIC-EUR — BUILDING_ACCELERATION — score 5.796/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- NOM-EUR — BUILDING_ACCELERATION — score 5.071/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- PROMPT-EUR — BUILDING_ACCELERATION — score 5.027/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- POND-EUR — BUILDING_ACCELERATION — score 4.802/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- U-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION — MEMORY_ONLY
- HAEDAL-EUR — MEMORY_24H — score mémoire 7.999/10 — sources ACCELERATION, DECISION_LAYER — MEMORY_ONLY
- GROVE-EUR — MEMORY_24H — score mémoire 7.991/10 — sources ACCELERATION — MEMORY_ONLY
- IMU-EUR — MEMORY_24H — score mémoire 7.235/10 — sources ACCELERATION — MEMORY_ONLY
- ELSA-EUR — ACTIVE_NOW — score mémoire 7.047/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- WIN-EUR — MEMORY_24H — score mémoire 7.011/10 — sources DECISION_LAYER, V4 — MEMORY_ONLY
- PTB-EUR — MEMORY_24H — score mémoire 6.908/10 — sources ACCELERATION — MEMORY_ONLY
- CAP-EUR — ACTIVE_NOW — score mémoire 6.806/10 — sources ACCELERATION, DECISION_LAYER — WATCH_ONLY
- BABY-EUR — ACTIVE_NOW — score mémoire 6.780/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- AZTEC-EUR — MEMORY_24H — score mémoire 6.763/10 — sources ACCELERATION — MEMORY_ONLY

## Audit des plus fortes hausses

- GROVE-EUR +106.97% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- HAEDAL-EUR +30.77% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- INIT-EUR +24.80% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- ACU-EUR +23.93% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- SOLV-EUR +16.04% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- REZ-EUR +14.59% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- XAN-EUR +14.06% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- TREAD-EUR +13.92% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- OSMO-EUR +12.07% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- DOS-EUR +11.35% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE

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
