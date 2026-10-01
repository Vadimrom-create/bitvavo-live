# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-10-01T20:59:00.133317+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : AAVE-EUR | action ACHETE_MAINTENANT | opportunité 9.183 | entrée 7.650 | trend 9.200 | rang 8.609
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : MAGIC-EUR | action PLACE_LIMITE_PASSIVE | opportunité 7.610 | entrée 6.350 | trend 8.450 | rang 7.532
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : DIA-EUR | action LATENT_ACCELERATOR | opportunité 8.190 | entrée 5.000 | trend 9.000 | rang 7.800
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : STX-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.104 | entrée 6.050 | trend 9.200 | rang 7.952
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Tous les achats immédiats

1. AAVE-EUR — ACHETE_MAINTENANT — rank 8.609 — opportunité 9.183 — entrée 7.650 — trend 9.200
2. AVAX-EUR — ACHETE_MAINTENANT — rank 8.006 — opportunité 8.076 — entrée 8.100 — trend 8.700
3. WLD-EUR — ACHETE_MAINTENANT — rank 7.945 — opportunité 8.316 — entrée 7.100 — trend 8.650
4. SUI-EUR — ACHETE_MAINTENANT — rank 7.875 — opportunité 8.132 — entrée 7.650 — trend 8.400
5. PUMP-EUR — ACHETE_MAINTENANT — rank 7.730 — opportunité 8.092 — entrée 7.250 — trend 8.500
6. LTC-EUR — ACHETE_MAINTENANT — rank 6.914 — opportunité 7.895 — entrée 7.850 — trend 6.100

## Top cross-sectionnel — aperçu non exhaustif

Ce top est une vue courte multi-buckets. Il ne doit jamais être utilisé comme liste exhaustive des achats immédiats.
1. AAVE-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.609
2. AVAX-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.006
3. STX-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.952

## Accélération indépendante

- SWEAT-EUR — CONFIRMED_ACCELERATION — score 8.500/10 — DETECTED_BUT_TOO_LATE
- GIGA-EUR — CONFIRMED_ACCELERATION — score 6.704/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- ACH-EUR — BUILDING_ACCELERATION — score 6.331/10 — DETECTED_BUT_TOO_LATE
- TWT-EUR — BUILDING_ACCELERATION — score 5.173/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- GTC-EUR — BUILDING_ACCELERATION — score 4.980/10 — DETECTED_BUT_TOO_LATE
- ALIGN-EUR — BUILDING_ACCELERATION — score 4.922/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- CPOOL-EUR — MEMORY_24H — score mémoire 10.000/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- CT-EUR — MEMORY_24H — score mémoire 8.691/10 — sources ACCELERATION — MEMORY_ONLY
- AAVE-EUR — ACTIVE_NOW — score mémoire 8.609/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- CHILLGUY-EUR — MEMORY_24H — score mémoire 8.548/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- SWEAT-EUR — ACTIVE_NOW — score mémoire 8.500/10 — sources ACCELERATION, V4 — DETECTED_BUT_TOO_LATE
- OSMO-EUR — MEMORY_24H — score mémoire 8.342/10 — sources ACCELERATION — MEMORY_ONLY
- AGI-EUR — MEMORY_24H — score mémoire 8.119/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- AVAX-EUR — ACTIVE_NOW — score mémoire 8.006/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- U-EUR — MEMORY_24H — score mémoire 8.002/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- STX-EUR — ACTIVE_NOW — score mémoire 7.952/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY

## Audit des plus fortes hausses

- SWEAT-EUR +216.46% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- MOVR-EUR +48.52% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ALICE-EUR +39.87% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- GTC-EUR +37.08% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- CAP-EUR +24.43% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- MEGA-EUR +23.11% — DETECTED_EARLY — couche NONE — action NONE
- CT-EUR +19.45% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- NOS-EUR +19.17% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- SYN-EUR +18.59% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- MOVE-EUR +18.46% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION

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
