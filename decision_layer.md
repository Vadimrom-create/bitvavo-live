# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-28T02:43:17.040082+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : GRAM-EUR | action ACHETE_MAINTENANT | opportunité 8.708 | entrée 7.050 | trend 8.400 | rang 8.015
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : TAIKO-EUR | action PLACE_LIMITE_PASSIVE | opportunité 7.835 | entrée 5.800 | trend 8.450 | rang 7.582
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : BIGTIME-EUR | action LATENT_ACCELERATOR | opportunité 7.517 | entrée 4.800 | trend 8.900 | rang 7.478
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : SUI-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.129 | entrée 7.650 | trend 8.950 | rang 8.058
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Tous les achats immédiats

1. GRAM-EUR — ACHETE_MAINTENANT — rank 8.015 — opportunité 8.708 — entrée 7.050 — trend 8.400
2. ONDO-EUR — ACHETE_MAINTENANT — rank 7.615 — opportunité 7.727 — entrée 7.550 — trend 8.450

## Top cross-sectionnel — aperçu non exhaustif

Ce top est une vue courte multi-buckets. Il ne doit jamais être utilisé comme liste exhaustive des achats immédiats.
1. SUI-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.058
2. GRAM-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.015
3. ALGO-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.998

## Accélération indépendante

- CAP-EUR — CONFIRMED_ACCELERATION — score 8.236/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- INX-EUR — CONFIRMED_ACCELERATION — score 6.721/10 — DETECTED_BUT_TOO_LATE
- AVNT-EUR — BUILDING_ACCELERATION — score 5.250/10 — DETECTED_BUT_TOO_LATE
- FOLD-EUR — BUILDING_ACCELERATION — score 4.811/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- ONDO-EUR — ACTIVE_NOW — score mémoire 7.615/10 — sources ACCELERATION, DECISION_LAYER, V4 — BUYABLE_NOW
- DGB-EUR — MEMORY_24H — score mémoire 10.000/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- FRAX-EUR — MEMORY_24H — score mémoire 8.380/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- CAP-EUR — ACTIVE_NOW — score mémoire 8.236/10 — sources ACCELERATION, V4 — WATCH_ONLY
- ACX-EUR — MEMORY_24H — score mémoire 8.120/10 — sources ACCELERATION — MEMORY_ONLY
- SUI-EUR — ACTIVE_NOW — score mémoire 8.058/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- GRAM-EUR — ACTIVE_NOW — score mémoire 8.015/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- ALGO-EUR — ACTIVE_NOW — score mémoire 7.998/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- SKY-EUR — ACTIVE_NOW — score mémoire 7.995/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- RAY-EUR — ACTIVE_NOW — score mémoire 7.941/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY

## Audit des plus fortes hausses

- QNT-EUR +61.12% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- TREAD-EUR +34.86% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- GRT-EUR +25.41% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- INX-EUR +22.92% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- IRYS-EUR +19.29% — NOT_DETECTED — couche SCANNER_COVERAGE — action NOT_APPLICABLE
- SEI-EUR +18.52% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- PUMP-EUR +17.33% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- GRASS-EUR +15.23% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- IMX-EUR +12.88% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- JASMY-EUR +11.77% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
