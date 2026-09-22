# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-22T17:31:33.407208+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : KAS-EUR | action ACHETE_MAINTENANT | opportunité 8.961 | entrée 6.950 | trend 8.300 | rang 8.131
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : RLC-EUR | action PLACE_LIMITE_PASSIVE | opportunité 7.991 | entrée 6.000 | trend 7.300 | rang 6.917
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : BEAM-EUR | action LATENT_ACCELERATOR | opportunité 9.171 | entrée 5.700 | trend 8.200 | rang 7.425
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : WAL-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.134 | entrée 6.500 | trend 8.850 | rang 7.894
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. KAS-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.131
2. SOL-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.083
3. ALGO-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.015

## Accélération indépendante

- CYBER-EUR — CONFIRMED_ACCELERATION — score 8.939/10 — DETECTED_BUT_TOO_LATE
- STO-EUR — CONFIRMED_ACCELERATION — score 8.874/10 — DETECTED_BUT_TOO_LATE
- APE-EUR — CONFIRMED_ACCELERATION — score 8.500/10 — DETECTED_BUT_TOO_LATE
- SXT-EUR — CONFIRMED_ACCELERATION — score 8.500/10 — DETECTED_BUT_TOO_LATE
- DRIFT-EUR — CONFIRMED_ACCELERATION — score 7.588/10 — DETECTED_BUT_TOO_LATE
- PROM-EUR — CONFIRMED_ACCELERATION — score 6.864/10 — DETECTED_BUT_TOO_LATE
- IKA-EUR — BUILDING_ACCELERATION — score 6.451/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- UP-EUR — BUILDING_ACCELERATION — score 6.123/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- VVV-EUR — BUILDING_ACCELERATION — score 6.123/10 — DETECTED_BUT_TOO_LATE
- DEEP-EUR — BUILDING_ACCELERATION — score 6.092/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- CYBER-EUR — ACTIVE_NOW — score mémoire 8.939/10 — sources ACCELERATION, V4 — DETECTED_BUT_TOO_LATE
- STO-EUR — ACTIVE_NOW — score mémoire 8.874/10 — sources ACCELERATION, V4 — DETECTED_BUT_TOO_LATE
- DEGEN-EUR — MEMORY_24H — score mémoire 8.739/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- APE-EUR — ACTIVE_NOW — score mémoire 8.500/10 — sources ACCELERATION, V4 — DETECTED_BUT_TOO_LATE
- AUDIO-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION — MEMORY_ONLY
- SXT-EUR — ACTIVE_NOW — score mémoire 8.500/10 — sources ACCELERATION, V4 — DETECTED_BUT_TOO_LATE
- KAS-EUR — ACTIVE_NOW — score mémoire 8.131/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- SOL-EUR — ACTIVE_NOW — score mémoire 8.083/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- ALGO-EUR — ACTIVE_NOW — score mémoire 8.015/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- TAIKO-EUR — ACTIVE_NOW — score mémoire 7.971/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY

## Audit des plus fortes hausses

- CHR-EUR +49.93% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- NIL-EUR +32.19% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- BCH-EUR +25.32% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- KERNEL-EUR +24.21% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ZRO-EUR +21.76% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- GRASS-EUR +19.20% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- FLOCK-EUR +16.86% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- S-EUR +16.01% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- KITE-EUR +15.87% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- AIOZ-EUR +14.97% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
