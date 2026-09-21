# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-21T02:32:26.543629+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : W-EUR | action PLACE_LIMITE_PASSIVE | opportunité 7.835 | entrée 6.100 | trend 8.500 | rang 7.636
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : MERL-EUR | action LATENT_ACCELERATOR | opportunité 8.189 | entrée 5.450 | trend 8.900 | rang 7.830
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : HEI-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 9.245 | entrée 6.950 | trend 8.100 | rang 8.195
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. HEI-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.195
2. CAKE-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.831
3. MERL-EUR — MEILLEUR_LATENT_ACCELERATOR — LATENT_ACCELERATOR — rank 7.830

## Accélération indépendante

- VVV-EUR — CONFIRMED_ACCELERATION — score 9.651/10 — DETECTED_BUT_TOO_LATE
- TREAD-EUR — CONFIRMED_ACCELERATION — score 9.590/10 — DETECTED_BUT_TOO_LATE
- CROSS-EUR — CONFIRMED_ACCELERATION — score 9.442/10 — DETECTED_BUT_TOO_LATE
- FOLD-EUR — CONFIRMED_ACCELERATION — score 7.106/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- PEAQ-EUR — CONFIRMED_ACCELERATION — score 6.974/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- PUFFER-EUR — CONFIRMED_ACCELERATION — score 6.574/10 — DETECTED_BUT_TOO_LATE
- REQ-EUR — BUILDING_ACCELERATION — score 5.728/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- ARB-EUR — BUILDING_ACCELERATION — score 5.685/10 — DETECTED_BUT_TOO_LATE
- BONK-EUR — BUILDING_ACCELERATION — score 5.247/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- MMT-EUR — BUILDING_ACCELERATION — score 5.048/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- VVV-EUR — ACTIVE_NOW — score mémoire 9.651/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- TREAD-EUR — ACTIVE_NOW — score mémoire 9.590/10 — sources ACCELERATION, V4 — DETECTED_BUT_TOO_LATE
- CROSS-EUR — ACTIVE_NOW — score mémoire 9.442/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- ICX-EUR — MEMORY_24H — score mémoire 9.062/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- NES-EUR — MEMORY_24H — score mémoire 8.883/10 — sources ACCELERATION — MEMORY_ONLY
- LSK-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- U-EUR — MEMORY_24H — score mémoire 8.376/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- HEI-EUR — ACTIVE_NOW — score mémoire 8.195/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- UP-EUR — MEMORY_24H — score mémoire 8.113/10 — sources ACCELERATION — MEMORY_ONLY
- CAKE-EUR — ACTIVE_NOW — score mémoire 7.831/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY

## Audit des plus fortes hausses

- PTB-EUR +75.40% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- SAGA-EUR +35.23% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- FTT-EUR +29.51% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- EPIC-EUR +23.24% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- NIL-EUR +23.04% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- VVV-EUR +22.57% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- KMNO-EUR +18.88% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- NEAR-EUR +18.62% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- TREAD-EUR +18.25% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- PEAQ-EUR +16.64% — DETECTED_EARLY — couche NONE — action INTERPRETATION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
