# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-10-16T09:41:01.764993+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : EDU-EUR | action PLACE_LIMITE_PASSIVE | opportunité 7.524 | entrée 6.400 | trend 8.950 | rang 7.299
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : aucun candidat matériel
- **MEILLEUR_PULLBACK_REENTRY** : PYTH-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 7.510 | entrée 6.350 | trend 8.500 | rang 7.234
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Tous les achats immédiats

Aucun ACHETE_MAINTENANT dans le classement complet.

## Top cross-sectionnel — aperçu non exhaustif

Ce top est une vue courte multi-buckets. Il ne doit jamais être utilisé comme liste exhaustive des achats immédiats.
1. EDU-EUR — MEILLEURE_LIMITE_PASSIVE — PLACE_LIMITE_PASSIVE — rank 7.299
2. PYTH-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.234
3. ZK-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.037

## Accélération indépendante

- XYO-EUR — BUILDING_ACCELERATION — score 5.551/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- RSR-EUR — BUILDING_ACCELERATION — score 4.833/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- GNS-EUR — MEMORY_24H — score mémoire 9.754/10 — sources ACCELERATION — MEMORY_ONLY
- ETHFI-EUR — MEMORY_24H — score mémoire 9.389/10 — sources ACCELERATION — MEMORY_ONLY
- BANANA-EUR — MEMORY_24H — score mémoire 9.000/10 — sources ACCELERATION — MEMORY_ONLY
- BREV-EUR — MEMORY_24H — score mémoire 9.000/10 — sources ACCELERATION — MEMORY_ONLY
- COW-EUR — MEMORY_24H — score mémoire 8.909/10 — sources ACCELERATION — MEMORY_ONLY
- ZRO-EUR — MEMORY_24H — score mémoire 8.832/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- MAGIC-EUR — MEMORY_DECAY_24_72H — score mémoire 8.588/10 — sources ACCELERATION — MEMORY_ONLY
- HOME-EUR — MEMORY_24H — score mémoire 8.559/10 — sources ACCELERATION — MEMORY_ONLY
- IRYS-EUR — MEMORY_24H — score mémoire 8.481/10 — sources ACCELERATION — MEMORY_ONLY
- BAT-EUR — MEMORY_24H — score mémoire 8.396/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY

## Audit des plus fortes hausses

- POND-EUR +29.22% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- TIA-EUR +27.65% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- INJ-EUR +25.56% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- ICNT-EUR +21.99% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- KMNO-EUR +19.24% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- ALIGN-EUR +18.81% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- ZRO-EUR +16.44% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- ETHFI-EUR +15.85% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- SOLV-EUR +15.84% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- ARB-EUR +14.14% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE

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
