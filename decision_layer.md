# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-22T07:24:00.231677+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : TREE-EUR | action PLACE_LIMITE_PASSIVE | opportunité 8.546 | entrée 5.800 | trend 7.950 | rang 7.626
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : INIT-EUR | action LATENT_ACCELERATOR | opportunité 8.441 | entrée 5.550 | trend 9.200 | rang 8.018
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : 0G-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.403 | entrée 6.250 | trend 8.600 | rang 7.813
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. INIT-EUR — MEILLEUR_LATENT_ACCELERATOR — LATENT_ACCELERATOR — rank 8.018
2. 0G-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.813
3. S-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.798

## Accélération indépendante

- VELO-EUR — CONFIRMED_ACCELERATION — score 7.635/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- USELESS-EUR — CONFIRMED_ACCELERATION — score 7.618/10 — DETECTED_BUT_TOO_LATE
- MLN-EUR — CONFIRMED_ACCELERATION — score 7.126/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- FORM-EUR — CONFIRMED_ACCELERATION — score 7.104/10 — DETECTED_BUT_TOO_LATE
- ICX-EUR — CONFIRMED_ACCELERATION — score 6.739/10 — DETECTED_BUT_TOO_LATE
- WIF-EUR — BUILDING_ACCELERATION — score 6.282/10 — DETECTED_BUT_TOO_LATE
- C-EUR — BUILDING_ACCELERATION — score 5.789/10 — DETECTED_BUT_TOO_LATE
- REZ-EUR — BUILDING_ACCELERATION — score 5.576/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- S-EUR — BUILDING_ACCELERATION — score 5.192/10 — DETECTED_BUT_TOO_LATE
- TOWNS-EUR — BUILDING_ACCELERATION — score 4.847/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- PHA-EUR — MEMORY_24H — score mémoire 9.177/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- GIGA-EUR — MEMORY_24H — score mémoire 9.062/10 — sources ACCELERATION — MEMORY_ONLY
- SWEAT-EUR — MEMORY_24H — score mémoire 9.062/10 — sources ACCELERATION — MEMORY_ONLY
- FLOCK-EUR — MEMORY_24H — score mémoire 8.979/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- ZEUS-EUR — MEMORY_24H — score mémoire 8.781/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- MEW-EUR — MEMORY_24H — score mémoire 8.523/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- XMN-EUR — MEMORY_24H — score mémoire 8.438/10 — sources ACCELERATION — MEMORY_ONLY
- BTT-EUR — MEMORY_24H — score mémoire 8.098/10 — sources ACCELERATION — MEMORY_ONLY
- INIT-EUR — ACTIVE_NOW — score mémoire 8.018/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- 0G-EUR — ACTIVE_NOW — score mémoire 7.813/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY

## Audit des plus fortes hausses

- ICX-EUR +108.82% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- ZRC-EUR +105.41% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- AIOZ-EUR +46.20% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- KERNEL-EUR +32.04% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- PEPE-EUR +28.72% — DETECTED_EARLY — couche NONE — action NONE
- WIF-EUR +23.82% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- GRASS-EUR +22.95% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- FORM-EUR +22.50% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- USELESS-EUR +19.99% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- FLOCK-EUR +19.88% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
