# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-22T06:30:30.746742+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : INIT-EUR | action PLACE_LIMITE_PASSIVE | opportunité 8.012 | entrée 6.000 | trend 9.200 | rang 7.879
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : ZIL-EUR | action LATENT_ACCELERATOR | opportunité 7.628 | entrée 5.600 | trend 8.100 | rang 6.953
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : THE-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 9.067 | entrée 6.750 | trend 8.700 | rang 8.216
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. THE-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.216
2. SOL-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.904
3. INIT-EUR — MEILLEURE_LIMITE_PASSIVE — PLACE_LIMITE_PASSIVE — rank 7.879

## Accélération indépendante

- MLN-EUR — CONFIRMED_ACCELERATION — score 10.000/10 — DETECTED_BUT_TOO_LATE
- NIL-EUR — CONFIRMED_ACCELERATION — score 7.780/10 — DETECTED_BUT_TOO_LATE
- ICX-EUR — BUILDING_ACCELERATION — score 6.354/10 — DETECTED_BUT_TOO_LATE
- QKC-EUR — BUILDING_ACCELERATION — score 6.022/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- TOSHI-EUR — BUILDING_ACCELERATION — score 5.954/10 — DETECTED_BUT_TOO_LATE
- ZIL-EUR — BUILDING_ACCELERATION — score 5.317/10 — DETECTED_BUT_TOO_LATE
- KITE-EUR — BUILDING_ACCELERATION — score 5.109/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- DYM-EUR — BUILDING_ACCELERATION — score 4.921/10 — DETECTED_BUT_TOO_LATE
- GROVE-EUR — BUILDING_ACCELERATION — score 4.878/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- MLN-EUR — ACTIVE_NOW — score mémoire 10.000/10 — sources ACCELERATION, V4 — DETECTED_BUT_TOO_LATE
- SAGA-EUR — MEMORY_24H — score mémoire 9.632/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- PHA-EUR — MEMORY_24H — score mémoire 9.177/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- GIGA-EUR — MEMORY_24H — score mémoire 9.062/10 — sources ACCELERATION — MEMORY_ONLY
- SWEAT-EUR — MEMORY_24H — score mémoire 9.062/10 — sources ACCELERATION — MEMORY_ONLY
- VELO-EUR — MEMORY_24H — score mémoire 9.000/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- ZEUS-EUR — MEMORY_24H — score mémoire 8.781/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- MEW-EUR — MEMORY_24H — score mémoire 8.523/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- ZRC-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION — MEMORY_ONLY
- XMN-EUR — MEMORY_24H — score mémoire 8.438/10 — sources ACCELERATION — MEMORY_ONLY

## Audit des plus fortes hausses

- ZRC-EUR +110.98% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ICX-EUR +107.06% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- AIOZ-EUR +54.80% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- KERNEL-EUR +29.28% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- PEPE-EUR +25.58% — DETECTED_EARLY — couche NONE — action NONE
- SAGA-EUR +23.99% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- WIF-EUR +20.09% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- FORM-EUR +19.55% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- GRASS-EUR +19.36% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- BONK-EUR +18.54% — DETECTED_TOO_LATE — couche NONE — action INTERPRETATION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
