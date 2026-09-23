# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-23T16:54:05.448042+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : ZORA-EUR | action PLACE_LIMITE_PASSIVE | opportunité 7.768 | entrée 5.800 | trend 8.200 | rang 7.383
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : BEAM-EUR | action LATENT_ACCELERATOR | opportunité 7.603 | entrée 5.300 | trend 8.750 | rang 7.482
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : WAL-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.203 | entrée 6.500 | trend 8.650 | rang 7.904
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. WAL-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.904
2. ENS-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.606
3. BAT-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.582

## Accélération indépendante

- SOSO-EUR — CONFIRMED_ACCELERATION — score 9.254/10 — DETECTED_BUT_TOO_LATE
- GROVE-EUR — CONFIRMED_ACCELERATION — score 7.439/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- AGI-EUR — CONFIRMED_ACCELERATION — score 6.816/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- POWR-EUR — BUILDING_ACCELERATION — score 5.136/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- SOSO-EUR — ACTIVE_NOW — score mémoire 9.254/10 — sources ACCELERATION — DETECTED_BUT_TOO_LATE
- TRIA-EUR — MEMORY_24H — score mémoire 9.219/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- U-EUR — MEMORY_24H — score mémoire 9.175/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- WIN-EUR — MEMORY_24H — score mémoire 8.088/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- LINK-EUR — MEMORY_24H — score mémoire 8.056/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- XMN-EUR — MEMORY_24H — score mémoire 8.003/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- PORTAL-EUR — MEMORY_24H — score mémoire 7.969/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- WAL-EUR — ACTIVE_NOW — score mémoire 7.904/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- XRP-EUR — MEMORY_24H — score mémoire 7.855/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- MLN-EUR — MEMORY_24H — score mémoire 7.821/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY

## Audit des plus fortes hausses

- CPOOL-EUR +33.74% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- SAGA-EUR +29.81% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- NIL-EUR +20.22% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- DBR-EUR +18.21% — NOT_DETECTED — couche SCANNER_COVERAGE — action NOT_APPLICABLE
- MET-EUR +17.09% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- RAY-EUR +15.75% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- PROM-EUR +15.67% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- XMN-EUR +12.62% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- LIGHTER-EUR +11.14% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- SUPER-EUR +10.97% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
