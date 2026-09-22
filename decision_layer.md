# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-22T12:17:17.207395+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : GOAT-EUR | action PLACE_LIMITE_PASSIVE | opportunité 7.842 | entrée 6.100 | trend 8.450 | rang 7.621
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : ARX-EUR | action LATENT_ACCELERATOR | opportunité 8.143 | entrée 5.550 | trend 8.550 | rang 7.580
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : NEAR-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.814 | entrée 8.250 | trend 8.100 | rang 7.938
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. NEAR-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.938
2. STX-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.852
3. FET-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.724

## Accélération indépendante

- XMN-EUR — CONFIRMED_ACCELERATION — score 9.774/10 — DETECTED_BUT_TOO_LATE
- NOS-EUR — CONFIRMED_ACCELERATION — score 7.037/10 — DETECTED_BUT_TOO_LATE
- ARX-EUR — CONFIRMED_ACCELERATION — score 6.639/10 — DETECTED_BUT_TOO_LATE
- PONKE-EUR — BUILDING_ACCELERATION — score 6.297/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- NEAR-EUR — BUILDING_ACCELERATION — score 5.130/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- XMN-EUR — ACTIVE_NOW — score mémoire 9.774/10 — sources ACCELERATION — DETECTED_BUT_TOO_LATE
- AUDIO-EUR — MEMORY_24H — score mémoire 9.640/10 — sources ACCELERATION — MEMORY_ONLY
- SWEAT-EUR — MEMORY_24H — score mémoire 9.062/10 — sources ACCELERATION — MEMORY_ONLY
- HFT-EUR — MEMORY_24H — score mémoire 8.783/10 — sources ACCELERATION — MEMORY_ONLY
- BTT-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION — MEMORY_ONLY
- GIGA-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION — MEMORY_ONLY
- U-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- NEAR-EUR — ACTIVE_NOW — score mémoire 7.938/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- STX-EUR — ACTIVE_NOW — score mémoire 7.852/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- FET-EUR — ACTIVE_NOW — score mémoire 7.724/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE

## Audit des plus fortes hausses

- ICX-EUR +96.86% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- ZRC-EUR +81.71% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- KERNEL-EUR +30.92% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- NIL-EUR +21.75% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- FORM-EUR +21.66% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- AIOZ-EUR +20.82% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- GRASS-EUR +16.99% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- PEPE-EUR +15.64% — DETECTED_EARLY — couche NONE — action NONE
- NOS-EUR +15.50% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- WIF-EUR +14.72% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
