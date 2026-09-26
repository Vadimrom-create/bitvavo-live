# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-26T22:40:32.458886+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : CC-EUR | action ACHETE_MAINTENANT | opportunité 9.452 | entrée 7.800 | trend 9.000 | rang 8.692
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : MERL-EUR | action PLACE_LIMITE_PASSIVE | opportunité 9.056 | entrée 6.050 | trend 7.700 | rang 7.782
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : IMX-EUR | action LATENT_ACCELERATOR | opportunité 7.896 | entrée 5.750 | trend 9.000 | rang 7.761
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : FORM-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 9.235 | entrée 7.350 | trend 8.400 | rang 8.370
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. CC-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.692
2. FORM-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.370
3. LTC-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.075

## Accélération indépendante

- QNT-EUR — CONFIRMED_ACCELERATION — score 8.252/10 — DETECTED_BUT_TOO_LATE
- AUDIO-EUR — CONFIRMED_ACCELERATION — score 6.967/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- MLN-EUR — BUILDING_ACCELERATION — score 6.181/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- ENSO-EUR — BUILDING_ACCELERATION — score 5.113/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- QUID-EUR — BUILDING_ACCELERATION — score 5.022/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- AMP-EUR — MEMORY_24H — score mémoire 10.000/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- PONKE-EUR — MEMORY_24H — score mémoire 9.578/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- HFT-EUR — MEMORY_24H — score mémoire 9.483/10 — sources ACCELERATION — MEMORY_ONLY
- ONT-EUR — MEMORY_24H — score mémoire 8.859/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- CC-EUR — ACTIVE_NOW — score mémoire 8.692/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- VELO-EUR — MEMORY_24H — score mémoire 8.605/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- FORM-EUR — ACTIVE_NOW — score mémoire 8.370/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- QNT-EUR — ACTIVE_NOW — score mémoire 8.252/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- ICX-EUR — MEMORY_24H — score mémoire 8.191/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- LTC-EUR — ACTIVE_NOW — score mémoire 8.075/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY

## Audit des plus fortes hausses

- POND-EUR +102.46% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- AMP-EUR +54.80% — DETECTED_TOO_LATE — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- EDGE-EUR +44.87% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- RARE-EUR +38.01% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- QNT-EUR +37.29% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- 2Z-EUR +24.84% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- KMNO-EUR +20.85% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- AGI-EUR +17.89% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- RUNE-EUR +16.24% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE
- SOON-EUR +14.38% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
