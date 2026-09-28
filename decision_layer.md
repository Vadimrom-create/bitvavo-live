# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-28T13:53:50.027907+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : MIOTA-EUR | action PLACE_LIMITE_PASSIVE | opportunité 7.846 | entrée 6.100 | trend 8.750 | rang 7.607
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : IMX-EUR | action LATENT_ACCELERATOR | opportunité 7.758 | entrée 5.150 | trend 8.900 | rang 7.576
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : KAS-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.226 | entrée 7.350 | trend 8.700 | rang 7.962
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Tous les achats immédiats

Aucun ACHETE_MAINTENANT dans le classement complet.

## Top cross-sectionnel — aperçu non exhaustif

Ce top est une vue courte multi-buckets. Il ne doit jamais être utilisé comme liste exhaustive des achats immédiats.
1. KAS-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.962
2. XDC-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.860
3. GRAM-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.837

## Accélération indépendante

- AMP-EUR — CONFIRMED_ACCELERATION — score 9.648/10 — DETECTED_BUT_TOO_LATE
- HUMA-EUR — CONFIRMED_ACCELERATION — score 6.860/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- NPC-EUR — CONFIRMED_ACCELERATION — score 6.681/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- ZRX-EUR — BUILDING_ACCELERATION — score 6.449/10 — DETECTED_BUT_TOO_LATE
- PEOPLE-EUR — BUILDING_ACCELERATION — score 6.142/10 — DETECTED_BUT_TOO_LATE
- DRIFT-EUR — BUILDING_ACCELERATION — score 5.719/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- FLOCK-EUR — BUILDING_ACCELERATION — score 5.494/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- GLM-EUR — BUILDING_ACCELERATION — score 5.239/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- NIL-EUR — BUILDING_ACCELERATION — score 5.019/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- DGB-EUR — BUILDING_ACCELERATION — score 4.921/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- WMTX-EUR — MEMORY_24H — score mémoire 9.914/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- AMP-EUR — ACTIVE_NOW — score mémoire 9.648/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- BTT-EUR — MEMORY_24H — score mémoire 9.434/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- IMU-EUR — MEMORY_24H — score mémoire 9.209/10 — sources ACCELERATION — MEMORY_ONLY
- ZRC-EUR — MEMORY_24H — score mémoire 8.779/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- AGI-EUR — MEMORY_24H — score mémoire 8.533/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- FUEL-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- SAGA-EUR — MEMORY_24H — score mémoire 8.221/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- ACX-EUR — MEMORY_24H — score mémoire 8.120/10 — sources ACCELERATION — MEMORY_ONLY
- FRAX-EUR — MEMORY_DECAY_24_72H — score mémoire 8.011/10 — sources ACCELERATION, V4 — MEMORY_ONLY

## Audit des plus fortes hausses

- QNT-EUR +51.60% — DETECTED_TOO_LATE — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- HBAR-EUR +27.60% — DETECTED_EARLY — couche NONE — action NONE
- XDP-EUR +24.27% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE
- GRT-EUR +14.93% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- NMR-EUR +14.30% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- ALGO-EUR +14.23% — DETECTED_EARLY — couche NONE — action NONE
- PUMP-EUR +13.73% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- DGB-EUR +10.22% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- SOON-EUR +9.47% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- MON-EUR +9.45% — DETECTED_EARLY — couche NONE — action INTERPRETATION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
