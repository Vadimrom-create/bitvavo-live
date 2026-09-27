# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-27T15:30:03.312770+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : TRUST-EUR | action PLACE_LIMITE_PASSIVE | opportunité 8.134 | entrée 6.000 | trend 9.000 | rang 7.874
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : AXL-EUR | action LATENT_ACCELERATOR | opportunité 8.182 | entrée 5.000 | trend 8.950 | rang 7.826
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : XDC-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 9.206 | entrée 7.300 | trend 8.350 | rang 8.296
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. XDC-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.296
2. RENDER-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.214
3. AAVE-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.133

## Accélération indépendante

- W-EUR — CONFIRMED_ACCELERATION — score 6.910/10 — DETECTED_BUT_TOO_LATE
- AGI-EUR — BUILDING_ACCELERATION — score 5.883/10 — DETECTED_BUT_TOO_LATE
- XDC-EUR — BUILDING_ACCELERATION — score 5.723/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- ALIGN-EUR — BUILDING_ACCELERATION — score 5.451/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- MMT-EUR — MEMORY_24H — score mémoire 9.122/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- GROVE-EUR — MEMORY_24H — score mémoire 8.518/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- FRAX-EUR — MEMORY_24H — score mémoire 8.380/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- SOON-EUR — MEMORY_24H — score mémoire 8.344/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- XDC-EUR — ACTIVE_NOW — score mémoire 8.296/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- RENDER-EUR — ACTIVE_NOW — score mémoire 8.214/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- AAVE-EUR — ACTIVE_NOW — score mémoire 8.133/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- AXS-EUR — ACTIVE_NOW — score mémoire 8.048/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- FET-EUR — ACTIVE_NOW — score mémoire 8.022/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- TRUST-EUR — ACTIVE_NOW — score mémoire 7.874/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY

## Audit des plus fortes hausses

- QNT-EUR +57.50% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- TREAD-EUR +49.46% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- SOON-EUR +35.00% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- GLMR-EUR +34.43% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- AGI-EUR +28.38% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ARX-EUR +27.56% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- AUDIO-EUR +26.67% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- W-EUR +17.24% — DETECTED_EARLY — couche NONE — action NONE
- GRASS-EUR +16.91% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- WELL-EUR +11.21% — NOT_DETECTED — couche SCANNER_COVERAGE — action NOT_APPLICABLE

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
