# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-22T14:19:28.756087+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : HBAR-EUR | action ACHETE_MAINTENANT | opportunité 9.261 | entrée 8.000 | trend 8.100 | rang 8.111
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : BEAM-EUR | action PLACE_LIMITE_PASSIVE | opportunité 8.844 | entrée 5.800 | trend 8.500 | rang 7.967
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : GOAT-EUR | action LATENT_ACCELERATOR | opportunité 7.827 | entrée 5.650 | trend 8.200 | rang 7.228
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : WAL-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.309 | entrée 6.600 | trend 8.850 | rang 7.979
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. HBAR-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.111
2. SOL-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.079
3. WAL-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.979

## Accélération indépendante

- CHR-EUR — CONFIRMED_ACCELERATION — score 8.881/10 — DETECTED_BUT_TOO_LATE
- FLOCK-EUR — CONFIRMED_ACCELERATION — score 8.500/10 — DETECTED_BUT_TOO_LATE
- PYTH-EUR — CONFIRMED_ACCELERATION — score 8.500/10 — DETECTED_BUT_TOO_LATE
- MON-EUR — CONFIRMED_ACCELERATION — score 6.985/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- HFT-EUR — CONFIRMED_ACCELERATION — score 6.625/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- ZRO-EUR — BUILDING_ACCELERATION — score 6.244/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- LRC-EUR — BUILDING_ACCELERATION — score 6.134/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- GNS-EUR — BUILDING_ACCELERATION — score 5.713/10 — DETECTED_BUT_TOO_LATE
- AUDIO-EUR — BUILDING_ACCELERATION — score 5.544/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- A-EUR — BUILDING_ACCELERATION — score 5.375/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- HBAR-EUR — ACTIVE_NOW — score mémoire 8.111/10 — sources ACCELERATION, DECISION_LAYER, V4 — BUYABLE_NOW
- ADA-EUR — ACTIVE_NOW — score mémoire 7.423/10 — sources ACCELERATION, DECISION_LAYER, V4 — BUYABLE_NOW
- IKA-EUR — MEMORY_24H — score mémoire 9.669/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- NIL-EUR — MEMORY_24H — score mémoire 9.319/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- SWEAT-EUR — MEMORY_24H — score mémoire 9.062/10 — sources ACCELERATION — MEMORY_ONLY
- MLN-EUR — MEMORY_24H — score mémoire 9.032/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- CHR-EUR — ACTIVE_NOW — score mémoire 8.881/10 — sources ACCELERATION, V4 — DETECTED_BUT_TOO_LATE
- DEGEN-EUR — MEMORY_24H — score mémoire 8.739/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- FLOCK-EUR — ACTIVE_NOW — score mémoire 8.500/10 — sources ACCELERATION, V4 — DETECTED_BUT_TOO_LATE
- GIGA-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION — MEMORY_ONLY

## Audit des plus fortes hausses

- ICX-EUR +90.11% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- ZRC-EUR +70.00% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- NIL-EUR +32.83% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- FLOCK-EUR +32.04% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- KERNEL-EUR +26.72% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- BCH-EUR +20.46% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- NOS-EUR +20.00% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- XMN-EUR +17.99% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- FORM-EUR +16.91% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- GRASS-EUR +15.13% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
