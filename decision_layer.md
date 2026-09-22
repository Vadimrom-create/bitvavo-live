# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-22T09:28:05.823984+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : TAIKO-EUR | action ACHETE_MAINTENANT | opportunité 9.366 | entrée 7.100 | trend 8.700 | rang 8.495
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : KAS-EUR | action PLACE_LIMITE_PASSIVE | opportunité 8.582 | entrée 6.500 | trend 8.050 | rang 7.866
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : COW-EUR | action LATENT_ACCELERATOR | opportunité 7.506 | entrée 4.500 | trend 8.700 | rang 7.365
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : INIT-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 9.298 | entrée 6.350 | trend 8.600 | rang 8.252
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. TAIKO-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.495
2. INIT-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.252
3. WAL-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.957

## Accélération indépendante

- U-EUR — CONFIRMED_ACCELERATION — score 7.467/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- VELO-EUR — CONFIRMED_ACCELERATION — score 6.770/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- DATAIP-EUR — BUILDING_ACCELERATION — score 6.273/10 — DETECTED_BUT_TOO_LATE
- NIL-EUR — BUILDING_ACCELERATION — score 6.268/10 — DETECTED_BUT_TOO_LATE
- ICX-EUR — BUILDING_ACCELERATION — score 5.562/10 — DETECTED_BUT_TOO_LATE
- ALIGN-EUR — BUILDING_ACCELERATION — score 5.436/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- BREV-EUR — BUILDING_ACCELERATION — score 5.227/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- CNPY-EUR — BUILDING_ACCELERATION — score 5.032/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- SWEAT-EUR — MEMORY_24H — score mémoire 9.062/10 — sources ACCELERATION — MEMORY_ONLY
- XMN-EUR — MEMORY_24H — score mémoire 9.015/10 — sources ACCELERATION — MEMORY_ONLY
- GIGA-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION — MEMORY_ONLY
- TAIKO-EUR — ACTIVE_NOW — score mémoire 8.495/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- INIT-EUR — ACTIVE_NOW — score mémoire 8.252/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- PONKE-EUR — MEMORY_24H — score mémoire 8.130/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- WAL-EUR — ACTIVE_NOW — score mémoire 7.957/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- FET-EUR — ACTIVE_NOW — score mémoire 7.957/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- TREAD-EUR — MEMORY_24H — score mémoire 7.941/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- NEAR-EUR — ACTIVE_NOW — score mémoire 7.922/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE

## Audit des plus fortes hausses

- ICX-EUR +126.65% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- ZRC-EUR +96.58% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- AIOZ-EUR +44.13% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- KERNEL-EUR +37.38% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- GRASS-EUR +23.29% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- TREAD-EUR +23.18% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- WIF-EUR +19.85% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- PEPE-EUR +18.95% — DETECTED_EARLY — couche NONE — action NONE
- CARV-EUR +18.27% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- FORM-EUR +15.82% — DETECTED_EARLY — couche NONE — action INTERPRETATION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
