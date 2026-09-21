# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-21T18:59:24.828881+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : TAO-EUR | action ACHETE_MAINTENANT | opportunité 8.429 | entrée 7.050 | trend 8.750 | rang 7.991
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : XTZ-EUR | action PLACE_LIMITE_PASSIVE | opportunité 9.102 | entrée 5.850 | trend 7.900 | rang 7.784
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : SUPER-EUR | action LATENT_ACCELERATOR | opportunité 8.206 | entrée 5.550 | trend 8.950 | rang 7.836
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : MERL-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.170 | entrée 6.250 | trend 8.950 | rang 7.957
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. TAO-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 7.991
2. STX-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 7.991
3. MERL-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.957

## Accélération indépendante

- ALIGN-EUR — CONFIRMED_ACCELERATION — score 9.033/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- PENGU-EUR — CONFIRMED_ACCELERATION — score 7.651/10 — DETECTED_BUT_TOO_LATE
- ZIG-EUR — CONFIRMED_ACCELERATION — score 7.500/10 — DETECTED_BUT_TOO_LATE
- VELO-EUR — CONFIRMED_ACCELERATION — score 7.233/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- FARTCOIN-EUR — CONFIRMED_ACCELERATION — score 6.622/10 — DETECTED_BUT_TOO_LATE
- U-EUR — BUILDING_ACCELERATION — score 6.393/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- USELESS-EUR — BUILDING_ACCELERATION — score 6.140/10 — DETECTED_BUT_TOO_LATE
- PHA-EUR — BUILDING_ACCELERATION — score 5.529/10 — DETECTED_BUT_TOO_LATE
- MET-EUR — BUILDING_ACCELERATION — score 5.489/10 — DETECTED_BUT_TOO_LATE
- ATH-EUR — BUILDING_ACCELERATION — score 5.379/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- TAO-EUR — ACTIVE_NOW — score mémoire 7.991/10 — sources ACCELERATION, DECISION_LAYER, V4 — BUYABLE_NOW
- RON-EUR — MEMORY_24H — score mémoire 9.938/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- THQ-EUR — MEMORY_24H — score mémoire 9.062/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- ACU-EUR — MEMORY_24H — score mémoire 9.053/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- ALIGN-EUR — ACTIVE_NOW — score mémoire 9.033/10 — sources ACCELERATION, V4 — WATCH_ONLY
- LUMIA-EUR — MEMORY_24H — score mémoire 8.655/10 — sources ACCELERATION — MEMORY_ONLY
- TRAC-EUR — MEMORY_24H — score mémoire 8.588/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- FTT-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- PUFFER-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- SFP-EUR — MEMORY_24H — score mémoire 8.323/10 — sources ACCELERATION — MEMORY_ONLY

## Audit des plus fortes hausses

- ZRC-EUR +103.38% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ICX-EUR +58.81% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- ZETA-EUR +58.04% — NOT_DETECTED — couche SCANNER_COVERAGE — action NOT_APPLICABLE
- PHA-EUR +39.45% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- FORM-EUR +38.97% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- PTB-EUR +29.42% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- AIOZ-EUR +25.37% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- PEPE-EUR +24.97% — DETECTED_EARLY — couche NONE — action NONE
- NOS-EUR +23.01% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- SWELL-EUR +22.08% — DETECTED_EARLY — couche NONE — action INTERPRETATION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
