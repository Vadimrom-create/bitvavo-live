# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-22T19:47:52.363156+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : LTC-EUR | action ACHETE_MAINTENANT | opportunité 9.272 | entrée 8.400 | trend 8.200 | rang 8.343
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : LISTA-EUR | action PLACE_LIMITE_PASSIVE | opportunité 7.977 | entrée 6.000 | trend 8.500 | rang 7.689
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : BEAM-EUR | action LATENT_ACCELERATOR | opportunité 7.587 | entrée 5.750 | trend 8.500 | rang 7.404
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : VET-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 9.261 | entrée 8.300 | trend 8.100 | rang 8.274
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. LTC-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.343
2. VET-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.274
3. RUNE-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.037

## Accélération indépendante

- TREAD-EUR — CONFIRMED_ACCELERATION — score 9.440/10 — DETECTED_BUT_TOO_LATE
- RAD-EUR — BUILDING_ACCELERATION — score 6.355/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- USELESS-EUR — BUILDING_ACCELERATION — score 6.255/10 — DETECTED_BUT_TOO_LATE
- FTT-EUR — BUILDING_ACCELERATION — score 6.222/10 — DETECTED_BUT_TOO_LATE
- TIA-EUR — BUILDING_ACCELERATION — score 5.661/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- TREAD-EUR — ACTIVE_NOW — score mémoire 9.440/10 — sources ACCELERATION, V4 — DETECTED_BUT_TOO_LATE
- TAI-EUR — MEMORY_24H — score mémoire 9.000/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- DEGEN-EUR — MEMORY_24H — score mémoire 8.739/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- APE-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- AUDIO-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION — MEMORY_ONLY
- LTC-EUR — ACTIVE_NOW — score mémoire 8.343/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- VET-EUR — ACTIVE_NOW — score mémoire 8.274/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- KAITO-EUR — MEMORY_24H — score mémoire 8.161/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- RUNE-EUR — ACTIVE_NOW — score mémoire 8.037/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- KMNO-EUR — ACTIVE_NOW — score mémoire 7.965/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY

## Audit des plus fortes hausses

- DRIFT-EUR +44.99% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- CHR-EUR +34.64% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- BCH-EUR +25.44% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- KERNEL-EUR +24.64% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- NIL-EUR +20.12% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- USELESS-EUR +17.83% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- KITE-EUR +17.51% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- TREAD-EUR +16.13% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- GRASS-EUR +16.02% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- GOAT-EUR +15.13% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
