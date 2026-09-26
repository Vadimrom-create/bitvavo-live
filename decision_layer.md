# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-26T07:51:32.136638+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : LTC-EUR | action ACHETE_MAINTENANT | opportunité 9.103 | entrée 7.800 | trend 8.850 | rang 8.415
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : ZK-EUR | action PLACE_LIMITE_PASSIVE | opportunité 8.403 | entrée 5.950 | trend 8.950 | rang 7.918
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : 0G-EUR | action LATENT_ACCELERATOR | opportunité 8.105 | entrée 5.200 | trend 8.950 | rang 7.754
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : GALA-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 9.318 | entrée 7.250 | trend 8.500 | rang 8.403
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. LTC-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.415
2. GALA-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.403
3. ICP-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.392

## Accélération indépendante

- WMTX-EUR — CONFIRMED_ACCELERATION — score 7.576/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- POND-EUR — CONFIRMED_ACCELERATION — score 6.612/10 — DETECTED_BUT_TOO_LATE
- BTT-EUR — CONFIRMED_ACCELERATION — score 6.561/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- ENJ-EUR — BUILDING_ACCELERATION — score 6.452/10 — DETECTED_BUT_TOO_LATE
- ALIGN-EUR — BUILDING_ACCELERATION — score 5.853/10 — DETECTED_BUT_TOO_LATE
- TNSR-EUR — BUILDING_ACCELERATION — score 5.131/10 — DETECTED_BUT_TOO_LATE
- XPL-EUR — BUILDING_ACCELERATION — score 5.038/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- BRETT-EUR — BUILDING_ACCELERATION — score 4.954/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- XPL-EUR — ACTIVE_NOW — score mémoire 7.573/10 — sources ACCELERATION, DECISION_LAYER, V4 — BUYABLE_NOW
- FUEL-EUR — MEMORY_24H — score mémoire 9.607/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- PONKE-EUR — MEMORY_24H — score mémoire 9.578/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- XMN-EUR — MEMORY_24H — score mémoire 8.896/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- CTC-EUR — MEMORY_24H — score mémoire 8.874/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- ONT-EUR — MEMORY_24H — score mémoire 8.859/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- WIN-EUR — MEMORY_24H — score mémoire 8.694/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- ACT-EUR — MEMORY_24H — score mémoire 8.555/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- 2Z-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- LTC-EUR — ACTIVE_NOW — score mémoire 8.415/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY

## Audit des plus fortes hausses

- POND-EUR +107.60% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- RARE-EUR +64.43% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ARK-EUR +35.14% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- PHA-EUR +33.48% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- 2Z-EUR +30.06% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- ENA-EUR +24.86% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- AERO-EUR +21.33% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- PUMP-EUR +17.75% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- KMNO-EUR +17.49% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- CC-EUR +17.37% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
