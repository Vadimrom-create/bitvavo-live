# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-11-20T17:26:30.967999+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : aucun candidat matériel
- **MEILLEUR_LATENT_ACCELERATOR** : aucun candidat matériel
- **MEILLEUR_PULLBACK_REENTRY** : CROSS-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 6.609 | entrée 5.450 | trend 7.800 | rang 6.502
  - Trend remains strong; candidate retained for re-entry instead of discarded.

## Tous les achats immédiats

Aucun ACHETE_MAINTENANT dans le classement complet.

## Top cross-sectionnel — aperçu non exhaustif

Ce top est une vue courte multi-buckets. Il ne doit jamais être utilisé comme liste exhaustive des achats immédiats.
1. CROSS-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 6.502
2. CTR-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 6.412

## Accélération indépendante

- IRYS-EUR — BUILDING_ACCELERATION — score 5.287/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- MEGA-EUR — BUILDING_ACCELERATION — score 5.158/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- CT-EUR — BUILDING_ACCELERATION — score 4.985/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- KERNEL-EUR — BUILDING_ACCELERATION — score 4.935/10 — DETECTED_BUT_TOO_LATE
- AXIS-EUR — BUILDING_ACCELERATION — score 4.769/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- HUMA-EUR — MEMORY_24H — score mémoire 8.000/10 — sources ACCELERATION — MEMORY_ONLY
- CSPR-EUR — MEMORY_24H — score mémoire 7.456/10 — sources ACCELERATION — MEMORY_ONLY
- IKA-EUR — MEMORY_24H — score mémoire 7.094/10 — sources ACCELERATION — MEMORY_ONLY
- KITE-EUR — MEMORY_24H — score mémoire 7.083/10 — sources DECISION_LAYER, V4 — MEMORY_ONLY
- BOB-EUR — MEMORY_24H — score mémoire 7.070/10 — sources ACCELERATION — MEMORY_ONLY
- DYDX-EUR — MEMORY_24H — score mémoire 6.782/10 — sources ACCELERATION — MEMORY_ONLY
- TREAD-EUR — MEMORY_24H — score mémoire 6.641/10 — sources ACCELERATION — MEMORY_ONLY
- SKY-EUR — MEMORY_24H — score mémoire 6.623/10 — sources ACCELERATION — MEMORY_ONLY
- DODO-EUR — MEMORY_24H — score mémoire 6.577/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- CROSS-EUR — ACTIVE_NOW — score mémoire 6.502/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE

## Audit des plus fortes hausses

- KERNEL-EUR +30.31% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- RARE-EUR +15.88% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- CYBER-EUR +15.77% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- HUMA-EUR +14.86% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- ELSA-EUR +12.88% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- BLUR-EUR +12.87% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- SKY-EUR +10.70% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- INIT-EUR +5.59% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ZKJ-EUR +5.32% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- ENSO-EUR +5.07% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE

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
