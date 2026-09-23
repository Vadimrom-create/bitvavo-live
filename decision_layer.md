# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-23T02:03:42.799342+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : VET-EUR | action ACHETE_MAINTENANT | opportunité 9.053 | entrée 8.050 | trend 8.350 | rang 8.113
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : LDO-EUR | action PLACE_LIMITE_PASSIVE | opportunité 7.657 | entrée 6.650 | trend 8.400 | rang 7.584
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : ARX-EUR | action LATENT_ACCELERATOR | opportunité 7.999 | entrée 5.450 | trend 8.850 | rang 7.446
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : SSV-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.071 | entrée 6.650 | trend 8.700 | rang 7.849
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. VET-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.113
2. SSV-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.849
3. LTC-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.833

## Accélération indépendante

- UP-EUR — CONFIRMED_ACCELERATION — score 10.000/10 — DETECTED_BUT_TOO_LATE
- ICX-EUR — CONFIRMED_ACCELERATION — score 9.089/10 — DETECTED_BUT_TOO_LATE
- AERO-EUR — CONFIRMED_ACCELERATION — score 7.431/10 — DETECTED_BUT_TOO_LATE
- NOS-EUR — CONFIRMED_ACCELERATION — score 7.028/10 — DETECTED_BUT_TOO_LATE
- IQ-EUR — BUILDING_ACCELERATION — score 6.413/10 — DETECTED_BUT_TOO_LATE
- VTHO-EUR — BUILDING_ACCELERATION — score 6.131/10 — DETECTED_BUT_TOO_LATE
- QUID-EUR — BUILDING_ACCELERATION — score 5.538/10 — DETECTED_BUT_TOO_LATE
- TREAD-EUR — BUILDING_ACCELERATION — score 5.513/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- UP-EUR — ACTIVE_NOW — score mémoire 10.000/10 — sources ACCELERATION — DETECTED_BUT_TOO_LATE
- ICX-EUR — ACTIVE_NOW — score mémoire 9.089/10 — sources ACCELERATION, V4 — DETECTED_BUT_TOO_LATE
- SLX-EUR — MEMORY_24H — score mémoire 8.896/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- DEGEN-EUR — MEMORY_24H — score mémoire 8.739/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- AUDIO-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION — MEMORY_ONLY
- DBR-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- NES-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- NIL-EUR — MEMORY_24H — score mémoire 8.234/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- PUFFER-EUR — MEMORY_24H — score mémoire 8.193/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- FTT-EUR — MEMORY_24H — score mémoire 8.118/10 — sources ACCELERATION, V4 — MEMORY_ONLY

## Audit des plus fortes hausses

- BCH-EUR +29.34% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- NIL-EUR +24.31% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- TREAD-EUR +23.57% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- USELESS-EUR +21.22% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- MET-EUR +19.95% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE
- DRIFT-EUR +19.59% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- ZRO-EUR +19.45% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- FLOCK-EUR +18.80% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- MLN-EUR +18.43% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- ALLO-EUR +16.56% — DETECTED_EARLY — couche NONE — action INTERPRETATION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
