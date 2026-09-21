# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-21T14:40:12.683840+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : STX-EUR | action ACHETE_MAINTENANT | opportunité 9.361 | entrée 7.550 | trend 8.600 | rang 8.443
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : PORTAL-EUR | action PLACE_LIMITE_PASSIVE | opportunité 7.669 | entrée 5.800 | trend 8.650 | rang 7.482
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : ACH-EUR | action LATENT_ACCELERATOR | opportunité 7.730 | entrée 5.000 | trend 9.000 | rang 7.636
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : MERL-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.386 | entrée 7.050 | trend 8.950 | rang 8.115
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. STX-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.443
2. MERL-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.115
3. COW-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.017

## Accélération indépendante

- LQTY-EUR — CONFIRMED_ACCELERATION — score 8.646/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- C-EUR — CONFIRMED_ACCELERATION — score 8.215/10 — DETECTED_BUT_TOO_LATE
- NEIRO-EUR — CONFIRMED_ACCELERATION — score 7.366/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- MEGA-EUR — CONFIRMED_ACCELERATION — score 6.746/10 — DETECTED_BUT_TOO_LATE
- EPIC-EUR — BUILDING_ACCELERATION — score 5.717/10 — DETECTED_BUT_TOO_LATE
- AGI-EUR — BUILDING_ACCELERATION — score 5.595/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- DEEP-EUR — BUILDING_ACCELERATION — score 5.443/10 — DETECTED_BUT_TOO_LATE
- SUI-EUR — BUILDING_ACCELERATION — score 5.345/10 — DETECTED_BUT_TOO_LATE
- MET-EUR — BUILDING_ACCELERATION — score 5.314/10 — DETECTED_BUT_TOO_LATE
- BONK-EUR — BUILDING_ACCELERATION — score 5.313/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- EDGE-EUR — MEMORY_24H — score mémoire 9.925/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- TAI-EUR — MEMORY_24H — score mémoire 9.488/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- ACU-EUR — MEMORY_24H — score mémoire 9.053/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- ARB-EUR — MEMORY_24H — score mémoire 8.746/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- LQTY-EUR — ACTIVE_NOW — score mémoire 8.646/10 — sources ACCELERATION, V4 — WATCH_ONLY
- FTT-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- TREAD-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- ICX-EUR — MEMORY_24H — score mémoire 8.457/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- STX-EUR — ACTIVE_NOW — score mémoire 8.443/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- SFP-EUR — MEMORY_24H — score mémoire 8.323/10 — sources ACCELERATION — MEMORY_ONLY

## Audit des plus fortes hausses

- ZETA-EUR +72.22% — NOT_DETECTED — couche SCANNER_COVERAGE — action NOT_APPLICABLE
- PHA-EUR +55.90% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- PTB-EUR +41.69% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- AIOZ-EUR +33.71% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- KMNO-EUR +31.06% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- FTT-EUR +30.22% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- NIL-EUR +29.96% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- SUI-EUR +26.51% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- SEI-EUR +26.22% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- PROVE-EUR +24.85% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
