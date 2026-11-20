# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-11-20T01:19:00.826228+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : MEGA-EUR | action PLACE_LIMITE_PASSIVE | opportunité 7.513 | entrée 5.850 | trend 8.650 | rang 7.238
  - Strong structure but imperfect current entry; prefer passive execution. High extension/chase reduces rank but does not erase the setup.
- **MEILLEUR_LATENT_ACCELERATOR** : aucun candidat matériel
- **MEILLEUR_PULLBACK_REENTRY** : CROSS-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 7.135 | entrée 6.700 | trend 8.200 | rang 6.928
  - Trend remains strong; candidate retained for re-entry instead of discarded.

## Tous les achats immédiats

Aucun ACHETE_MAINTENANT dans le classement complet.

## Top cross-sectionnel — aperçu non exhaustif

Ce top est une vue courte multi-buckets. Il ne doit jamais être utilisé comme liste exhaustive des achats immédiats.
1. MEGA-EUR — MEILLEURE_LIMITE_PASSIVE — PLACE_LIMITE_PASSIVE — rank 7.238
2. CROSS-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 6.928

## Accélération indépendante

- HUMA-EUR — CONFIRMED_ACCELERATION — score 8.000/10 — DETECTED_BUT_TOO_LATE
- BOB-EUR — CONFIRMED_ACCELERATION — score 7.070/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- CT-EUR — BUILDING_ACCELERATION — score 6.257/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- FOLD-EUR — BUILDING_ACCELERATION — score 5.825/10 — DETECTED_BUT_TOO_LATE
- DEGEN-EUR — BUILDING_ACCELERATION — score 5.414/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- ICNT-EUR — BUILDING_ACCELERATION — score 5.275/10 — DETECTED_BUT_TOO_LATE
- ROBO-EUR — BUILDING_ACCELERATION — score 5.170/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- XYO-EUR — BUILDING_ACCELERATION — score 5.085/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- TOWNS-EUR — MEMORY_DECAY_24_72H — score mémoire 8.971/10 — sources ACCELERATION — MEMORY_ONLY
- HUMA-EUR — ACTIVE_NOW — score mémoire 8.000/10 — sources ACCELERATION — DETECTED_BUT_TOO_LATE
- ADX-EUR — MEMORY_24H — score mémoire 7.477/10 — sources ACCELERATION — MEMORY_ONLY
- CSPR-EUR — MEMORY_24H — score mémoire 7.456/10 — sources ACCELERATION — MEMORY_ONLY
- MEGA-EUR — ACTIVE_NOW — score mémoire 7.238/10 — sources DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- EDGE-EUR — MEMORY_24H — score mémoire 7.201/10 — sources ACCELERATION — MEMORY_ONLY
- KITE-EUR — MEMORY_24H — score mémoire 7.083/10 — sources DECISION_LAYER, V4 — MEMORY_ONLY
- BOB-EUR — ACTIVE_NOW — score mémoire 7.070/10 — sources ACCELERATION — WATCH_ONLY
- CPOOL-EUR — MEMORY_24H — score mémoire 7.000/10 — sources ACCELERATION — MEMORY_ONLY
- CROSS-EUR — ACTIVE_NOW — score mémoire 6.928/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE

## Audit des plus fortes hausses

- ICNT-EUR +29.77% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- PUFFER-EUR +27.12% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- IKA-EUR +26.32% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- MMT-EUR +20.76% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- NES-EUR +20.22% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- RARE-EUR +17.62% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- YB-EUR +16.35% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- CTR-EUR +16.20% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- HUMA-EUR +15.20% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- LAPTOP-EUR +10.80% — DETECTED_EARLY — couche NONE — action INTERPRETATION

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
