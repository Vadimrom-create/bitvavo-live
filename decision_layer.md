# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-10-08T21:55:52.621226+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : PARTI-EUR | action PLACE_LIMITE_PASSIVE | opportunité 7.437 | entrée 6.550 | trend 8.300 | rang 7.271
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : MAGIC-EUR | action LATENT_ACCELERATOR | opportunité 8.376 | entrée 5.300 | trend 8.650 | rang 7.173
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : W-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.392 | entrée 6.550 | trend 8.650 | rang 7.848
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Tous les achats immédiats

Aucun ACHETE_MAINTENANT dans le classement complet.

## Top cross-sectionnel — aperçu non exhaustif

Ce top est une vue courte multi-buckets. Il ne doit jamais être utilisé comme liste exhaustive des achats immédiats.
1. W-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.848
2. NMR-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.581
3. RAY-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.330

## Accélération indépendante

- AMP-EUR — CONFIRMED_ACCELERATION — score 8.113/10 — DETECTED_BUT_TOO_LATE
- AGI-EUR — CONFIRMED_ACCELERATION — score 7.345/10 — DETECTED_BUT_TOO_LATE
- PLUME-EUR — CONFIRMED_ACCELERATION — score 7.079/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- GLMR-EUR — CONFIRMED_ACCELERATION — score 6.770/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- ZRC-EUR — BUILDING_ACCELERATION — score 6.227/10 — DETECTED_BUT_TOO_LATE
- GRASS-EUR — BUILDING_ACCELERATION — score 5.871/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- UP-EUR — BUILDING_ACCELERATION — score 5.375/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- GNS-EUR — MEMORY_24H — score mémoire 10.000/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- RLC-EUR — MEMORY_24H — score mémoire 10.000/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- GTC-EUR — MEMORY_24H — score mémoire 8.274/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- AMP-EUR — ACTIVE_NOW — score mémoire 8.113/10 — sources ACCELERATION — DETECTED_BUT_TOO_LATE
- W-EUR — ACTIVE_NOW — score mémoire 7.848/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- QUID-EUR — MEMORY_24H — score mémoire 7.798/10 — sources ACCELERATION — MEMORY_ONLY
- SWELL-EUR — MEMORY_DECAY_24_72H — score mémoire 7.682/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- NMR-EUR — ACTIVE_NOW — score mémoire 7.581/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- VELO-EUR — MEMORY_DECAY_24_72H — score mémoire 7.494/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- AGI-EUR — ACTIVE_NOW — score mémoire 7.345/10 — sources ACCELERATION — DETECTED_BUT_TOO_LATE

## Audit des plus fortes hausses

- OGN-EUR +107.16% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- ZRC-EUR +70.18% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- RLC-EUR +29.15% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- AMP-EUR +24.38% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- DRV-EUR +19.18% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- PYTH-EUR +15.05% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- CTSI-EUR +14.16% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- TIA-EUR +13.99% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- GTC-EUR +13.90% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- STRK-EUR +13.73% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE

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
