# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-23T04:58:15.814595+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : LTC-EUR | action ACHETE_MAINTENANT | opportunité 9.422 | entrée 8.150 | trend 8.750 | rang 8.590
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : BEAM-EUR | action PLACE_LIMITE_PASSIVE | opportunité 8.223 | entrée 6.100 | trend 8.700 | rang 7.697
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : DEEP-EUR | action LATENT_ACCELERATOR | opportunité 9.227 | entrée 5.650 | trend 8.550 | rang 8.060
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : FET-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 9.329 | entrée 8.200 | trend 8.400 | rang 8.272
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. LTC-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.590
2. FET-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.272
3. SOL-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.230

## Accélération indépendante

- SAGA-EUR — CONFIRMED_ACCELERATION — score 8.874/10 — DETECTED_BUT_TOO_LATE
- CHR-EUR — BUILDING_ACCELERATION — score 6.214/10 — DETECTED_BUT_TOO_LATE
- AVA-EUR — BUILDING_ACCELERATION — score 6.016/10 — DETECTED_BUT_TOO_LATE
- EPIC-EUR — BUILDING_ACCELERATION — score 5.615/10 — DETECTED_BUT_TOO_LATE
- SXT-EUR — BUILDING_ACCELERATION — score 5.356/10 — DETECTED_BUT_TOO_LATE
- PROVE-EUR — BUILDING_ACCELERATION — score 5.164/10 — DETECTED_BUT_TOO_LATE
- ZAMA-EUR — BUILDING_ACCELERATION — score 4.988/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- XRP-EUR — ACTIVE_NOW — score mémoire 7.611/10 — sources ACCELERATION, DECISION_LAYER, V4 — BUYABLE_NOW
- GIGA-EUR — MEMORY_24H — score mémoire 9.062/10 — sources ACCELERATION — MEMORY_ONLY
- SAGA-EUR — ACTIVE_NOW — score mémoire 8.874/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- LTC-EUR — ACTIVE_NOW — score mémoire 8.590/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- AUDIO-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION — MEMORY_ONLY
- NES-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- FET-EUR — ACTIVE_NOW — score mémoire 8.272/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- SOL-EUR — ACTIVE_NOW — score mémoire 8.230/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- KAS-EUR — ACTIVE_NOW — score mémoire 8.218/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- HYPE-EUR — ACTIVE_NOW — score mémoire 8.189/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY

## Audit des plus fortes hausses

- NIL-EUR +39.65% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- USELESS-EUR +34.85% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- MET-EUR +29.77% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- BCH-EUR +29.22% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- CHR-EUR +27.19% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- TREAD-EUR +23.85% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- SUPER-EUR +23.60% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- PENGU-EUR +22.74% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ZRO-EUR +22.42% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- FLOCK-EUR +22.28% — DETECTED_EARLY — couche NONE — action INTERPRETATION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
