# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-22T09:45:38.432939+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : NPC-EUR | action ACHETE_MAINTENANT | opportunité 8.793 | entrée 7.050 | trend 7.200 | rang 7.433
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : ARX-EUR | action PLACE_LIMITE_PASSIVE | opportunité 8.044 | entrée 5.850 | trend 8.850 | rang 7.580
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : COW-EUR | action LATENT_ACCELERATOR | opportunité 7.632 | entrée 5.750 | trend 8.700 | rang 7.573
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : TAIKO-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.428 | entrée 6.750 | trend 8.700 | rang 7.998
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. TAIKO-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.998
2. NEAR-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.853
3. INIT-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.808

## Accélération indépendante

- NIL-EUR — CONFIRMED_ACCELERATION — score 6.893/10 — DETECTED_BUT_TOO_LATE
- NPC-EUR — CONFIRMED_ACCELERATION — score 6.756/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- FLOCK-EUR — BUILDING_ACCELERATION — score 6.146/10 — DETECTED_BUT_TOO_LATE
- EGLD-EUR — BUILDING_ACCELERATION — score 5.436/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- PEAQ-EUR — BUILDING_ACCELERATION — score 4.844/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- NPC-EUR — ACTIVE_NOW — score mémoire 7.433/10 — sources ACCELERATION, DECISION_LAYER, V4 — BUYABLE_NOW
- WIF-EUR — ACTIVE_NOW — score mémoire 6.728/10 — sources ACCELERATION, DECISION_LAYER, V4 — BUYABLE_NOW
- SWEAT-EUR — MEMORY_24H — score mémoire 9.062/10 — sources ACCELERATION — MEMORY_ONLY
- XMN-EUR — MEMORY_24H — score mémoire 9.015/10 — sources ACCELERATION — MEMORY_ONLY
- GIGA-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION — MEMORY_ONLY
- PONKE-EUR — MEMORY_24H — score mémoire 8.130/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- TAIKO-EUR — ACTIVE_NOW — score mémoire 7.998/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- TREAD-EUR — MEMORY_24H — score mémoire 7.941/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- MERL-EUR — MEMORY_24H — score mémoire 7.909/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- NEAR-EUR — ACTIVE_NOW — score mémoire 7.853/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE

## Audit des plus fortes hausses

- ICX-EUR +101.11% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- ZRC-EUR +94.35% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- AIOZ-EUR +41.78% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- KERNEL-EUR +37.50% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- TREAD-EUR +23.41% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- WIF-EUR +21.71% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- GRASS-EUR +21.49% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- NIL-EUR +21.21% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- CARV-EUR +18.74% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- PEPE-EUR +18.47% — DETECTED_EARLY — couche NONE — action NONE

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
