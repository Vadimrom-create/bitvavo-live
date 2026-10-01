# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-10-01T16:22:18.742308+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : AAVE-EUR | action ACHETE_MAINTENANT | opportunité 8.030 | entrée 7.050 | trend 8.700 | rang 7.865
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : SKY-EUR | action PLACE_LIMITE_PASSIVE | opportunité 8.043 | entrée 6.300 | trend 7.350 | rang 7.061
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : KSM-EUR | action LATENT_ACCELERATOR | opportunité 8.277 | entrée 5.650 | trend 9.200 | rang 7.939
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : KAIA-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.428 | entrée 6.650 | trend 8.750 | rang 7.864
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Tous les achats immédiats

1. AAVE-EUR — ACHETE_MAINTENANT — rank 7.865 — opportunité 8.030 — entrée 7.050 — trend 8.700
2. ZIG-EUR — ACHETE_MAINTENANT — rank 7.808 — opportunité 8.288 — entrée 7.400 — trend 8.500
3. TRX-EUR — ACHETE_MAINTENANT — rank 6.212 — opportunité 8.315 — entrée 7.500 — trend 4.000

## Top cross-sectionnel — aperçu non exhaustif

Ce top est une vue courte multi-buckets. Il ne doit jamais être utilisé comme liste exhaustive des achats immédiats.
1. KSM-EUR — MEILLEUR_LATENT_ACCELERATOR — LATENT_ACCELERATOR — rank 7.939
2. AAVE-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 7.865
3. KAIA-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.864

## Accélération indépendante

- MOVR-EUR — CONFIRMED_ACCELERATION — score 10.000/10 — DETECTED_BUT_TOO_LATE
- TAI-EUR — CONFIRMED_ACCELERATION — score 9.062/10 — DETECTED_BUT_TOO_LATE
- ENSO-EUR — CONFIRMED_ACCELERATION — score 7.743/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- GIGA-EUR — CONFIRMED_ACCELERATION — score 6.560/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- ZRO-EUR — BUILDING_ACCELERATION — score 5.872/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- ENJ-EUR — BUILDING_ACCELERATION — score 5.752/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- SLX-EUR — BUILDING_ACCELERATION — score 5.135/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- ZRC-EUR — BUILDING_ACCELERATION — score 5.120/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- SPX-EUR — BUILDING_ACCELERATION — score 5.069/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- REQ-EUR — BUILDING_ACCELERATION — score 4.939/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- CPOOL-EUR — MEMORY_24H — score mémoire 10.000/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- MOVR-EUR — ACTIVE_NOW — score mémoire 10.000/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- TAI-EUR — ACTIVE_NOW — score mémoire 9.062/10 — sources ACCELERATION, V4 — DETECTED_BUT_TOO_LATE
- CT-EUR — MEMORY_24H — score mémoire 8.691/10 — sources ACCELERATION — MEMORY_ONLY
- ARPA-EUR — MEMORY_DECAY_24_72H — score mémoire 8.522/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- OSMO-EUR — MEMORY_24H — score mémoire 8.342/10 — sources ACCELERATION — MEMORY_ONLY
- KSM-EUR — ACTIVE_NOW — score mémoire 7.939/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- AAVE-EUR — ACTIVE_NOW — score mémoire 7.865/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- KAIA-EUR — ACTIVE_NOW — score mémoire 7.864/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- ZRO-EUR — ACTIVE_NOW — score mémoire 7.835/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY

## Audit des plus fortes hausses

- SWEAT-EUR +118.32% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- MOVR-EUR +86.18% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- CAP-EUR +28.39% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- ALICE-EUR +24.40% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- CT-EUR +24.21% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- NOS-EUR +20.64% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- MEGA-EUR +20.28% — DETECTED_EARLY — couche NONE — action NONE
- SYN-EUR +19.44% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- MON-EUR +18.48% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- NOM-EUR +14.18% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION

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
