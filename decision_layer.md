# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-30T15:37:33.419977+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : BLUR-EUR | action PLACE_LIMITE_PASSIVE | opportunité 8.550 | entrée 5.900 | trend 8.700 | rang 7.882
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : COMP-EUR | action LATENT_ACCELERATOR | opportunité 7.601 | entrée 5.500 | trend 9.000 | rang 7.636
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : KSM-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.342 | entrée 6.350 | trend 9.200 | rang 8.015
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Tous les achats immédiats

Aucun ACHETE_MAINTENANT dans le classement complet.

## Top cross-sectionnel — aperçu non exhaustif

Ce top est une vue courte multi-buckets. Il ne doit jamais être utilisé comme liste exhaustive des achats immédiats.
1. KSM-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.015
2. ICP-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.952
3. BLUR-EUR — MEILLEURE_LIMITE_PASSIVE — PLACE_LIMITE_PASSIVE — rank 7.882

## Accélération indépendante

- MOVR-EUR — CONFIRMED_ACCELERATION — score 8.615/10 — DETECTED_BUT_TOO_LATE
- TRAC-EUR — CONFIRMED_ACCELERATION — score 8.528/10 — DETECTED_BUT_TOO_LATE
- TAI-EUR — CONFIRMED_ACCELERATION — score 6.947/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- LIGHTER-EUR — CONFIRMED_ACCELERATION — score 6.807/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- UP-EUR — CONFIRMED_ACCELERATION — score 6.742/10 — DETECTED_BUT_TOO_LATE
- REZ-EUR — BUILDING_ACCELERATION — score 6.095/10 — DETECTED_BUT_TOO_LATE
- SOON-EUR — BUILDING_ACCELERATION — score 5.373/10 — DETECTED_BUT_TOO_LATE
- DUSK-EUR — BUILDING_ACCELERATION — score 5.343/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- ACE-EUR — BUILDING_ACCELERATION — score 4.890/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- EDGE-EUR — MEMORY_24H — score mémoire 9.861/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- NOM-EUR — MEMORY_24H — score mémoire 9.770/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- BTT-EUR — MEMORY_24H — score mémoire 9.062/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- CTR-EUR — MEMORY_24H — score mémoire 8.902/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- DGB-EUR — MEMORY_24H — score mémoire 8.670/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- MOVR-EUR — ACTIVE_NOW — score mémoire 8.615/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- CVC-EUR — MEMORY_24H — score mémoire 8.565/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- TRAC-EUR — ACTIVE_NOW — score mémoire 8.528/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- LRC-EUR — MEMORY_24H — score mémoire 8.342/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- ARK-EUR — MEMORY_24H — score mémoire 8.293/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY

## Audit des plus fortes hausses

- MOVR-EUR +67.91% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- SOON-EUR +44.98% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- CT-EUR +40.36% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- ARK-EUR +25.13% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- NOM-EUR +20.56% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- QNT-EUR +19.46% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- GLMR-EUR +16.19% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- NIL-EUR +16.08% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- EPIC-EUR +14.58% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE
- PROM-EUR +13.22% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE

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
