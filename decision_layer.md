# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-27T03:41:23.921505+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : WLD-EUR | action ACHETE_MAINTENANT | opportunité 8.931 | entrée 8.250 | trend 8.900 | rang 8.414
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : AVNT-EUR | action PLACE_LIMITE_PASSIVE | opportunité 8.168 | entrée 5.850 | trend 8.700 | rang 7.793
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : IMX-EUR | action LATENT_ACCELERATOR | opportunité 8.863 | entrée 5.650 | trend 8.750 | rang 8.028
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : LPT-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 9.306 | entrée 7.150 | trend 8.450 | rang 8.223
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. WLD-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.414
2. LPT-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.223
3. JUP-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.041

## Accélération indépendante

- INX-EUR — CONFIRMED_ACCELERATION — score 10.000/10 — DETECTED_BUT_TOO_LATE
- WMTX-EUR — CONFIRMED_ACCELERATION — score 9.062/10 — DETECTED_BUT_TOO_LATE
- SOON-EUR — CONFIRMED_ACCELERATION — score 8.076/10 — DETECTED_BUT_TOO_LATE
- TOWNS-EUR — CONFIRMED_ACCELERATION — score 7.941/10 — DETECTED_BUT_TOO_LATE
- RE-EUR — BUILDING_ACCELERATION — score 5.955/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- TRUST-EUR — BUILDING_ACCELERATION — score 5.874/10 — DETECTED_BUT_TOO_LATE
- STX-EUR — BUILDING_ACCELERATION — score 5.673/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- XAN-EUR — BUILDING_ACCELERATION — score 5.539/10 — DETECTED_BUT_TOO_LATE
- LPT-EUR — BUILDING_ACCELERATION — score 5.192/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- JTO-EUR — BUILDING_ACCELERATION — score 5.019/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- INX-EUR — ACTIVE_NOW — score mémoire 10.000/10 — sources ACCELERATION, V4 — DETECTED_BUT_TOO_LATE
- SAGA-EUR — MEMORY_24H — score mémoire 9.476/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- WMTX-EUR — ACTIVE_NOW — score mémoire 9.062/10 — sources ACCELERATION — DETECTED_BUT_TOO_LATE
- RARE-EUR — MEMORY_24H — score mémoire 8.845/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- PONKE-EUR — MEMORY_DECAY_24_72H — score mémoire 8.658/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- VELO-EUR — MEMORY_24H — score mémoire 8.605/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- WLD-EUR — ACTIVE_NOW — score mémoire 8.414/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- SCR-EUR — MEMORY_24H — score mémoire 8.302/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- LPT-EUR — ACTIVE_NOW — score mémoire 8.223/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- ONT-EUR — MEMORY_DECAY_24_72H — score mémoire 8.196/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY

## Audit des plus fortes hausses

- QNT-EUR +71.74% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- SOON-EUR +41.84% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- AMP-EUR +39.46% — DETECTED_TOO_LATE — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- RARE-EUR +30.73% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- AGI-EUR +22.17% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- 2Z-EUR +20.49% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- RUNE-EUR +20.08% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- GRASS-EUR +15.58% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- W-EUR +14.41% — DETECTED_EARLY — couche NONE — action NONE
- EDGE-EUR +13.57% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
