# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-21T13:27:44.531641+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : AERO-EUR | action ACHETE_MAINTENANT | opportunité 8.004 | entrée 7.250 | trend 8.450 | rang 7.725
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : TIA-EUR | action PLACE_LIMITE_PASSIVE | opportunité 7.506 | entrée 6.450 | trend 7.300 | rang 6.892
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : GRASS-EUR | action LATENT_ACCELERATOR | opportunité 7.447 | entrée 4.500 | trend 8.450 | rang 7.213
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : COW-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.280 | entrée 6.200 | trend 9.200 | rang 8.081
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. COW-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.081
2. KAS-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.034
3. SOL-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.871

## Accélération indépendante

- PROVE-EUR — CONFIRMED_ACCELERATION — score 8.500/10 — DETECTED_BUT_TOO_LATE
- AIOZ-EUR — CONFIRMED_ACCELERATION — score 6.921/10 — DETECTED_BUT_TOO_LATE
- OSMO-EUR — BUILDING_ACCELERATION — score 5.701/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- U-EUR — BUILDING_ACCELERATION — score 5.464/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- DBR-EUR — BUILDING_ACCELERATION — score 4.783/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- LTC-EUR — ACTIVE_NOW — score mémoire 7.653/10 — sources ACCELERATION, DECISION_LAYER, V4 — BUYABLE_NOW
- EDGE-EUR — MEMORY_24H — score mémoire 9.925/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- ARKM-EUR — MEMORY_24H — score mémoire 9.893/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- TAI-EUR — MEMORY_24H — score mémoire 9.488/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- RLC-EUR — MEMORY_24H — score mémoire 9.465/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- ACU-EUR — MEMORY_24H — score mémoire 9.053/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- ARB-EUR — MEMORY_24H — score mémoire 8.746/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- PROVE-EUR — ACTIVE_NOW — score mémoire 8.500/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- TREAD-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- ICX-EUR — MEMORY_24H — score mémoire 8.457/10 — sources ACCELERATION, V4 — MEMORY_ONLY

## Audit des plus fortes hausses

- ZETA-EUR +68.71% — NOT_DETECTED — couche SCANNER_COVERAGE — action NOT_APPLICABLE
- PHA-EUR +63.67% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- PTB-EUR +46.27% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- AIOZ-EUR +44.70% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- NIL-EUR +31.68% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- SEI-EUR +30.13% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- KMNO-EUR +28.45% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- SUI-EUR +27.59% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- FTT-EUR +26.63% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- DUSK-EUR +24.13% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
