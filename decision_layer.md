# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-22T22:10:48.895529+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : 0G-EUR | action PLACE_LIMITE_PASSIVE | opportunité 8.004 | entrée 6.000 | trend 8.600 | rang 7.682
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : LISTA-EUR | action LATENT_ACCELERATOR | opportunité 7.693 | entrée 5.300 | trend 8.500 | rang 7.472
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : AVAX-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.916 | entrée 7.850 | trend 7.950 | rang 7.856
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. AVAX-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.856
2. ANIME-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.830
3. THE-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.806

## Accélération indépendante

- LMWR-EUR — CONFIRMED_ACCELERATION — score 8.748/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- BTT-EUR — CONFIRMED_ACCELERATION — score 8.062/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- FARTCOIN-EUR — CONFIRMED_ACCELERATION — score 7.360/10 — DETECTED_BUT_TOO_LATE
- POND-EUR — CONFIRMED_ACCELERATION — score 6.689/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- ICX-EUR — BUILDING_ACCELERATION — score 6.452/10 — DETECTED_BUT_TOO_LATE
- KERNEL-EUR — BUILDING_ACCELERATION — score 5.346/10 — DETECTED_BUT_TOO_LATE
- SAGA-EUR — BUILDING_ACCELERATION — score 5.278/10 — DETECTED_BUT_TOO_LATE
- HNT-EUR — BUILDING_ACCELERATION — score 4.944/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- TREAD-EUR — MEMORY_24H — score mémoire 9.440/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- NES-EUR — MEMORY_24H — score mémoire 8.853/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- LUNA2-EUR — MEMORY_24H — score mémoire 8.762/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- LMWR-EUR — ACTIVE_NOW — score mémoire 8.748/10 — sources ACCELERATION, V4 — WATCH_ONLY
- DEGEN-EUR — MEMORY_24H — score mémoire 8.739/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- AUDIO-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION — MEMORY_ONLY
- LAPTOP-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- BTT-EUR — ACTIVE_NOW — score mémoire 8.062/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- AVAX-EUR — ACTIVE_NOW — score mémoire 7.856/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- ANIME-EUR — ACTIVE_NOW — score mémoire 7.830/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY

## Audit des plus fortes hausses

- KERNEL-EUR +35.51% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- DRIFT-EUR +30.22% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- CHR-EUR +25.38% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- USELESS-EUR +24.81% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- BCH-EUR +24.33% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- FLOCK-EUR +19.40% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- KITE-EUR +16.51% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- NIL-EUR +14.97% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- ZRO-EUR +14.59% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- GOAT-EUR +13.58% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
