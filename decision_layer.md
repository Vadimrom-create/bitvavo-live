# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-27T04:35:56.740452+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : RENDER-EUR | action ACHETE_MAINTENANT | opportunité 9.364 | entrée 7.050 | trend 8.900 | rang 8.582
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : DOT-EUR | action PLACE_LIMITE_PASSIVE | opportunité 8.749 | entrée 6.100 | trend 8.150 | rang 7.775
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : AEVO-EUR | action LATENT_ACCELERATOR | opportunité 8.227 | entrée 5.150 | trend 9.000 | rang 7.882
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : TNSR-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 9.206 | entrée 6.500 | trend 8.450 | rang 8.297
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. RENDER-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.582
2. JUP-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.369
3. ENA-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.340

## Accélération indépendante

- TAIKO-EUR — CONFIRMED_ACCELERATION — score 9.268/10 — DETECTED_BUT_TOO_LATE
- HEI-EUR — CONFIRMED_ACCELERATION — score 8.862/10 — DETECTED_BUT_TOO_LATE
- FTT-EUR — CONFIRMED_ACCELERATION — score 8.427/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- ZRC-EUR — CONFIRMED_ACCELERATION — score 6.835/10 — DETECTED_BUT_TOO_LATE
- NES-EUR — BUILDING_ACCELERATION — score 5.833/10 — DETECTED_BUT_TOO_LATE
- GLMR-EUR — BUILDING_ACCELERATION — score 5.576/10 — DETECTED_BUT_TOO_LATE
- COMP-EUR — BUILDING_ACCELERATION — score 5.332/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- ARK-EUR — BUILDING_ACCELERATION — score 5.294/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- INX-EUR — MEMORY_24H — score mémoire 10.000/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- SAGA-EUR — MEMORY_24H — score mémoire 9.476/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- TAIKO-EUR — ACTIVE_NOW — score mémoire 9.268/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- QNT-EUR — MEMORY_24H — score mémoire 9.139/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- HEI-EUR — ACTIVE_NOW — score mémoire 8.862/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- RARE-EUR — MEMORY_24H — score mémoire 8.845/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- VELO-EUR — MEMORY_24H — score mémoire 8.605/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- RENDER-EUR — ACTIVE_NOW — score mémoire 8.582/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- PONKE-EUR — MEMORY_DECAY_24_72H — score mémoire 8.477/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- FTT-EUR — ACTIVE_NOW — score mémoire 8.427/10 — sources ACCELERATION, V4 — WATCH_ONLY

## Audit des plus fortes hausses

- QNT-EUR +86.97% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- SOON-EUR +43.62% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- AMP-EUR +40.26% — DETECTED_TOO_LATE — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- RARE-EUR +24.39% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- RUNE-EUR +22.49% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- ZRC-EUR +20.42% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- GLMR-EUR +19.52% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- 2Z-EUR +19.28% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- AGI-EUR +18.58% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- TAIKO-EUR +17.14% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
