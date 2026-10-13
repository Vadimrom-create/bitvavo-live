# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-10-13T17:13:11.626768+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : AZTEC-EUR | action PLACE_LIMITE_PASSIVE | opportunité 7.421 | entrée 6.650 | trend 8.650 | rang 7.180
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : aucun candidat matériel
- **MEILLEUR_PULLBACK_REENTRY** : STX-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 7.932 | entrée 6.850 | trend 8.900 | rang 7.434
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Tous les achats immédiats

Aucun ACHETE_MAINTENANT dans le classement complet.

## Top cross-sectionnel — aperçu non exhaustif

Ce top est une vue courte multi-buckets. Il ne doit jamais être utilisé comme liste exhaustive des achats immédiats.
1. STX-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.434
2. AZTEC-EUR — MEILLEURE_LIMITE_PASSIVE — PLACE_LIMITE_PASSIVE — rank 7.180
3. DUSK-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.056

## Accélération indépendante

- ATH-EUR — CONFIRMED_ACCELERATION — score 9.087/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- ZRC-EUR — CONFIRMED_ACCELERATION — score 7.892/10 — DETECTED_BUT_TOO_LATE
- GNS-EUR — CONFIRMED_ACCELERATION — score 7.867/10 — DETECTED_BUT_TOO_LATE
- TRAC-EUR — BUILDING_ACCELERATION — score 4.829/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- ATH-EUR — ACTIVE_NOW — score mémoire 9.087/10 — sources ACCELERATION — WATCH_ONLY
- STRK-EUR — MEMORY_24H — score mémoire 8.881/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- AMP-EUR — MEMORY_24H — score mémoire 8.417/10 — sources ACCELERATION, DECISION_LAYER — MEMORY_ONLY
- RAD-EUR — MEMORY_DECAY_24_72H — score mémoire 8.300/10 — sources ACCELERATION, DECISION_LAYER — MEMORY_ONLY
- ZRC-EUR — ACTIVE_NOW — score mémoire 7.892/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- CTR-EUR — MEMORY_24H — score mémoire 7.878/10 — sources ACCELERATION — MEMORY_ONLY
- GNS-EUR — ACTIVE_NOW — score mémoire 7.867/10 — sources ACCELERATION — DETECTED_BUT_TOO_LATE
- REQ-EUR — MEMORY_24H — score mémoire 7.776/10 — sources ACCELERATION — MEMORY_ONLY
- GRASS-EUR — MEMORY_24H — score mémoire 7.726/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- PROM-EUR — MEMORY_24H — score mémoire 7.577/10 — sources ACCELERATION — MEMORY_ONLY

## Audit des plus fortes hausses

- GNS-EUR +106.37% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- BAT-EUR +27.00% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- ZRC-EUR +25.04% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- AMP-EUR +19.43% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- DUSK-EUR +12.00% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- CTR-EUR +10.78% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- AZTEC-EUR +9.54% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- CNPY-EUR +7.87% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- SYN-EUR +7.80% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- FTT-EUR +7.49% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE

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
