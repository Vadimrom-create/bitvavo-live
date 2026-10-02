# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-10-02T14:09:46.227712+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : LTC-EUR | action ACHETE_MAINTENANT | opportunité 8.856 | entrée 7.650 | trend 6.600 | rang 7.375
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : C-EUR | action PLACE_LIMITE_PASSIVE | opportunité 7.766 | entrée 6.350 | trend 8.500 | rang 7.544
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : KSM-EUR | action LATENT_ACCELERATOR | opportunité 7.683 | entrée 5.650 | trend 8.700 | rang 7.528
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : DYDX-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.589 | entrée 5.350 | trend 8.950 | rang 8.042
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Tous les achats immédiats

1. LTC-EUR — ACHETE_MAINTENANT — rank 7.375 — opportunité 8.856 — entrée 7.650 — trend 6.600
2. EIGEN-EUR — ACHETE_MAINTENANT — rank 7.331 — opportunité 8.649 — entrée 7.300 — trend 6.800

## Top cross-sectionnel — aperçu non exhaustif

Ce top est une vue courte multi-buckets. Il ne doit jamais être utilisé comme liste exhaustive des achats immédiats.
1. DYDX-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.042
2. SYRUP-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.904
3. ZIG-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.891

## Accélération indépendante

- ZRC-EUR — CONFIRMED_ACCELERATION — score 8.500/10 — DETECTED_BUT_TOO_LATE
- C98-EUR — CONFIRMED_ACCELERATION — score 6.741/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- ARX-EUR — BUILDING_ACCELERATION — score 6.035/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- MAV-EUR — BUILDING_ACCELERATION — score 5.453/10 — DETECTED_BUT_TOO_LATE
- SYRUP-EUR — BUILDING_ACCELERATION — score 5.240/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- IMU-EUR — BUILDING_ACCELERATION — score 5.144/10 — DETECTED_BUT_TOO_LATE
- CELR-EUR — BUILDING_ACCELERATION — score 5.075/10 — DETECTED_BUT_TOO_LATE
- BAND-EUR — BUILDING_ACCELERATION — score 4.894/10 — DETECTED_BUT_TOO_LATE
- PHA-EUR — BUILDING_ACCELERATION — score 4.865/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- BIO-EUR — BUILDING_ACCELERATION — score 4.862/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- EDGE-EUR — MEMORY_24H — score mémoire 10.000/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- CAP-EUR — MEMORY_24H — score mémoire 9.289/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- TREAD-EUR — MEMORY_24H — score mémoire 9.258/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- PEOPLE-EUR — MEMORY_24H — score mémoire 9.036/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- AIOZ-EUR — MEMORY_24H — score mémoire 8.925/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- U-EUR — MEMORY_24H — score mémoire 8.740/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- ZRC-EUR — ACTIVE_NOW — score mémoire 8.500/10 — sources ACCELERATION, V4 — DETECTED_BUT_TOO_LATE
- OSMO-EUR — MEMORY_DECAY_24_72H — score mémoire 8.078/10 — sources ACCELERATION — MEMORY_ONLY
- DYDX-EUR — ACTIVE_NOW — score mémoire 8.042/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- SAND-EUR — MEMORY_24H — score mémoire 8.000/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY

## Audit des plus fortes hausses

- SAND-EUR +58.27% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- GTC-EUR +27.69% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- APE-EUR +20.74% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ENJ-EUR +18.43% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- MANA-EUR +17.74% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- GALA-EUR +17.41% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- NOS-EUR +17.20% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- SKY-EUR +16.52% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- ZRO-EUR +16.13% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- BAT-EUR +15.92% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE

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
