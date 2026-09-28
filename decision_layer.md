# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-28T04:23:22.265392+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : SUI-EUR | action PLACE_LIMITE_PASSIVE | opportunité 7.686 | entrée 6.700 | trend 8.500 | rang 7.598
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : SKY-EUR | action LATENT_ACCELERATOR | opportunité 7.665 | entrée 5.550 | trend 8.750 | rang 7.454
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : KAS-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.708 | entrée 6.750 | trend 8.550 | rang 8.116
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Tous les achats immédiats

Aucun ACHETE_MAINTENANT dans le classement complet.

## Top cross-sectionnel — aperçu non exhaustif

Ce top est une vue courte multi-buckets. Il ne doit jamais être utilisé comme liste exhaustive des achats immédiats.
1. KAS-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.116
2. CC-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.071
3. JUP-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.765

## Accélération indépendante

- SOON-EUR — CONFIRMED_ACCELERATION — score 7.666/10 — DETECTED_BUT_TOO_LATE
- AGI-EUR — CONFIRMED_ACCELERATION — score 7.463/10 — DETECTED_BUT_TOO_LATE
- GRT-EUR — CONFIRMED_ACCELERATION — score 6.582/10 — DETECTED_BUT_TOO_LATE
- ARX-EUR — BUILDING_ACCELERATION — score 5.868/10 — DETECTED_BUT_TOO_LATE
- AZTEC-EUR — BUILDING_ACCELERATION — score 5.565/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- W-EUR — BUILDING_ACCELERATION — score 5.475/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- DODO-EUR — BUILDING_ACCELERATION — score 5.206/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- WELL-EUR — BUILDING_ACCELERATION — score 4.994/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- DGB-EUR — MEMORY_24H — score mémoire 10.000/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- FRAX-EUR — MEMORY_24H — score mémoire 8.380/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- CAP-EUR — MEMORY_24H — score mémoire 8.149/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- ACX-EUR — MEMORY_24H — score mémoire 8.120/10 — sources ACCELERATION — MEMORY_ONLY
- KAS-EUR — ACTIVE_NOW — score mémoire 8.116/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- CC-EUR — ACTIVE_NOW — score mémoire 8.071/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- SAFE-EUR — MEMORY_24H — score mémoire 7.933/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- TOSHI-EUR — MEMORY_24H — score mémoire 7.894/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- JUP-EUR — ACTIVE_NOW — score mémoire 7.765/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- W-EUR — ACTIVE_NOW — score mémoire 7.734/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY

## Audit des plus fortes hausses

- QNT-EUR +48.15% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- TREAD-EUR +36.43% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- PUMP-EUR +20.38% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- IRYS-EUR +20.34% — NOT_DETECTED — couche SCANNER_COVERAGE — action NOT_APPLICABLE
- GRT-EUR +20.21% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- SOON-EUR +17.27% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- SEI-EUR +14.45% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- AUDIO-EUR +13.32% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- JASMY-EUR +12.22% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- IMX-EUR +11.57% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
