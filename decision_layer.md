# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-10-17T10:30:56.205972+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : aucun candidat matériel
- **MEILLEUR_LATENT_ACCELERATOR** : aucun candidat matériel
- **MEILLEUR_PULLBACK_REENTRY** : INJ-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 7.981 | entrée 6.750 | trend 8.900 | rang 7.707
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Tous les achats immédiats

Aucun ACHETE_MAINTENANT dans le classement complet.

## Top cross-sectionnel — aperçu non exhaustif

Ce top est une vue courte multi-buckets. Il ne doit jamais être utilisé comme liste exhaustive des achats immédiats.
1. INJ-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.707
2. METIS-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.359
3. KMNO-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.010

## Accélération indépendante

- ZRC-EUR — CONFIRMED_ACCELERATION — score 8.245/10 — DETECTED_BUT_TOO_LATE
- CPOOL-EUR — CONFIRMED_ACCELERATION — score 7.716/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- PROM-EUR — CONFIRMED_ACCELERATION — score 7.030/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- RARE-EUR — BUILDING_ACCELERATION — score 6.275/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- EPIC-EUR — MEMORY_24H — score mémoire 10.000/10 — sources ACCELERATION — MEMORY_ONLY
- AXL-EUR — MEMORY_24H — score mémoire 9.132/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- BTT-EUR — MEMORY_24H — score mémoire 8.833/10 — sources ACCELERATION — MEMORY_ONLY
- ZRC-EUR — ACTIVE_NOW — score mémoire 8.245/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- CPOOL-EUR — ACTIVE_NOW — score mémoire 7.716/10 — sources ACCELERATION — WATCH_ONLY
- INJ-EUR — ACTIVE_NOW — score mémoire 7.707/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- METIS-EUR — ACTIVE_NOW — score mémoire 7.359/10 — sources DECISION_LAYER, V4 — WATCH_ONLY
- EIGEN-EUR — MEMORY_24H — score mémoire 7.165/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- LAPTOP-EUR — MEMORY_24H — score mémoire 7.122/10 — sources ACCELERATION — MEMORY_ONLY
- STRAX-EUR — MEMORY_24H — score mémoire 7.054/10 — sources ACCELERATION — MEMORY_ONLY

## Audit des plus fortes hausses

- ICNT-EUR +43.03% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- EPIC-EUR +24.51% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- GTC-EUR +21.48% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- AVA-EUR +12.45% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- THQ-EUR +8.28% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- METIS-EUR +8.06% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE
- KMNO-EUR +7.92% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE
- ZRC-EUR +6.71% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- RECALL-EUR +6.33% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE
- SAND-EUR +6.20% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE

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
