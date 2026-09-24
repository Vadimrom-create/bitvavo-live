# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-24T20:09:28.808220+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : ZIG-EUR | action ACHETE_MAINTENANT | opportunité 9.240 | entrée 7.450 | trend 8.100 | rang 8.241
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : F-EUR | action PLACE_LIMITE_PASSIVE | opportunité 7.954 | entrée 6.150 | trend 7.950 | rang 7.446
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : IOST-EUR | action LATENT_ACCELERATOR | opportunité 9.079 | entrée 5.700 | trend 7.650 | rang 7.772
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : COMP-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.744 | entrée 7.050 | trend 9.000 | rang 8.063
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. ZIG-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.241
2. UNI-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.196
3. COMP-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.063

## Accélération indépendante

- TREAD-EUR — CONFIRMED_ACCELERATION — score 8.500/10 — DETECTED_BUT_TOO_LATE
- GIGA-EUR — CONFIRMED_ACCELERATION — score 7.176/10 — DETECTED_BUT_TOO_LATE
- FRAX-EUR — CONFIRMED_ACCELERATION — score 6.567/10 — DETECTED_BUT_TOO_LATE
- TAI-EUR — BUILDING_ACCELERATION — score 6.479/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- ALIGN-EUR — BUILDING_ACCELERATION — score 6.291/10 — DETECTED_BUT_TOO_LATE
- ZRC-EUR — BUILDING_ACCELERATION — score 6.056/10 — DETECTED_BUT_TOO_LATE
- ICX-EUR — BUILDING_ACCELERATION — score 5.106/10 — DETECTED_BUT_TOO_LATE
- SHELL-EUR — BUILDING_ACCELERATION — score 4.902/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- FET-EUR — ACTIVE_NOW — score mémoire 7.324/10 — sources ACCELERATION, DECISION_LAYER, V4 — BUYABLE_NOW
- VVV-EUR — ACTIVE_NOW — score mémoire 6.363/10 — sources ACCELERATION, DECISION_LAYER, V4 — BUYABLE_NOW
- DYDX-EUR — MEMORY_24H — score mémoire 9.010/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- XYO-EUR — MEMORY_24H — score mémoire 8.937/10 — sources ACCELERATION — MEMORY_ONLY
- CNPY-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- TREAD-EUR — ACTIVE_NOW — score mémoire 8.500/10 — sources ACCELERATION, V4 — DETECTED_BUT_TOO_LATE
- HFT-EUR — MEMORY_24H — score mémoire 8.258/10 — sources ACCELERATION — MEMORY_ONLY
- ZIG-EUR — ACTIVE_NOW — score mémoire 8.241/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- UNI-EUR — ACTIVE_NOW — score mémoire 8.196/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- COMP-EUR — ACTIVE_NOW — score mémoire 8.063/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE

## Audit des plus fortes hausses

- XAI-EUR +40.56% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- LSK-EUR +35.69% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- TREAD-EUR +34.77% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ONDO-EUR +24.57% — DETECTED_EARLY — couche NONE — action NONE
- NOM-EUR +22.32% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- QNT-EUR +21.90% — DETECTED_EARLY — couche NONE — action NONE
- XPL-EUR +21.09% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- PEAQ-EUR +19.20% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- PLUME-EUR +18.84% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- ARK-EUR +18.21% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
