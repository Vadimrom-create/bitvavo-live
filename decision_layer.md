# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-27T00:25:24.256106+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : WLD-EUR | action ACHETE_MAINTENANT | opportunité 8.117 | entrée 7.250 | trend 8.700 | rang 7.976
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : VTHO-EUR | action PLACE_LIMITE_PASSIVE | opportunité 7.618 | entrée 6.000 | trend 7.800 | rang 7.272
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : TNSR-EUR | action LATENT_ACCELERATOR | opportunité 8.120 | entrée 5.750 | trend 8.750 | rang 7.788
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : ROSE-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.602 | entrée 6.300 | trend 8.950 | rang 8.080
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. ROSE-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.080
2. COMP-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.990
3. EIGEN-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.981

## Accélération indépendante

- HFT-EUR — CONFIRMED_ACCELERATION — score 8.062/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- CTR-EUR — CONFIRMED_ACCELERATION — score 7.500/10 — DETECTED_BUT_TOO_LATE
- VTHO-EUR — CONFIRMED_ACCELERATION — score 6.762/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- PYTH-EUR — BUILDING_ACCELERATION — score 5.576/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- COW-EUR — BUILDING_ACCELERATION — score 5.000/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- PONKE-EUR — MEMORY_DECAY_24_72H — score mémoire 9.310/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- TAI-EUR — MEMORY_24H — score mémoire 9.062/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- ONT-EUR — MEMORY_DECAY_24_72H — score mémoire 8.799/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- VELO-EUR — MEMORY_24H — score mémoire 8.605/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- AMP-EUR — MEMORY_24H — score mémoire 8.528/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- ROSE-EUR — ACTIVE_NOW — score mémoire 8.080/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- HFT-EUR — ACTIVE_NOW — score mémoire 8.062/10 — sources ACCELERATION — WATCH_ONLY
- COMP-EUR — ACTIVE_NOW — score mémoire 7.990/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- EIGEN-EUR — ACTIVE_NOW — score mémoire 7.981/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- WLD-EUR — ACTIVE_NOW — score mémoire 7.976/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY

## Audit des plus fortes hausses

- AMP-EUR +56.63% — DETECTED_TOO_LATE — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- QNT-EUR +55.36% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- RARE-EUR +39.56% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- EDGE-EUR +34.44% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- KMNO-EUR +21.36% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- 2Z-EUR +20.30% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- RUNE-EUR +18.29% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE
- AGI-EUR +16.06% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- COW-EUR +15.49% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- GRASS-EUR +15.12% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
