# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-26T17:47:48.727539+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : RPL-EUR | action PLACE_LIMITE_PASSIVE | opportunité 8.290 | entrée 5.850 | trend 9.000 | rang 7.978
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : MANTRA-EUR | action LATENT_ACCELERATOR | opportunité 7.992 | entrée 5.650 | trend 9.000 | rang 7.788
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : AXS-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.326 | entrée 7.450 | trend 9.000 | rang 8.204
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. AXS-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.204
2. LDO-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.007
3. RPL-EUR — MEILLEURE_LIMITE_PASSIVE — PLACE_LIMITE_PASSIVE — rank 7.978

## Accélération indépendante

- C98-EUR — CONFIRMED_ACCELERATION — score 9.652/10 — DETECTED_BUT_TOO_LATE
- TREAD-EUR — CONFIRMED_ACCELERATION — score 7.918/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- RARE-EUR — CONFIRMED_ACCELERATION — score 7.510/10 — DETECTED_BUT_TOO_LATE
- BEAM-EUR — CONFIRMED_ACCELERATION — score 6.766/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- IOST-EUR — BUILDING_ACCELERATION — score 5.575/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- ARK-EUR — BUILDING_ACCELERATION — score 5.061/10 — DETECTED_BUT_TOO_LATE
- FLUX-EUR — BUILDING_ACCELERATION — score 4.925/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- GRASS-EUR — BUILDING_ACCELERATION — score 4.879/10 — DETECTED_BUT_TOO_LATE
- ATOM-EUR — BUILDING_ACCELERATION — score 4.760/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- XMN-EUR — MEMORY_24H — score mémoire 9.942/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- C98-EUR — ACTIVE_NOW — score mémoire 9.652/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- PONKE-EUR — MEMORY_24H — score mémoire 9.578/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- HFT-EUR — MEMORY_24H — score mémoire 9.483/10 — sources ACCELERATION — MEMORY_ONLY
- RAD-EUR — MEMORY_24H — score mémoire 9.291/10 — sources ACCELERATION — MEMORY_ONLY
- ONT-EUR — MEMORY_24H — score mémoire 8.859/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- AMP-EUR — MEMORY_24H — score mémoire 8.728/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- CTC-EUR — MEMORY_DECAY_24_72H — score mémoire 8.579/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- ACT-EUR — MEMORY_24H — score mémoire 8.555/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- AGI-EUR — MEMORY_24H — score mémoire 8.418/10 — sources ACCELERATION, V4 — MEMORY_ONLY

## Audit des plus fortes hausses

- POND-EUR +97.47% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- EDGE-EUR +49.88% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- RARE-EUR +41.47% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- AMP-EUR +39.16% — DETECTED_TOO_LATE — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- QNT-EUR +26.19% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- 2Z-EUR +20.53% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- KAS-EUR +20.27% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- AGI-EUR +18.55% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- KMNO-EUR +18.40% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- WLD-EUR +17.99% — DETECTED_EARLY — couche NONE — action NONE

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
