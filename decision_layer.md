# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-11-01T07:01:28.903674+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : aucun candidat matériel
- **MEILLEUR_LATENT_ACCELERATOR** : aucun candidat matériel
- **MEILLEUR_PULLBACK_REENTRY** : PEPE-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 7.530 | entrée 6.600 | trend 8.100 | rang 7.232
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Tous les achats immédiats

Aucun ACHETE_MAINTENANT dans le classement complet.

## Top cross-sectionnel — aperçu non exhaustif

Ce top est une vue courte multi-buckets. Il ne doit jamais être utilisé comme liste exhaustive des achats immédiats.
1. PEPE-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.232

## Accélération indépendante

- ZRC-EUR — CONFIRMED_ACCELERATION — score 6.619/10 — DETECTED_BUT_TOO_LATE
- POND-EUR — BUILDING_ACCELERATION — score 5.900/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- HOT-EUR — BUILDING_ACCELERATION — score 5.574/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- ADX-EUR — MEMORY_24H — score mémoire 10.000/10 — sources ACCELERATION — MEMORY_ONLY
- U-EUR — MEMORY_24H — score mémoire 9.449/10 — sources ACCELERATION — MEMORY_ONLY
- PROMPT-EUR — MEMORY_24H — score mémoire 9.000/10 — sources ACCELERATION — MEMORY_ONLY
- POWR-EUR — MEMORY_24H — score mémoire 8.642/10 — sources ACCELERATION — MEMORY_ONLY
- OSMO-EUR — MEMORY_24H — score mémoire 8.400/10 — sources ACCELERATION, DECISION_LAYER — MEMORY_ONLY
- GNS-EUR — MEMORY_24H — score mémoire 8.246/10 — sources ACCELERATION — MEMORY_ONLY
- STO-EUR — MEMORY_24H — score mémoire 8.082/10 — sources ACCELERATION — MEMORY_ONLY
- LAPTOP-EUR — MEMORY_24H — score mémoire 8.004/10 — sources ACCELERATION — MEMORY_ONLY
- RECALL-EUR — MEMORY_DECAY_24_72H — score mémoire 7.710/10 — sources ACCELERATION — MEMORY_ONLY
- PEPE-EUR — ACTIVE_NOW — score mémoire 7.232/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY

## Audit des plus fortes hausses

- BEAM-EUR +19.40% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- ZAMA-EUR +17.10% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- G-EUR +15.91% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- KITE-EUR +15.09% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- LIGHTER-EUR +14.07% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- POWR-EUR +13.87% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- BTT-EUR +12.14% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE
- HOT-EUR +10.17% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- PROM-EUR +9.05% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- MORPHO-EUR +8.91% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE

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
