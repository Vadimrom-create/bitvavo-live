# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-26T10:52:05.557756+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : WLD-EUR | action ACHETE_MAINTENANT | opportunité 9.342 | entrée 7.800 | trend 8.400 | rang 8.407
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : BEAM-EUR | action PLACE_LIMITE_PASSIVE | opportunité 8.437 | entrée 6.000 | trend 9.000 | rang 8.000
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : 0G-EUR | action LATENT_ACCELERATOR | opportunité 8.145 | entrée 5.450 | trend 8.950 | rang 7.765
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : SKY-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 9.055 | entrée 7.350 | trend 8.200 | rang 8.206
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. WLD-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.407
2. LINK-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.249
3. SKY-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.206

## Accélération indépendante

- FOLD-EUR — CONFIRMED_ACCELERATION — score 8.262/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- KMNO-EUR — CONFIRMED_ACCELERATION — score 6.675/10 — DETECTED_BUT_TOO_LATE
- DGB-EUR — CONFIRMED_ACCELERATION — score 6.543/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- AERO-EUR — BUILDING_ACCELERATION — score 6.026/10 — DETECTED_BUT_TOO_LATE
- WAXP-EUR — BUILDING_ACCELERATION — score 5.906/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- XPL-EUR — BUILDING_ACCELERATION — score 5.753/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- ARK-EUR — BUILDING_ACCELERATION — score 5.405/10 — DETECTED_BUT_TOO_LATE
- ROSE-EUR — BUILDING_ACCELERATION — score 5.264/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- LISTA-EUR — BUILDING_ACCELERATION — score 5.130/10 — DETECTED_BUT_TOO_LATE
- BRETT-EUR — BUILDING_ACCELERATION — score 5.085/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- OP-EUR — ACTIVE_NOW — score mémoire 7.968/10 — sources ACCELERATION, DECISION_LAYER, V4 — BUYABLE_NOW
- XPL-EUR — ACTIVE_NOW — score mémoire 7.931/10 — sources ACCELERATION, DECISION_LAYER, V4 — BUYABLE_NOW
- GALA-EUR — ACTIVE_NOW — score mémoire 7.891/10 — sources ACCELERATION, DECISION_LAYER, V4 — BUYABLE_NOW
- ZRC-EUR — MEMORY_24H — score mémoire 9.830/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- PONKE-EUR — MEMORY_24H — score mémoire 9.578/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- CTC-EUR — MEMORY_24H — score mémoire 8.874/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- ONT-EUR — MEMORY_24H — score mémoire 8.859/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- ACT-EUR — MEMORY_24H — score mémoire 8.555/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- POND-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- RARE-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY

## Audit des plus fortes hausses

- POND-EUR +155.65% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- RARE-EUR +78.90% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- 2Z-EUR +33.20% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- PHA-EUR +30.26% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ENA-EUR +24.61% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- ARK-EUR +17.73% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- AERO-EUR +17.24% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- PROM-EUR +16.34% — DETECTED_TOO_LATE — couche NONE — action INTERPRETATION
- KMNO-EUR +14.98% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- EDGE-EUR +13.91% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
