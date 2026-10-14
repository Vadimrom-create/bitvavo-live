# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-10-14T00:42:29.038454+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : TIA-EUR | action PLACE_LIMITE_PASSIVE | opportunité 7.528 | entrée 6.650 | trend 8.150 | rang 7.057
  - Strong structure but imperfect current entry; prefer passive execution. High extension/chase reduces rank but does not erase the setup.
- **MEILLEUR_LATENT_ACCELERATOR** : CTR-EUR | action LATENT_ACCELERATOR | opportunité 8.065 | entrée 5.700 | trend 9.200 | rang 7.678
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : STX-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.188 | entrée 7.450 | trend 8.900 | rang 7.736
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Tous les achats immédiats

Aucun ACHETE_MAINTENANT dans le classement complet.

## Top cross-sectionnel — aperçu non exhaustif

Ce top est une vue courte multi-buckets. Il ne doit jamais être utilisé comme liste exhaustive des achats immédiats.
1. STX-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.736
2. CTR-EUR — MEILLEUR_LATENT_ACCELERATOR — LATENT_ACCELERATOR — rank 7.678
3. SKL-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.220

## Accélération indépendante

- GNS-EUR — CONFIRMED_ACCELERATION — score 7.386/10 — DETECTED_BUT_TOO_LATE
- FARTCOIN-EUR — CONFIRMED_ACCELERATION — score 7.230/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- CTC-EUR — CONFIRMED_ACCELERATION — score 7.143/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- NES-EUR — CONFIRMED_ACCELERATION — score 6.894/10 — DETECTED_BUT_TOO_LATE
- WAL-EUR — BUILDING_ACCELERATION — score 5.714/10 — DETECTED_BUT_TOO_LATE
- REZ-EUR — BUILDING_ACCELERATION — score 5.485/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- PYTH-EUR — BUILDING_ACCELERATION — score 5.416/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- ZK-EUR — BUILDING_ACCELERATION — score 5.081/10 — DETECTED_BUT_TOO_LATE
- ATH-EUR — BUILDING_ACCELERATION — score 5.054/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- ETHFI-EUR — BUILDING_ACCELERATION — score 5.036/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- AMP-EUR — MEMORY_DECAY_24_72H — score mémoire 7.923/10 — sources ACCELERATION, DECISION_LAYER — MEMORY_ONLY
- ZRC-EUR — MEMORY_24H — score mémoire 7.892/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- STX-EUR — ACTIVE_NOW — score mémoire 7.736/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- CTR-EUR — ACTIVE_NOW — score mémoire 7.678/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- STRK-EUR — MEMORY_DECAY_24_72H — score mémoire 7.558/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- GNS-EUR — ACTIVE_NOW — score mémoire 7.386/10 — sources ACCELERATION — DETECTED_BUT_TOO_LATE
- CT-EUR — MEMORY_24H — score mémoire 7.250/10 — sources ACCELERATION — MEMORY_ONLY
- FARTCOIN-EUR — ACTIVE_NOW — score mémoire 7.230/10 — sources ACCELERATION — WATCH_ONLY
- SKL-EUR — ACTIVE_NOW — score mémoire 7.220/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- HUMA-EUR — ACTIVE_NOW — score mémoire 7.162/10 — sources DECISION_LAYER, V4 — WATCH_ONLY

## Audit des plus fortes hausses

- GNS-EUR +121.92% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- BAT-EUR +29.74% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- ZRC-EUR +26.20% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- OP-EUR +24.05% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- U-EUR +17.83% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- CNPY-EUR +17.40% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- ZK-EUR +16.73% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- AGI-EUR +14.92% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- DUSK-EUR +14.48% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- WAL-EUR +14.28% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE

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
