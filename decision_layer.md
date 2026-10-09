# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-10-09T18:10:25.239802+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : PARTI-EUR | action PLACE_LIMITE_PASSIVE | opportunité 8.013 | entrée 6.100 | trend 8.900 | rang 7.575
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : aucun candidat matériel
- **MEILLEUR_PULLBACK_REENTRY** : RAY-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 7.457 | entrée 6.550 | trend 8.500 | rang 7.357
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Tous les achats immédiats

Aucun ACHETE_MAINTENANT dans le classement complet.

## Top cross-sectionnel — aperçu non exhaustif

Ce top est une vue courte multi-buckets. Il ne doit jamais être utilisé comme liste exhaustive des achats immédiats.
1. PARTI-EUR — MEILLEURE_LIMITE_PASSIVE — PLACE_LIMITE_PASSIVE — rank 7.575
2. SOSO-EUR — MEILLEURE_LIMITE_PASSIVE — PLACE_LIMITE_PASSIVE — rank 7.541
3. PYTH-EUR — MEILLEURE_LIMITE_PASSIVE — PLACE_LIMITE_PASSIVE — rank 7.421

## Accélération indépendante

- CT-EUR — CONFIRMED_ACCELERATION — score 9.114/10 — DETECTED_BUT_TOO_LATE
- PIXEL-EUR — CONFIRMED_ACCELERATION — score 7.676/10 — DETECTED_BUT_TOO_LATE
- RON-EUR — CONFIRMED_ACCELERATION — score 6.993/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- ANIME-EUR — CONFIRMED_ACCELERATION — score 6.601/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- ACE-EUR — BUILDING_ACCELERATION — score 6.284/10 — DETECTED_BUT_TOO_LATE
- ZKC-EUR — BUILDING_ACCELERATION — score 6.240/10 — DETECTED_BUT_TOO_LATE
- ATOM-EUR — BUILDING_ACCELERATION — score 5.980/10 — DETECTED_BUT_TOO_LATE
- CELO-EUR — BUILDING_ACCELERATION — score 5.739/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- ALIGN-EUR — BUILDING_ACCELERATION — score 5.329/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- CAP-EUR — BUILDING_ACCELERATION — score 5.166/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- ZEUS-EUR — MEMORY_24H — score mémoire 10.000/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- CELR-EUR — MEMORY_24H — score mémoire 9.531/10 — sources ACCELERATION — MEMORY_ONLY
- OP-EUR — MEMORY_24H — score mémoire 9.301/10 — sources ACCELERATION — MEMORY_ONLY
- CT-EUR — ACTIVE_NOW — score mémoire 9.114/10 — sources ACCELERATION — DETECTED_BUT_TOO_LATE
- MAGIC-EUR — MEMORY_24H — score mémoire 8.742/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- W-EUR — MEMORY_24H — score mémoire 8.700/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- AGI-EUR — MEMORY_24H — score mémoire 8.443/10 — sources ACCELERATION — MEMORY_ONLY
- GLMR-EUR — MEMORY_24H — score mémoire 8.432/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- GNS-EUR — MEMORY_24H — score mémoire 8.425/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- SCR-EUR — MEMORY_24H — score mémoire 8.302/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY

## Audit des plus fortes hausses

- MAGIC-EUR +81.94% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- KAIA-EUR +45.03% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- BAT-EUR +37.90% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- DRV-EUR +32.87% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- ZK-EUR +28.90% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- STRK-EUR +28.22% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- XDP-EUR +27.14% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- ATOM-EUR +22.69% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- PIXEL-EUR +20.14% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- DOT-EUR +18.62% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE

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
