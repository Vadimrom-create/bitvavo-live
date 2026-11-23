# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-11-23T21:41:03.318247+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : aucun candidat matériel
- **MEILLEUR_LATENT_ACCELERATOR** : aucun candidat matériel
- **MEILLEUR_PULLBACK_REENTRY** : KITE-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 7.159 | entrée 5.350 | trend 8.500 | rang 6.995
  - Trend remains strong; candidate retained for re-entry instead of discarded.

## Tous les achats immédiats

Aucun ACHETE_MAINTENANT dans le classement complet.

## Top cross-sectionnel — aperçu non exhaustif

Ce top est une vue courte multi-buckets. Il ne doit jamais être utilisé comme liste exhaustive des achats immédiats.
1. KITE-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 6.995
2. DODO-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 6.804
3. VVV-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 6.536

## Accélération indépendante

- INIT-EUR — CONFIRMED_ACCELERATION — score 8.690/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- ZRC-EUR — CONFIRMED_ACCELERATION — score 6.918/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- LISTA-EUR — BUILDING_ACCELERATION — score 5.472/10 — DETECTED_BUT_TOO_LATE
- RARE-EUR — BUILDING_ACCELERATION — score 5.006/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- QUID-EUR — BUILDING_ACCELERATION — score 4.896/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- HUMA-EUR — BUILDING_ACCELERATION — score 4.895/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- INIT-EUR — ACTIVE_NOW — score mémoire 8.690/10 — sources ACCELERATION — WATCH_ONLY
- KITE-EUR — ACTIVE_NOW — score mémoire 6.995/10 — sources DECISION_LAYER, V4 — WATCH_ONLY
- NES-EUR — MEMORY_DECAY_24_72H — score mémoire 6.972/10 — sources ACCELERATION — MEMORY_ONLY
- ZRC-EUR — ACTIVE_NOW — score mémoire 6.918/10 — sources ACCELERATION — WATCH_ONLY
- EPIC-EUR — MEMORY_24H — score mémoire 6.856/10 — sources ACCELERATION — MEMORY_ONLY
- DODO-EUR — ACTIVE_NOW — score mémoire 6.804/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- VVV-EUR — ACTIVE_NOW — score mémoire 6.536/10 — sources DECISION_LAYER — WATCH_ONLY
- ZEUS-EUR — MEMORY_DECAY_24_72H — score mémoire 6.489/10 — sources ACCELERATION — MEMORY_ONLY
- CROSS-EUR — MEMORY_24H — score mémoire 6.452/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- TRUST-EUR — MEMORY_24H — score mémoire 6.037/10 — sources ACCELERATION — MEMORY_ONLY

## Audit des plus fortes hausses

- INX-EUR +32.13% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- LISTA-EUR +21.94% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- ELSA-EUR +20.50% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- LSK-EUR +12.23% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- GROVE-EUR +12.13% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- CAP-EUR +12.05% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- QNT-EUR +11.64% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- FLUX-EUR +11.60% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- PROM-EUR +11.17% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- PEAQ-EUR +10.04% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE

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
