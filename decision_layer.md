# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-26T08:58:50.367956+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : AXS-EUR | action ACHETE_MAINTENANT | opportunité 9.452 | entrée 7.650 | trend 9.000 | rang 8.701
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : SAFE-EUR | action PLACE_LIMITE_PASSIVE | opportunité 8.223 | entrée 6.000 | trend 8.750 | rang 7.848
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : LDO-EUR | action LATENT_ACCELERATOR | opportunité 8.165 | entrée 5.550 | trend 8.950 | rang 7.832
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : API3-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.695 | entrée 6.800 | trend 8.450 | rang 8.047
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. AXS-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.701
2. EIGEN-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.257
3. ADA-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.147

## Accélération indépendante

- XPL-EUR — CONFIRMED_ACCELERATION — score 8.830/10 — DETECTED_BUT_TOO_LATE
- DYM-EUR — CONFIRMED_ACCELERATION — score 8.342/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- ACE-EUR — CONFIRMED_ACCELERATION — score 7.500/10 — DETECTED_BUT_TOO_LATE
- RARE-EUR — BUILDING_ACCELERATION — score 5.186/10 — DETECTED_BUT_TOO_LATE
- CYBER-EUR — BUILDING_ACCELERATION — score 5.019/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- KAITO-EUR — BUILDING_ACCELERATION — score 4.887/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- WMTX-EUR — BUILDING_ACCELERATION — score 4.776/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- FUEL-EUR — MEMORY_24H — score mémoire 9.607/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- PONKE-EUR — MEMORY_24H — score mémoire 9.578/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- ICX-EUR — MEMORY_24H — score mémoire 9.063/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- XMN-EUR — MEMORY_24H — score mémoire 8.896/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- CTC-EUR — MEMORY_24H — score mémoire 8.874/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- ONT-EUR — MEMORY_24H — score mémoire 8.859/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- XPL-EUR — ACTIVE_NOW — score mémoire 8.830/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- AXS-EUR — ACTIVE_NOW — score mémoire 8.701/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- ACT-EUR — MEMORY_24H — score mémoire 8.555/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- DYM-EUR — ACTIVE_NOW — score mémoire 8.342/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY

## Audit des plus fortes hausses

- POND-EUR +122.76% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- RARE-EUR +67.42% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- 2Z-EUR +34.49% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- PHA-EUR +32.38% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ARK-EUR +26.37% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- ENA-EUR +24.24% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- AERO-EUR +20.50% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- KMNO-EUR +16.41% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- PROM-EUR +16.17% — DETECTED_TOO_LATE — couche NONE — action INTERPRETATION
- EDGE-EUR +15.57% — DETECTED_EARLY — couche NONE — action INTERPRETATION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
