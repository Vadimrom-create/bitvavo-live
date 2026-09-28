# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-28T02:23:29.774632+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : ALGO-EUR | action ACHETE_MAINTENANT | opportunité 8.198 | entrée 7.200 | trend 8.750 | rang 7.972
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : WLD-EUR | action PLACE_LIMITE_PASSIVE | opportunité 7.596 | entrée 6.000 | trend 8.650 | rang 7.568
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : AXL-EUR | action LATENT_ACCELERATOR | opportunité 8.990 | entrée 4.750 | trend 8.100 | rang 7.861
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : AVNT-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 9.240 | entrée 6.700 | trend 8.500 | rang 8.335
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Tous les achats immédiats

1. ALGO-EUR — ACHETE_MAINTENANT — rank 7.972 — opportunité 8.198 — entrée 7.200 — trend 8.750
2. GRAM-EUR — ACHETE_MAINTENANT — rank 7.871 — opportunité 8.556 — entrée 6.850 — trend 8.400
3. ONDO-EUR — ACHETE_MAINTENANT — rank 7.643 — opportunité 8.009 — entrée 7.600 — trend 8.450

## Top cross-sectionnel — aperçu non exhaustif

Ce top est une vue courte multi-buckets. Il ne doit jamais être utilisé comme liste exhaustive des achats immédiats.
1. AVNT-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.335
2. LDO-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.292
3. ALGO-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 7.972

## Accélération indépendante

- HFT-EUR — CONFIRMED_ACCELERATION — score 6.889/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- QNT-EUR — BUILDING_ACCELERATION — score 6.425/10 — DETECTED_BUT_TOO_LATE
- CATI-EUR — BUILDING_ACCELERATION — score 5.786/10 — DETECTED_BUT_TOO_LATE
- NIL-EUR — BUILDING_ACCELERATION — score 5.053/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- GRAM-EUR — BUILDING_ACCELERATION — score 5.010/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- BONK-EUR — BUILDING_ACCELERATION — score 4.974/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- SEI-EUR — BUILDING_ACCELERATION — score 4.961/10 — DETECTED_BUT_TOO_LATE
- XVG-EUR — BUILDING_ACCELERATION — score 4.866/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- ONDO-EUR — ACTIVE_NOW — score mémoire 7.643/10 — sources ACCELERATION, DECISION_LAYER, V4 — BUYABLE_NOW
- DGB-EUR — MEMORY_24H — score mémoire 10.000/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- YB-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- FRAX-EUR — MEMORY_24H — score mémoire 8.380/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- AVNT-EUR — ACTIVE_NOW — score mémoire 8.335/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- LDO-EUR — ACTIVE_NOW — score mémoire 8.292/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- ACX-EUR — MEMORY_24H — score mémoire 8.120/10 — sources ACCELERATION — MEMORY_ONLY
- ALGO-EUR — ACTIVE_NOW — score mémoire 7.972/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- SUI-EUR — ACTIVE_NOW — score mémoire 7.934/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- TOSHI-EUR — MEMORY_24H — score mémoire 7.894/10 — sources ACCELERATION, V4 — MEMORY_ONLY

## Audit des plus fortes hausses

- QNT-EUR +49.46% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- TREAD-EUR +31.70% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- GRT-EUR +27.29% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- SOON-EUR +25.18% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- IRYS-EUR +23.12% — NOT_DETECTED — couche SCANNER_COVERAGE — action NOT_APPLICABLE
- INX-EUR +19.02% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- PUMP-EUR +17.39% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- GRASS-EUR +17.26% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- SEI-EUR +17.15% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- IMX-EUR +13.50% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
