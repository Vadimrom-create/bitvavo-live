# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-11-16T00:08:23.947676+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : aucun candidat matériel
- **MEILLEUR_LATENT_ACCELERATOR** : aucun candidat matériel
- **MEILLEUR_PULLBACK_REENTRY** : DODO-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 7.100 | entrée 5.550 | trend 8.300 | rang 6.888
  - Trend remains strong; candidate retained for re-entry instead of discarded.

## Tous les achats immédiats

Aucun ACHETE_MAINTENANT dans le classement complet.

## Top cross-sectionnel — aperçu non exhaustif

Ce top est une vue courte multi-buckets. Il ne doit jamais être utilisé comme liste exhaustive des achats immédiats.
1. DODO-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 6.888
2. CAP-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 6.340

## Accélération indépendante

- AMP-EUR — BUILDING_ACCELERATION — score 5.717/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- RARE-EUR — BUILDING_ACCELERATION — score 5.583/10 — DETECTED_BUT_TOO_LATE
- CVC-EUR — BUILDING_ACCELERATION — score 5.389/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- BIGTIME-EUR — BUILDING_ACCELERATION — score 5.254/10 — DETECTED_BUT_TOO_LATE
- AGLD-EUR — BUILDING_ACCELERATION — score 4.980/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- NES-EUR — MEMORY_24H — score mémoire 8.757/10 — sources ACCELERATION — MEMORY_ONLY
- HNT-EUR — MEMORY_24H — score mémoire 8.218/10 — sources ACCELERATION — MEMORY_ONLY
- ASTER-EUR — MEMORY_24H — score mémoire 7.937/10 — sources ACCELERATION — MEMORY_ONLY
- IMU-EUR — MEMORY_DECAY_24_72H — score mémoire 7.680/10 — sources ACCELERATION — MEMORY_ONLY
- GLMR-EUR — MEMORY_24H — score mémoire 7.500/10 — sources ACCELERATION — MEMORY_ONLY
- GNS-EUR — MEMORY_24H — score mémoire 7.099/10 — sources ACCELERATION — MEMORY_ONLY
- CROSS-EUR — ACTIVE_NOW — score mémoire 6.926/10 — sources V4 — WATCH_ONLY
- DODO-EUR — ACTIVE_NOW — score mémoire 6.888/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- KITE-EUR — MEMORY_24H — score mémoire 6.468/10 — sources DECISION_LAYER — MEMORY_ONLY
- SHELL-EUR — MEMORY_24H — score mémoire 6.367/10 — sources DECISION_LAYER — MEMORY_ONLY

## Audit des plus fortes hausses

- RARE-EUR +53.57% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- NES-EUR +37.82% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- DRV-EUR +25.40% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- TREAD-EUR +23.20% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- VVV-EUR +18.36% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- CSPR-EUR +14.92% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- GLMR-EUR +13.99% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- CC-EUR +11.07% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- QNT-EUR +10.59% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- MEGA-EUR +10.49% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE

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
