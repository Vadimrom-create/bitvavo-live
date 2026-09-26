# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-26T16:25:56.703567+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : XLM-EUR | action ACHETE_MAINTENANT | opportunité 9.353 | entrée 8.300 | trend 8.450 | rang 8.528
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : ALT-EUR | action PLACE_LIMITE_PASSIVE | opportunité 8.376 | entrée 6.050 | trend 9.000 | rang 8.046
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : BEAM-EUR | action LATENT_ACCELERATOR | opportunité 8.426 | entrée 5.350 | trend 8.700 | rang 7.863
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : LDO-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.424 | entrée 6.900 | trend 8.950 | rang 8.114
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. XLM-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.528
2. HBAR-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.511
3. LTC-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.217

## Accélération indépendante

- QNT-EUR — CONFIRMED_ACCELERATION — score 6.751/10 — DETECTED_BUT_TOO_LATE
- NOT-EUR — BUILDING_ACCELERATION — score 6.456/10 — DETECTED_BUT_TOO_LATE
- MASK-EUR — BUILDING_ACCELERATION — score 5.876/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- SSV-EUR — BUILDING_ACCELERATION — score 5.751/10 — DETECTED_BUT_TOO_LATE
- METIS-EUR — BUILDING_ACCELERATION — score 5.351/10 — DETECTED_BUT_TOO_LATE
- NEIRO-EUR — BUILDING_ACCELERATION — score 5.132/10 — DETECTED_BUT_TOO_LATE
- ALLO-EUR — BUILDING_ACCELERATION — score 5.091/10 — DETECTED_BUT_TOO_LATE
- WELL-EUR — BUILDING_ACCELERATION — score 4.969/10 — DETECTED_BUT_TOO_LATE
- FTT-EUR — BUILDING_ACCELERATION — score 4.926/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- OSMO-EUR — BUILDING_ACCELERATION — score 4.793/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- DOT-EUR — ACTIVE_NOW — score mémoire 8.038/10 — sources ACCELERATION, DECISION_LAYER, V4 — BUYABLE_NOW
- ICP-EUR — ACTIVE_NOW — score mémoire 7.910/10 — sources ACCELERATION, DECISION_LAYER, V4 — BUYABLE_NOW
- XMN-EUR — MEMORY_24H — score mémoire 9.942/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- PONKE-EUR — MEMORY_24H — score mémoire 9.578/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- RAD-EUR — MEMORY_24H — score mémoire 9.291/10 — sources ACCELERATION — MEMORY_ONLY
- ONT-EUR — MEMORY_24H — score mémoire 8.859/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- CTC-EUR — MEMORY_DECAY_24_72H — score mémoire 8.831/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- ACT-EUR — MEMORY_24H — score mémoire 8.555/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- XLM-EUR — ACTIVE_NOW — score mémoire 8.528/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- HBAR-EUR — ACTIVE_NOW — score mémoire 8.511/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY

## Audit des plus fortes hausses

- POND-EUR +117.93% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- EDGE-EUR +33.36% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- AMP-EUR +31.20% — DETECTED_TOO_LATE — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- RARE-EUR +28.49% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- QNT-EUR +23.62% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- ACE-EUR +20.94% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- RUNE-EUR +19.32% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE
- 2Z-EUR +18.47% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- KMNO-EUR +18.46% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- WLD-EUR +17.65% — DETECTED_EARLY — couche NONE — action NONE

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
