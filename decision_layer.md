# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-23T04:43:19.950644+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : HYPE-EUR | action ACHETE_MAINTENANT | opportunité 8.974 | entrée 8.200 | trend 8.500 | rang 8.402
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : ACH-EUR | action PLACE_LIMITE_PASSIVE | opportunité 9.213 | entrée 6.100 | trend 8.200 | rang 8.086
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : SSV-EUR | action LATENT_ACCELERATOR | opportunité 8.036 | entrée 4.500 | trend 8.700 | rang 7.588
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : AXS-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 9.231 | entrée 7.050 | trend 8.450 | rang 8.280
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. HYPE-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.402
2. AXS-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.280
3. KAS-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.227

## Accélération indépendante

- XMN-EUR — CONFIRMED_ACCELERATION — score 7.988/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- BAND-EUR — CONFIRMED_ACCELERATION — score 7.838/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- FLOCK-EUR — CONFIRMED_ACCELERATION — score 7.593/10 — DETECTED_BUT_TOO_LATE
- CHR-EUR — CONFIRMED_ACCELERATION — score 7.521/10 — DETECTED_BUT_TOO_LATE
- MET-EUR — CONFIRMED_ACCELERATION — score 7.178/10 — DETECTED_BUT_TOO_LATE
- KAIA-EUR — CONFIRMED_ACCELERATION — score 7.176/10 — DETECTED_BUT_TOO_LATE
- PENGU-EUR — CONFIRMED_ACCELERATION — score 7.176/10 — DETECTED_BUT_TOO_LATE
- PEPE-EUR — BUILDING_ACCELERATION — score 6.117/10 — DETECTED_BUT_TOO_LATE
- DIA-EUR — BUILDING_ACCELERATION — score 6.023/10 — DETECTED_BUT_TOO_LATE
- CAP-EUR — BUILDING_ACCELERATION — score 5.974/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- XRP-EUR — ACTIVE_NOW — score mémoire 7.820/10 — sources ACCELERATION, DECISION_LAYER, V4 — BUYABLE_NOW
- GIGA-EUR — MEMORY_24H — score mémoire 9.062/10 — sources ACCELERATION — MEMORY_ONLY
- AUDIO-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION — MEMORY_ONLY
- NES-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- HYPE-EUR — ACTIVE_NOW — score mémoire 8.402/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- AXS-EUR — ACTIVE_NOW — score mémoire 8.280/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- KAS-EUR — ACTIVE_NOW — score mémoire 8.227/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- FTT-EUR — MEMORY_24H — score mémoire 8.118/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- WIN-EUR — MEMORY_24H — score mémoire 8.088/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- ACH-EUR — ACTIVE_NOW — score mémoire 8.086/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY

## Audit des plus fortes hausses

- USELESS-EUR +35.19% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- NIL-EUR +34.38% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- BCH-EUR +29.48% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- MET-EUR +29.15% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- CHR-EUR +24.08% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- FLOCK-EUR +21.73% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ZRO-EUR +21.15% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- TREAD-EUR +20.67% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- SUPER-EUR +19.89% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- SENT-EUR +18.59% — DETECTED_EARLY — couche NONE — action INTERPRETATION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
