# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-11-21T12:37:38.821230+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : aucun candidat matériel
- **MEILLEUR_LATENT_ACCELERATOR** : aucun candidat matériel
- **MEILLEUR_PULLBACK_REENTRY** : CROSS-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 6.638 | entrée 5.900 | trend 7.800 | rang 6.475
  - Trend remains strong; candidate retained for re-entry instead of discarded.

## Tous les achats immédiats

Aucun ACHETE_MAINTENANT dans le classement complet.

## Top cross-sectionnel — aperçu non exhaustif

Ce top est une vue courte multi-buckets. Il ne doit jamais être utilisé comme liste exhaustive des achats immédiats.
1. CROSS-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 6.475

## Accélération indépendante

- PROMPT-EUR — CONFIRMED_ACCELERATION — score 9.490/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- ELSA-EUR — CONFIRMED_ACCELERATION — score 7.143/10 — DETECTED_BUT_TOO_LATE
- HOT-EUR — CONFIRMED_ACCELERATION — score 7.098/10 — DETECTED_BUT_TOO_LATE
- ZEUS-EUR — CONFIRMED_ACCELERATION — score 7.029/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- PEAQ-EUR — BUILDING_ACCELERATION — score 5.794/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- BOB-EUR — BUILDING_ACCELERATION — score 5.500/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- AGLD-EUR — BUILDING_ACCELERATION — score 5.391/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- STO-EUR — BUILDING_ACCELERATION — score 5.291/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- AI-EUR — BUILDING_ACCELERATION — score 5.255/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- DOS-EUR — BUILDING_ACCELERATION — score 4.957/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- PROMPT-EUR — ACTIVE_NOW — score mémoire 9.490/10 — sources ACCELERATION — WATCH_ONLY
- ELSA-EUR — ACTIVE_NOW — score mémoire 7.143/10 — sources ACCELERATION — DETECTED_BUT_TOO_LATE
- O-EUR — ACTIVE_NOW — score mémoire 7.124/10 — sources V4 — WATCH_ONLY
- HOT-EUR — ACTIVE_NOW — score mémoire 7.098/10 — sources ACCELERATION — DETECTED_BUT_TOO_LATE
- ZEUS-EUR — ACTIVE_NOW — score mémoire 7.029/10 — sources ACCELERATION — WATCH_ONLY
- DODO-EUR — MEMORY_24H — score mémoire 6.638/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- IKA-EUR — MEMORY_DECAY_24_72H — score mémoire 6.525/10 — sources ACCELERATION — MEMORY_ONLY
- CROSS-EUR — ACTIVE_NOW — score mémoire 6.475/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- CTR-EUR — MEMORY_24H — score mémoire 6.371/10 — sources DECISION_LAYER — MEMORY_ONLY
- DYDX-EUR — MEMORY_DECAY_24_72H — score mémoire 6.238/10 — sources ACCELERATION — MEMORY_ONLY

## Audit des plus fortes hausses

- DODO-EUR +37.47% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- DRV-EUR +28.64% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- RARE-EUR +24.70% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- PARTI-EUR +14.08% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- ENSO-EUR +12.47% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- ELSA-EUR +12.27% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- HOT-EUR +11.74% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- VVV-EUR +10.52% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- SAPIEN-EUR +10.33% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- MLN-EUR +9.31% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE

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
