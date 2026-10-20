# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-10-20T02:12:04.162079+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : aucun candidat matériel
- **MEILLEUR_LATENT_ACCELERATOR** : aucun candidat matériel
- **MEILLEUR_PULLBACK_REENTRY** : ALT-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 7.405 | entrée 4.850 | trend 8.500 | rang 7.082
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Tous les achats immédiats

Aucun ACHETE_MAINTENANT dans le classement complet.

## Top cross-sectionnel — aperçu non exhaustif

Ce top est une vue courte multi-buckets. Il ne doit jamais être utilisé comme liste exhaustive des achats immédiats.
1. ALT-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.082
2. DUSK-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 6.654

## Accélération indépendante

- GIGA-EUR — CONFIRMED_ACCELERATION — score 6.780/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- ZEUS-EUR — BUILDING_ACCELERATION — score 5.934/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- CTR-EUR — MEMORY_24H — score mémoire 9.247/10 — sources ACCELERATION — MEMORY_ONLY
- POND-EUR — MEMORY_24H — score mémoire 8.833/10 — sources ACCELERATION — MEMORY_ONLY
- WHUF-EUR — MEMORY_DECAY_24_72H — score mémoire 8.362/10 — sources ACCELERATION — MEMORY_ONLY
- VVV-EUR — MEMORY_DECAY_24_72H — score mémoire 8.281/10 — sources ACCELERATION — MEMORY_ONLY
- MANTRA-EUR — MEMORY_DECAY_24_72H — score mémoire 7.811/10 — sources ACCELERATION — MEMORY_ONLY
- LSK-EUR — MEMORY_24H — score mémoire 7.457/10 — sources ACCELERATION — MEMORY_ONLY
- BEAM-EUR — MEMORY_24H — score mémoire 7.244/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- ALT-EUR — ACTIVE_NOW — score mémoire 7.082/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- HUMA-EUR — MEMORY_24H — score mémoire 6.991/10 — sources ACCELERATION — MEMORY_ONLY
- DODO-EUR — MEMORY_24H — score mémoire 6.968/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY

## Audit des plus fortes hausses

- CTR-EUR +29.75% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- PHA-EUR +23.38% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- AVA-EUR +17.96% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- OSMO-EUR +17.48% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- GTC-EUR +14.74% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- NOS-EUR +12.56% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- WELL-EUR +12.01% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- CT-EUR +11.84% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- NIL-EUR +11.58% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- S-EUR +10.56% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE

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
