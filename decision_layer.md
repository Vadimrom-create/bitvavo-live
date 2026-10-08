# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-10-08T21:59:37.202109+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : PARTI-EUR | action PLACE_LIMITE_PASSIVE | opportunité 7.437 | entrée 6.550 | trend 8.300 | rang 7.271
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : MAGIC-EUR | action LATENT_ACCELERATOR | opportunité 8.376 | entrée 5.300 | trend 8.650 | rang 7.173
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : NMR-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.104 | entrée 7.400 | trend 8.650 | rang 7.779
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Tous les achats immédiats

Aucun ACHETE_MAINTENANT dans le classement complet.

## Top cross-sectionnel — aperçu non exhaustif

Ce top est une vue courte multi-buckets. Il ne doit jamais être utilisé comme liste exhaustive des achats immédiats.
1. NMR-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.779
2. RAY-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.411
3. PARTI-EUR — MEILLEURE_LIMITE_PASSIVE — PLACE_LIMITE_PASSIVE — rank 7.271

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
- W-EUR — MEMORY_24H — score mémoire 7.848/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- QUID-EUR — MEMORY_24H — score mémoire 7.798/10 — sources ACCELERATION — MEMORY_ONLY
- NMR-EUR — ACTIVE_NOW — score mémoire 7.779/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- SWELL-EUR — MEMORY_DECAY_24_72H — score mémoire 7.670/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- VELO-EUR — MEMORY_DECAY_24_72H — score mémoire 7.484/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- RAY-EUR — ACTIVE_NOW — score mémoire 7.411/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY

## Audit des plus fortes hausses

- OGN-EUR +106.11% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- ZRC-EUR +68.10% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- RLC-EUR +28.31% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- AMP-EUR +24.15% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- DRV-EUR +19.19% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- PYTH-EUR +15.05% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- TIA-EUR +13.81% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- SKL-EUR +13.76% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- STRK-EUR +13.73% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- GTC-EUR +13.65% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE

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
