# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-23T01:36:35.208988+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : SHIB-EUR | action ACHETE_MAINTENANT | opportunité 9.155 | entrée 7.500 | trend 7.900 | rang 8.082
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : CROSS-EUR | action PLACE_LIMITE_PASSIVE | opportunité 8.719 | entrée 6.100 | trend 8.100 | rang 7.719
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : LISTA-EUR | action LATENT_ACCELERATOR | opportunité 7.884 | entrée 4.650 | trend 8.750 | rang 7.575
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : VET-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 9.318 | entrée 8.200 | trend 8.350 | rang 8.130
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. VET-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.130
2. SHIB-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.082
3. LTC-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.064

## Accélération indépendante

- DBR-EUR — CONFIRMED_ACCELERATION — score 8.500/10 — DETECTED_BUT_TOO_LATE
- NIL-EUR — CONFIRMED_ACCELERATION — score 8.234/10 — DETECTED_BUT_TOO_LATE
- ENS-EUR — CONFIRMED_ACCELERATION — score 7.733/10 — DETECTED_BUT_TOO_LATE
- CAKE-EUR — CONFIRMED_ACCELERATION — score 7.352/10 — DETECTED_BUT_TOO_LATE
- AIOZ-EUR — CONFIRMED_ACCELERATION — score 6.963/10 — DETECTED_BUT_TOO_LATE
- FARTCOIN-EUR — BUILDING_ACCELERATION — score 6.164/10 — DETECTED_BUT_TOO_LATE
- ZBCN-EUR — BUILDING_ACCELERATION — score 5.818/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- BONK-EUR — BUILDING_ACCELERATION — score 5.722/10 — DETECTED_BUT_TOO_LATE
- BIRB-EUR — BUILDING_ACCELERATION — score 5.440/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- SNX-EUR — BUILDING_ACCELERATION — score 5.126/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- PEAQ-EUR — MEMORY_24H — score mémoire 9.314/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- TREAD-EUR — MEMORY_24H — score mémoire 9.012/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- SLX-EUR — MEMORY_24H — score mémoire 8.896/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- DEGEN-EUR — MEMORY_24H — score mémoire 8.739/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- AUDIO-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION — MEMORY_ONLY
- DBR-EUR — ACTIVE_NOW — score mémoire 8.500/10 — sources ACCELERATION, V4 — DETECTED_BUT_TOO_LATE
- NES-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- MET-EUR — MEMORY_24H — score mémoire 8.271/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- NIL-EUR — ACTIVE_NOW — score mémoire 8.234/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- PUFFER-EUR — MEMORY_24H — score mémoire 8.193/10 — sources ACCELERATION, V4 — MEMORY_ONLY

## Audit des plus fortes hausses

- BCH-EUR +28.33% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- NIL-EUR +27.41% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- DRIFT-EUR +21.66% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- USELESS-EUR +21.53% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ZRO-EUR +20.63% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- MET-EUR +19.33% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE
- FLOCK-EUR +18.69% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- TREAD-EUR +18.04% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- MLN-EUR +17.65% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- CHR-EUR +17.44% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
