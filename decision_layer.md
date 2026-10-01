# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-10-01T16:40:16.159890+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : TRX-EUR | action ACHETE_MAINTENANT | opportunité 7.752 | entrée 7.200 | trend 4.000 | rang 6.053
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : DRIFT-EUR | action PLACE_LIMITE_PASSIVE | opportunité 9.118 | entrée 5.850 | trend 8.000 | rang 7.628
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : RED-EUR | action LATENT_ACCELERATOR | opportunité 8.228 | entrée 5.550 | trend 8.950 | rang 7.913
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : KAIA-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.488 | entrée 6.950 | trend 8.750 | rang 7.973
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Tous les achats immédiats

1. TRX-EUR — ACHETE_MAINTENANT — rank 6.053 — opportunité 7.752 — entrée 7.200 — trend 4.000

## Top cross-sectionnel — aperçu non exhaustif

Ce top est une vue courte multi-buckets. Il ne doit jamais être utilisé comme liste exhaustive des achats immédiats.
1. KAIA-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.973
2. RED-EUR — MEILLEUR_LATENT_ACCELERATOR — LATENT_ACCELERATOR — rank 7.913
3. PROM-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.849

## Accélération indépendante

- SWEAT-EUR — CONFIRMED_ACCELERATION — score 8.000/10 — DETECTED_BUT_TOO_LATE
- CAP-EUR — BUILDING_ACCELERATION — score 6.429/10 — DETECTED_BUT_TOO_LATE
- THQ-EUR — BUILDING_ACCELERATION — score 6.113/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- TRAC-EUR — BUILDING_ACCELERATION — score 5.693/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- O-EUR — BUILDING_ACCELERATION — score 5.526/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- MOVE-EUR — BUILDING_ACCELERATION — score 5.433/10 — DETECTED_BUT_TOO_LATE
- CTC-EUR — BUILDING_ACCELERATION — score 5.432/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- DRIFT-EUR — BUILDING_ACCELERATION — score 5.207/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- BEAM-EUR — BUILDING_ACCELERATION — score 4.978/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- LIGHTER-EUR — BUILDING_ACCELERATION — score 4.963/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- CPOOL-EUR — MEMORY_24H — score mémoire 10.000/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- MOVR-EUR — MEMORY_24H — score mémoire 10.000/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- TAI-EUR — MEMORY_24H — score mémoire 9.062/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- CT-EUR — MEMORY_24H — score mémoire 8.691/10 — sources ACCELERATION — MEMORY_ONLY
- ARPA-EUR — MEMORY_DECAY_24_72H — score mémoire 8.469/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- OSMO-EUR — MEMORY_24H — score mémoire 8.342/10 — sources ACCELERATION — MEMORY_ONLY
- SWEAT-EUR — ACTIVE_NOW — score mémoire 8.000/10 — sources ACCELERATION, V4 — DETECTED_BUT_TOO_LATE
- KAIA-EUR — ACTIVE_NOW — score mémoire 7.973/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- RED-EUR — ACTIVE_NOW — score mémoire 7.913/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- PROM-EUR — ACTIVE_NOW — score mémoire 7.849/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY

## Audit des plus fortes hausses

- SWEAT-EUR +135.26% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- MOVR-EUR +80.72% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- CAP-EUR +30.75% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- ALICE-EUR +23.33% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- NOS-EUR +21.24% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- CT-EUR +20.95% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- SYN-EUR +20.02% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- MEGA-EUR +19.92% — DETECTED_EARLY — couche NONE — action NONE
- MON-EUR +16.83% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- MOVE-EUR +14.16% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION

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
