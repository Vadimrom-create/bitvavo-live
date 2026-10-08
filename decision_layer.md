# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-10-08T22:22:15.707340+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : AVNT-EUR | action PLACE_LIMITE_PASSIVE | opportunité 7.507 | entrée 6.550 | trend 8.000 | rang 7.261
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : aucun candidat matériel
- **MEILLEUR_PULLBACK_REENTRY** : W-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.103 | entrée 5.900 | trend 8.650 | rang 7.789
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Tous les achats immédiats

Aucun ACHETE_MAINTENANT dans le classement complet.

## Top cross-sectionnel — aperçu non exhaustif

Ce top est une vue courte multi-buckets. Il ne doit jamais être utilisé comme liste exhaustive des achats immédiats.
1. W-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.789
2. NMR-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.729
3. MAGIC-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.553

## Accélération indépendante

- GNS-EUR — CONFIRMED_ACCELERATION — score 8.425/10 — DETECTED_BUT_TOO_LATE
- SXT-EUR — CONFIRMED_ACCELERATION — score 8.096/10 — DETECTED_BUT_TOO_LATE
- OGN-EUR — BUILDING_ACCELERATION — score 5.642/10 — DETECTED_BUT_TOO_LATE
- AUDIO-EUR — BUILDING_ACCELERATION — score 5.197/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- ORCA-EUR — BUILDING_ACCELERATION — score 4.939/10 — DETECTED_BUT_TOO_LATE
- SCR-EUR — BUILDING_ACCELERATION — score 4.931/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- INIT-EUR — BUILDING_ACCELERATION — score 4.856/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- RLC-EUR — MEMORY_24H — score mémoire 10.000/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- AMP-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION — MEMORY_ONLY
- GNS-EUR — ACTIVE_NOW — score mémoire 8.425/10 — sources ACCELERATION, V4 — DETECTED_BUT_TOO_LATE
- GTC-EUR — MEMORY_24H — score mémoire 8.274/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- SXT-EUR — ACTIVE_NOW — score mémoire 8.096/10 — sources ACCELERATION — DETECTED_BUT_TOO_LATE
- QUID-EUR — MEMORY_24H — score mémoire 7.798/10 — sources ACCELERATION — MEMORY_ONLY
- W-EUR — ACTIVE_NOW — score mémoire 7.789/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- NMR-EUR — ACTIVE_NOW — score mémoire 7.729/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- SWELL-EUR — MEMORY_DECAY_24_72H — score mémoire 7.596/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- MAGIC-EUR — ACTIVE_NOW — score mémoire 7.553/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY

## Audit des plus fortes hausses

- OGN-EUR +109.86% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- ZRC-EUR +65.08% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- RLC-EUR +29.48% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- DRV-EUR +19.25% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- AMP-EUR +18.88% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- SKL-EUR +17.71% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- PYTH-EUR +15.46% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- STRK-EUR +14.40% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- SOSO-EUR +12.45% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- TIA-EUR +12.41% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE

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
