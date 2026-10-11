# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-10-11T16:46:48.543374+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : RAY-EUR | action ACHETE_MAINTENANT | opportunité 8.412 | entrée 7.150 | trend 8.650 | rang 7.371
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : PARTI-EUR | action PLACE_LIMITE_PASSIVE | opportunité 8.027 | entrée 6.100 | trend 8.600 | rang 7.379
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : ZK-EUR | action LATENT_ACCELERATOR | opportunité 7.630 | entrée 5.450 | trend 8.950 | rang 7.418
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : AVNT-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.032 | entrée 5.700 | trend 8.750 | rang 7.589
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Tous les achats immédiats

1. RAY-EUR — ACHETE_MAINTENANT — rank 7.371 — opportunité 8.412 — entrée 7.150 — trend 8.650

## Top cross-sectionnel — aperçu non exhaustif

Ce top est une vue courte multi-buckets. Il ne doit jamais être utilisé comme liste exhaustive des achats immédiats.
1. AVNT-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.589
2. AERO-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.438
3. ZK-EUR — MEILLEUR_LATENT_ACCELERATOR — LATENT_ACCELERATOR — rank 7.418

## Accélération indépendante

- MANTA-EUR — CONFIRMED_ACCELERATION — score 7.990/10 — DETECTED_BUT_TOO_LATE
- FET-EUR — CONFIRMED_ACCELERATION — score 7.244/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- ZBCN-EUR — CONFIRMED_ACCELERATION — score 6.676/10 — DETECTED_BUT_TOO_LATE
- UP-EUR — CONFIRMED_ACCELERATION — score 6.631/10 — DETECTED_BUT_TOO_LATE
- QUID-EUR — CONFIRMED_ACCELERATION — score 6.510/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- RAY-EUR — BUILDING_ACCELERATION — score 5.445/10 — DETECTED_BUT_TOO_LATE
- NPC-EUR — BUILDING_ACCELERATION — score 5.341/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- TRAC-EUR — BUILDING_ACCELERATION — score 5.151/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- S-EUR — BUILDING_ACCELERATION — score 5.033/10 — DETECTED_BUT_TOO_LATE
- CTC-EUR — BUILDING_ACCELERATION — score 4.992/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- TREAD-EUR — MEMORY_24H — score mémoire 8.918/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- GTC-EUR — MEMORY_DECAY_24_72H — score mémoire 8.826/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- IO-EUR — MEMORY_24H — score mémoire 8.545/10 — sources ACCELERATION — MEMORY_ONLY
- OSMO-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION — MEMORY_ONLY
- BEL-EUR — MEMORY_24H — score mémoire 8.196/10 — sources ACCELERATION — MEMORY_ONLY
- RON-EUR — MEMORY_24H — score mémoire 8.054/10 — sources ACCELERATION — MEMORY_ONLY
- MANTA-EUR — ACTIVE_NOW — score mémoire 7.990/10 — sources ACCELERATION — DETECTED_BUT_TOO_LATE
- LRC-EUR — MEMORY_24H — score mémoire 7.831/10 — sources ACCELERATION — MEMORY_ONLY
- AVNT-EUR — ACTIVE_NOW — score mémoire 7.589/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- AERO-EUR — ACTIVE_NOW — score mémoire 7.438/10 — sources DECISION_LAYER, V4 — WATCH_ONLY

## Audit des plus fortes hausses

- ZRC-EUR +89.32% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- S-EUR +40.23% — DETECTED_TOO_LATE — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- ZEUS-EUR +34.77% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- STRK-EUR +25.43% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- CHIP-EUR +24.94% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- MAGIC-EUR +21.57% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- GRASS-EUR +17.80% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- BAT-EUR +15.90% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- TIA-EUR +14.88% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- ROSE-EUR +12.97% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE

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
