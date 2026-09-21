# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-21T01:39:02.601642+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : TAO-EUR | action ACHETE_MAINTENANT | opportunité 8.721 | entrée 7.050 | trend 8.250 | rang 7.949
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : ARX-EUR | action PLACE_LIMITE_PASSIVE | opportunité 7.918 | entrée 6.100 | trend 8.900 | rang 7.818
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : ZK-EUR | action LATENT_ACCELERATOR | opportunité 7.898 | entrée 5.700 | trend 8.400 | rang 7.581
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : WAL-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.107 | entrée 6.050 | trend 9.200 | rang 7.958
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. WAL-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.958
2. TAO-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 7.949
3. AERO-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 7.929

## Accélération indépendante

- XPL-EUR — CONFIRMED_ACCELERATION — score 7.110/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- PEAQ-EUR — BUILDING_ACCELERATION — score 6.258/10 — DETECTED_BUT_TOO_LATE
- VVV-EUR — BUILDING_ACCELERATION — score 5.883/10 — DETECTED_BUT_TOO_LATE
- SYN-EUR — BUILDING_ACCELERATION — score 5.814/10 — DETECTED_BUT_TOO_LATE
- PONKE-EUR — BUILDING_ACCELERATION — score 5.456/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- ICNT-EUR — BUILDING_ACCELERATION — score 5.344/10 — DETECTED_BUT_TOO_LATE
- YB-EUR — BUILDING_ACCELERATION — score 5.142/10 — DETECTED_BUT_TOO_LATE
- MAVIA-EUR — BUILDING_ACCELERATION — score 4.879/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- TREAD-EUR — BUILDING_ACCELERATION — score 4.823/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- XPL-EUR — ACTIVE_NOW — score mémoire 7.110/10 — sources ACCELERATION, DECISION_LAYER, V4 — BUYABLE_NOW
- ICX-EUR — MEMORY_24H — score mémoire 9.062/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- NES-EUR — MEMORY_24H — score mémoire 8.883/10 — sources ACCELERATION — MEMORY_ONLY
- U-EUR — MEMORY_24H — score mémoire 8.376/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- UP-EUR — MEMORY_24H — score mémoire 8.113/10 — sources ACCELERATION — MEMORY_ONLY
- WAL-EUR — ACTIVE_NOW — score mémoire 7.958/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- TAO-EUR — ACTIVE_NOW — score mémoire 7.949/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- AERO-EUR — ACTIVE_NOW — score mémoire 7.929/10 — sources DECISION_LAYER, V4 — WATCH_ONLY
- INJ-EUR — ACTIVE_NOW — score mémoire 7.853/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- ARX-EUR — ACTIVE_NOW — score mémoire 7.818/10 — sources DECISION_LAYER, V4 — WATCH_ONLY

## Audit des plus fortes hausses

- SAGA-EUR +48.21% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- PTB-EUR +38.61% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- FTT-EUR +32.76% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- EPIC-EUR +24.77% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- NIL-EUR +23.29% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- KMNO-EUR +21.57% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- NEAR-EUR +18.29% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- CFG-EUR +17.83% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- VVV-EUR +17.30% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE
- S-EUR +15.57% — DETECTED_EARLY — couche NONE — action INTERPRETATION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
