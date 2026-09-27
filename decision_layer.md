# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-27T11:46:58.056664+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : SNX-EUR | action PLACE_LIMITE_PASSIVE | opportunité 8.608 | entrée 6.150 | trend 8.750 | rang 8.017
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : SPK-EUR | action LATENT_ACCELERATOR | opportunité 8.190 | entrée 5.400 | trend 8.900 | rang 7.780
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : EIGEN-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.242 | entrée 6.700 | trend 9.200 | rang 8.144
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. EIGEN-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.144
2. RENDER-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.052
3. SNX-EUR — MEILLEURE_LIMITE_PASSIVE — PLACE_LIMITE_PASSIVE — rank 8.017

## Accélération indépendante

- FRAX-EUR — CONFIRMED_ACCELERATION — score 8.380/10 — DETECTED_BUT_TOO_LATE
- LUMIA-EUR — CONFIRMED_ACCELERATION — score 6.908/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- VVV-EUR — BUILDING_ACCELERATION — score 6.305/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- TAI-EUR — BUILDING_ACCELERATION — score 4.842/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- EDGE-EUR — MEMORY_24H — score mémoire 10.000/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- XMN-EUR — MEMORY_24H — score mémoire 9.365/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- AMP-EUR — MEMORY_24H — score mémoire 9.138/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- MMT-EUR — MEMORY_24H — score mémoire 9.122/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- VELO-EUR — MEMORY_24H — score mémoire 8.767/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- GROVE-EUR — MEMORY_24H — score mémoire 8.518/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- FRAX-EUR — ACTIVE_NOW — score mémoire 8.380/10 — sources ACCELERATION, V4 — DETECTED_BUT_TOO_LATE
- EIGEN-EUR — ACTIVE_NOW — score mémoire 8.144/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- RENDER-EUR — ACTIVE_NOW — score mémoire 8.052/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- SNX-EUR — ACTIVE_NOW — score mémoire 8.017/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY

## Audit des plus fortes hausses

- QNT-EUR +55.63% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- TREAD-EUR +52.88% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- GLMR-EUR +50.18% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- SOON-EUR +26.42% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- EDGE-EUR +24.44% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- AMP-EUR +19.64% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- WLD-EUR +18.71% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- AGI-EUR +18.06% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- HFT-EUR +16.30% — NOT_DETECTED — couche SCANNER_COVERAGE — action NOT_APPLICABLE
- GRASS-EUR +15.36% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
