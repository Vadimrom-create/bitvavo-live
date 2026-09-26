# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-26T16:57:15.117710+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : LINK-EUR | action ACHETE_MAINTENANT | opportunité 8.479 | entrée 7.750 | trend 8.750 | rang 8.210
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : ZK-EUR | action PLACE_LIMITE_PASSIVE | opportunité 8.274 | entrée 6.050 | trend 8.700 | rang 7.683
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : CAKE-EUR | action LATENT_ACCELERATOR | opportunité 7.813 | entrée 4.500 | trend 8.950 | rang 7.585
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : ALT-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.678 | entrée 6.700 | trend 9.000 | rang 8.218
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. ALT-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.218
2. LINK-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.210
3. AAVE-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.145

## Accélération indépendante

- TAI-EUR — CONFIRMED_ACCELERATION — score 9.000/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- AMP-EUR — CONFIRMED_ACCELERATION — score 8.728/10 — DETECTED_BUT_TOO_LATE
- TREE-EUR — CONFIRMED_ACCELERATION — score 7.583/10 — DETECTED_BUT_TOO_LATE
- WELL-EUR — CONFIRMED_ACCELERATION — score 7.236/10 — DETECTED_BUT_TOO_LATE
- CPOOL-EUR — CONFIRMED_ACCELERATION — score 7.227/10 — DETECTED_BUT_TOO_LATE
- GALA-EUR — BUILDING_ACCELERATION — score 5.928/10 — DETECTED_BUT_TOO_LATE
- HOT-EUR — BUILDING_ACCELERATION — score 5.009/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- XMN-EUR — MEMORY_24H — score mémoire 9.942/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- PONKE-EUR — MEMORY_24H — score mémoire 9.578/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- RAD-EUR — MEMORY_24H — score mémoire 9.291/10 — sources ACCELERATION — MEMORY_ONLY
- TAI-EUR — ACTIVE_NOW — score mémoire 9.000/10 — sources ACCELERATION, V4 — WATCH_ONLY
- ONT-EUR — MEMORY_24H — score mémoire 8.859/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- CTC-EUR — MEMORY_DECAY_24_72H — score mémoire 8.735/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- AMP-EUR — ACTIVE_NOW — score mémoire 8.728/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- ACT-EUR — MEMORY_24H — score mémoire 8.555/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- AGI-EUR — MEMORY_24H — score mémoire 8.418/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- IMU-EUR — MEMORY_24H — score mémoire 8.394/10 — sources ACCELERATION — MEMORY_ONLY

## Audit des plus fortes hausses

- POND-EUR +115.87% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- AMP-EUR +48.78% — DETECTED_TOO_LATE — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- RARE-EUR +34.58% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- EDGE-EUR +32.98% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- QNT-EUR +23.08% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- AGI-EUR +21.30% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- FIL-EUR +19.25% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- 2Z-EUR +18.39% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- ACE-EUR +16.90% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- RUNE-EUR +16.65% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
