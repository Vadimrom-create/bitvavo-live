# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-10-17T23:23:09.237905+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : RSR-EUR | action PLACE_LIMITE_PASSIVE | opportunité 7.577 | entrée 6.450 | trend 8.000 | rang 7.093
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : aucun candidat matériel
- **MEILLEUR_PULLBACK_REENTRY** : INJ-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 7.507 | entrée 5.900 | trend 8.450 | rang 7.294
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Tous les achats immédiats

Aucun ACHETE_MAINTENANT dans le classement complet.

## Top cross-sectionnel — aperçu non exhaustif

Ce top est une vue courte multi-buckets. Il ne doit jamais être utilisé comme liste exhaustive des achats immédiats.
1. INJ-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.294
2. DUSK-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.281
3. ALT-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.202

## Accélération indépendante

- DUSK-EUR — CONFIRMED_ACCELERATION — score 9.204/10 — DETECTED_BUT_TOO_LATE
- AEVO-EUR — BUILDING_ACCELERATION — score 6.307/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- GNS-EUR — BUILDING_ACCELERATION — score 5.960/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- ANIME-EUR — BUILDING_ACCELERATION — score 5.634/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- EPIC-EUR — BUILDING_ACCELERATION — score 5.197/10 — DETECTED_BUT_TOO_LATE
- DGB-EUR — BUILDING_ACCELERATION — score 5.049/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- DUSK-EUR — ACTIVE_NOW — score mémoire 9.204/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- AXL-EUR — MEMORY_24H — score mémoire 9.132/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- BTT-EUR — MEMORY_DECAY_24_72H — score mémoire 8.399/10 — sources ACCELERATION — MEMORY_ONLY
- ZRC-EUR — MEMORY_24H — score mémoire 8.245/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- GTC-EUR — MEMORY_24H — score mémoire 7.849/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- CPOOL-EUR — MEMORY_24H — score mémoire 7.716/10 — sources ACCELERATION — MEMORY_ONLY
- U-EUR — MEMORY_24H — score mémoire 7.667/10 — sources ACCELERATION — MEMORY_ONLY
- INJ-EUR — ACTIVE_NOW — score mémoire 7.294/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- ALT-EUR — ACTIVE_NOW — score mémoire 7.202/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- WAL-EUR — MEMORY_24H — score mémoire 7.199/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY

## Audit des plus fortes hausses

- AVA-EUR +30.45% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- GTC-EUR +20.23% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- EPIC-EUR +15.82% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- LSK-EUR +12.72% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- BTT-EUR +11.71% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- SAND-EUR +10.70% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- ZEUS-EUR +10.58% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- ZRC-EUR +8.52% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- SPX-EUR +6.66% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE
- DUSK-EUR +6.50% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE

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
