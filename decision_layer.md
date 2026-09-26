# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-26T15:19:05.518456+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : ADA-EUR | action ACHETE_MAINTENANT | opportunité 9.139 | entrée 8.650 | trend 8.750 | rang 8.586
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : FLUX-EUR | action PLACE_LIMITE_PASSIVE | opportunité 8.338 | entrée 5.950 | trend 9.200 | rang 8.066
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : HOT-EUR | action LATENT_ACCELERATOR | opportunité 9.113 | entrée 5.650 | trend 8.450 | rang 8.132
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : RENDER-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 9.445 | entrée 8.250 | trend 8.850 | rang 8.610
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. RENDER-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.610
2. ADA-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.586
3. DOT-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.255

## Accélération indépendante

- WLD-EUR — CONFIRMED_ACCELERATION — score 8.812/10 — DETECTED_BUT_TOO_LATE
- DYDX-EUR — CONFIRMED_ACCELERATION — score 7.375/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- AIXBT-EUR — CONFIRMED_ACCELERATION — score 7.238/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- EGLD-EUR — BUILDING_ACCELERATION — score 6.350/10 — DETECTED_BUT_TOO_LATE
- POND-EUR — BUILDING_ACCELERATION — score 6.244/10 — DETECTED_BUT_TOO_LATE
- GOAT-EUR — BUILDING_ACCELERATION — score 5.811/10 — DETECTED_BUT_TOO_LATE
- SNX-EUR — BUILDING_ACCELERATION — score 5.639/10 — DETECTED_BUT_TOO_LATE
- KITE-EUR — BUILDING_ACCELERATION — score 5.592/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- EDEN-EUR — BUILDING_ACCELERATION — score 5.386/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- HUMA-EUR — BUILDING_ACCELERATION — score 5.380/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- DOT-EUR — ACTIVE_NOW — score mémoire 8.255/10 — sources ACCELERATION, DECISION_LAYER, V4 — BUYABLE_NOW
- AVAX-EUR — ACTIVE_NOW — score mémoire 8.253/10 — sources ACCELERATION, DECISION_LAYER, V4 — BUYABLE_NOW
- WIF-EUR — ACTIVE_NOW — score mémoire 7.934/10 — sources ACCELERATION, DECISION_LAYER, V4 — BUYABLE_NOW
- XMN-EUR — MEMORY_24H — score mémoire 9.942/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- WMTX-EUR — MEMORY_24H — score mémoire 9.837/10 — sources ACCELERATION — MEMORY_ONLY
- PONKE-EUR — MEMORY_24H — score mémoire 9.578/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- RAD-EUR — MEMORY_24H — score mémoire 9.291/10 — sources ACCELERATION — MEMORY_ONLY
- CTC-EUR — MEMORY_24H — score mémoire 8.874/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- ONT-EUR — MEMORY_24H — score mémoire 8.859/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- WLD-EUR — ACTIVE_NOW — score mémoire 8.812/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE

## Audit des plus fortes hausses

- POND-EUR +132.01% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- RARE-EUR +62.51% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- EDGE-EUR +32.51% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- AMP-EUR +28.94% — DETECTED_TOO_LATE — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- 2Z-EUR +28.41% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- ARK-EUR +19.61% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- FIL-EUR +18.60% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- WLD-EUR +17.93% — DETECTED_EARLY — couche NONE — action NONE
- HUMA-EUR +17.34% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- RUNE-EUR +16.65% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
