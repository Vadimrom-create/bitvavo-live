# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-21T13:46:16.245676+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : LTC-EUR | action ACHETE_MAINTENANT | opportunité 7.695 | entrée 7.350 | trend 7.900 | rang 7.251
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : HBAR-EUR | action PLACE_LIMITE_PASSIVE | opportunité 7.666 | entrée 6.750 | trend 8.450 | rang 7.498
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : CAKE-EUR | action LATENT_ACCELERATOR | opportunité 9.134 | entrée 5.600 | trend 7.900 | rang 7.729
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : ACH-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.646 | entrée 5.950 | trend 9.000 | rang 8.171
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. ACH-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.171
2. COW-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.014
3. KAS-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.903

## Accélération indépendante

- GIGA-EUR — CONFIRMED_ACCELERATION — score 10.000/10 — DETECTED_BUT_TOO_LATE
- FTT-EUR — CONFIRMED_ACCELERATION — score 8.500/10 — DETECTED_BUT_TOO_LATE
- MLN-EUR — CONFIRMED_ACCELERATION — score 8.288/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- HFT-EUR — CONFIRMED_ACCELERATION — score 7.367/10 — DETECTED_BUT_TOO_LATE
- ARX-EUR — CONFIRMED_ACCELERATION — score 7.110/10 — DETECTED_BUT_TOO_LATE
- PROVE-EUR — BUILDING_ACCELERATION — score 6.443/10 — DETECTED_BUT_TOO_LATE
- ZIG-EUR — BUILDING_ACCELERATION — score 5.551/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- BTT-EUR — BUILDING_ACCELERATION — score 5.449/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- ACX-EUR — BUILDING_ACCELERATION — score 5.422/10 — DETECTED_BUT_TOO_LATE
- PONKE-EUR — BUILDING_ACCELERATION — score 5.285/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- LTC-EUR — ACTIVE_NOW — score mémoire 7.251/10 — sources ACCELERATION, DECISION_LAYER, V4 — BUYABLE_NOW
- GIGA-EUR — ACTIVE_NOW — score mémoire 10.000/10 — sources ACCELERATION — DETECTED_BUT_TOO_LATE
- EDGE-EUR — MEMORY_24H — score mémoire 9.925/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- TAI-EUR — MEMORY_24H — score mémoire 9.488/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- RLC-EUR — MEMORY_24H — score mémoire 9.465/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- ACU-EUR — MEMORY_24H — score mémoire 9.053/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- ARB-EUR — MEMORY_24H — score mémoire 8.746/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- FTT-EUR — ACTIVE_NOW — score mémoire 8.500/10 — sources ACCELERATION, V4 — DETECTED_BUT_TOO_LATE
- TREAD-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- ICX-EUR — MEMORY_24H — score mémoire 8.457/10 — sources ACCELERATION, V4 — MEMORY_ONLY

## Audit des plus fortes hausses

- ZETA-EUR +63.13% — NOT_DETECTED — couche SCANNER_COVERAGE — action NOT_APPLICABLE
- PHA-EUR +57.20% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- PTB-EUR +51.30% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- AIOZ-EUR +33.75% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- FTT-EUR +33.57% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- PROVE-EUR +29.96% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- NIL-EUR +29.22% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- SUI-EUR +28.23% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- SEI-EUR +27.77% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- KMNO-EUR +27.65% — DETECTED_EARLY — couche NONE — action INTERPRETATION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
