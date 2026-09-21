# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-21T20:00:57.580099+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : VET-EUR | action ACHETE_MAINTENANT | opportunité 9.353 | entrée 8.000 | trend 8.450 | rang 8.353
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : IMX-EUR | action PLACE_LIMITE_PASSIVE | opportunité 7.702 | entrée 5.850 | trend 8.450 | rang 7.502
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : MERL-EUR | action LATENT_ACCELERATOR | opportunité 8.144 | entrée 4.950 | trend 8.900 | rang 7.784
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : RENDER-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 9.124 | entrée 8.400 | trend 8.100 | rang 8.246
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. VET-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.353
2. RENDER-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.246
3. WAL-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.074

## Accélération indépendante

- TAO-EUR — CONFIRMED_ACCELERATION — score 10.000/10 — DETECTED_BUT_TOO_LATE
- TNSR-EUR — CONFIRMED_ACCELERATION — score 9.496/10 — DETECTED_BUT_TOO_LATE
- GLMR-EUR — CONFIRMED_ACCELERATION — score 8.100/10 — DETECTED_BUT_TOO_LATE
- ZEUS-EUR — CONFIRMED_ACCELERATION — score 7.198/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- PUFFER-EUR — BUILDING_ACCELERATION — score 6.382/10 — DETECTED_BUT_TOO_LATE
- PROMPT-EUR — BUILDING_ACCELERATION — score 6.336/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- XVG-EUR — BUILDING_ACCELERATION — score 6.190/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- SAGA-EUR — BUILDING_ACCELERATION — score 5.960/10 — DETECTED_BUT_TOO_LATE
- RUNE-EUR — BUILDING_ACCELERATION — score 5.722/10 — DETECTED_BUT_TOO_LATE
- NES-EUR — BUILDING_ACCELERATION — score 5.635/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- VET-EUR — ACTIVE_NOW — score mémoire 8.353/10 — sources ACCELERATION, DECISION_LAYER, V4 — BUYABLE_NOW
- RAY-EUR — ACTIVE_NOW — score mémoire 7.256/10 — sources ACCELERATION, DECISION_LAYER, V4 — BUYABLE_NOW
- TAO-EUR — ACTIVE_NOW — score mémoire 10.000/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- RON-EUR — MEMORY_24H — score mémoire 9.938/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- PTB-EUR — MEMORY_24H — score mémoire 9.534/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- TNSR-EUR — ACTIVE_NOW — score mémoire 9.496/10 — sources ACCELERATION, V4 — DETECTED_BUT_TOO_LATE
- ZKJ-EUR — MEMORY_24H — score mémoire 9.182/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- THQ-EUR — MEMORY_24H — score mémoire 9.062/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- LUMIA-EUR — MEMORY_24H — score mémoire 8.655/10 — sources ACCELERATION — MEMORY_ONLY
- FTT-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION, V4 — MEMORY_ONLY

## Audit des plus fortes hausses

- ICX-EUR +109.68% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- ZRC-EUR +107.99% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ZETA-EUR +57.78% — NOT_DETECTED — couche SCANNER_COVERAGE — action NOT_APPLICABLE
- PHA-EUR +40.19% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- AIOZ-EUR +37.18% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- FORM-EUR +36.20% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- PTB-EUR +31.51% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- SWELL-EUR +28.48% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- NOS-EUR +24.68% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- PEPE-EUR +23.91% — DETECTED_EARLY — couche NONE — action NONE

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
