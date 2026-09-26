# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-26T17:15:59.385850+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : LINK-EUR | action ACHETE_MAINTENANT | opportunité 8.236 | entrée 7.950 | trend 8.750 | rang 8.107
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : EGLD-EUR | action PLACE_LIMITE_PASSIVE | opportunité 8.722 | entrée 5.850 | trend 8.150 | rang 7.874
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : JUP-EUR | action LATENT_ACCELERATOR | opportunité 7.811 | entrée 4.500 | trend 8.950 | rang 7.595
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : W-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 9.389 | entrée 7.050 | trend 8.950 | rang 8.441
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. W-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.441
2. RPL-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.356
3. LTC-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.116

## Accélération indépendante

- HFT-EUR — CONFIRMED_ACCELERATION — score 9.483/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- EDGE-EUR — CONFIRMED_ACCELERATION — score 8.077/10 — DETECTED_BUT_TOO_LATE
- ZRO-EUR — CONFIRMED_ACCELERATION — score 7.789/10 — DETECTED_BUT_TOO_LATE
- ESP-EUR — BUILDING_ACCELERATION — score 6.371/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- C98-EUR — BUILDING_ACCELERATION — score 6.369/10 — DETECTED_BUT_TOO_LATE
- FUEL-EUR — BUILDING_ACCELERATION — score 6.288/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- KITE-EUR — BUILDING_ACCELERATION — score 5.596/10 — DETECTED_BUT_TOO_LATE
- BLEND-EUR — BUILDING_ACCELERATION — score 5.464/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- BAT-EUR — BUILDING_ACCELERATION — score 5.295/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- LSK-EUR — BUILDING_ACCELERATION — score 5.227/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- XMN-EUR — MEMORY_24H — score mémoire 9.942/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- PONKE-EUR — MEMORY_24H — score mémoire 9.578/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- HFT-EUR — ACTIVE_NOW — score mémoire 9.483/10 — sources ACCELERATION — WATCH_ONLY
- RAD-EUR — MEMORY_24H — score mémoire 9.291/10 — sources ACCELERATION — MEMORY_ONLY
- TAI-EUR — MEMORY_24H — score mémoire 9.000/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- ONT-EUR — MEMORY_24H — score mémoire 8.859/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- AMP-EUR — MEMORY_24H — score mémoire 8.728/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- CTC-EUR — MEMORY_DECAY_24_72H — score mémoire 8.677/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- ACT-EUR — MEMORY_24H — score mémoire 8.555/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- W-EUR — ACTIVE_NOW — score mémoire 8.441/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY

## Audit des plus fortes hausses

- POND-EUR +115.72% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- EDGE-EUR +47.11% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- AMP-EUR +46.36% — DETECTED_TOO_LATE — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- RARE-EUR +34.29% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- QNT-EUR +25.82% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- AGI-EUR +18.84% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- 2Z-EUR +17.83% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- ACE-EUR +17.41% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- RUNE-EUR +17.09% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE
- KAS-EUR +16.62% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
