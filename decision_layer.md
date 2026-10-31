# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-10-31T14:55:03.462107+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : aucun candidat matériel
- **MEILLEUR_LATENT_ACCELERATOR** : aucun candidat matériel
- **MEILLEUR_PULLBACK_REENTRY** : SOLV-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 6.766 | entrée 4.650 | trend 8.200 | rang 6.622
  - Trend remains strong; candidate retained for re-entry instead of discarded.

## Tous les achats immédiats

Aucun ACHETE_MAINTENANT dans le classement complet.

## Top cross-sectionnel — aperçu non exhaustif

Ce top est une vue courte multi-buckets. Il ne doit jamais être utilisé comme liste exhaustive des achats immédiats.
1. SOLV-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 6.622

## Accélération indépendante

- COW-EUR — CONFIRMED_ACCELERATION — score 7.102/10 — DETECTED_BUT_TOO_LATE
- LIGHTER-EUR — CONFIRMED_ACCELERATION — score 6.560/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- ZK-EUR — CONFIRMED_ACCELERATION — score 6.520/10 — DETECTED_BUT_TOO_LATE
- WIN-EUR — CONFIRMED_ACCELERATION — score 6.513/10 — DETECTED_BUT_TOO_LATE
- RSR-EUR — BUILDING_ACCELERATION — score 6.434/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- REZ-EUR — BUILDING_ACCELERATION — score 5.899/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- PROMPT-EUR — BUILDING_ACCELERATION — score 5.744/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- CATI-EUR — BUILDING_ACCELERATION — score 5.379/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- STRK-EUR — BUILDING_ACCELERATION — score 4.934/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- RECALL-EUR — MEMORY_24H — score mémoire 9.168/10 — sources ACCELERATION — MEMORY_ONLY
- GWEI-EUR — MEMORY_DECAY_24_72H — score mémoire 8.619/10 — sources ACCELERATION — MEMORY_ONLY
- OSMO-EUR — MEMORY_24H — score mémoire 8.400/10 — sources ACCELERATION, DECISION_LAYER — MEMORY_ONLY
- XMN-EUR — MEMORY_24H — score mémoire 7.637/10 — sources ACCELERATION — MEMORY_ONLY
- NIL-EUR — MEMORY_24H — score mémoire 7.182/10 — sources ACCELERATION — MEMORY_ONLY
- COW-EUR — ACTIVE_NOW — score mémoire 7.102/10 — sources ACCELERATION — DETECTED_BUT_TOO_LATE
- HFT-EUR — MEMORY_24H — score mémoire 7.021/10 — sources ACCELERATION — MEMORY_ONLY
- PEPE-EUR — MEMORY_24H — score mémoire 6.997/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- LSK-EUR — MEMORY_24H — score mémoire 6.818/10 — sources ACCELERATION — MEMORY_ONLY
- BEAM-EUR — MEMORY_24H — score mémoire 6.795/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY

## Audit des plus fortes hausses

- LSK-EUR +41.12% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- COW-EUR +35.13% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- RED-EUR +14.15% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- INX-EUR +12.77% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE
- EDEN-EUR +12.76% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- RAD-EUR +12.43% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- POND-EUR +12.11% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- U-EUR +11.15% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- STX-EUR +11.05% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- CVC-EUR +10.83% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE

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
