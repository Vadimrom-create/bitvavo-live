# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-27T01:02:39.111192+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : GALA-EUR | action ACHETE_MAINTENANT | opportunité 8.024 | entrée 7.300 | trend 9.000 | rang 8.016
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : EIGEN-EUR | action PLACE_LIMITE_PASSIVE | opportunité 7.973 | entrée 5.800 | trend 9.200 | rang 7.916
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : FLUX-EUR | action LATENT_ACCELERATOR | opportunité 8.309 | entrée 5.450 | trend 8.950 | rang 7.822
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : SPK-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.691 | entrée 5.450 | trend 8.700 | rang 8.024
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. SPK-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.024
2. GALA-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.016
3. OP-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.986

## Accélération indépendante

- W-EUR — CONFIRMED_ACCELERATION — score 9.239/10 — DETECTED_BUT_TOO_LATE
- SOON-EUR — CONFIRMED_ACCELERATION — score 7.916/10 — DETECTED_BUT_TOO_LATE
- HFT-EUR — BUILDING_ACCELERATION — score 6.000/10 — DETECTED_BUT_TOO_LATE
- TREAD-EUR — BUILDING_ACCELERATION — score 5.430/10 — DETECTED_BUT_TOO_LATE
- BAND-EUR — BUILDING_ACCELERATION — score 5.293/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- W-EUR — ACTIVE_NOW — score mémoire 9.239/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- PONKE-EUR — MEMORY_DECAY_24_72H — score mémoire 9.186/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- TAI-EUR — MEMORY_24H — score mémoire 9.062/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- RARE-EUR — MEMORY_24H — score mémoire 8.845/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- ONT-EUR — MEMORY_DECAY_24_72H — score mémoire 8.684/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- VELO-EUR — MEMORY_24H — score mémoire 8.605/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- AMP-EUR — MEMORY_24H — score mémoire 8.528/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- SPK-EUR — ACTIVE_NOW — score mémoire 8.024/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- GALA-EUR — ACTIVE_NOW — score mémoire 8.016/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- OP-EUR — ACTIVE_NOW — score mémoire 7.986/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY

## Audit des plus fortes hausses

- QNT-EUR +62.98% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- AMP-EUR +56.65% — DETECTED_TOO_LATE — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- HFT-EUR +40.46% — NOT_DETECTED — couche SCANNER_COVERAGE — action NOT_APPLICABLE
- RARE-EUR +32.56% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- 2Z-EUR +19.88% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- RUNE-EUR +18.18% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE
- SOON-EUR +17.90% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- TREAD-EUR +16.36% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- KMNO-EUR +15.87% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- COW-EUR +15.65% — DETECTED_EARLY — couche NONE — action INTERPRETATION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
