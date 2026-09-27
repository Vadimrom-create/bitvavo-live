# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-27T17:56:37.815110+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : KAS-EUR | action ACHETE_MAINTENANT | opportunité 8.959 | entrée 8.100 | trend 8.900 | rang 8.494
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : BRETT-EUR | action PLACE_LIMITE_PASSIVE | opportunité 8.551 | entrée 6.050 | trend 9.000 | rang 8.067
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : BAT-EUR | action LATENT_ACCELERATOR | opportunité 7.756 | entrée 4.500 | trend 8.950 | rang 7.556
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : ZK-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 9.377 | entrée 6.450 | trend 8.750 | rang 8.384
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. KAS-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.494
2. ZK-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.384
3. MOVR-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.226

## Accélération indépendante

- SOSO-EUR — CONFIRMED_ACCELERATION — score 6.747/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- DGB-EUR — BUILDING_ACCELERATION — score 5.988/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- AMP-EUR — BUILDING_ACCELERATION — score 5.509/10 — DETECTED_BUT_TOO_LATE
- NOM-EUR — BUILDING_ACCELERATION — score 5.481/10 — DETECTED_BUT_TOO_LATE
- WLFI-EUR — BUILDING_ACCELERATION — score 4.858/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- ENA-EUR — ACTIVE_NOW — score mémoire 7.708/10 — sources ACCELERATION, DECISION_LAYER, V4 — BUYABLE_NOW
- MMT-EUR — MEMORY_24H — score mémoire 9.122/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- GROVE-EUR — MEMORY_24H — score mémoire 8.518/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- YB-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- KAS-EUR — ACTIVE_NOW — score mémoire 8.494/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- ZK-EUR — ACTIVE_NOW — score mémoire 8.384/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- FRAX-EUR — MEMORY_24H — score mémoire 8.380/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- AGI-EUR — MEMORY_24H — score mémoire 8.320/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- MOVR-EUR — ACTIVE_NOW — score mémoire 8.226/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- AAVE-EUR — ACTIVE_NOW — score mémoire 8.132/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY

## Audit des plus fortes hausses

- QNT-EUR +51.34% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- SOON-EUR +46.76% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- TREAD-EUR +46.07% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- AUDIO-EUR +25.49% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- INX-EUR +24.10% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ARX-EUR +20.83% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- W-EUR +19.99% — DETECTED_EARLY — couche NONE — action NONE
- GLMR-EUR +17.74% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- GRASS-EUR +17.07% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- AGI-EUR +15.08% — DETECTED_EARLY — couche NONE — action INTERPRETATION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
