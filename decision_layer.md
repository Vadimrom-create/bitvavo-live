# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-10-19T23:48:45.791082+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : BEAM-EUR | action PLACE_LIMITE_PASSIVE | opportunité 7.605 | entrée 5.800 | trend 8.700 | rang 7.244
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : ALT-EUR | action LATENT_ACCELERATOR | opportunité 7.711 | entrée 5.700 | trend 8.450 | rang 7.107
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : KMNO-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 7.441 | entrée 5.700 | trend 7.800 | rang 6.888
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Tous les achats immédiats

Aucun ACHETE_MAINTENANT dans le classement complet.

## Top cross-sectionnel — aperçu non exhaustif

Ce top est une vue courte multi-buckets. Il ne doit jamais être utilisé comme liste exhaustive des achats immédiats.
1. BEAM-EUR — MEILLEURE_LIMITE_PASSIVE — PLACE_LIMITE_PASSIVE — rank 7.244
2. ALT-EUR — MEILLEUR_LATENT_ACCELERATOR — LATENT_ACCELERATOR — rank 7.107
3. KMNO-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 6.888

## Accélération indépendante

- POND-EUR — CONFIRMED_ACCELERATION — score 8.833/10 — DETECTED_BUT_TOO_LATE
- OSMO-EUR — BUILDING_ACCELERATION — score 6.090/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- USELESS-EUR — BUILDING_ACCELERATION — score 5.028/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- HAEDAL-EUR — BUILDING_ACCELERATION — score 4.901/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- CTR-EUR — MEMORY_24H — score mémoire 9.247/10 — sources ACCELERATION — MEMORY_ONLY
- POND-EUR — ACTIVE_NOW — score mémoire 8.833/10 — sources ACCELERATION — DETECTED_BUT_TOO_LATE
- WHUF-EUR — MEMORY_DECAY_24_72H — score mémoire 8.801/10 — sources ACCELERATION — MEMORY_ONLY
- VVV-EUR — MEMORY_24H — score mémoire 8.341/10 — sources ACCELERATION — MEMORY_ONLY
- MANTRA-EUR — MEMORY_DECAY_24_72H — score mémoire 8.238/10 — sources ACCELERATION — MEMORY_ONLY
- LSK-EUR — MEMORY_24H — score mémoire 7.457/10 — sources ACCELERATION — MEMORY_ONLY
- BEAM-EUR — ACTIVE_NOW — score mémoire 7.244/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- ALT-EUR — ACTIVE_NOW — score mémoire 7.107/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- HUMA-EUR — MEMORY_24H — score mémoire 6.991/10 — sources ACCELERATION — MEMORY_ONLY
- DODO-EUR — MEMORY_24H — score mémoire 6.968/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY

## Audit des plus fortes hausses

- AVA-EUR +31.90% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- GTC-EUR +31.52% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- PHA-EUR +28.83% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- CTR-EUR +27.32% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- OSMO-EUR +17.94% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- POND-EUR +14.80% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- NOS-EUR +13.75% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- S-EUR +13.19% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- WELL-EUR +12.51% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- NIL-EUR +11.39% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE

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
