# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-27T09:19:45.161623+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : EIGEN-EUR | action ACHETE_MAINTENANT | opportunité 8.983 | entrée 6.900 | trend 9.200 | rang 8.398
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : SPK-EUR | action PLACE_LIMITE_PASSIVE | opportunité 8.309 | entrée 5.850 | trend 8.900 | rang 7.941
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : MIOTA-EUR | action LATENT_ACCELERATOR | opportunité 8.441 | entrée 5.000 | trend 8.250 | rang 7.693
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : CAKE-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 9.021 | entrée 6.300 | trend 8.200 | rang 8.098
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. EIGEN-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.398
2. CAKE-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.098
3. OP-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.960

## Accélération indépendante

- VELO-EUR — CONFIRMED_ACCELERATION — score 8.767/10 — DETECTED_BUT_TOO_LATE
- TREAD-EUR — CONFIRMED_ACCELERATION — score 7.909/10 — DETECTED_BUT_TOO_LATE
- ZIG-EUR — CONFIRMED_ACCELERATION — score 7.340/10 — DETECTED_BUT_TOO_LATE
- POND-EUR — CONFIRMED_ACCELERATION — score 7.274/10 — DETECTED_BUT_TOO_LATE
- JASMY-EUR — CONFIRMED_ACCELERATION — score 6.663/10 — DETECTED_BUT_TOO_LATE
- ARX-EUR — BUILDING_ACCELERATION — score 5.910/10 — DETECTED_BUT_TOO_LATE
- FOLD-EUR — BUILDING_ACCELERATION — score 4.801/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- ORCA-EUR — ACTIVE_NOW — score mémoire 7.704/10 — sources ACCELERATION, DECISION_LAYER, V4 — BUYABLE_NOW
- XMN-EUR — MEMORY_24H — score mémoire 9.365/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- VELO-EUR — ACTIVE_NOW — score mémoire 8.767/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- AMP-EUR — MEMORY_24H — score mémoire 8.589/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- HFT-EUR — MEMORY_24H — score mémoire 8.432/10 — sources ACCELERATION — MEMORY_ONLY
- FTT-EUR — MEMORY_24H — score mémoire 8.427/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- EIGEN-EUR — ACTIVE_NOW — score mémoire 8.398/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- CAKE-EUR — ACTIVE_NOW — score mémoire 8.098/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- ZEUS-EUR — MEMORY_24H — score mémoire 7.964/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- OP-EUR — ACTIVE_NOW — score mémoire 7.960/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY

## Audit des plus fortes hausses

- QNT-EUR +68.72% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- GLMR-EUR +47.83% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- SOON-EUR +44.38% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- AMP-EUR +32.89% — DETECTED_TOO_LATE — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- W-EUR +23.62% — DETECTED_EARLY — couche NONE — action NONE
- AGI-EUR +23.44% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- HFT-EUR +21.22% — NOT_DETECTED — couche SCANNER_COVERAGE — action NOT_APPLICABLE
- TREAD-EUR +19.35% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- EDGE-EUR +15.80% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- TRIA-EUR +15.45% — DETECTED_EARLY — couche NONE — action INTERPRETATION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
