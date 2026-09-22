# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-22T02:55:56.753714+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : TAIKO-EUR | action ACHETE_MAINTENANT | opportunité 8.123 | entrée 7.050 | trend 8.700 | rang 7.869
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : ICP-EUR | action PLACE_LIMITE_PASSIVE | opportunité 7.490 | entrée 6.000 | trend 8.250 | rang 7.375
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : BEAM-EUR | action LATENT_ACCELERATOR | opportunité 7.941 | entrée 5.550 | trend 8.500 | rang 7.452
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : MERL-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.427 | entrée 6.450 | trend 8.950 | rang 8.062
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. MERL-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.062
2. SOMI-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.899
3. TAIKO-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 7.869

## Accélération indépendante

- PHA-EUR — CONFIRMED_ACCELERATION — score 9.177/10 — DETECTED_BUT_TOO_LATE
- ZETA-EUR — CONFIRMED_ACCELERATION — score 8.967/10 — DETECTED_BUT_TOO_LATE
- EPIC-EUR — CONFIRMED_ACCELERATION — score 8.334/10 — DETECTED_BUT_TOO_LATE
- XYO-EUR — CONFIRMED_ACCELERATION — score 6.713/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- LUMIA-EUR — BUILDING_ACCELERATION — score 5.885/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- NIL-EUR — BUILDING_ACCELERATION — score 5.265/10 — DETECTED_BUT_TOO_LATE
- SHELL-EUR — BUILDING_ACCELERATION — score 5.260/10 — DETECTED_BUT_TOO_LATE
- SOMI-EUR — BUILDING_ACCELERATION — score 4.928/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- GWEI-EUR — BUILDING_ACCELERATION — score 4.906/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- ARK-EUR — BUILDING_ACCELERATION — score 4.844/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- GIGA-EUR — MEMORY_24H — score mémoire 9.738/10 — sources ACCELERATION — MEMORY_ONLY
- PHA-EUR — ACTIVE_NOW — score mémoire 9.177/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- SWEAT-EUR — MEMORY_24H — score mémoire 9.062/10 — sources ACCELERATION — MEMORY_ONLY
- BOB-EUR — MEMORY_24H — score mémoire 9.007/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- ZETA-EUR — ACTIVE_NOW — score mémoire 8.967/10 — sources ACCELERATION, V4 — DETECTED_BUT_TOO_LATE
- ZEUS-EUR — MEMORY_24H — score mémoire 8.781/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- DGB-EUR — MEMORY_24H — score mémoire 8.732/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- AIOZ-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- PUFFER-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- XMN-EUR — MEMORY_24H — score mémoire 8.438/10 — sources ACCELERATION — MEMORY_ONLY

## Audit des plus fortes hausses

- ICX-EUR +85.93% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- ZRC-EUR +76.08% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ZETA-EUR +60.28% — NOT_DETECTED — couche SCANNER_COVERAGE — action NOT_APPLICABLE
- KERNEL-EUR +55.70% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- PHA-EUR +42.86% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- AIOZ-EUR +40.80% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- FORM-EUR +29.08% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- PEPE-EUR +25.44% — DETECTED_EARLY — couche NONE — action NONE
- WIF-EUR +23.06% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- NOS-EUR +22.03% — DETECTED_EARLY — couche NONE — action INTERPRETATION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
