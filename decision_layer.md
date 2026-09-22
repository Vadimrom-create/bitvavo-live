# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-22T12:31:37.345638+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : ZORA-EUR | action ACHETE_MAINTENANT | opportunité 8.530 | entrée 7.000 | trend 6.500 | rang 7.101
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : GOAT-EUR | action PLACE_LIMITE_PASSIVE | opportunité 7.555 | entrée 5.900 | trend 8.450 | rang 7.457
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : BAT-EUR | action LATENT_ACCELERATOR | opportunité 8.671 | entrée 5.350 | trend 7.950 | rang 7.716
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : FET-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.548 | entrée 7.800 | trend 8.400 | rang 7.844
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. FET-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.844
2. TAO-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.800
3. HYPE-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.766

## Accélération indépendante

- XMN-EUR — CONFIRMED_ACCELERATION — score 9.152/10 — DETECTED_BUT_TOO_LATE
- ZORA-EUR — BUILDING_ACCELERATION — score 6.243/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- WIF-EUR — BUILDING_ACCELERATION — score 5.973/10 — DETECTED_BUT_TOO_LATE
- PENGU-EUR — BUILDING_ACCELERATION — score 5.619/10 — DETECTED_BUT_TOO_LATE
- QNT-EUR — BUILDING_ACCELERATION — score 4.899/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- NIL-EUR — BUILDING_ACCELERATION — score 4.753/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- AUDIO-EUR — MEMORY_24H — score mémoire 9.640/10 — sources ACCELERATION — MEMORY_ONLY
- XMN-EUR — ACTIVE_NOW — score mémoire 9.152/10 — sources ACCELERATION — DETECTED_BUT_TOO_LATE
- SWEAT-EUR — MEMORY_24H — score mémoire 9.062/10 — sources ACCELERATION — MEMORY_ONLY
- BTT-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION — MEMORY_ONLY
- GIGA-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION — MEMORY_ONLY
- U-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- FET-EUR — ACTIVE_NOW — score mémoire 7.844/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- TAO-EUR — ACTIVE_NOW — score mémoire 7.800/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- HYPE-EUR — ACTIVE_NOW — score mémoire 7.766/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- SOL-EUR — ACTIVE_NOW — score mémoire 7.741/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY

## Audit des plus fortes hausses

- ICX-EUR +97.83% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- ZRC-EUR +78.69% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- XMN-EUR +36.36% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- KERNEL-EUR +29.15% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- NIL-EUR +24.54% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- AIOZ-EUR +22.60% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- FORM-EUR +21.31% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- WIF-EUR +19.99% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- GRASS-EUR +17.37% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- PEPE-EUR +16.57% — DETECTED_EARLY — couche NONE — action NONE

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
