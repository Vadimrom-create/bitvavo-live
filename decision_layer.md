# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-20T20:54:05.239135+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : STX-EUR | action ACHETE_MAINTENANT | opportunité 8.793 | entrée 6.800 | trend 8.950 | rang 8.228
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : ZK-EUR | action PLACE_LIMITE_PASSIVE | opportunité 7.591 | entrée 5.800 | trend 7.900 | rang 7.084
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : ZIL-EUR | action LATENT_ACCELERATOR | opportunité 8.380 | entrée 5.450 | trend 8.750 | rang 7.878
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : CAKE-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 9.157 | entrée 7.200 | trend 8.950 | rang 8.355
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. CAKE-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.355
2. STX-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.228
3. COW-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.109

## Accélération indépendante

- GOAT-EUR — CONFIRMED_ACCELERATION — score 8.459/10 — DETECTED_BUT_TOO_LATE
- O-EUR — CONFIRMED_ACCELERATION — score 7.433/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- METIS-EUR — BUILDING_ACCELERATION — score 6.163/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- DUSK-EUR — BUILDING_ACCELERATION — score 5.737/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- SUPER-EUR — BUILDING_ACCELERATION — score 5.634/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- POND-EUR — BUILDING_ACCELERATION — score 5.237/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- ARPA-EUR — BUILDING_ACCELERATION — score 5.141/10 — DETECTED_BUT_TOO_LATE
- BICO-EUR — BUILDING_ACCELERATION — score 5.112/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- HFT-EUR — BUILDING_ACCELERATION — score 4.993/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- U-EUR — BUILDING_ACCELERATION — score 4.887/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- STX-EUR — ACTIVE_NOW — score mémoire 8.228/10 — sources DECISION_LAYER, V4 — BUYABLE_NOW
- NES-EUR — MEMORY_24H — score mémoire 8.883/10 — sources ACCELERATION — MEMORY_ONLY
- PTB-EUR — MEMORY_24H — score mémoire 8.518/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- GOAT-EUR — ACTIVE_NOW — score mémoire 8.459/10 — sources ACCELERATION, V4 — DETECTED_BUT_TOO_LATE
- NOS-EUR — MEMORY_24H — score mémoire 8.445/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- FTT-EUR — MEMORY_24H — score mémoire 8.388/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- CAKE-EUR — ACTIVE_NOW — score mémoire 8.355/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- NIL-EUR — MEMORY_24H — score mémoire 8.150/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- COW-EUR — ACTIVE_NOW — score mémoire 8.109/10 — sources DECISION_LAYER, V4 — WATCH_ONLY
- RAY-EUR — ACTIVE_NOW — score mémoire 7.980/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY

## Audit des plus fortes hausses

- SAGA-EUR +49.52% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- FTT-EUR +37.33% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- PTB-EUR +29.04% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- S-EUR +22.40% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- NIL-EUR +21.92% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- CELR-EUR +20.36% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- NEAR-EUR +18.56% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- KMNO-EUR +17.45% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- STRK-EUR +17.02% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- LUNA2-EUR +16.13% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
