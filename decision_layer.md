# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-23T10:59:11.171590+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : PYTH-EUR | action PLACE_LIMITE_PASSIVE | opportunité 7.783 | entrée 6.650 | trend 8.300 | rang 7.470
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : ARPA-EUR | action LATENT_ACCELERATOR | opportunité 8.025 | entrée 5.750 | trend 9.000 | rang 7.726
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : ROSE-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.804 | entrée 6.800 | trend 8.600 | rang 7.995
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. ROSE-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.995
2. ZBT-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.970
3. CAKE-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.948

## Accélération indépendante

- CSPR-EUR — CONFIRMED_ACCELERATION — score 6.772/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- U-EUR — CONFIRMED_ACCELERATION — score 6.738/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- EDGE-EUR — CONFIRMED_ACCELERATION — score 6.586/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- MET-EUR — BUILDING_ACCELERATION — score 6.059/10 — DETECTED_BUT_TOO_LATE
- CHR-EUR — BUILDING_ACCELERATION — score 5.828/10 — DETECTED_BUT_TOO_LATE
- G-EUR — BUILDING_ACCELERATION — score 5.664/10 — DETECTED_BUT_TOO_LATE
- ATH-EUR — BUILDING_ACCELERATION — score 5.065/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- TRIA-EUR — MEMORY_24H — score mémoire 9.219/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- ZRC-EUR — MEMORY_24H — score mémoire 9.216/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- NES-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- WIN-EUR — MEMORY_24H — score mémoire 8.088/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- LINK-EUR — MEMORY_24H — score mémoire 8.056/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- ROSE-EUR — ACTIVE_NOW — score mémoire 7.995/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- ZBT-EUR — ACTIVE_NOW — score mémoire 7.970/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- PORTAL-EUR — MEMORY_24H — score mémoire 7.969/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- CAKE-EUR — ACTIVE_NOW — score mémoire 7.948/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- LTC-EUR — ACTIVE_NOW — score mémoire 7.941/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY

## Audit des plus fortes hausses

- CPOOL-EUR +39.08% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- MET-EUR +37.79% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- BCH-EUR +30.68% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- CHR-EUR +30.35% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- ZRO-EUR +27.21% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- SUPER-EUR +26.48% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- NIL-EUR +23.32% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- TIA-EUR +22.87% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- ALLO-EUR +22.33% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- BONK-EUR +19.97% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
