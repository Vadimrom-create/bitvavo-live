# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-10-04T18:01:17.204119+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : PEAQ-EUR | action ACHETE_MAINTENANT | opportunité 9.008 | entrée 7.400 | trend 7.350 | rang 7.669
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : MAGIC-EUR | action PLACE_LIMITE_PASSIVE | opportunité 7.426 | entrée 5.800 | trend 8.650 | rang 7.315
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : GALA-EUR | action LATENT_ACCELERATOR | opportunité 7.451 | entrée 5.550 | trend 8.700 | rang 7.346
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : SKY-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.576 | entrée 6.700 | trend 8.950 | rang 7.969
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Tous les achats immédiats

1. PEAQ-EUR — ACHETE_MAINTENANT — rank 7.669 — opportunité 9.008 — entrée 7.400 — trend 7.350

## Top cross-sectionnel — aperçu non exhaustif

Ce top est une vue courte multi-buckets. Il ne doit jamais être utilisé comme liste exhaustive des achats immédiats.
1. SKY-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.969
2. AAVE-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.854
3. STX-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.834

## Accélération indépendante

- PHA-EUR — CONFIRMED_ACCELERATION — score 9.370/10 — DETECTED_BUT_TOO_LATE
- SWELL-EUR — CONFIRMED_ACCELERATION — score 9.171/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- HFT-EUR — CONFIRMED_ACCELERATION — score 8.166/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- LRC-EUR — CONFIRMED_ACCELERATION — score 7.425/10 — DETECTED_BUT_TOO_LATE
- GTC-EUR — CONFIRMED_ACCELERATION — score 6.715/10 — DETECTED_BUT_TOO_LATE
- MON-EUR — CONFIRMED_ACCELERATION — score 6.612/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- SCR-EUR — BUILDING_ACCELERATION — score 5.196/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- SOMI-EUR — BUILDING_ACCELERATION — score 4.829/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- PHA-EUR — ACTIVE_NOW — score mémoire 9.370/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- SWELL-EUR — ACTIVE_NOW — score mémoire 9.171/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- FIDA-EUR — MEMORY_24H — score mémoire 9.160/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- HAEDAL-EUR — MEMORY_24H — score mémoire 9.157/10 — sources ACCELERATION — MEMORY_ONLY
- HFT-EUR — ACTIVE_NOW — score mémoire 8.166/10 — sources ACCELERATION, DECISION_LAYER — WATCH_ONLY
- W-EUR — MEMORY_24H — score mémoire 8.059/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- SKY-EUR — ACTIVE_NOW — score mémoire 7.969/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- MAV-EUR — MEMORY_24H — score mémoire 7.946/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- AAVE-EUR — ACTIVE_NOW — score mémoire 7.854/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- STX-EUR — ACTIVE_NOW — score mémoire 7.834/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY

## Audit des plus fortes hausses

- GTC-EUR +28.44% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- EDGE-EUR +24.23% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- BEAM-EUR +22.95% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- AKT-EUR +16.04% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- NOS-EUR +15.29% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- AXS-EUR +12.79% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- POND-EUR +12.24% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- PHA-EUR +11.58% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- NOM-EUR +11.34% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- SENT-EUR +11.20% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE

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
