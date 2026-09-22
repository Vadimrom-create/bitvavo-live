# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-22T05:14:17.149474+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : TAIKO-EUR | action ACHETE_MAINTENANT | opportunité 8.115 | entrée 7.100 | trend 8.700 | rang 7.913
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : COW-EUR | action PLACE_LIMITE_PASSIVE | opportunité 8.363 | entrée 6.000 | trend 8.500 | rang 7.862
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : ALGO-EUR | action LATENT_ACCELERATOR | opportunité 8.309 | entrée 5.750 | trend 7.800 | rang 7.560
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : MERL-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.296 | entrée 6.450 | trend 8.950 | rang 7.984
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. MERL-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.984
2. TAIKO-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 7.913
3. COW-EUR — MEILLEURE_LIMITE_PASSIVE — PLACE_LIMITE_PASSIVE — rank 7.862

## Accélération indépendante

- NIL-EUR — CONFIRMED_ACCELERATION — score 7.589/10 — DETECTED_BUT_TOO_LATE
- NEWT-EUR — CONFIRMED_ACCELERATION — score 7.584/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- EDGE-EUR — BUILDING_ACCELERATION — score 6.476/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- SWELL-EUR — BUILDING_ACCELERATION — score 6.088/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- COTI-EUR — BUILDING_ACCELERATION — score 5.875/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- NPC-EUR — BUILDING_ACCELERATION — score 5.693/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- CHILLGUY-EUR — BUILDING_ACCELERATION — score 5.614/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- ICX-EUR — BUILDING_ACCELERATION — score 5.500/10 — DETECTED_BUT_TOO_LATE
- ZORA-EUR — BUILDING_ACCELERATION — score 5.487/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- GRASS-EUR — BUILDING_ACCELERATION — score 5.262/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- ZRC-EUR — MEMORY_24H — score mémoire 9.953/10 — sources ACCELERATION — MEMORY_ONLY
- PHA-EUR — MEMORY_24H — score mémoire 9.177/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- BTT-EUR — MEMORY_24H — score mémoire 9.062/10 — sources ACCELERATION — MEMORY_ONLY
- SWEAT-EUR — MEMORY_24H — score mémoire 9.062/10 — sources ACCELERATION — MEMORY_ONLY
- VELO-EUR — MEMORY_24H — score mémoire 9.000/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- ZEUS-EUR — MEMORY_24H — score mémoire 8.781/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- DGB-EUR — MEMORY_24H — score mémoire 8.732/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- MEW-EUR — MEMORY_24H — score mémoire 8.523/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- XMN-EUR — MEMORY_24H — score mémoire 8.438/10 — sources ACCELERATION — MEMORY_ONLY
- MERL-EUR — ACTIVE_NOW — score mémoire 7.984/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY

## Audit des plus fortes hausses

- ZRC-EUR +114.12% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ICX-EUR +72.77% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- AIOZ-EUR +49.83% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- KERNEL-EUR +37.57% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- PHA-EUR +37.03% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- PEPE-EUR +25.60% — DETECTED_EARLY — couche NONE — action NONE
- GRASS-EUR +22.93% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- WIF-EUR +21.24% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- FORM-EUR +20.53% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- SWELL-EUR +19.31% — DETECTED_EARLY — couche NONE — action INTERPRETATION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
