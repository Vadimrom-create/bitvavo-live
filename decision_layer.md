# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-23T06:30:37.521816+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : ICP-EUR | action ACHETE_MAINTENANT | opportunité 9.115 | entrée 7.800 | trend 8.200 | rang 8.239
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : AUCTION-EUR | action PLACE_LIMITE_PASSIVE | opportunité 7.925 | entrée 6.050 | trend 8.500 | rang 7.571
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : RUNE-EUR | action LATENT_ACCELERATOR | opportunité 8.160 | entrée 5.750 | trend 8.550 | rang 7.486
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : VET-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.741 | entrée 7.850 | trend 8.350 | rang 8.008
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. ICP-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.239
2. LTC-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.160
3. ETC-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.107

## Accélération indépendante

- IKA-EUR — CONFIRMED_ACCELERATION — score 10.000/10 — DETECTED_BUT_TOO_LATE
- ZORA-EUR — CONFIRMED_ACCELERATION — score 7.547/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- ZRC-EUR — CONFIRMED_ACCELERATION — score 7.104/10 — DETECTED_BUT_TOO_LATE
- PEAQ-EUR — CONFIRMED_ACCELERATION — score 6.912/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- XAN-EUR — BUILDING_ACCELERATION — score 6.310/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- LSK-EUR — BUILDING_ACCELERATION — score 5.888/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- DEEP-EUR — BUILDING_ACCELERATION — score 5.777/10 — DETECTED_BUT_TOO_LATE
- 0G-EUR — BUILDING_ACCELERATION — score 5.637/10 — DETECTED_BUT_TOO_LATE
- PENGU-EUR — BUILDING_ACCELERATION — score 5.494/10 — DETECTED_BUT_TOO_LATE
- NEIRO-EUR — BUILDING_ACCELERATION — score 5.439/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- IKA-EUR — ACTIVE_NOW — score mémoire 10.000/10 — sources ACCELERATION, V4 — DETECTED_BUT_TOO_LATE
- SLX-EUR — MEMORY_24H — score mémoire 9.336/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- GIGA-EUR — MEMORY_24H — score mémoire 9.062/10 — sources ACCELERATION — MEMORY_ONLY
- NES-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- ICP-EUR — ACTIVE_NOW — score mémoire 8.239/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- LTC-EUR — ACTIVE_NOW — score mémoire 8.160/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- FTT-EUR — MEMORY_24H — score mémoire 8.118/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- ETC-EUR — ACTIVE_NOW — score mémoire 8.107/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- WIN-EUR — MEMORY_24H — score mémoire 8.088/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- LINK-EUR — MEMORY_24H — score mémoire 8.056/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY

## Audit des plus fortes hausses

- NIL-EUR +51.67% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- BCH-EUR +35.02% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- MET-EUR +32.83% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- CPOOL-EUR +29.49% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- CHR-EUR +26.30% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- TREAD-EUR +25.53% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- SUPER-EUR +24.25% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- ZRO-EUR +23.60% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- PENGU-EUR +20.73% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- USELESS-EUR +20.61% — DETECTED_EARLY — couche NONE — action INTERPRETATION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
