# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-10-17T17:00:49.364660+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : RSR-EUR | action PLACE_LIMITE_PASSIVE | opportunité 7.589 | entrée 6.500 | trend 8.000 | rang 7.211
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : aucun candidat matériel
- **MEILLEUR_PULLBACK_REENTRY** : INJ-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 7.545 | entrée 6.100 | trend 8.450 | rang 7.304
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Tous les achats immédiats

Aucun ACHETE_MAINTENANT dans le classement complet.

## Top cross-sectionnel — aperçu non exhaustif

Ce top est une vue courte multi-buckets. Il ne doit jamais être utilisé comme liste exhaustive des achats immédiats.
1. INJ-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.304
2. RSR-EUR — MEILLEURE_LIMITE_PASSIVE — PLACE_LIMITE_PASSIVE — rank 7.211
3. DUSK-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 6.998

## Accélération indépendante

- ICNT-EUR — CONFIRMED_ACCELERATION — score 7.720/10 — DETECTED_BUT_TOO_LATE
- ALT-EUR — BUILDING_ACCELERATION — score 5.193/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- EPIC-EUR — MEMORY_24H — score mémoire 10.000/10 — sources ACCELERATION — MEMORY_ONLY
- AXL-EUR — MEMORY_24H — score mémoire 9.132/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- BTT-EUR — MEMORY_24H — score mémoire 8.833/10 — sources ACCELERATION — MEMORY_ONLY
- ZRC-EUR — MEMORY_24H — score mémoire 8.245/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- GTC-EUR — MEMORY_24H — score mémoire 7.849/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- ICNT-EUR — ACTIVE_NOW — score mémoire 7.720/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- CPOOL-EUR — MEMORY_24H — score mémoire 7.716/10 — sources ACCELERATION — MEMORY_ONLY
- U-EUR — MEMORY_24H — score mémoire 7.667/10 — sources ACCELERATION — MEMORY_ONLY
- METIS-EUR — MEMORY_24H — score mémoire 7.359/10 — sources DECISION_LAYER, V4 — MEMORY_ONLY
- INJ-EUR — ACTIVE_NOW — score mémoire 7.304/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY

## Audit des plus fortes hausses

- EPIC-EUR +33.57% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- AVA-EUR +30.35% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- ICNT-EUR +28.47% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- BTT-EUR +14.16% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- SAND-EUR +12.74% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- GTC-EUR +12.32% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- ZEUS-EUR +10.49% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- LAPTOP-EUR +6.50% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- REQ-EUR +6.27% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- NMR-EUR +6.27% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE

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
