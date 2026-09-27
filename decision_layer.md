# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-27T22:38:51.471395+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : KAS-EUR | action PLACE_LIMITE_PASSIVE | opportunité 8.258 | entrée 6.050 | trend 9.200 | rang 8.077
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : AIXBT-EUR | action LATENT_ACCELERATOR | opportunité 8.290 | entrée 5.450 | trend 9.000 | rang 7.893
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : SNX-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.943 | entrée 5.650 | trend 9.000 | rang 8.098
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Tous les achats immédiats

Aucun ACHETE_MAINTENANT dans le classement complet.

## Top cross-sectionnel — aperçu non exhaustif

Ce top est une vue courte multi-buckets. Il ne doit jamais être utilisé comme liste exhaustive des achats immédiats.
1. SNX-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.098
2. KAS-EUR — MEILLEURE_LIMITE_PASSIVE — PLACE_LIMITE_PASSIVE — rank 8.077
3. AAVE-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.056

## Accélération indépendante

- TREAD-EUR — CONFIRMED_ACCELERATION — score 8.170/10 — DETECTED_BUT_TOO_LATE
- QNT-EUR — CONFIRMED_ACCELERATION — score 7.387/10 — DETECTED_BUT_TOO_LATE
- SNX-EUR — CONFIRMED_ACCELERATION — score 7.187/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- JUP-EUR — CONFIRMED_ACCELERATION — score 6.624/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- INX-EUR — CONFIRMED_ACCELERATION — score 6.602/10 — DETECTED_BUT_TOO_LATE
- RARE-EUR — BUILDING_ACCELERATION — score 6.452/10 — DETECTED_BUT_TOO_LATE
- GRT-EUR — BUILDING_ACCELERATION — score 6.351/10 — DETECTED_BUT_TOO_LATE
- BTT-EUR — BUILDING_ACCELERATION — score 6.331/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- TRIA-EUR — BUILDING_ACCELERATION — score 5.425/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- REZ-EUR — BUILDING_ACCELERATION — score 5.353/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- YB-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- ZEUS-EUR — MEMORY_24H — score mémoire 8.458/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- FRAX-EUR — MEMORY_24H — score mémoire 8.380/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- TREAD-EUR — ACTIVE_NOW — score mémoire 8.170/10 — sources ACCELERATION, V4 — DETECTED_BUT_TOO_LATE
- ACX-EUR — MEMORY_24H — score mémoire 8.120/10 — sources ACCELERATION — MEMORY_ONLY
- SNX-EUR — ACTIVE_NOW — score mémoire 8.098/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- KAS-EUR — ACTIVE_NOW — score mémoire 8.077/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- AAVE-EUR — ACTIVE_NOW — score mémoire 8.056/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- ORCA-EUR — ACTIVE_NOW — score mémoire 8.036/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- C-EUR — ACTIVE_NOW — score mémoire 7.993/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY

## Audit des plus fortes hausses

- QNT-EUR +90.69% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- SOON-EUR +41.56% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- INX-EUR +34.69% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- TREAD-EUR +31.41% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- GRT-EUR +26.53% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- W-EUR +19.68% — DETECTED_EARLY — couche NONE — action NONE
- PUMP-EUR +15.45% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- AGI-EUR +13.91% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- NOM-EUR +13.10% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- GLMR-EUR +11.67% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
