# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-29T05:34:41.862088+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : ICP-EUR | action ACHETE_MAINTENANT | opportunité 8.145 | entrée 7.400 | trend 7.950 | rang 7.410
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : AZTEC-EUR | action PLACE_LIMITE_PASSIVE | opportunité 7.715 | entrée 6.200 | trend 8.400 | rang 7.432
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : MIOTA-EUR | action LATENT_ACCELERATOR | opportunité 7.764 | entrée 4.950 | trend 8.700 | rang 7.369
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : AERO-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.851 | entrée 6.950 | trend 7.900 | rang 7.833
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Tous les achats immédiats

1. ICP-EUR — ACHETE_MAINTENANT — rank 7.410 — opportunité 8.145 — entrée 7.400 — trend 7.950

## Top cross-sectionnel — aperçu non exhaustif

Ce top est une vue courte multi-buckets. Il ne doit jamais être utilisé comme liste exhaustive des achats immédiats.
1. AERO-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.833
2. SEI-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.747
3. LINK-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.727

## Accélération indépendante

- POND-EUR — CONFIRMED_ACCELERATION — score 9.183/10 — DETECTED_BUT_TOO_LATE
- TAI-EUR — CONFIRMED_ACCELERATION — score 6.806/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- PROVE-EUR — BUILDING_ACCELERATION — score 6.172/10 — DETECTED_BUT_TOO_LATE
- POPCAT-EUR — BUILDING_ACCELERATION — score 5.666/10 — DETECTED_BUT_TOO_LATE
- SIGN-EUR — BUILDING_ACCELERATION — score 5.629/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- NMR-EUR — BUILDING_ACCELERATION — score 5.450/10 — DETECTED_BUT_TOO_LATE
- PUMP-EUR — BUILDING_ACCELERATION — score 5.427/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- FLUID-EUR — BUILDING_ACCELERATION — score 5.303/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- O-EUR — BUILDING_ACCELERATION — score 5.237/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- RUNE-EUR — BUILDING_ACCELERATION — score 5.123/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- ICP-EUR — ACTIVE_NOW — score mémoire 7.410/10 — sources ACCELERATION, DECISION_LAYER, V4 — BUYABLE_NOW
- POND-EUR — ACTIVE_NOW — score mémoire 9.183/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- PUFFER-EUR — MEMORY_24H — score mémoire 9.062/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- ZRC-EUR — MEMORY_24H — score mémoire 9.000/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- ZEUS-EUR — MEMORY_24H — score mémoire 8.844/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- IMU-EUR — MEMORY_24H — score mémoire 8.632/10 — sources ACCELERATION — MEMORY_ONLY
- QUID-EUR — MEMORY_24H — score mémoire 8.100/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- OSMO-EUR — MEMORY_24H — score mémoire 7.990/10 — sources ACCELERATION — MEMORY_ONLY
- AERO-EUR — ACTIVE_NOW — score mémoire 7.833/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- U-EUR — MEMORY_24H — score mémoire 7.773/10 — sources ACCELERATION, V4 — MEMORY_ONLY

## Audit des plus fortes hausses

- NMR-EUR +38.90% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- HBAR-EUR +24.72% — DETECTED_EARLY — couche NONE — action NONE
- ALGO-EUR +18.12% — DETECTED_EARLY — couche NONE — action NONE
- CRV-EUR +18.06% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- 0G-EUR +17.01% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- POND-EUR +13.07% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- ARX-EUR +10.91% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- CELO-EUR +10.22% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- MIOTA-EUR +8.72% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- GRASS-EUR +8.57% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION

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
