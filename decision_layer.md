# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-22T05:32:23.091223+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : EPIC-EUR | action PLACE_LIMITE_PASSIVE | opportunité 7.504 | entrée 6.500 | trend 7.850 | rang 6.674
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : AXL-EUR | action LATENT_ACCELERATOR | opportunité 9.118 | entrée 4.800 | trend 8.000 | rang 7.890
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : MERL-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.795 | entrée 6.100 | trend 8.950 | rang 8.177
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. MERL-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.177
2. SSV-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.047
3. AXL-EUR — MEILLEUR_LATENT_ACCELERATOR — LATENT_ACCELERATOR — rank 7.890

## Accélération indépendante

- GIGA-EUR — CONFIRMED_ACCELERATION — score 9.062/10 — DETECTED_BUT_TOO_LATE
- AIOZ-EUR — CONFIRMED_ACCELERATION — score 8.449/10 — DETECTED_BUT_TOO_LATE
- DGB-EUR — CONFIRMED_ACCELERATION — score 6.575/10 — DETECTED_BUT_TOO_LATE
- ICX-EUR — CONFIRMED_ACCELERATION — score 6.549/10 — DETECTED_BUT_TOO_LATE
- SAGA-EUR — BUILDING_ACCELERATION — score 6.469/10 — DETECTED_BUT_TOO_LATE
- XDC-EUR — BUILDING_ACCELERATION — score 5.471/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- ZRC-EUR — MEMORY_24H — score mémoire 9.953/10 — sources ACCELERATION — MEMORY_ONLY
- PHA-EUR — MEMORY_24H — score mémoire 9.177/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- BTT-EUR — MEMORY_24H — score mémoire 9.062/10 — sources ACCELERATION — MEMORY_ONLY
- GIGA-EUR — ACTIVE_NOW — score mémoire 9.062/10 — sources ACCELERATION — DETECTED_BUT_TOO_LATE
- SWEAT-EUR — MEMORY_24H — score mémoire 9.062/10 — sources ACCELERATION — MEMORY_ONLY
- VELO-EUR — MEMORY_24H — score mémoire 9.000/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- ZEUS-EUR — MEMORY_24H — score mémoire 8.781/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- MEW-EUR — MEMORY_24H — score mémoire 8.523/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- AIOZ-EUR — ACTIVE_NOW — score mémoire 8.449/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- XMN-EUR — MEMORY_24H — score mémoire 8.438/10 — sources ACCELERATION — MEMORY_ONLY

## Audit des plus fortes hausses

- ZRC-EUR +100.64% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ICX-EUR +92.97% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- AIOZ-EUR +60.47% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- PHA-EUR +33.68% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- KERNEL-EUR +28.16% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- PEPE-EUR +24.16% — DETECTED_EARLY — couche NONE — action NONE
- GRASS-EUR +20.89% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- FORM-EUR +19.26% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- SAGA-EUR +17.93% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- SWELL-EUR +17.85% — DETECTED_EARLY — couche NONE — action INTERPRETATION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
