# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-10-22T22:20:04.813515+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : aucun candidat matériel
- **MEILLEUR_LATENT_ACCELERATOR** : aucun candidat matériel
- **MEILLEUR_PULLBACK_REENTRY** : CVX-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 7.436 | entrée 6.100 | trend 8.700 | rang 7.254
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Tous les achats immédiats

Aucun ACHETE_MAINTENANT dans le classement complet.

## Top cross-sectionnel — aperçu non exhaustif

Ce top est une vue courte multi-buckets. Il ne doit jamais être utilisé comme liste exhaustive des achats immédiats.
1. CVX-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.254
2. ICNT-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.112
3. IRYS-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 6.475

## Accélération indépendante

- CPOOL-EUR — CONFIRMED_ACCELERATION — score 8.820/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- U-EUR — CONFIRMED_ACCELERATION — score 7.699/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- UP-EUR — CONFIRMED_ACCELERATION — score 6.852/10 — DETECTED_BUT_TOO_LATE
- MEW-EUR — BUILDING_ACCELERATION — score 5.888/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- CPOOL-EUR — ACTIVE_NOW — score mémoire 8.820/10 — sources ACCELERATION — WATCH_ONLY
- ORCA-EUR — MEMORY_24H — score mémoire 8.261/10 — sources ACCELERATION — MEMORY_ONLY
- VELO-EUR — MEMORY_24H — score mémoire 7.742/10 — sources ACCELERATION — MEMORY_ONLY
- U-EUR — ACTIVE_NOW — score mémoire 7.699/10 — sources ACCELERATION — WATCH_ONLY
- METIS-EUR — MEMORY_24H — score mémoire 7.328/10 — sources DECISION_LAYER, V4 — MEMORY_ONLY
- CVX-EUR — ACTIVE_NOW — score mémoire 7.254/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- BEAM-EUR — MEMORY_24H — score mémoire 7.238/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- ELSA-EUR — ACTIVE_NOW — score mémoire 7.115/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- ICNT-EUR — ACTIVE_NOW — score mémoire 7.112/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- KMNO-EUR — MEMORY_24H — score mémoire 7.027/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY

## Audit des plus fortes hausses

- GROVE-EUR +36.75% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- AXIS-EUR +15.01% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- GTC-EUR +13.00% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- CTR-EUR +8.77% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- MEW-EUR +8.67% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE
- OSMO-EUR +6.15% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- IRYS-EUR +5.46% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- DODO-EUR +4.94% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE
- KERNEL-EUR +4.86% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE
- WIN-EUR +4.15% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE

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
