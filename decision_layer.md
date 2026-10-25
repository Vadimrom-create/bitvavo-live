# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-10-25T16:47:53.594218+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : ELSA-EUR | action PLACE_LIMITE_PASSIVE | opportunité 7.502 | entrée 6.700 | trend 8.450 | rang 7.270
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : INIT-EUR | action LATENT_ACCELERATOR | opportunité 7.960 | entrée 5.500 | trend 8.850 | rang 7.260
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : GRASS-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 6.716 | entrée 6.950 | trend 7.950 | rang 6.459
  - Trend remains strong; candidate retained for re-entry instead of discarded.

## Tous les achats immédiats

Aucun ACHETE_MAINTENANT dans le classement complet.

## Top cross-sectionnel — aperçu non exhaustif

Ce top est une vue courte multi-buckets. Il ne doit jamais être utilisé comme liste exhaustive des achats immédiats.
1. ELSA-EUR — MEILLEURE_LIMITE_PASSIVE — PLACE_LIMITE_PASSIVE — rank 7.270
2. INIT-EUR — MEILLEUR_LATENT_ACCELERATOR — LATENT_ACCELERATOR — rank 7.260
3. GRASS-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 6.459

## Accélération indépendante

- REZ-EUR — CONFIRMED_ACCELERATION — score 7.835/10 — DETECTED_BUT_TOO_LATE
- AMP-EUR — CONFIRMED_ACCELERATION — score 7.596/10 — DETECTED_BUT_TOO_LATE
- BABY-EUR — CONFIRMED_ACCELERATION — score 7.580/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- VVV-EUR — BUILDING_ACCELERATION — score 6.115/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- LRC-EUR — BUILDING_ACCELERATION — score 5.780/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- NEAR-EUR — BUILDING_ACCELERATION — score 5.038/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- ETHFI-EUR — BUILDING_ACCELERATION — score 4.957/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- TREAD-EUR — MEMORY_24H — score mémoire 8.974/10 — sources ACCELERATION — MEMORY_ONLY
- BIRB-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION — MEMORY_ONLY
- CHIP-EUR — MEMORY_24H — score mémoire 7.845/10 — sources ACCELERATION — MEMORY_ONLY
- REZ-EUR — ACTIVE_NOW — score mémoire 7.835/10 — sources ACCELERATION, DECISION_LAYER — DETECTED_BUT_TOO_LATE
- U-EUR — MEMORY_24H — score mémoire 7.794/10 — sources ACCELERATION — MEMORY_ONLY
- IQ-EUR — MEMORY_24H — score mémoire 7.702/10 — sources ACCELERATION — MEMORY_ONLY
- 0G-EUR — MEMORY_24H — score mémoire 7.620/10 — sources ACCELERATION — MEMORY_ONLY
- AMP-EUR — ACTIVE_NOW — score mémoire 7.596/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- BABY-EUR — ACTIVE_NOW — score mémoire 7.580/10 — sources ACCELERATION — WATCH_ONLY
- CSPR-EUR — MEMORY_24H — score mémoire 7.452/10 — sources ACCELERATION — MEMORY_ONLY

## Audit des plus fortes hausses

- CAP-EUR +38.21% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- TREAD-EUR +23.04% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- T-EUR +21.65% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- CNPY-EUR +20.62% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- REZ-EUR +13.66% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- GRASS-EUR +13.02% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- USELESS-EUR +11.80% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE
- OSMO-EUR +10.58% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- BILL-EUR +10.22% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- CT-EUR +10.17% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE

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
