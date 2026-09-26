# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-26T09:34:57.260610+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : AXS-EUR | action ACHETE_MAINTENANT | opportunité 9.376 | entrée 7.550 | trend 9.000 | rang 8.586
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : 0G-EUR | action PLACE_LIMITE_PASSIVE | opportunité 8.524 | entrée 6.150 | trend 8.950 | rang 8.004
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : FLUX-EUR | action LATENT_ACCELERATOR | opportunité 7.694 | entrée 4.500 | trend 9.200 | rang 7.619
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : AEVO-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.641 | entrée 6.550 | trend 8.200 | rang 7.953
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. AXS-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.586
2. TAO-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.154
3. LTC-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.124

## Accélération indépendante

- POND-EUR — CONFIRMED_ACCELERATION — score 8.474/10 — DETECTED_BUT_TOO_LATE
- 2Z-EUR — CONFIRMED_ACCELERATION — score 8.359/10 — DETECTED_BUT_TOO_LATE
- LUMIA-EUR — CONFIRMED_ACCELERATION — score 7.901/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- NOS-EUR — CONFIRMED_ACCELERATION — score 7.098/10 — DETECTED_BUT_TOO_LATE
- OSMO-EUR — BUILDING_ACCELERATION — score 6.177/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- TREAD-EUR — BUILDING_ACCELERATION — score 5.079/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- RLC-EUR — BUILDING_ACCELERATION — score 4.914/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- PONKE-EUR — MEMORY_24H — score mémoire 9.578/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- ICX-EUR — MEMORY_24H — score mémoire 9.063/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- CTC-EUR — MEMORY_24H — score mémoire 8.874/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- ONT-EUR — MEMORY_24H — score mémoire 8.859/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- AXS-EUR — ACTIVE_NOW — score mémoire 8.586/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- ACT-EUR — MEMORY_24H — score mémoire 8.555/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- POND-EUR — ACTIVE_NOW — score mémoire 8.474/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- 2Z-EUR — ACTIVE_NOW — score mémoire 8.359/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- ZRC-EUR — MEMORY_24H — score mémoire 8.270/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- PUFFER-EUR — MEMORY_24H — score mémoire 8.207/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY

## Audit des plus fortes hausses

- POND-EUR +156.44% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- RARE-EUR +64.47% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- 2Z-EUR +41.05% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- ARK-EUR +28.39% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- PHA-EUR +26.02% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ENA-EUR +25.12% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- EDGE-EUR +18.10% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- AERO-EUR +17.25% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- KMNO-EUR +15.16% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- TNSR-EUR +14.47% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
