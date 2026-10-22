# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-10-22T15:04:28.433148+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : aucun candidat matériel
- **MEILLEUR_LATENT_ACCELERATOR** : CTR-EUR | action LATENT_ACCELERATOR | opportunité 7.411 | entrée 5.350 | trend 8.850 | rang 6.892
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : CVX-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 6.858 | entrée 5.850 | trend 8.450 | rang 6.876
  - Trend remains strong; candidate retained for re-entry instead of discarded.

## Tous les achats immédiats

Aucun ACHETE_MAINTENANT dans le classement complet.

## Top cross-sectionnel — aperçu non exhaustif

Ce top est une vue courte multi-buckets. Il ne doit jamais être utilisé comme liste exhaustive des achats immédiats.
1. CTR-EUR — MEILLEUR_LATENT_ACCELERATOR — LATENT_ACCELERATOR — rank 6.892
2. CVX-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 6.876
3. ELSA-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 6.764

## Accélération indépendante

- AMP-EUR — BUILDING_ACCELERATION — score 5.437/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- REZ-EUR — BUILDING_ACCELERATION — score 4.861/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- ORCA-EUR — MEMORY_24H — score mémoire 8.261/10 — sources ACCELERATION — MEMORY_ONLY
- U-EUR — MEMORY_24H — score mémoire 7.898/10 — sources ACCELERATION — MEMORY_ONLY
- ZAMA-EUR — MEMORY_24H — score mémoire 7.670/10 — sources ACCELERATION — MEMORY_ONLY
- HFT-EUR — MEMORY_24H — score mémoire 7.606/10 — sources ACCELERATION — MEMORY_ONLY
- METIS-EUR — MEMORY_24H — score mémoire 7.328/10 — sources DECISION_LAYER, V4 — MEMORY_ONLY
- BEAM-EUR — MEMORY_24H — score mémoire 7.238/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- IRYS-EUR — MEMORY_DECAY_24_72H — score mémoire 7.224/10 — sources ACCELERATION — MEMORY_ONLY
- KMNO-EUR — MEMORY_24H — score mémoire 7.027/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- AVA-EUR — MEMORY_24H — score mémoire 7.011/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- CTR-EUR — ACTIVE_NOW — score mémoire 6.892/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE

## Audit des plus fortes hausses

- PTB-EUR +41.93% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- BILL-EUR +16.24% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- DGB-EUR +14.24% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- CTR-EUR +13.33% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- BTT-EUR +9.97% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- AXIS-EUR +7.53% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- CNPY-EUR +6.52% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE
- XMN-EUR +6.16% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- PHA-EUR +6.08% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- LIGHTER-EUR +5.90% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE

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
