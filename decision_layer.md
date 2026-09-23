# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-23T06:51:54.765366+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : ETC-EUR | action ACHETE_MAINTENANT | opportunité 9.211 | entrée 7.850 | trend 8.650 | rang 8.399
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : AUCTION-EUR | action PLACE_LIMITE_PASSIVE | opportunité 8.746 | entrée 6.050 | trend 8.500 | rang 7.947
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : DEEP-EUR | action LATENT_ACCELERATOR | opportunité 7.981 | entrée 5.000 | trend 8.550 | rang 7.524
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : TAIKO-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.845 | entrée 7.000 | trend 8.700 | rang 8.205
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. ETC-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.399
2. TAIKO-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.205
3. AVNT-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.094

## Accélération indépendante

- BONK-EUR — CONFIRMED_ACCELERATION — score 8.726/10 — DETECTED_BUT_TOO_LATE
- PTB-EUR — CONFIRMED_ACCELERATION — score 8.701/10 — DETECTED_BUT_TOO_LATE
- ICX-EUR — CONFIRMED_ACCELERATION — score 7.326/10 — DETECTED_BUT_TOO_LATE
- CPOOL-EUR — CONFIRMED_ACCELERATION — score 6.952/10 — DETECTED_BUT_TOO_LATE
- MEME-EUR — BUILDING_ACCELERATION — score 6.085/10 — DETECTED_BUT_TOO_LATE
- TOSHI-EUR — BUILDING_ACCELERATION — score 5.800/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- O-EUR — BUILDING_ACCELERATION — score 5.696/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- TURBO-EUR — BUILDING_ACCELERATION — score 5.607/10 — DETECTED_BUT_TOO_LATE
- MOODENG-EUR — BUILDING_ACCELERATION — score 5.475/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- OP-EUR — BUILDING_ACCELERATION — score 5.419/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- IKA-EUR — MEMORY_24H — score mémoire 10.000/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- SLX-EUR — MEMORY_24H — score mémoire 9.336/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- GIGA-EUR — MEMORY_24H — score mémoire 9.062/10 — sources ACCELERATION — MEMORY_ONLY
- BONK-EUR — ACTIVE_NOW — score mémoire 8.726/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- PTB-EUR — ACTIVE_NOW — score mémoire 8.701/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- NES-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- ETC-EUR — ACTIVE_NOW — score mémoire 8.399/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- TAIKO-EUR — ACTIVE_NOW — score mémoire 8.205/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- FTT-EUR — MEMORY_24H — score mémoire 8.118/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- AVNT-EUR — ACTIVE_NOW — score mémoire 8.094/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY

## Audit des plus fortes hausses

- NIL-EUR +43.51% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- CPOOL-EUR +36.60% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- MET-EUR +35.07% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- BCH-EUR +30.91% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- CHR-EUR +27.08% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- SUPER-EUR +26.06% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- ZRO-EUR +22.95% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- TREAD-EUR +21.84% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- PENGU-EUR +20.31% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- DRIFT-EUR +18.50% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
