# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-24T14:45:34.330462+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : UNI-EUR | action ACHETE_MAINTENANT | opportunité 9.173 | entrée 7.850 | trend 7.750 | rang 8.028
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : LPT-EUR | action PLACE_LIMITE_PASSIVE | opportunité 8.342 | entrée 6.700 | trend 7.400 | rang 7.241
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : BEAM-EUR | action LATENT_ACCELERATOR | opportunité 8.197 | entrée 5.550 | trend 8.650 | rang 7.614
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : ARPA-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 9.192 | entrée 5.000 | trend 8.400 | rang 8.005
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. UNI-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.028
2. ARPA-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.005
3. ADA-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 7.938

## Accélération indépendante

- NOS-EUR — CONFIRMED_ACCELERATION — score 9.062/10 — DETECTED_BUT_TOO_LATE
- CETUS-EUR — CONFIRMED_ACCELERATION — score 9.059/10 — DETECTED_BUT_TOO_LATE
- FET-EUR — CONFIRMED_ACCELERATION — score 8.975/10 — DETECTED_BUT_TOO_LATE
- ZRX-EUR — CONFIRMED_ACCELERATION — score 8.963/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- METIS-EUR — CONFIRMED_ACCELERATION — score 8.661/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- OGN-EUR — CONFIRMED_ACCELERATION — score 7.854/10 — DETECTED_BUT_TOO_LATE
- NEAR-EUR — CONFIRMED_ACCELERATION — score 7.633/10 — DETECTED_BUT_TOO_LATE
- LQTY-EUR — CONFIRMED_ACCELERATION — score 7.441/10 — DETECTED_BUT_TOO_LATE
- XYO-EUR — CONFIRMED_ACCELERATION — score 7.357/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- BEAM-EUR — CONFIRMED_ACCELERATION — score 6.759/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- ADA-EUR — ACTIVE_NOW — score mémoire 7.938/10 — sources ACCELERATION, DECISION_LAYER, V4 — BUYABLE_NOW
- HBAR-EUR — ACTIVE_NOW — score mémoire 7.889/10 — sources ACCELERATION, DECISION_LAYER, V4 — BUYABLE_NOW
- AMP-EUR — MEMORY_24H — score mémoire 10.000/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- ICX-EUR — MEMORY_24H — score mémoire 9.456/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- FLOCK-EUR — MEMORY_24H — score mémoire 9.446/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- U-EUR — MEMORY_24H — score mémoire 9.175/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- NOS-EUR — ACTIVE_NOW — score mémoire 9.062/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- CETUS-EUR — ACTIVE_NOW — score mémoire 9.059/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- DYDX-EUR — MEMORY_24H — score mémoire 9.010/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- FET-EUR — ACTIVE_NOW — score mémoire 8.975/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE

## Audit des plus fortes hausses

- NOM-EUR +36.78% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- LSK-EUR +29.42% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- NIL-EUR +26.58% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- ONDO-EUR +21.67% — DETECTED_EARLY — couche NONE — action NONE
- LTC-EUR +20.93% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- ARX-EUR +15.66% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- PEAQ-EUR +15.49% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- PLUME-EUR +14.88% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- FET-EUR +13.28% — DETECTED_EARLY — couche NONE — action NONE
- ETC-EUR +13.27% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
