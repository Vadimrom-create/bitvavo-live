# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-28T03:43:25.338966+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : OP-EUR | action PLACE_LIMITE_PASSIVE | opportunité 7.798 | entrée 5.850 | trend 8.450 | rang 7.571
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : XVG-EUR | action LATENT_ACCELERATOR | opportunité 7.868 | entrée 5.550 | trend 8.200 | rang 7.477
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : ROSE-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 9.344 | entrée 4.900 | trend 8.950 | rang 8.348
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Tous les achats immédiats

Aucun ACHETE_MAINTENANT dans le classement complet.

## Top cross-sectionnel — aperçu non exhaustif

Ce top est une vue courte multi-buckets. Il ne doit jamais être utilisé comme liste exhaustive des achats immédiats.
1. ROSE-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.348
2. FET-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.190
3. SUI-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.939

## Accélération indépendante

- TREAD-EUR — BUILDING_ACCELERATION — score 6.355/10 — DETECTED_BUT_TOO_LATE
- AVNT-EUR — BUILDING_ACCELERATION — score 5.476/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- EDGE-EUR — BUILDING_ACCELERATION — score 4.800/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- DGB-EUR — MEMORY_24H — score mémoire 10.000/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- FRAX-EUR — MEMORY_24H — score mémoire 8.380/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- ROSE-EUR — ACTIVE_NOW — score mémoire 8.348/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- FET-EUR — ACTIVE_NOW — score mémoire 8.190/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- ACX-EUR — MEMORY_24H — score mémoire 8.120/10 — sources ACCELERATION — MEMORY_ONLY
- SUI-EUR — ACTIVE_NOW — score mémoire 7.939/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- SAFE-EUR — ACTIVE_NOW — score mémoire 7.933/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- TOSHI-EUR — MEMORY_24H — score mémoire 7.894/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- AVNT-EUR — ACTIVE_NOW — score mémoire 7.818/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- MOVR-EUR — ACTIVE_NOW — score mémoire 7.808/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY

## Audit des plus fortes hausses

- QNT-EUR +48.68% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- TREAD-EUR +37.59% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- IRYS-EUR +23.06% — NOT_DETECTED — couche SCANNER_COVERAGE — action NOT_APPLICABLE
- PUMP-EUR +18.77% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- GRT-EUR +17.60% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- GRASS-EUR +15.10% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- SEI-EUR +14.71% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- AUDIO-EUR +12.42% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- SKY-EUR +10.72% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- SOSO-EUR +8.83% — NOT_DETECTED — couche SCANNER_COVERAGE — action NOT_APPLICABLE

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
