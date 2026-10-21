# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-10-21T21:39:30.434259+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : AVA-EUR | action PLACE_LIMITE_PASSIVE | opportunité 7.495 | entrée 5.900 | trend 8.300 | rang 7.011
  - Strong structure but imperfect current entry; prefer passive execution. High extension/chase reduces rank but does not erase the setup.
- **MEILLEUR_LATENT_ACCELERATOR** : aucun candidat matériel
- **MEILLEUR_PULLBACK_REENTRY** : WLD-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 7.737 | entrée 7.450 | trend 8.450 | rang 7.512
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Tous les achats immédiats

Aucun ACHETE_MAINTENANT dans le classement complet.

## Top cross-sectionnel — aperçu non exhaustif

Ce top est une vue courte multi-buckets. Il ne doit jamais être utilisé comme liste exhaustive des achats immédiats.
1. WLD-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.512
2. AMP-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.072
3. AVA-EUR — MEILLEURE_LIMITE_PASSIVE — PLACE_LIMITE_PASSIVE — rank 7.011

## Accélération indépendante

- U-EUR — CONFIRMED_ACCELERATION — score 8.716/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- UP-EUR — CONFIRMED_ACCELERATION — score 6.640/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- BILL-EUR — BUILDING_ACCELERATION — score 6.025/10 — DETECTED_BUT_TOO_LATE
- ALIGN-EUR — BUILDING_ACCELERATION — score 5.969/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- LIGHTER-EUR — BUILDING_ACCELERATION — score 5.587/10 — DETECTED_BUT_TOO_LATE
- NEAR-EUR — BUILDING_ACCELERATION — score 5.183/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- AXIS-EUR — BUILDING_ACCELERATION — score 5.120/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- GRT-EUR — BUILDING_ACCELERATION — score 5.044/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- PUFFER-EUR — BUILDING_ACCELERATION — score 4.953/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- MOODENG-EUR — MEMORY_24H — score mémoire 9.291/10 — sources ACCELERATION — MEMORY_ONLY
- WHUF-EUR — MEMORY_24H — score mémoire 9.147/10 — sources ACCELERATION — MEMORY_ONLY
- U-EUR — ACTIVE_NOW — score mémoire 8.716/10 — sources ACCELERATION — WATCH_ONLY
- W-EUR — MEMORY_24H — score mémoire 7.838/10 — sources ACCELERATION — MEMORY_ONLY
- ZAMA-EUR — MEMORY_24H — score mémoire 7.670/10 — sources ACCELERATION — MEMORY_ONLY
- HFT-EUR — MEMORY_24H — score mémoire 7.606/10 — sources ACCELERATION — MEMORY_ONLY
- IRYS-EUR — MEMORY_24H — score mémoire 7.518/10 — sources ACCELERATION — MEMORY_ONLY
- WLD-EUR — ACTIVE_NOW — score mémoire 7.512/10 — sources DECISION_LAYER, V4 — WATCH_ONLY
- BEAM-EUR — MEMORY_24H — score mémoire 7.510/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- STRK-EUR — MEMORY_24H — score mémoire 7.490/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY

## Audit des plus fortes hausses

- IRYS-EUR +52.76% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- IOST-EUR +48.87% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- ALT-EUR +35.68% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- BILL-EUR +22.01% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- PROM-EUR +15.60% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE
- LIGHTER-EUR +15.14% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- DYM-EUR +14.79% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- PARTI-EUR +14.19% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- WELL-EUR +13.35% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- GRASS-EUR +13.24% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE

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
