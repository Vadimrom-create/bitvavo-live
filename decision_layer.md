# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-10-05T07:53:02.871756+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : SKY-EUR | action PLACE_LIMITE_PASSIVE | opportunité 7.722 | entrée 6.450 | trend 8.950 | rang 7.666
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : DEEP-EUR | action LATENT_ACCELERATOR | opportunité 7.722 | entrée 5.450 | trend 8.950 | rang 7.479
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : AXS-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.306 | entrée 6.300 | trend 8.650 | rang 7.811
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Tous les achats immédiats

Aucun ACHETE_MAINTENANT dans le classement complet.

## Top cross-sectionnel — aperçu non exhaustif

Ce top est une vue courte multi-buckets. Il ne doit jamais être utilisé comme liste exhaustive des achats immédiats.
1. AXS-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.811
2. BAT-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.668
3. SKY-EUR — MEILLEURE_LIMITE_PASSIVE — PLACE_LIMITE_PASSIVE — rank 7.666

## Accélération indépendante

- EDU-EUR — CONFIRMED_ACCELERATION — score 7.499/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- USELESS-EUR — CONFIRMED_ACCELERATION — score 7.317/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- ENA-EUR — CONFIRMED_ACCELERATION — score 6.627/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- DYDX-EUR — BUILDING_ACCELERATION — score 5.704/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- SCR-EUR — BUILDING_ACCELERATION — score 5.605/10 — DETECTED_BUT_TOO_LATE
- PHA-EUR — BUILDING_ACCELERATION — score 5.234/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- FET-EUR — BUILDING_ACCELERATION — score 5.116/10 — DETECTED_BUT_TOO_LATE
- STRK-EUR — BUILDING_ACCELERATION — score 4.898/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- SWELL-EUR — MEMORY_24H — score mémoire 9.171/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- FIDA-EUR — MEMORY_24H — score mémoire 9.160/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- HAEDAL-EUR — MEMORY_24H — score mémoire 9.157/10 — sources ACCELERATION — MEMORY_ONLY
- HNT-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- NIL-EUR — MEMORY_24H — score mémoire 8.392/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- PORTAL-EUR — MEMORY_24H — score mémoire 8.374/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- ZKP-EUR — MEMORY_24H — score mémoire 8.310/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- W-EUR — MEMORY_24H — score mémoire 8.059/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- MAV-EUR — MEMORY_24H — score mémoire 7.946/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- AXS-EUR — ACTIVE_NOW — score mémoire 7.811/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY

## Audit des plus fortes hausses

- GTC-EUR +78.74% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- SCR-EUR +18.16% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- CARV-EUR +17.55% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- FET-EUR +17.02% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- ADA-EUR +11.39% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ORCA-EUR +11.01% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- CHIP-EUR +10.52% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- VIRTUAL-EUR +10.50% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- NOS-EUR +10.02% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- NIL-EUR +9.94% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE

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
