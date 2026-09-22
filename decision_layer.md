# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-22T07:03:55.403023+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : INIT-EUR | action PLACE_LIMITE_PASSIVE | opportunité 8.613 | entrée 6.000 | trend 9.200 | rang 8.131
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : PYTH-EUR | action LATENT_ACCELERATOR | opportunité 7.695 | entrée 5.550 | trend 8.450 | rang 7.488
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : 0G-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.336 | entrée 6.550 | trend 8.600 | rang 7.866
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. INIT-EUR — MEILLEURE_LIMITE_PASSIVE — PLACE_LIMITE_PASSIVE — rank 8.131
2. 0G-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.866
3. THE-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.773

## Accélération indépendante

- FLOKI-EUR — CONFIRMED_ACCELERATION — score 6.602/10 — DETECTED_BUT_TOO_LATE
- TAI-EUR — BUILDING_ACCELERATION — score 5.138/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- BIO-EUR — BUILDING_ACCELERATION — score 4.893/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- PHA-EUR — MEMORY_24H — score mémoire 9.177/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- GIGA-EUR — MEMORY_24H — score mémoire 9.062/10 — sources ACCELERATION — MEMORY_ONLY
- SWEAT-EUR — MEMORY_24H — score mémoire 9.062/10 — sources ACCELERATION — MEMORY_ONLY
- VELO-EUR — MEMORY_24H — score mémoire 9.000/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- FLOCK-EUR — MEMORY_24H — score mémoire 8.979/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- ZEUS-EUR — MEMORY_24H — score mémoire 8.781/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- MEW-EUR — MEMORY_24H — score mémoire 8.523/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- XMN-EUR — MEMORY_24H — score mémoire 8.438/10 — sources ACCELERATION — MEMORY_ONLY
- INIT-EUR — ACTIVE_NOW — score mémoire 8.131/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- BTT-EUR — MEMORY_24H — score mémoire 8.098/10 — sources ACCELERATION — MEMORY_ONLY

## Audit des plus fortes hausses

- ICX-EUR +106.34% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- ZRC-EUR +101.09% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- AIOZ-EUR +52.57% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- PEPE-EUR +27.92% — DETECTED_EARLY — couche NONE — action NONE
- KERNEL-EUR +22.95% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- WIF-EUR +21.84% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- CARV-EUR +21.46% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- GRASS-EUR +21.40% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- FORM-EUR +19.17% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- FARTCOIN-EUR +17.62% — DETECTED_EARLY — couche NONE — action INTERPRETATION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
