# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-10-20T23:47:03.040342+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : BEAM-EUR | action PLACE_LIMITE_PASSIVE | opportunité 7.873 | entrée 6.100 | trend 8.750 | rang 7.510
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : aucun candidat matériel
- **MEILLEUR_PULLBACK_REENTRY** : WLD-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 7.563 | entrée 7.200 | trend 8.650 | rang 7.388
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Tous les achats immédiats

Aucun ACHETE_MAINTENANT dans le classement complet.

## Top cross-sectionnel — aperçu non exhaustif

Ce top est une vue courte multi-buckets. Il ne doit jamais être utilisé comme liste exhaustive des achats immédiats.
1. BEAM-EUR — MEILLEURE_LIMITE_PASSIVE — PLACE_LIMITE_PASSIVE — rank 7.510
2. ALT-EUR — MEILLEURE_LIMITE_PASSIVE — PLACE_LIMITE_PASSIVE — rank 7.392
3. WLD-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.388

## Accélération indépendante

- AMP-EUR — CONFIRMED_ACCELERATION — score 8.353/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- ALT-EUR — BUILDING_ACCELERATION — score 5.861/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- GNS-EUR — MEMORY_24H — score mémoire 9.505/10 — sources ACCELERATION — MEMORY_ONLY
- POND-EUR — MEMORY_24H — score mémoire 8.833/10 — sources ACCELERATION — MEMORY_ONLY
- AMP-EUR — ACTIVE_NOW — score mémoire 8.353/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- IOST-EUR — MEMORY_24H — score mémoire 7.706/10 — sources ACCELERATION — MEMORY_ONLY
- WHUF-EUR — MEMORY_24H — score mémoire 7.643/10 — sources ACCELERATION — MEMORY_ONLY
- BEAM-EUR — ACTIVE_NOW — score mémoire 7.510/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- ALT-EUR — ACTIVE_NOW — score mémoire 7.392/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- WLD-EUR — ACTIVE_NOW — score mémoire 7.388/10 — sources DECISION_LAYER, V4 — WATCH_ONLY
- CTR-EUR — ACTIVE_NOW — score mémoire 7.008/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- INJ-EUR — ACTIVE_NOW — score mémoire 6.920/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY

## Audit des plus fortes hausses

- IOST-EUR +46.56% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- COMP-EUR +20.32% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- ICNT-EUR +16.04% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- CVX-EUR +15.48% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- REZ-EUR +14.52% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- GNS-EUR +13.76% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- SOSO-EUR +13.43% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- TOSHI-EUR +10.87% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE
- USELESS-EUR +10.51% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- AERO-EUR +10.37% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE

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
