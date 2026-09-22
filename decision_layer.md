# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-22T04:23:11.933843+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : HBAR-EUR | action ACHETE_MAINTENANT | opportunité 8.710 | entrée 7.600 | trend 7.850 | rang 7.781
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : SOL-EUR | action PLACE_LIMITE_PASSIVE | opportunité 7.668 | entrée 6.000 | trend 8.500 | rang 7.534
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : INIT-EUR | action LATENT_ACCELERATOR | opportunité 8.069 | entrée 5.550 | trend 8.900 | rang 7.645
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : MERL-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.212 | entrée 6.550 | trend 8.950 | rang 7.965
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. MERL-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.965
2. PROVE-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.799
3. HBAR-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 7.781

## Accélération indépendante

- ICX-EUR — CONFIRMED_ACCELERATION — score 10.000/10 — DETECTED_BUT_TOO_LATE
- PNUT-EUR — CONFIRMED_ACCELERATION — score 8.930/10 — DETECTED_BUT_TOO_LATE
- MEW-EUR — CONFIRMED_ACCELERATION — score 8.523/10 — DETECTED_BUT_TOO_LATE
- FARTCOIN-EUR — CONFIRMED_ACCELERATION — score 7.581/10 — DETECTED_BUT_TOO_LATE
- DOGS-EUR — CONFIRMED_ACCELERATION — score 7.526/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- TOSHI-EUR — CONFIRMED_ACCELERATION — score 6.730/10 — DETECTED_BUT_TOO_LATE
- SAGA-EUR — CONFIRMED_ACCELERATION — score 6.658/10 — DETECTED_BUT_TOO_LATE
- TRAC-EUR — BUILDING_ACCELERATION — score 6.172/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- GOAT-EUR — BUILDING_ACCELERATION — score 5.643/10 — DETECTED_BUT_TOO_LATE
- TRUMP-EUR — BUILDING_ACCELERATION — score 5.572/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- HBAR-EUR — ACTIVE_NOW — score mémoire 7.781/10 — sources ACCELERATION, DECISION_LAYER, V4 — BUYABLE_NOW
- ICX-EUR — ACTIVE_NOW — score mémoire 10.000/10 — sources ACCELERATION, V4 — DETECTED_BUT_TOO_LATE
- GIGA-EUR — MEMORY_24H — score mémoire 9.738/10 — sources ACCELERATION — MEMORY_ONLY
- PHA-EUR — MEMORY_24H — score mémoire 9.177/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- BTT-EUR — MEMORY_24H — score mémoire 9.062/10 — sources ACCELERATION — MEMORY_ONLY
- SWEAT-EUR — MEMORY_24H — score mémoire 9.062/10 — sources ACCELERATION — MEMORY_ONLY
- PNUT-EUR — ACTIVE_NOW — score mémoire 8.930/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- ZEUS-EUR — MEMORY_24H — score mémoire 8.781/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- DGB-EUR — MEMORY_24H — score mémoire 8.732/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- MEW-EUR — ACTIVE_NOW — score mémoire 8.523/10 — sources ACCELERATION, V4 — DETECTED_BUT_TOO_LATE

## Audit des plus fortes hausses

- ICX-EUR +119.84% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- ZRC-EUR +75.77% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- KERNEL-EUR +46.67% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- AIOZ-EUR +44.45% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- PHA-EUR +36.79% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- PEPE-EUR +33.68% — DETECTED_EARLY — couche NONE — action NONE
- WIF-EUR +26.88% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- CARV-EUR +22.72% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- FORM-EUR +21.10% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- DOGE-EUR +19.64% — DETECTED_EARLY — couche NONE — action INTERPRETATION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
