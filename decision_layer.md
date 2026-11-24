# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-11-24T05:44:40.389436+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : aucun candidat matériel
- **MEILLEUR_LATENT_ACCELERATOR** : aucun candidat matériel
- **MEILLEUR_PULLBACK_REENTRY** : KITE-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 7.022 | entrée 6.050 | trend 8.300 | rang 6.944
  - Trend remains strong; candidate retained for re-entry instead of discarded.

## Tous les achats immédiats

Aucun ACHETE_MAINTENANT dans le classement complet.

## Top cross-sectionnel — aperçu non exhaustif

Ce top est une vue courte multi-buckets. Il ne doit jamais être utilisé comme liste exhaustive des achats immédiats.
1. KITE-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 6.944

## Accélération indépendante

- MMT-EUR — CONFIRMED_ACCELERATION — score 9.836/10 — DETECTED_BUT_TOO_LATE
- FIDA-EUR — BUILDING_ACCELERATION — score 6.234/10 — DETECTED_BUT_TOO_LATE
- SOMI-EUR — BUILDING_ACCELERATION — score 6.201/10 — DETECTED_BUT_TOO_LATE
- ENJ-EUR — BUILDING_ACCELERATION — score 6.183/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- MAV-EUR — BUILDING_ACCELERATION — score 5.917/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- FLOCK-EUR — BUILDING_ACCELERATION — score 5.770/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- T-EUR — BUILDING_ACCELERATION — score 5.633/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- HEI-EUR — BUILDING_ACCELERATION — score 5.030/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- AVA-EUR — BUILDING_ACCELERATION — score 4.971/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- LISTA-EUR — BUILDING_ACCELERATION — score 4.891/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- MMT-EUR — ACTIVE_NOW — score mémoire 9.836/10 — sources ACCELERATION — DETECTED_BUT_TOO_LATE
- INIT-EUR — MEMORY_24H — score mémoire 8.690/10 — sources ACCELERATION — MEMORY_ONLY
- DODO-EUR — ACTIVE_NOW — score mémoire 7.114/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- KITE-EUR — ACTIVE_NOW — score mémoire 6.944/10 — sources DECISION_LAYER, V4 — WATCH_ONLY
- ZRC-EUR — MEMORY_24H — score mémoire 6.918/10 — sources ACCELERATION — MEMORY_ONLY
- VVV-EUR — MEMORY_24H — score mémoire 6.536/10 — sources DECISION_LAYER — MEMORY_ONLY
- EPIC-EUR — MEMORY_DECAY_24_72H — score mémoire 6.236/10 — sources ACCELERATION — MEMORY_ONLY
- FIDA-EUR — ACTIVE_NOW — score mémoire 6.234/10 — sources ACCELERATION — DETECTED_BUT_TOO_LATE
- SOMI-EUR — ACTIVE_NOW — score mémoire 6.201/10 — sources ACCELERATION — DETECTED_BUT_TOO_LATE
- ENJ-EUR — ACTIVE_NOW — score mémoire 6.183/10 — sources ACCELERATION — WATCH_ONLY

## Audit des plus fortes hausses

- LISTA-EUR +44.81% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- INX-EUR +28.54% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- MMT-EUR +21.63% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- RPL-EUR +15.49% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- BABY-EUR +14.70% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- TREAD-EUR +13.34% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- ZIL-EUR +13.01% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- SQD-EUR +11.53% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- ZRC-EUR +11.48% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- ATOM-EUR +11.38% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE

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
