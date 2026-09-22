# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-22T21:24:11.534106+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : QNT-EUR | action ACHETE_MAINTENANT | opportunité 9.030 | entrée 7.600 | trend 7.100 | rang 7.740
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : FLOKI-EUR | action PLACE_LIMITE_PASSIVE | opportunité 8.982 | entrée 6.100 | trend 7.300 | rang 7.672
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : LISTA-EUR | action LATENT_ACCELERATOR | opportunité 7.691 | entrée 5.300 | trend 8.500 | rang 7.458
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : INIT-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 9.246 | entrée 6.450 | trend 8.600 | rang 8.077
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. INIT-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.077
2. THE-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.984
3. ZORA-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.980

## Accélération indépendante

- LUNA2-EUR — CONFIRMED_ACCELERATION — score 8.762/10 — DETECTED_BUT_TOO_LATE
- PONKE-EUR — CONFIRMED_ACCELERATION — score 6.785/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- LUNA-EUR — BUILDING_ACCELERATION — score 5.248/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- QNT-EUR — ACTIVE_NOW — score mémoire 7.740/10 — sources ACCELERATION, DECISION_LAYER, V4 — BUYABLE_NOW
- TREAD-EUR — MEMORY_24H — score mémoire 9.440/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- CTC-EUR — MEMORY_24H — score mémoire 8.914/10 — sources ACCELERATION — MEMORY_ONLY
- LUNA2-EUR — ACTIVE_NOW — score mémoire 8.762/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- DEGEN-EUR — MEMORY_24H — score mémoire 8.739/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- APE-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- AUDIO-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION — MEMORY_ONLY
- LAPTOP-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- INIT-EUR — ACTIVE_NOW — score mémoire 8.077/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- THE-EUR — ACTIVE_NOW — score mémoire 7.984/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY

## Audit des plus fortes hausses

- DRIFT-EUR +35.08% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- CHR-EUR +31.32% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- BCH-EUR +28.63% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- KERNEL-EUR +22.19% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- PENGU-EUR +18.83% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- NIL-EUR +16.96% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- FLOCK-EUR +16.84% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- KITE-EUR +16.59% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- USELESS-EUR +16.34% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ZRO-EUR +15.31% — DETECTED_EARLY — couche NONE — action INTERPRETATION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
