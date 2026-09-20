# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-20T22:30:27.750379+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : KAS-EUR | action ACHETE_MAINTENANT | opportunité 9.040 | entrée 7.050 | trend 8.650 | rang 8.206
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : SUPER-EUR | action PLACE_LIMITE_PASSIVE | opportunité 8.602 | entrée 6.100 | trend 8.650 | rang 7.918
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : ZIL-EUR | action LATENT_ACCELERATOR | opportunité 7.609 | entrée 5.400 | trend 8.600 | rang 7.430
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : COW-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.402 | entrée 6.350 | trend 9.000 | rang 8.001
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. KAS-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.206
2. JUP-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.093
3. COW-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.001

## Accélération indépendante

- ENS-EUR — CONFIRMED_ACCELERATION — score 7.561/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- CFG-EUR — CONFIRMED_ACCELERATION — score 6.814/10 — DETECTED_BUT_TOO_LATE
- CELO-EUR — CONFIRMED_ACCELERATION — score 6.629/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- FTT-EUR — CONFIRMED_ACCELERATION — score 6.583/10 — DETECTED_BUT_TOO_LATE
- CHIP-EUR — BUILDING_ACCELERATION — score 6.453/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- RAY-EUR — BUILDING_ACCELERATION — score 6.330/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- DEEP-EUR — BUILDING_ACCELERATION — score 6.315/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- U-EUR — BUILDING_ACCELERATION — score 5.724/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- LIGHTER-EUR — BUILDING_ACCELERATION — score 5.700/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- PONKE-EUR — BUILDING_ACCELERATION — score 5.184/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- JUP-EUR — ACTIVE_NOW — score mémoire 8.093/10 — sources ACCELERATION, DECISION_LAYER, V4 — BUYABLE_NOW
- ICX-EUR — MEMORY_24H — score mémoire 9.062/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- NES-EUR — MEMORY_24H — score mémoire 8.883/10 — sources ACCELERATION — MEMORY_ONLY
- NOS-EUR — MEMORY_24H — score mémoire 8.445/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- KAS-EUR — ACTIVE_NOW — score mémoire 8.206/10 — sources DECISION_LAYER, V4 — WATCH_ONLY
- UP-EUR — MEMORY_24H — score mémoire 8.113/10 — sources ACCELERATION — MEMORY_ONLY
- S-EUR — MEMORY_24H — score mémoire 8.013/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- COW-EUR — ACTIVE_NOW — score mémoire 8.001/10 — sources DECISION_LAYER, V4 — WATCH_ONLY
- CAKE-EUR — ACTIVE_NOW — score mémoire 7.927/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- SUPER-EUR — ACTIVE_NOW — score mémoire 7.918/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY

## Audit des plus fortes hausses

- SAGA-EUR +39.95% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- FTT-EUR +34.69% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- PTB-EUR +31.95% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- NIL-EUR +25.55% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- S-EUR +21.82% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- EPIC-EUR +19.59% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- KMNO-EUR +19.43% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- NEAR-EUR +19.40% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- CFG-EUR +18.11% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- AVAX-EUR +17.04% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
