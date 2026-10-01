# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-10-01T16:57:30.128045+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : TRX-EUR | action ACHETE_MAINTENANT | opportunité 8.166 | entrée 7.650 | trend 4.000 | rang 6.286
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : KITE-EUR | action PLACE_LIMITE_PASSIVE | opportunité 7.560 | entrée 5.850 | trend 8.450 | rang 7.417
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : DIA-EUR | action LATENT_ACCELERATOR | opportunité 8.206 | entrée 5.350 | trend 8.750 | rang 7.730
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : PROM-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.102 | entrée 6.950 | trend 8.950 | rang 7.994
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Tous les achats immédiats

1. TRX-EUR — ACHETE_MAINTENANT — rank 6.286 — opportunité 8.166 — entrée 7.650 — trend 4.000

## Top cross-sectionnel — aperçu non exhaustif

Ce top est une vue courte multi-buckets. Il ne doit jamais être utilisé comme liste exhaustive des achats immédiats.
1. PROM-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.994
2. STX-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.854
3. C-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.847

## Accélération indépendante

- AGI-EUR — CONFIRMED_ACCELERATION — score 8.119/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- FUN-EUR — BUILDING_ACCELERATION — score 6.121/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- MEGA-EUR — BUILDING_ACCELERATION — score 5.823/10 — DETECTED_BUT_TOO_LATE
- BEAM-EUR — BUILDING_ACCELERATION — score 5.444/10 — DETECTED_BUT_TOO_LATE
- INIT-EUR — BUILDING_ACCELERATION — score 4.891/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- CPOOL-EUR — MEMORY_24H — score mémoire 10.000/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- MOVR-EUR — MEMORY_24H — score mémoire 10.000/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- TAI-EUR — MEMORY_24H — score mémoire 9.062/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- CT-EUR — MEMORY_24H — score mémoire 8.691/10 — sources ACCELERATION — MEMORY_ONLY
- ARPA-EUR — MEMORY_DECAY_24_72H — score mémoire 8.417/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- OSMO-EUR — MEMORY_24H — score mémoire 8.342/10 — sources ACCELERATION — MEMORY_ONLY
- AGI-EUR — ACTIVE_NOW — score mémoire 8.119/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- SWEAT-EUR — MEMORY_24H — score mémoire 8.000/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- PROM-EUR — ACTIVE_NOW — score mémoire 7.994/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- STX-EUR — ACTIVE_NOW — score mémoire 7.854/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE

## Audit des plus fortes hausses

- SWEAT-EUR +135.69% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- MOVR-EUR +79.76% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- CAP-EUR +27.99% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- ALICE-EUR +26.00% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- MEGA-EUR +25.59% — DETECTED_EARLY — couche NONE — action NONE
- NOS-EUR +23.05% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- SYN-EUR +19.32% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- MON-EUR +16.82% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- MOVE-EUR +15.32% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- CT-EUR +15.18% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE

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
