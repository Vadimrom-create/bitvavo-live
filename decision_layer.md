# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-26T16:43:35.105738+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : XLM-EUR | action ACHETE_MAINTENANT | opportunité 9.311 | entrée 8.550 | trend 8.450 | rang 8.512
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : GOAT-EUR | action PLACE_LIMITE_PASSIVE | opportunité 9.211 | entrée 5.850 | trend 8.450 | rang 8.067
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : BEAM-EUR | action LATENT_ACCELERATOR | opportunité 8.150 | entrée 5.350 | trend 8.700 | rang 7.763
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : W-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.517 | entrée 7.400 | trend 8.950 | rang 8.173
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. XLM-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.512
2. LINK-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.428
3. HBAR-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.210

## Accélération indépendante

- AGI-EUR — CONFIRMED_ACCELERATION — score 8.418/10 — DETECTED_BUT_TOO_LATE
- AMP-EUR — CONFIRMED_ACCELERATION — score 7.857/10 — DETECTED_BUT_TOO_LATE
- LSK-EUR — CONFIRMED_ACCELERATION — score 6.854/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- DBR-EUR — CONFIRMED_ACCELERATION — score 6.644/10 — DETECTED_BUT_TOO_LATE
- QNT-EUR — BUILDING_ACCELERATION — score 6.085/10 — DETECTED_BUT_TOO_LATE
- LDO-EUR — BUILDING_ACCELERATION — score 5.291/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- DGB-EUR — BUILDING_ACCELERATION — score 5.013/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- BILL-EUR — BUILDING_ACCELERATION — score 4.792/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- ASTR-EUR — BUILDING_ACCELERATION — score 4.778/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- DOT-EUR — ACTIVE_NOW — score mémoire 7.915/10 — sources ACCELERATION, DECISION_LAYER, V4 — BUYABLE_NOW
- XMN-EUR — MEMORY_24H — score mémoire 9.942/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- PONKE-EUR — MEMORY_24H — score mémoire 9.578/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- RAD-EUR — MEMORY_24H — score mémoire 9.291/10 — sources ACCELERATION — MEMORY_ONLY
- ONT-EUR — MEMORY_24H — score mémoire 8.859/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- CTC-EUR — MEMORY_DECAY_24_72H — score mémoire 8.777/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- ACT-EUR — MEMORY_24H — score mémoire 8.555/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- XLM-EUR — ACTIVE_NOW — score mémoire 8.512/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- LINK-EUR — ACTIVE_NOW — score mémoire 8.428/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- AGI-EUR — ACTIVE_NOW — score mémoire 8.418/10 — sources ACCELERATION, V4 — DETECTED_BUT_TOO_LATE

## Audit des plus fortes hausses

- POND-EUR +123.24% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- AMP-EUR +38.15% — DETECTED_TOO_LATE — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- RARE-EUR +35.49% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- EDGE-EUR +29.18% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- QNT-EUR +24.20% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- AGI-EUR +22.07% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ACE-EUR +21.92% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- FIL-EUR +18.54% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- RUNE-EUR +18.51% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE
- 2Z-EUR +18.46% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
