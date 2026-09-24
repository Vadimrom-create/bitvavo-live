# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-24T10:23:10.178051+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : QNT-EUR | action ACHETE_MAINTENANT | opportunité 9.105 | entrée 7.200 | trend 7.750 | rang 8.076
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : APT-EUR | action PLACE_LIMITE_PASSIVE | opportunité 8.712 | entrée 5.800 | trend 7.550 | rang 7.481
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : EDEN-EUR | action LATENT_ACCELERATOR | opportunité 7.625 | entrée 5.400 | trend 8.200 | rang 7.261
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : ETC-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.319 | entrée 7.400 | trend 8.700 | rang 8.087
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. ETC-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.087
2. QNT-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.076
3. LTC-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.976

## Accélération indépendante

- BTT-EUR — CONFIRMED_ACCELERATION — score 8.485/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- ZBCN-EUR — CONFIRMED_ACCELERATION — score 6.588/10 — DETECTED_BUT_TOO_LATE
- GWEI-EUR — CONFIRMED_ACCELERATION — score 6.576/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- ICX-EUR — CONFIRMED_ACCELERATION — score 6.500/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- PUFFER-EUR — BUILDING_ACCELERATION — score 5.993/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- IMU-EUR — MEMORY_24H — score mémoire 9.725/10 — sources ACCELERATION — MEMORY_ONLY
- ZRC-EUR — MEMORY_24H — score mémoire 9.712/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- PEAQ-EUR — MEMORY_24H — score mémoire 9.627/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- PROM-EUR — MEMORY_24H — score mémoire 9.255/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- U-EUR — MEMORY_24H — score mémoire 9.175/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- PEOPLE-EUR — MEMORY_24H — score mémoire 8.917/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- CNPY-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- FLOCK-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- BTT-EUR — ACTIVE_NOW — score mémoire 8.485/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- C98-EUR — MEMORY_24H — score mémoire 8.347/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY

## Audit des plus fortes hausses

- NIL-EUR +45.63% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- NOM-EUR +38.50% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- LSK-EUR +20.36% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- IMU-EUR +19.75% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- ARX-EUR +13.24% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- CNPY-EUR +11.97% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- SOSO-EUR +10.34% — NOT_DETECTED — couche SCANNER_COVERAGE — action NOT_APPLICABLE
- CVC-EUR +8.17% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- LTC-EUR +7.20% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- PLUME-EUR +6.43% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
