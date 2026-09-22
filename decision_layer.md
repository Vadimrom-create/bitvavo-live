# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-22T19:18:00.381900+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : LTC-EUR | action ACHETE_MAINTENANT | opportunité 9.284 | entrée 7.950 | trend 8.200 | rang 8.294
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : EDEN-EUR | action PLACE_LIMITE_PASSIVE | opportunité 8.639 | entrée 5.850 | trend 8.150 | rang 7.804
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : PYTH-EUR | action LATENT_ACCELERATOR | opportunité 7.618 | entrée 4.500 | trend 8.400 | rang 7.308
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : RUNE-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.339 | entrée 6.750 | trend 8.850 | rang 8.072
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. LTC-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.294
2. TAIKO-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.117
3. RUNE-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.072

## Accélération indépendante

- MOVR-EUR — CONFIRMED_ACCELERATION — score 10.000/10 — DETECTED_BUT_TOO_LATE
- SENT-EUR — CONFIRMED_ACCELERATION — score 8.469/10 — DETECTED_BUT_TOO_LATE
- GIGA-EUR — CONFIRMED_ACCELERATION — score 7.474/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- SWELL-EUR — CONFIRMED_ACCELERATION — score 6.854/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- PUFFER-EUR — BUILDING_ACCELERATION — score 6.315/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- ICX-EUR — BUILDING_ACCELERATION — score 5.586/10 — DETECTED_BUT_TOO_LATE
- PEOPLE-EUR — BUILDING_ACCELERATION — score 5.192/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- BCH-EUR — BUILDING_ACCELERATION — score 5.080/10 — DETECTED_BUT_TOO_LATE
- MOODENG-EUR — BUILDING_ACCELERATION — score 4.992/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- PENGU-EUR — BUILDING_ACCELERATION — score 4.849/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- MOVR-EUR — ACTIVE_NOW — score mémoire 10.000/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- TAI-EUR — MEMORY_24H — score mémoire 9.000/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- DEGEN-EUR — MEMORY_24H — score mémoire 8.739/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- APE-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- AUDIO-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION — MEMORY_ONLY
- SENT-EUR — ACTIVE_NOW — score mémoire 8.469/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- LTC-EUR — ACTIVE_NOW — score mémoire 8.294/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- HMSTR-EUR — MEMORY_24H — score mémoire 8.203/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- TAIKO-EUR — ACTIVE_NOW — score mémoire 8.117/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- RUNE-EUR — ACTIVE_NOW — score mémoire 8.072/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY

## Audit des plus fortes hausses

- DRIFT-EUR +55.24% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- CHR-EUR +37.38% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- BCH-EUR +30.67% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- KERNEL-EUR +23.75% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- NIL-EUR +22.11% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- KITE-EUR +17.90% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- GOAT-EUR +17.30% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- ZRO-EUR +17.20% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- TREAD-EUR +17.06% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- GRASS-EUR +15.65% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
