# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-26T13:08:06.341884+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : KAS-EUR | action ACHETE_MAINTENANT | opportunité 9.166 | entrée 7.650 | trend 8.700 | rang 8.348
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : LDO-EUR | action PLACE_LIMITE_PASSIVE | opportunité 7.876 | entrée 5.850 | trend 8.650 | rang 7.631
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : AXS-EUR | action LATENT_ACCELERATOR | opportunité 7.995 | entrée 5.600 | trend 8.700 | rang 7.722
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : EIGEN-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.449 | entrée 7.150 | trend 8.950 | rang 8.075
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. KAS-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.348
2. EIGEN-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.075
3. WAL-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.068

## Accélération indépendante

- RUNE-EUR — CONFIRMED_ACCELERATION — score 9.041/10 — DETECTED_BUT_TOO_LATE
- ZEN-EUR — CONFIRMED_ACCELERATION — score 6.853/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- MIOTA-EUR — BUILDING_ACCELERATION — score 6.411/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- XVG-EUR — BUILDING_ACCELERATION — score 6.239/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- JUP-EUR — BUILDING_ACCELERATION — score 5.813/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- ZEUS-EUR — BUILDING_ACCELERATION — score 5.681/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- ICX-EUR — BUILDING_ACCELERATION — score 5.034/10 — DETECTED_BUT_TOO_LATE
- AUDIO-EUR — BUILDING_ACCELERATION — score 4.894/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- TAO-EUR — ACTIVE_NOW — score mémoire 7.371/10 — sources ACCELERATION, DECISION_LAYER, V4 — BUYABLE_NOW
- XMN-EUR — MEMORY_24H — score mémoire 9.942/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- ZRC-EUR — MEMORY_24H — score mémoire 9.830/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- PONKE-EUR — MEMORY_24H — score mémoire 9.578/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- RAD-EUR — MEMORY_24H — score mémoire 9.291/10 — sources ACCELERATION — MEMORY_ONLY
- RUNE-EUR — ACTIVE_NOW — score mémoire 9.041/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- CTC-EUR — MEMORY_24H — score mémoire 8.874/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- ONT-EUR — MEMORY_24H — score mémoire 8.859/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- ACT-EUR — MEMORY_24H — score mémoire 8.555/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- IMU-EUR — MEMORY_24H — score mémoire 8.394/10 — sources ACCELERATION — MEMORY_ONLY

## Audit des plus fortes hausses

- POND-EUR +155.04% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- RARE-EUR +65.47% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- AMP-EUR +36.67% — DETECTED_TOO_LATE — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- 2Z-EUR +28.75% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- ARK-EUR +21.48% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- EDGE-EUR +19.31% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- PROM-EUR +16.26% — DETECTED_TOO_LATE — couche NONE — action INTERPRETATION
- RUNE-EUR +15.59% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE
- AERO-EUR +15.56% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- ACE-EUR +13.14% — DETECTED_EARLY — couche NONE — action INTERPRETATION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
