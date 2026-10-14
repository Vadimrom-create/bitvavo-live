# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-10-14T05:31:53.409406+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : aucun candidat matériel
- **MEILLEUR_LATENT_ACCELERATOR** : CTR-EUR | action LATENT_ACCELERATOR | opportunité 7.723 | entrée 5.450 | trend 9.200 | rang 7.568
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : STX-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 7.816 | entrée 7.050 | trend 8.900 | rang 7.674
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Tous les achats immédiats

Aucun ACHETE_MAINTENANT dans le classement complet.

## Top cross-sectionnel — aperçu non exhaustif

Ce top est une vue courte multi-buckets. Il ne doit jamais être utilisé comme liste exhaustive des achats immédiats.
1. STX-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.674
2. CTR-EUR — MEILLEUR_LATENT_ACCELERATOR — LATENT_ACCELERATOR — rank 7.568
3. FLUID-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.182

## Accélération indépendante

- AVA-EUR — CONFIRMED_ACCELERATION — score 7.431/10 — DETECTED_BUT_TOO_LATE
- WAL-EUR — CONFIRMED_ACCELERATION — score 7.023/10 — DETECTED_BUT_TOO_LATE
- CELR-EUR — CONFIRMED_ACCELERATION — score 6.904/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- TRAC-EUR — CONFIRMED_ACCELERATION — score 6.847/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- AMP-EUR — CONFIRMED_ACCELERATION — score 6.546/10 — DETECTED_BUT_TOO_LATE
- DODO-EUR — BUILDING_ACCELERATION — score 5.184/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- BAT-EUR — BUILDING_ACCELERATION — score 5.034/10 — DETECTED_BUT_TOO_LATE
- LSK-EUR — BUILDING_ACCELERATION — score 5.018/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- ZRC-EUR — MEMORY_24H — score mémoire 7.892/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- STX-EUR — ACTIVE_NOW — score mémoire 7.674/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- CTR-EUR — ACTIVE_NOW — score mémoire 7.568/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- AVA-EUR — ACTIVE_NOW — score mémoire 7.431/10 — sources ACCELERATION — DETECTED_BUT_TOO_LATE
- GNS-EUR — MEMORY_24H — score mémoire 7.386/10 — sources ACCELERATION — MEMORY_ONLY
- FIL-EUR — ACTIVE_NOW — score mémoire 7.293/10 — sources DECISION_LAYER, V4 — WATCH_ONLY
- DUSK-EUR — ACTIVE_NOW — score mémoire 7.240/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- FARTCOIN-EUR — MEMORY_24H — score mémoire 7.230/10 — sources ACCELERATION — MEMORY_ONLY
- FLUID-EUR — ACTIVE_NOW — score mémoire 7.182/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- AZTEC-EUR — ACTIVE_NOW — score mémoire 7.167/10 — sources DECISION_LAYER, V4 — WATCH_ONLY

## Audit des plus fortes hausses

- GNS-EUR +105.78% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- AMP-EUR +24.31% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- AVA-EUR +20.80% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- CNPY-EUR +16.48% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- BAT-EUR +16.48% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- ZRC-EUR +16.12% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- PUFFER-EUR +14.73% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- WAL-EUR +12.52% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- CT-EUR +10.86% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- OP-EUR +10.36% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE

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
