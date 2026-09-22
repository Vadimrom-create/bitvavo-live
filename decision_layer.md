# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-22T13:01:37.456984+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : LTC-EUR | action ACHETE_MAINTENANT | opportunité 8.625 | entrée 7.000 | trend 7.850 | rang 7.696
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : BREV-EUR | action PLACE_LIMITE_PASSIVE | opportunité 7.763 | entrée 6.050 | trend 8.150 | rang 7.457
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : MERL-EUR | action LATENT_ACCELERATOR | opportunité 8.435 | entrée 5.650 | trend 8.850 | rang 7.791
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : WAL-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 9.383 | entrée 6.150 | trend 8.850 | rang 8.117
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. WAL-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.117
2. RENDER-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.989
3. SOL-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.916

## Accélération indépendante

- MLN-EUR — CONFIRMED_ACCELERATION — score 9.032/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- BCH-EUR — CONFIRMED_ACCELERATION — score 8.500/10 — DETECTED_BUT_TOO_LATE
- UNI-EUR — CONFIRMED_ACCELERATION — score 8.500/10 — DETECTED_BUT_TOO_LATE
- BONK-EUR — CONFIRMED_ACCELERATION — score 7.964/10 — DETECTED_BUT_TOO_LATE
- PENDLE-EUR — CONFIRMED_ACCELERATION — score 7.134/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- TRUMP-EUR — CONFIRMED_ACCELERATION — score 6.967/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- SUSHI-EUR — BUILDING_ACCELERATION — score 6.462/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- CRV-EUR — BUILDING_ACCELERATION — score 6.455/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- NOS-EUR — BUILDING_ACCELERATION — score 6.420/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- BAND-EUR — BUILDING_ACCELERATION — score 6.082/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- NEAR-EUR — ACTIVE_NOW — score mémoire 7.327/10 — sources ACCELERATION, DECISION_LAYER, V4 — BUYABLE_NOW
- ZORA-EUR — ACTIVE_NOW — score mémoire 7.240/10 — sources ACCELERATION, DECISION_LAYER, V4 — BUYABLE_NOW
- AAVE-EUR — ACTIVE_NOW — score mémoire 6.781/10 — sources ACCELERATION, DECISION_LAYER, V4 — BUYABLE_NOW
- AUDIO-EUR — MEMORY_24H — score mémoire 9.640/10 — sources ACCELERATION — MEMORY_ONLY
- NIL-EUR — MEMORY_24H — score mémoire 9.319/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- SWEAT-EUR — MEMORY_24H — score mémoire 9.062/10 — sources ACCELERATION — MEMORY_ONLY
- MLN-EUR — ACTIVE_NOW — score mémoire 9.032/10 — sources ACCELERATION, V4 — WATCH_ONLY
- BCH-EUR — ACTIVE_NOW — score mémoire 8.500/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- GIGA-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION — MEMORY_ONLY
- U-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION, V4 — MEMORY_ONLY

## Audit des plus fortes hausses

- ICX-EUR +95.99% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- ZRC-EUR +80.10% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- KERNEL-EUR +28.91% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- XMN-EUR +27.55% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- WIF-EUR +21.88% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- FORM-EUR +21.73% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- NIL-EUR +21.09% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- GRASS-EUR +17.69% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- PEPE-EUR +15.65% — DETECTED_EARLY — couche NONE — action NONE
- BCH-EUR +14.98% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
