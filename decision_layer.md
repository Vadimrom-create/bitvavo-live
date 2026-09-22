# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-22T17:58:35.657489+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : SOL-EUR | action ACHETE_MAINTENANT | opportunité 8.074 | entrée 7.450 | trend 8.750 | rang 7.970
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : ZEN-EUR | action PLACE_LIMITE_PASSIVE | opportunité 8.471 | entrée 6.750 | trend 8.300 | rang 7.803
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : SOMI-EUR | action LATENT_ACCELERATOR | opportunité 8.272 | entrée 5.600 | trend 7.800 | rang 7.473
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : JUP-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 9.234 | entrée 7.400 | trend 8.050 | rang 7.964
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. SOL-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 7.970
2. JUP-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.964
3. TAIKO-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 7.896

## Accélération indépendante

- DRIFT-EUR — CONFIRMED_ACCELERATION — score 9.779/10 — DETECTED_BUT_TOO_LATE
- TAI-EUR — CONFIRMED_ACCELERATION — score 9.000/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- TRAC-EUR — CONFIRMED_ACCELERATION — score 7.788/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- ZRC-EUR — CONFIRMED_ACCELERATION — score 7.577/10 — DETECTED_BUT_TOO_LATE
- NIL-EUR — BUILDING_ACCELERATION — score 5.694/10 — DETECTED_BUT_TOO_LATE
- FOLD-EUR — BUILDING_ACCELERATION — score 4.855/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- DRIFT-EUR — ACTIVE_NOW — score mémoire 9.779/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- TAI-EUR — ACTIVE_NOW — score mémoire 9.000/10 — sources ACCELERATION, V4 — WATCH_ONLY
- DEGEN-EUR — MEMORY_24H — score mémoire 8.739/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- APE-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- AUDIO-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION — MEMORY_ONLY
- HMSTR-EUR — MEMORY_24H — score mémoire 8.203/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- SOL-EUR — ACTIVE_NOW — score mémoire 7.970/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- JUP-EUR — ACTIVE_NOW — score mémoire 7.964/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- TAIKO-EUR — ACTIVE_NOW — score mémoire 7.896/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- HYPE-EUR — ACTIVE_NOW — score mémoire 7.888/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY

## Audit des plus fortes hausses

- CHR-EUR +43.57% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- NIL-EUR +32.30% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- BCH-EUR +27.29% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- DRIFT-EUR +25.18% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- KERNEL-EUR +24.21% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ZRO-EUR +21.68% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- GRASS-EUR +18.45% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- FLOCK-EUR +17.04% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- KITE-EUR +16.52% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- MERL-EUR +15.57% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
