# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-22T03:34:11.287758+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : TAIKO-EUR | action ACHETE_MAINTENANT | opportunité 8.426 | entrée 7.350 | trend 8.700 | rang 8.085
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : LPT-EUR | action PLACE_LIMITE_PASSIVE | opportunité 7.973 | entrée 5.800 | trend 8.100 | rang 7.520
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : ATH-EUR | action LATENT_ACCELERATOR | opportunité 8.857 | entrée 5.450 | trend 7.300 | rang 7.304
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : MERL-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 7.890 | entrée 6.450 | trend 8.950 | rang 7.864
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. TAIKO-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.085
2. MERL-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.864
3. PYTH-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.849

## Accélération indépendante

- PEPE-EUR — CONFIRMED_ACCELERATION — score 9.294/10 — DETECTED_BUT_TOO_LATE
- FTT-EUR — CONFIRMED_ACCELERATION — score 7.531/10 — DETECTED_BUT_TOO_LATE
- PENGU-EUR — CONFIRMED_ACCELERATION — score 6.849/10 — DETECTED_BUT_TOO_LATE
- PYTH-EUR — CONFIRMED_ACCELERATION — score 6.655/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- FLOKI-EUR — BUILDING_ACCELERATION — score 5.997/10 — DETECTED_BUT_TOO_LATE
- UP-EUR — BUILDING_ACCELERATION — score 5.900/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- ENA-EUR — BUILDING_ACCELERATION — score 5.660/10 — DETECTED_BUT_TOO_LATE
- FLOCK-EUR — BUILDING_ACCELERATION — score 5.606/10 — DETECTED_BUT_TOO_LATE
- XPL-EUR — BUILDING_ACCELERATION — score 5.556/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- TRIA-EUR — BUILDING_ACCELERATION — score 5.452/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- GIGA-EUR — MEMORY_24H — score mémoire 9.738/10 — sources ACCELERATION — MEMORY_ONLY
- PEPE-EUR — ACTIVE_NOW — score mémoire 9.294/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- PHA-EUR — MEMORY_24H — score mémoire 9.177/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- SWEAT-EUR — MEMORY_24H — score mémoire 9.062/10 — sources ACCELERATION — MEMORY_ONLY
- ZEUS-EUR — MEMORY_24H — score mémoire 8.781/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- DGB-EUR — MEMORY_24H — score mémoire 8.732/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- AIOZ-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- PUFFER-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- XMN-EUR — MEMORY_24H — score mémoire 8.438/10 — sources ACCELERATION — MEMORY_ONLY
- SFP-EUR — MEMORY_24H — score mémoire 8.323/10 — sources ACCELERATION — MEMORY_ONLY

## Audit des plus fortes hausses

- ICX-EUR +97.22% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- ZRC-EUR +70.91% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- KERNEL-EUR +56.34% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ZETA-EUR +48.60% — NOT_DETECTED — couche SCANNER_COVERAGE — action NOT_APPLICABLE
- AIOZ-EUR +41.05% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- PHA-EUR +39.92% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- PEPE-EUR +29.24% — DETECTED_EARLY — couche NONE — action NONE
- CARV-EUR +25.25% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- WIF-EUR +22.02% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- FORM-EUR +18.12% — DETECTED_EARLY — couche NONE — action INTERPRETATION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
