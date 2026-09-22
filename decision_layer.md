# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-22T13:26:57.551842+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : VET-EUR | action ACHETE_MAINTENANT | opportunité 8.576 | entrée 7.250 | trend 8.050 | rang 7.778
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : TURBO-EUR | action PLACE_LIMITE_PASSIVE | opportunité 8.158 | entrée 5.800 | trend 7.550 | rang 7.270
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : BEAM-EUR | action LATENT_ACCELERATOR | opportunité 8.034 | entrée 5.600 | trend 8.500 | rang 7.601
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : RUNE-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 9.361 | entrée 7.450 | trend 8.600 | rang 8.183
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. RUNE-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.183
2. WAL-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.927
3. W-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.874

## Accélération indépendante

- DEGEN-EUR — CONFIRMED_ACCELERATION — score 8.676/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- GOAT-EUR — CONFIRMED_ACCELERATION — score 8.500/10 — DETECTED_BUT_TOO_LATE
- IKA-EUR — CONFIRMED_ACCELERATION — score 8.098/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- TREAD-EUR — CONFIRMED_ACCELERATION — score 7.581/10 — DETECTED_BUT_TOO_LATE
- FLOCK-EUR — CONFIRMED_ACCELERATION — score 7.288/10 — DETECTED_BUT_TOO_LATE
- THQ-EUR — BUILDING_ACCELERATION — score 5.724/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- ENS-EUR — BUILDING_ACCELERATION — score 5.546/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- C98-EUR — BUILDING_ACCELERATION — score 5.544/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- CTC-EUR — BUILDING_ACCELERATION — score 5.491/10 — DETECTED_BUT_TOO_LATE
- SYN-EUR — BUILDING_ACCELERATION — score 5.455/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- AUDIO-EUR — MEMORY_24H — score mémoire 9.640/10 — sources ACCELERATION — MEMORY_ONLY
- NIL-EUR — MEMORY_24H — score mémoire 9.319/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- SWEAT-EUR — MEMORY_24H — score mémoire 9.062/10 — sources ACCELERATION — MEMORY_ONLY
- MLN-EUR — MEMORY_24H — score mémoire 9.032/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- DEGEN-EUR — ACTIVE_NOW — score mémoire 8.676/10 — sources ACCELERATION, V4 — WATCH_ONLY
- GIGA-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION — MEMORY_ONLY
- GOAT-EUR — ACTIVE_NOW — score mémoire 8.500/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- U-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- RUNE-EUR — ACTIVE_NOW — score mémoire 8.183/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- IKA-EUR — ACTIVE_NOW — score mémoire 8.098/10 — sources ACCELERATION, V4 — WATCH_ONLY

## Audit des plus fortes hausses

- ZRC-EUR +83.84% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ICX-EUR +83.67% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- XMN-EUR +28.71% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- KERNEL-EUR +26.56% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- NIL-EUR +22.85% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- FORM-EUR +22.24% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- BCH-EUR +19.38% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- FLOCK-EUR +18.72% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- GRASS-EUR +18.09% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- WIF-EUR +17.47% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
