# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-22T13:19:12.433902+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : XLM-EUR | action ACHETE_MAINTENANT | opportunité 9.029 | entrée 7.400 | trend 7.300 | rang 7.741
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : TURBO-EUR | action PLACE_LIMITE_PASSIVE | opportunité 7.817 | entrée 5.800 | trend 7.550 | rang 7.113
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : MERL-EUR | action LATENT_ACCELERATOR | opportunité 8.239 | entrée 5.200 | trend 8.850 | rang 7.783
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : THE-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 9.206 | entrée 6.900 | trend 8.350 | rang 8.192
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. THE-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.192
2. RUNE-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.125
3. WAL-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.978

## Accélération indépendante

- GOAT-EUR — CONFIRMED_ACCELERATION — score 10.000/10 — DETECTED_BUT_TOO_LATE
- VELO-EUR — CONFIRMED_ACCELERATION — score 9.886/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- TREAD-EUR — CONFIRMED_ACCELERATION — score 8.500/10 — DETECTED_BUT_TOO_LATE
- THQ-EUR — CONFIRMED_ACCELERATION — score 8.025/10 — DETECTED_BUT_TOO_LATE
- ETC-EUR — CONFIRMED_ACCELERATION — score 7.700/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- BOB-EUR — CONFIRMED_ACCELERATION — score 7.460/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- CTC-EUR — CONFIRMED_ACCELERATION — score 7.336/10 — DETECTED_BUT_TOO_LATE
- RUNE-EUR — CONFIRMED_ACCELERATION — score 6.868/10 — DETECTED_BUT_TOO_LATE
- TIA-EUR — CONFIRMED_ACCELERATION — score 6.745/10 — DETECTED_BUT_TOO_LATE
- TRUMP-EUR — BUILDING_ACCELERATION — score 6.438/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- VET-EUR — ACTIVE_NOW — score mémoire 7.592/10 — sources ACCELERATION, DECISION_LAYER, V4 — BUYABLE_NOW
- GOAT-EUR — ACTIVE_NOW — score mémoire 10.000/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- VELO-EUR — ACTIVE_NOW — score mémoire 9.886/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- AUDIO-EUR — MEMORY_24H — score mémoire 9.640/10 — sources ACCELERATION — MEMORY_ONLY
- NIL-EUR — MEMORY_24H — score mémoire 9.319/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- SWEAT-EUR — MEMORY_24H — score mémoire 9.062/10 — sources ACCELERATION — MEMORY_ONLY
- MLN-EUR — MEMORY_24H — score mémoire 9.032/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- GIGA-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION — MEMORY_ONLY
- TREAD-EUR — ACTIVE_NOW — score mémoire 8.500/10 — sources ACCELERATION, V4 — DETECTED_BUT_TOO_LATE
- U-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION, V4 — MEMORY_ONLY

## Audit des plus fortes hausses

- ZRC-EUR +87.91% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ICX-EUR +83.67% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- KERNEL-EUR +26.61% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- XMN-EUR +23.54% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- FORM-EUR +23.51% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- NIL-EUR +22.77% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- GRASS-EUR +18.22% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- WIF-EUR +18.13% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- BCH-EUR +18.01% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- FLOCK-EUR +17.43% — DETECTED_EARLY — couche NONE — action INTERPRETATION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
