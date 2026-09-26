# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-26T18:24:02.021765+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : WAL-EUR | action ACHETE_MAINTENANT | opportunité 8.429 | entrée 6.850 | trend 8.950 | rang 8.128
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : OP-EUR | action PLACE_LIMITE_PASSIVE | opportunité 7.935 | entrée 6.100 | trend 8.950 | rang 7.844
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : ROSE-EUR | action LATENT_ACCELERATOR | opportunité 8.408 | entrée 5.450 | trend 8.950 | rang 7.920
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : FLUX-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.544 | entrée 7.350 | trend 8.600 | rang 8.071
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. WAL-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.128
2. FLUX-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.071
3. AXS-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.040

## Accélération indépendante

- KAIA-EUR — CONFIRMED_ACCELERATION — score 7.938/10 — DETECTED_BUT_TOO_LATE
- SUPER-EUR — CONFIRMED_ACCELERATION — score 7.887/10 — DETECTED_BUT_TOO_LATE
- WELL-EUR — CONFIRMED_ACCELERATION — score 7.862/10 — DETECTED_BUT_TOO_LATE
- CETUS-EUR — CONFIRMED_ACCELERATION — score 7.509/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- POND-EUR — BUILDING_ACCELERATION — score 6.287/10 — DETECTED_BUT_TOO_LATE
- ICX-EUR — BUILDING_ACCELERATION — score 6.277/10 — DETECTED_BUT_TOO_LATE
- PTB-EUR — BUILDING_ACCELERATION — score 6.168/10 — DETECTED_BUT_TOO_LATE
- ZRC-EUR — BUILDING_ACCELERATION — score 6.053/10 — DETECTED_BUT_TOO_LATE
- LUMIA-EUR — BUILDING_ACCELERATION — score 5.017/10 — DETECTED_BUT_TOO_LATE
- UP-EUR — BUILDING_ACCELERATION — score 4.966/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- XMN-EUR — MEMORY_24H — score mémoire 9.942/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- PONKE-EUR — MEMORY_24H — score mémoire 9.578/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- HFT-EUR — MEMORY_24H — score mémoire 9.483/10 — sources ACCELERATION — MEMORY_ONLY
- RAD-EUR — MEMORY_24H — score mémoire 9.291/10 — sources ACCELERATION — MEMORY_ONLY
- ONT-EUR — MEMORY_24H — score mémoire 8.859/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- ACT-EUR — MEMORY_24H — score mémoire 8.555/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- CTC-EUR — MEMORY_DECAY_24_72H — score mémoire 8.467/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- AGI-EUR — MEMORY_24H — score mémoire 8.418/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- WAL-EUR — ACTIVE_NOW — score mémoire 8.128/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- FLUX-EUR — ACTIVE_NOW — score mémoire 8.071/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY

## Audit des plus fortes hausses

- POND-EUR +115.64% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- RARE-EUR +43.05% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- EDGE-EUR +42.50% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- AMP-EUR +40.48% — DETECTED_TOO_LATE — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- QNT-EUR +25.22% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- 2Z-EUR +21.45% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- KMNO-EUR +21.39% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- WELL-EUR +19.58% — NOT_DETECTED — couche SCANNER_COVERAGE — action NOT_APPLICABLE
- AGI-EUR +18.39% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- KAS-EUR +17.67% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
