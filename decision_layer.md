# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-26T15:51:31.375494+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : ADA-EUR | action ACHETE_MAINTENANT | opportunité 9.145 | entrée 8.150 | trend 8.750 | rang 8.482
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : FLUX-EUR | action PLACE_LIMITE_PASSIVE | opportunité 8.538 | entrée 5.900 | trend 9.200 | rang 8.113
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : CAKE-EUR | action LATENT_ACCELERATOR | opportunité 8.207 | entrée 5.750 | trend 8.950 | rang 7.927
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : RENDER-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 9.433 | entrée 7.950 | trend 8.850 | rang 8.519
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. RENDER-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.519
2. ADA-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.482
3. DOT-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.362

## Accélération indépendante

- DBR-EUR — CONFIRMED_ACCELERATION — score 9.101/10 — DETECTED_BUT_TOO_LATE
- ETHFI-EUR — CONFIRMED_ACCELERATION — score 7.754/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- AMP-EUR — CONFIRMED_ACCELERATION — score 7.335/10 — DETECTED_BUT_TOO_LATE
- QNT-EUR — CONFIRMED_ACCELERATION — score 6.985/10 — DETECTED_BUT_TOO_LATE
- PIXEL-EUR — CONFIRMED_ACCELERATION — score 6.821/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- PEOPLE-EUR — CONFIRMED_ACCELERATION — score 6.510/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- ILV-EUR — BUILDING_ACCELERATION — score 5.793/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- FTT-EUR — BUILDING_ACCELERATION — score 5.476/10 — DETECTED_BUT_TOO_LATE
- WMTX-EUR — BUILDING_ACCELERATION — score 5.359/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- DUSK-EUR — BUILDING_ACCELERATION — score 5.277/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- DOT-EUR — ACTIVE_NOW — score mémoire 8.362/10 — sources ACCELERATION, DECISION_LAYER, V4 — BUYABLE_NOW
- ALGO-EUR — ACTIVE_NOW — score mémoire 7.920/10 — sources ACCELERATION, DECISION_LAYER, V4 — BUYABLE_NOW
- VIRTUAL-EUR — ACTIVE_NOW — score mémoire 7.548/10 — sources ACCELERATION, DECISION_LAYER, V4 — BUYABLE_NOW
- XMN-EUR — MEMORY_24H — score mémoire 9.942/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- PONKE-EUR — MEMORY_24H — score mémoire 9.578/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- RAD-EUR — MEMORY_24H — score mémoire 9.291/10 — sources ACCELERATION — MEMORY_ONLY
- DBR-EUR — ACTIVE_NOW — score mémoire 9.101/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- CTC-EUR — MEMORY_24H — score mémoire 8.874/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- ONT-EUR — MEMORY_24H — score mémoire 8.859/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- ACT-EUR — MEMORY_24H — score mémoire 8.555/10 — sources ACCELERATION, V4 — MEMORY_ONLY

## Audit des plus fortes hausses

- POND-EUR +105.22% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- EDGE-EUR +39.55% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- AMP-EUR +36.97% — DETECTED_TOO_LATE — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- QNT-EUR +24.91% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- RARE-EUR +24.33% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- 2Z-EUR +23.91% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- HUMA-EUR +21.88% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- KMNO-EUR +19.75% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- ACE-EUR +18.87% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- RUNE-EUR +18.16% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
