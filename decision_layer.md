# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-18T16:54:28.556627+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : NPC-EUR | action PLACE_LIMITE_PASSIVE | opportunité 7.638 | entrée 6.750 | trend 7.750 | rang 6.990
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : S-EUR | action LATENT_ACCELERATOR | opportunité 7.505 | entrée 4.700 | trend 7.950 | rang 6.250
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : USELESS-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.629 | entrée 6.550 | trend 8.100 | rang 7.297
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. USELESS-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.297
2. SYRUP-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.268
3. NPC-EUR — MEILLEURE_LIMITE_PASSIVE — PLACE_LIMITE_PASSIVE — rank 6.990

## Accélération indépendante

- CNPY-EUR — CONFIRMED_ACCELERATION — score 8.500/10 — DETECTED_BUT_TOO_LATE
- TREAD-EUR — BUILDING_ACCELERATION — score 6.374/10 — REQUIRES_V4_ENTRY_AND_EXECUTION_VALIDATION
- LPT-EUR — BUILDING_ACCELERATION — score 5.594/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- CNPY-EUR — ACTIVE_NOW — score mémoire 8.500/10 — sources ACCELERATION, V4 — DETECTED_BUT_TOO_LATE
- LDO-EUR — ACTIVE_NOW — score mémoire 8.146/10 — sources V4 — WATCH_ONLY
- VTHO-EUR — ACTIVE_NOW — score mémoire 8.111/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- ZIG-EUR — MEMORY_24H — score mémoire 8.066/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- YB-EUR — ACTIVE_NOW — score mémoire 8.055/10 — sources V4 — WATCH_ONLY
- KAS-EUR — ACTIVE_NOW — score mémoire 8.002/10 — sources DECISION_LAYER, V4 — WATCH_ONLY
- XVG-EUR — ACTIVE_NOW — score mémoire 7.834/10 — sources V4 — WATCH_ONLY
- VET-EUR — ACTIVE_NOW — score mémoire 7.693/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- ENA-EUR — MEMORY_24H — score mémoire 7.668/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- DUSK-EUR — ACTIVE_NOW — score mémoire 7.665/10 — sources V4 — WATCH_ONLY

## Audit des plus fortes hausses

- G-EUR +84.97% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- CNPY-EUR +65.30% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- F-EUR +62.39% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- C-EUR +36.89% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- STRK-EUR +30.97% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ARB-EUR +24.64% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- NEAR-EUR +24.37% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- A-EUR +22.21% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- DRIFT-EUR +20.40% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- LPT-EUR +19.75% — DETECTED_EARLY — couche NONE — action INTERPRETATION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
