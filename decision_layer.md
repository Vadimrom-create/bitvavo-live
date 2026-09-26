# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-26T12:11:31.645843+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : AVAX-EUR | action ACHETE_MAINTENANT | opportunité 9.284 | entrée 8.050 | trend 8.150 | rang 8.229
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : BEAM-EUR | action PLACE_LIMITE_PASSIVE | opportunité 7.927 | entrée 5.950 | trend 9.000 | rang 7.807
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : MANTRA-EUR | action LATENT_ACCELERATOR | opportunité 8.383 | entrée 5.700 | trend 8.050 | rang 7.587
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : AXS-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.721 | entrée 6.350 | trend 9.000 | rang 8.232
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. AXS-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.232
2. AVAX-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.229
3. CAKE-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.204

## Accélération indépendante

- XMN-EUR — CONFIRMED_ACCELERATION — score 9.942/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- AGI-EUR — CONFIRMED_ACCELERATION — score 6.984/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- AMP-EUR — BUILDING_ACCELERATION — score 6.000/10 — DETECTED_BUT_TOO_LATE
- TAO-EUR — BUILDING_ACCELERATION — score 5.230/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- TAO-EUR — ACTIVE_NOW — score mémoire 8.063/10 — sources ACCELERATION, DECISION_LAYER, V4 — BUYABLE_NOW
- RAY-EUR — ACTIVE_NOW — score mémoire 7.665/10 — sources ACCELERATION, DECISION_LAYER, V4 — BUYABLE_NOW
- XMN-EUR — ACTIVE_NOW — score mémoire 9.942/10 — sources ACCELERATION, V4 — WATCH_ONLY
- ZRC-EUR — MEMORY_24H — score mémoire 9.830/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- PONKE-EUR — MEMORY_24H — score mémoire 9.578/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- RAD-EUR — MEMORY_24H — score mémoire 9.291/10 — sources ACCELERATION — MEMORY_ONLY
- WMTX-EUR — MEMORY_24H — score mémoire 9.000/10 — sources ACCELERATION — MEMORY_ONLY
- CTC-EUR — MEMORY_24H — score mémoire 8.874/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- ONT-EUR — MEMORY_24H — score mémoire 8.859/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- ACT-EUR — MEMORY_24H — score mémoire 8.555/10 — sources ACCELERATION, V4 — MEMORY_ONLY

## Audit des plus fortes hausses

- POND-EUR +156.77% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- RARE-EUR +70.01% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- AMP-EUR +45.82% — DETECTED_TOO_LATE — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- 2Z-EUR +27.97% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- PHA-EUR +24.13% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ARK-EUR +21.34% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- PROM-EUR +20.18% — DETECTED_TOO_LATE — couche NONE — action INTERPRETATION
- AERO-EUR +17.39% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- ENA-EUR +17.08% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- WAXP-EUR +12.84% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
