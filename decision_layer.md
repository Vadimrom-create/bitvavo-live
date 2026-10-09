# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-10-09T16:18:45.504783+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : aucun candidat matériel
- **MEILLEUR_LATENT_ACCELERATOR** : SOSO-EUR | action LATENT_ACCELERATOR | opportunité 7.575 | entrée 5.500 | trend 9.000 | rang 7.438
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : JUP-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.018 | entrée 6.600 | trend 9.200 | rang 7.610
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Tous les achats immédiats

Aucun ACHETE_MAINTENANT dans le classement complet.

## Top cross-sectionnel — aperçu non exhaustif

Ce top est une vue courte multi-buckets. Il ne doit jamais être utilisé comme liste exhaustive des achats immédiats.
1. JUP-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.610
2. SOSO-EUR — MEILLEUR_LATENT_ACCELERATOR — LATENT_ACCELERATOR — rank 7.438
3. PARTI-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.355

## Accélération indépendante

- CELR-EUR — CONFIRMED_ACCELERATION — score 9.531/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- OP-EUR — CONFIRMED_ACCELERATION — score 9.301/10 — DETECTED_BUT_TOO_LATE
- MAGIC-EUR — CONFIRMED_ACCELERATION — score 8.742/10 — DETECTED_BUT_TOO_LATE
- PORTAL-EUR — CONFIRMED_ACCELERATION — score 8.136/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- DYDX-EUR — CONFIRMED_ACCELERATION — score 7.095/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- ICNT-EUR — CONFIRMED_ACCELERATION — score 7.043/10 — DETECTED_BUT_TOO_LATE
- PIXEL-EUR — CONFIRMED_ACCELERATION — score 6.856/10 — DETECTED_BUT_TOO_LATE
- HFT-EUR — CONFIRMED_ACCELERATION — score 6.755/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- RON-EUR — CONFIRMED_ACCELERATION — score 6.689/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- GMT-EUR — BUILDING_ACCELERATION — score 6.398/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- ZEUS-EUR — MEMORY_24H — score mémoire 10.000/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- CELR-EUR — ACTIVE_NOW — score mémoire 9.531/10 — sources ACCELERATION — WATCH_ONLY
- OP-EUR — ACTIVE_NOW — score mémoire 9.301/10 — sources ACCELERATION — DETECTED_BUT_TOO_LATE
- MAGIC-EUR — ACTIVE_NOW — score mémoire 8.742/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- W-EUR — MEMORY_24H — score mémoire 8.700/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- AGI-EUR — MEMORY_24H — score mémoire 8.443/10 — sources ACCELERATION — MEMORY_ONLY
- GLMR-EUR — MEMORY_24H — score mémoire 8.432/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- GNS-EUR — MEMORY_24H — score mémoire 8.425/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- SCR-EUR — MEMORY_24H — score mémoire 8.302/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- GTC-EUR — MEMORY_24H — score mémoire 8.274/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY

## Audit des plus fortes hausses

- MAGIC-EUR +61.63% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- KAIA-EUR +42.49% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- DRV-EUR +37.10% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- BAT-EUR +28.48% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- ZK-EUR +28.37% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- STRK-EUR +27.94% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- XDP-EUR +25.76% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- RAD-EUR +19.02% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- ATOM-EUR +18.18% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- PEAQ-EUR +17.26% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE

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
