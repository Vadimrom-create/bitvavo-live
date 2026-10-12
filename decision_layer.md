# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-10-12T18:21:09.035961+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : BEAM-EUR | action PLACE_LIMITE_PASSIVE | opportunité 7.432 | entrée 6.200 | trend 8.000 | rang 6.786
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : AXL-EUR | action LATENT_ACCELERATOR | opportunité 7.571 | entrée 5.700 | trend 8.150 | rang 6.962
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : TIA-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 7.538 | entrée 6.450 | trend 8.500 | rang 7.481
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Tous les achats immédiats

Aucun ACHETE_MAINTENANT dans le classement complet.

## Top cross-sectionnel — aperçu non exhaustif

Ce top est une vue courte multi-buckets. Il ne doit jamais être utilisé comme liste exhaustive des achats immédiats.
1. TIA-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.481
2. ZK-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.340
3. PARTI-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.083

## Accélération indépendante

- OSMO-EUR — CONFIRMED_ACCELERATION — score 8.696/10 — DETECTED_BUT_TOO_LATE
- REQ-EUR — CONFIRMED_ACCELERATION — score 7.776/10 — DETECTED_BUT_TOO_LATE
- DODO-EUR — CONFIRMED_ACCELERATION — score 6.818/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- TAI-EUR — BUILDING_ACCELERATION — score 6.469/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- LINEA-EUR — BUILDING_ACCELERATION — score 6.243/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- BEAM-EUR — BUILDING_ACCELERATION — score 5.837/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- PIXEL-EUR — BUILDING_ACCELERATION — score 5.674/10 — DETECTED_BUT_TOO_LATE
- AVA-EUR — BUILDING_ACCELERATION — score 5.423/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- SOON-EUR — BUILDING_ACCELERATION — score 5.386/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- ATOM-EUR — BUILDING_ACCELERATION — score 5.091/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- RAD-EUR — MEMORY_24H — score mémoire 9.000/10 — sources ACCELERATION, DECISION_LAYER — MEMORY_ONLY
- STRK-EUR — MEMORY_24H — score mémoire 8.881/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- OSMO-EUR — ACTIVE_NOW — score mémoire 8.696/10 — sources ACCELERATION — DETECTED_BUT_TOO_LATE
- DBR-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION — MEMORY_ONLY
- SXT-EUR — MEMORY_24H — score mémoire 8.267/10 — sources ACCELERATION — MEMORY_ONLY
- CTR-EUR — MEMORY_24H — score mémoire 7.878/10 — sources ACCELERATION — MEMORY_ONLY
- REQ-EUR — ACTIVE_NOW — score mémoire 7.776/10 — sources ACCELERATION — DETECTED_BUT_TOO_LATE
- GRASS-EUR — MEMORY_24H — score mémoire 7.726/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- EDU-EUR — ACTIVE_NOW — score mémoire 7.614/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- RAY-EUR — MEMORY_24H — score mémoire 7.600/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY

## Audit des plus fortes hausses

- GTC-EUR +75.74% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- OSMO-EUR +41.54% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- RSR-EUR +39.50% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- CTK-EUR +16.04% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- OGN-EUR +13.82% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- SAFE-EUR +12.71% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- SKL-EUR +11.85% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- W-EUR +11.37% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- PYTH-EUR +9.77% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- AVA-EUR +8.13% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE

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
