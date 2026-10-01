# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-10-01T23:47:15.753258+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : WLD-EUR | action ACHETE_MAINTENANT | opportunité 9.342 | entrée 7.400 | trend 8.400 | rang 8.353
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : PROM-EUR | action PLACE_LIMITE_PASSIVE | opportunité 7.806 | entrée 5.800 | trend 8.950 | rang 7.747
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : KAIA-EUR | action LATENT_ACCELERATOR | opportunité 7.491 | entrée 5.300 | trend 8.550 | rang 7.338
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : REZ-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.774 | entrée 6.200 | trend 8.400 | rang 7.949
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Tous les achats immédiats

1. WLD-EUR — ACHETE_MAINTENANT — rank 8.353 — opportunité 9.342 — entrée 7.400 — trend 8.400
2. AAVE-EUR — ACHETE_MAINTENANT — rank 8.249 — opportunité 8.551 — entrée 7.200 — trend 9.200

## Top cross-sectionnel — aperçu non exhaustif

Ce top est une vue courte multi-buckets. Il ne doit jamais être utilisé comme liste exhaustive des achats immédiats.
1. WLD-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.353
2. AAVE-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.249
3. REZ-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.949

## Accélération indépendante

- ICX-EUR — CONFIRMED_ACCELERATION — score 6.500/10 — DETECTED_BUT_TOO_LATE
- MOVR-EUR — BUILDING_ACCELERATION — score 6.359/10 — DETECTED_BUT_TOO_LATE
- CT-EUR — BUILDING_ACCELERATION — score 5.767/10 — DETECTED_BUT_TOO_LATE
- SWEAT-EUR — BUILDING_ACCELERATION — score 5.500/10 — DETECTED_BUT_TOO_LATE
- CELO-EUR — BUILDING_ACCELERATION — score 5.234/10 — DETECTED_BUT_TOO_LATE
- SUPER-EUR — BUILDING_ACCELERATION — score 5.022/10 — DETECTED_BUT_TOO_LATE
- KAITO-EUR — BUILDING_ACCELERATION — score 4.882/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- CHILLGUY-EUR — BUILDING_ACCELERATION — score 4.862/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- PUMP-EUR — ACTIVE_NOW — score mémoire 7.619/10 — sources ACCELERATION, DECISION_LAYER, V4 — BUYABLE_NOW
- CPOOL-EUR — MEMORY_24H — score mémoire 10.000/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- ZRC-EUR — MEMORY_24H — score mémoire 8.847/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- WLD-EUR — ACTIVE_NOW — score mémoire 8.353/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- OSMO-EUR — MEMORY_24H — score mémoire 8.342/10 — sources ACCELERATION — MEMORY_ONLY
- AAVE-EUR — ACTIVE_NOW — score mémoire 8.249/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- AGI-EUR — MEMORY_24H — score mémoire 8.119/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- U-EUR — MEMORY_24H — score mémoire 8.002/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- REZ-EUR — ACTIVE_NOW — score mémoire 7.949/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- ZRO-EUR — ACTIVE_NOW — score mémoire 7.930/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY

## Audit des plus fortes hausses

- SWEAT-EUR +138.48% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- GTC-EUR +48.82% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- MOVR-EUR +36.01% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ALICE-EUR +25.57% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- CT-EUR +25.01% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- MEGA-EUR +21.41% — DETECTED_EARLY — couche NONE — action NONE
- NOM-EUR +18.86% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- SYN-EUR +16.97% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- SUPER-EUR +15.75% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- NOS-EUR +14.43% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION

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
