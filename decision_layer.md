# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-24T14:25:02.985555+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : UNI-EUR | action ACHETE_MAINTENANT | opportunité 9.180 | entrée 7.850 | trend 7.750 | rang 8.044
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : 0G-EUR | action PLACE_LIMITE_PASSIVE | opportunité 8.319 | entrée 6.100 | trend 8.650 | rang 7.783
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : SIGN-EUR | action LATENT_ACCELERATOR | opportunité 8.298 | entrée 4.500 | trend 8.950 | rang 7.670
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : DRIFT-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.327 | entrée 6.450 | trend 8.650 | rang 7.847
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. UNI-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.044
2. ADA-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.014
3. HBAR-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 7.977

## Accélération indépendante

- EIGEN-EUR — CONFIRMED_ACCELERATION — score 9.309/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- DYDX-EUR — CONFIRMED_ACCELERATION — score 9.010/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- 2Z-EUR — CONFIRMED_ACCELERATION — score 8.723/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- ZK-EUR — CONFIRMED_ACCELERATION — score 8.639/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- UMA-EUR — CONFIRMED_ACCELERATION — score 8.631/10 — DETECTED_BUT_TOO_LATE
- APT-EUR — CONFIRMED_ACCELERATION — score 8.469/10 — DETECTED_BUT_TOO_LATE
- SYRUP-EUR — CONFIRMED_ACCELERATION — score 8.308/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- PLUME-EUR — CONFIRMED_ACCELERATION — score 7.952/10 — DETECTED_BUT_TOO_LATE
- LDO-EUR — CONFIRMED_ACCELERATION — score 7.898/10 — DETECTED_BUT_TOO_LATE
- ONDO-EUR — CONFIRMED_ACCELERATION — score 7.380/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- ADA-EUR — ACTIVE_NOW — score mémoire 8.014/10 — sources ACCELERATION, DECISION_LAYER, V4 — BUYABLE_NOW
- HBAR-EUR — ACTIVE_NOW — score mémoire 7.977/10 — sources ACCELERATION, DECISION_LAYER, V4 — BUYABLE_NOW
- AMP-EUR — MEMORY_24H — score mémoire 10.000/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- ICX-EUR — MEMORY_24H — score mémoire 9.456/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- FLOCK-EUR — MEMORY_24H — score mémoire 9.446/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- EIGEN-EUR — ACTIVE_NOW — score mémoire 9.309/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- U-EUR — MEMORY_24H — score mémoire 9.175/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- DYDX-EUR — ACTIVE_NOW — score mémoire 9.010/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- 2Z-EUR — ACTIVE_NOW — score mémoire 8.723/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- ZK-EUR — ACTIVE_NOW — score mémoire 8.639/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY

## Audit des plus fortes hausses

- NOM-EUR +41.57% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- NIL-EUR +34.57% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- LSK-EUR +31.23% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ONDO-EUR +23.22% — DETECTED_EARLY — couche NONE — action NONE
- LTC-EUR +23.00% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- PLUME-EUR +16.44% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- MORPHO-EUR +15.96% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- ARX-EUR +15.48% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- ETC-EUR +15.33% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- ARK-EUR +12.21% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
