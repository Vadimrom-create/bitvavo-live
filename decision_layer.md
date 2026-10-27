# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-10-27T14:22:53.804575+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : aucun candidat matériel
- **MEILLEUR_LATENT_ACCELERATOR** : aucun candidat matériel
- **MEILLEUR_PULLBACK_REENTRY** : DOS-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 6.245 | entrée 5.800 | trend 7.600 | rang 6.299
  - Trend remains strong; candidate retained for re-entry instead of discarded.

## Tous les achats immédiats

Aucun ACHETE_MAINTENANT dans le classement complet.

## Top cross-sectionnel — aperçu non exhaustif

Ce top est une vue courte multi-buckets. Il ne doit jamais être utilisé comme liste exhaustive des achats immédiats.
1. DOS-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 6.299

## Accélération indépendante

- HAEDAL-EUR — CONFIRMED_ACCELERATION — score 7.999/10 — DETECTED_BUT_TOO_LATE
- GROVE-EUR — CONFIRMED_ACCELERATION — score 7.991/10 — DETECTED_BUT_TOO_LATE
- AZTEC-EUR — CONFIRMED_ACCELERATION — score 6.763/10 — DETECTED_BUT_TOO_LATE
- MAVIA-EUR — BUILDING_ACCELERATION — score 6.483/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- FLUX-EUR — BUILDING_ACCELERATION — score 6.476/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- FTT-EUR — BUILDING_ACCELERATION — score 6.404/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- GWEI-EUR — BUILDING_ACCELERATION — score 5.957/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- PONKE-EUR — BUILDING_ACCELERATION — score 5.484/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- MEGA-EUR — BUILDING_ACCELERATION — score 5.183/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- CHILLGUY-EUR — BUILDING_ACCELERATION — score 5.157/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- CAP-EUR — MEMORY_24H — score mémoire 9.112/10 — sources ACCELERATION — MEMORY_ONLY
- U-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION — MEMORY_ONLY
- HAEDAL-EUR — ACTIVE_NOW — score mémoire 7.999/10 — sources ACCELERATION, DECISION_LAYER — DETECTED_BUT_TOO_LATE
- GROVE-EUR — ACTIVE_NOW — score mémoire 7.991/10 — sources ACCELERATION — DETECTED_BUT_TOO_LATE
- IMU-EUR — MEMORY_24H — score mémoire 7.235/10 — sources ACCELERATION — MEMORY_ONLY
- DODO-EUR — MEMORY_24H — score mémoire 7.130/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- WIN-EUR — MEMORY_24H — score mémoire 7.011/10 — sources DECISION_LAYER, V4 — MEMORY_ONLY
- ELSA-EUR — MEMORY_24H — score mémoire 6.990/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- KAT-EUR — MEMORY_DECAY_24_72H — score mémoire 6.964/10 — sources ACCELERATION — MEMORY_ONLY
- PTB-EUR — MEMORY_24H — score mémoire 6.908/10 — sources ACCELERATION — MEMORY_ONLY

## Audit des plus fortes hausses

- HAEDAL-EUR +31.04% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- OSMO-EUR +19.86% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ZRC-EUR +19.45% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- REZ-EUR +18.32% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- ARX-EUR +18.31% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- ELSA-EUR +17.05% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE
- HUMA-EUR +14.63% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- GROVE-EUR +14.53% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- ACU-EUR +13.94% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE
- BREV-EUR +13.05% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE

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
