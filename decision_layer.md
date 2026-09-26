# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-26T19:32:23.536513+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : PYTH-EUR | action ACHETE_MAINTENANT | opportunité 8.547 | entrée 7.050 | trend 8.850 | rang 8.106
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : DOT-EUR | action PLACE_LIMITE_PASSIVE | opportunité 7.862 | entrée 6.050 | trend 8.950 | rang 7.804
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : ALICE-EUR | action LATENT_ACCELERATOR | opportunité 9.168 | entrée 5.700 | trend 8.100 | rang 8.057
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : WCT-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 9.131 | entrée 6.450 | trend 8.100 | rang 8.070
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. PYTH-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.106
2. WCT-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.070
3. ALICE-EUR — MEILLEUR_LATENT_ACCELERATOR — LATENT_ACCELERATOR — rank 8.057

## Accélération indépendante

- LAPTOP-EUR — CONFIRMED_ACCELERATION — score 8.204/10 — DETECTED_BUT_TOO_LATE
- 2Z-EUR — BUILDING_ACCELERATION — score 5.332/10 — DETECTED_BUT_TOO_LATE
- SUPER-EUR — BUILDING_ACCELERATION — score 5.077/10 — DETECTED_BUT_TOO_LATE
- REQ-EUR — BUILDING_ACCELERATION — score 4.904/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- PONKE-EUR — MEMORY_24H — score mémoire 9.578/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- HFT-EUR — MEMORY_24H — score mémoire 9.483/10 — sources ACCELERATION — MEMORY_ONLY
- RAD-EUR — MEMORY_24H — score mémoire 9.291/10 — sources ACCELERATION — MEMORY_ONLY
- ONT-EUR — MEMORY_24H — score mémoire 8.859/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- ACT-EUR — MEMORY_24H — score mémoire 8.555/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- AGI-EUR — MEMORY_24H — score mémoire 8.418/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- CTC-EUR — MEMORY_DECAY_24_72H — score mémoire 8.257/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- LAPTOP-EUR — ACTIVE_NOW — score mémoire 8.204/10 — sources ACCELERATION, V4 — DETECTED_BUT_TOO_LATE
- PYTH-EUR — ACTIVE_NOW — score mémoire 8.106/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- WCT-EUR — ACTIVE_NOW — score mémoire 8.070/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY

## Audit des plus fortes hausses

- POND-EUR +112.97% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- EDGE-EUR +40.01% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- AMP-EUR +39.88% — DETECTED_TOO_LATE — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- RARE-EUR +39.55% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- QNT-EUR +26.12% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- 2Z-EUR +21.70% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- KMNO-EUR +21.13% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- KAS-EUR +17.69% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- AGI-EUR +17.64% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- RUNE-EUR +15.14% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
