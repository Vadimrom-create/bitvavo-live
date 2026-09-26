# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-26T10:37:22.238638+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : ONDO-EUR | action ACHETE_MAINTENANT | opportunité 9.367 | entrée 8.050 | trend 8.550 | rang 8.396
  - V4 buy-ready with acceptable current entry; no structural veto. High extension/chase is retained as risk context, not an automatic veto.
- **MEILLEURE_LIMITE_PASSIVE** : 0G-EUR | action PLACE_LIMITE_PASSIVE | opportunité 8.449 | entrée 5.900 | trend 8.950 | rang 7.948
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : COMP-EUR | action LATENT_ACCELERATOR | opportunité 7.971 | entrée 4.500 | trend 9.000 | rang 7.687
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : ROSE-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.776 | entrée 7.000 | trend 8.950 | rang 8.310
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. ONDO-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.396
2. WLD-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.358
3. ROSE-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.310

## Accélération indépendante

- PHA-EUR — CONFIRMED_ACCELERATION — score 7.274/10 — DETECTED_BUT_TOO_LATE
- TRAC-EUR — CONFIRMED_ACCELERATION — score 7.253/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- W-EUR — BUILDING_ACCELERATION — score 6.415/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- WAL-EUR — BUILDING_ACCELERATION — score 5.791/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- XYO-EUR — BUILDING_ACCELERATION — score 5.476/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- FLUX-EUR — BUILDING_ACCELERATION — score 5.091/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- ZK-EUR — BUILDING_ACCELERATION — score 4.875/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- LINEA-EUR — BUILDING_ACCELERATION — score 4.790/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- XPL-EUR — ACTIVE_NOW — score mémoire 7.604/10 — sources ACCELERATION, DECISION_LAYER, V4 — BUYABLE_NOW
- ZRC-EUR — MEMORY_24H — score mémoire 9.830/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- PONKE-EUR — MEMORY_24H — score mémoire 9.578/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- CTC-EUR — MEMORY_24H — score mémoire 8.874/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- ONT-EUR — MEMORY_24H — score mémoire 8.859/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- ACT-EUR — MEMORY_24H — score mémoire 8.555/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- POND-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- RARE-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- ONDO-EUR — ACTIVE_NOW — score mémoire 8.396/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- IMU-EUR — MEMORY_24H — score mémoire 8.394/10 — sources ACCELERATION — MEMORY_ONLY

## Audit des plus fortes hausses

- POND-EUR +159.25% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- RARE-EUR +73.49% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- 2Z-EUR +33.50% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- PHA-EUR +30.56% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ARK-EUR +25.13% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- ENA-EUR +24.21% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- AERO-EUR +16.16% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- PROM-EUR +14.23% — DETECTED_TOO_LATE — couche NONE — action INTERPRETATION
- WAXP-EUR +13.47% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- CC-EUR +13.23% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
