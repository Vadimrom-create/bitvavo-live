# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-22T03:50:04.239106+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : TAIKO-EUR | action ACHETE_MAINTENANT | opportunité 9.187 | entrée 7.500 | trend 8.700 | rang 8.428
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : 0G-EUR | action PLACE_LIMITE_PASSIVE | opportunité 8.516 | entrée 6.000 | trend 8.450 | rang 7.369
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : BEAM-EUR | action LATENT_ACCELERATOR | opportunité 7.611 | entrée 5.550 | trend 8.500 | rang 7.467
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : KAS-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.493 | entrée 7.500 | trend 8.350 | rang 7.918
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. TAIKO-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.428
2. HBAR-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.285
3. PYTH-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.105

## Accélération indépendante

- BTT-EUR — CONFIRMED_ACCELERATION — score 9.062/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- CARV-EUR — CONFIRMED_ACCELERATION — score 8.500/10 — DETECTED_BUT_TOO_LATE
- 0G-EUR — CONFIRMED_ACCELERATION — score 7.047/10 — DETECTED_BUT_TOO_LATE
- CHILLGUY-EUR — CONFIRMED_ACCELERATION — score 6.834/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- PROMPT-EUR — CONFIRMED_ACCELERATION — score 6.775/10 — DETECTED_BUT_TOO_LATE
- SAFE-EUR — BUILDING_ACCELERATION — score 6.043/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- PUFFER-EUR — BUILDING_ACCELERATION — score 5.804/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- ZRC-EUR — BUILDING_ACCELERATION — score 5.588/10 — DETECTED_BUT_TOO_LATE
- FARTCOIN-EUR — BUILDING_ACCELERATION — score 5.511/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- GIGA-EUR — MEMORY_24H — score mémoire 9.738/10 — sources ACCELERATION — MEMORY_ONLY
- PEPE-EUR — MEMORY_24H — score mémoire 9.294/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- PHA-EUR — MEMORY_24H — score mémoire 9.177/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- BTT-EUR — ACTIVE_NOW — score mémoire 9.062/10 — sources ACCELERATION — WATCH_ONLY
- SWEAT-EUR — MEMORY_24H — score mémoire 9.062/10 — sources ACCELERATION — MEMORY_ONLY
- ZEUS-EUR — MEMORY_24H — score mémoire 8.781/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- DGB-EUR — MEMORY_24H — score mémoire 8.732/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- AIOZ-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- CARV-EUR — ACTIVE_NOW — score mémoire 8.500/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- XMN-EUR — MEMORY_24H — score mémoire 8.438/10 — sources ACCELERATION — MEMORY_ONLY

## Audit des plus fortes hausses

- ICX-EUR +91.42% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- ZRC-EUR +72.17% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- KERNEL-EUR +48.80% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- PHA-EUR +42.91% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- AIOZ-EUR +40.72% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- ZETA-EUR +37.91% — NOT_DETECTED — couche SCANNER_COVERAGE — action NOT_APPLICABLE
- PEPE-EUR +29.39% — DETECTED_EARLY — couche NONE — action NONE
- CARV-EUR +25.41% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- WIF-EUR +23.12% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- FORM-EUR +21.07% — DETECTED_EARLY — couche NONE — action INTERPRETATION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
