# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-23T20:02:15.561775+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : AERO-EUR | action ACHETE_MAINTENANT | opportunité 8.535 | entrée 6.950 | trend 8.450 | rang 7.949
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : aucun candidat matériel
- **MEILLEUR_LATENT_ACCELERATOR** : LIGHTER-EUR | action LATENT_ACCELERATOR | opportunité 7.438 | entrée 5.700 | trend 8.400 | rang 6.842
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : BEAM-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.770 | entrée 5.850 | trend 8.150 | rang 7.788
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. AERO-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 7.949
2. LTC-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 7.902
3. BEAM-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.788

## Accélération indépendante

- AMP-EUR — CONFIRMED_ACCELERATION — score 10.000/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- CELR-EUR — BUILDING_ACCELERATION — score 6.072/10 — DETECTED_BUT_TOO_LATE
- CSPR-EUR — BUILDING_ACCELERATION — score 5.482/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- SWELL-EUR — BUILDING_ACCELERATION — score 5.215/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- AMP-EUR — ACTIVE_NOW — score mémoire 10.000/10 — sources ACCELERATION, V4 — WATCH_ONLY
- SOSO-EUR — MEMORY_24H — score mémoire 9.254/10 — sources ACCELERATION — MEMORY_ONLY
- TRIA-EUR — MEMORY_24H — score mémoire 9.219/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- U-EUR — MEMORY_24H — score mémoire 9.175/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- ICX-EUR — MEMORY_24H — score mémoire 8.369/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- WIN-EUR — MEMORY_24H — score mémoire 8.088/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- ZBCN-EUR — MEMORY_24H — score mémoire 8.056/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- AERO-EUR — ACTIVE_NOW — score mémoire 7.949/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- LTC-EUR — ACTIVE_NOW — score mémoire 7.902/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- XRP-EUR — MEMORY_24H — score mémoire 7.855/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY

## Audit des plus fortes hausses

- SAGA-EUR +30.33% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- CPOOL-EUR +28.08% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- DBR-EUR +24.61% — NOT_DETECTED — couche SCANNER_COVERAGE — action NOT_APPLICABLE
- NIL-EUR +23.46% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- RAY-EUR +19.74% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- SUPER-EUR +15.88% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- ZRO-EUR +15.34% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- LIGHTER-EUR +13.36% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- MET-EUR +12.08% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- ALLO-EUR +9.51% — DETECTED_EARLY — couche NONE — action INTERPRETATION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
