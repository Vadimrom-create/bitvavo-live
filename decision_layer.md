# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-22T08:53:17.839555+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : TAIKO-EUR | action ACHETE_MAINTENANT | opportunité 9.366 | entrée 7.300 | trend 8.700 | rang 8.463
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : BEAM-EUR | action PLACE_LIMITE_PASSIVE | opportunité 9.215 | entrée 6.000 | trend 8.500 | rang 7.934
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : 0G-EUR | action LATENT_ACCELERATOR | opportunité 8.065 | entrée 4.500 | trend 8.600 | rang 7.453
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : SUPER-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 9.271 | entrée 6.500 | trend 8.300 | rang 7.944
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. TAIKO-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.463
2. SOL-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.187
3. SUPER-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.944

## Accélération indépendante

- WIF-EUR — CONFIRMED_ACCELERATION — score 9.227/10 — DETECTED_BUT_TOO_LATE
- XMN-EUR — CONFIRMED_ACCELERATION — score 9.015/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- THQ-EUR — CONFIRMED_ACCELERATION — score 8.550/10 — DETECTED_BUT_TOO_LATE
- NIL-EUR — CONFIRMED_ACCELERATION — score 8.500/10 — DETECTED_BUT_TOO_LATE
- AERO-EUR — CONFIRMED_ACCELERATION — score 8.350/10 — DETECTED_BUT_TOO_LATE
- JUP-EUR — CONFIRMED_ACCELERATION — score 7.997/10 — DETECTED_BUT_TOO_LATE
- BABY-EUR — CONFIRMED_ACCELERATION — score 7.699/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- MET-EUR — CONFIRMED_ACCELERATION — score 7.611/10 — DETECTED_BUT_TOO_LATE
- RAY-EUR — CONFIRMED_ACCELERATION — score 7.535/10 — DETECTED_BUT_TOO_LATE
- SHIB-EUR — CONFIRMED_ACCELERATION — score 7.382/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- HBAR-EUR — ACTIVE_NOW — score mémoire 7.565/10 — sources ACCELERATION, DECISION_LAYER, V4 — BUYABLE_NOW
- ICX-EUR — MEMORY_24H — score mémoire 9.941/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- WIF-EUR — ACTIVE_NOW — score mémoire 9.227/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- GIGA-EUR — MEMORY_24H — score mémoire 9.062/10 — sources ACCELERATION — MEMORY_ONLY
- SWEAT-EUR — MEMORY_24H — score mémoire 9.062/10 — sources ACCELERATION — MEMORY_ONLY
- XMN-EUR — ACTIVE_NOW — score mémoire 9.015/10 — sources ACCELERATION — WATCH_ONLY
- THQ-EUR — ACTIVE_NOW — score mémoire 8.550/10 — sources ACCELERATION, V4 — DETECTED_BUT_TOO_LATE
- MEW-EUR — MEMORY_24H — score mémoire 8.523/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- NIL-EUR — ACTIVE_NOW — score mémoire 8.500/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- TAIKO-EUR — ACTIVE_NOW — score mémoire 8.463/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY

## Audit des plus fortes hausses

- ICX-EUR +127.32% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- ZRC-EUR +96.70% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- AIOZ-EUR +44.27% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- KERNEL-EUR +36.36% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- WIF-EUR +24.78% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- GRASS-EUR +24.76% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- PEPE-EUR +20.84% — DETECTED_EARLY — couche NONE — action NONE
- NIL-EUR +18.61% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- CARV-EUR +17.93% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- TREAD-EUR +17.47% — DETECTED_EARLY — couche NONE — action INTERPRETATION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
