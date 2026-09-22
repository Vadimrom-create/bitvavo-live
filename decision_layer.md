# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-22T06:37:23.959945+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : HYPE-EUR | action ACHETE_MAINTENANT | opportunité 8.173 | entrée 7.600 | trend 7.400 | rang 7.481
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : INIT-EUR | action PLACE_LIMITE_PASSIVE | opportunité 8.077 | entrée 6.000 | trend 9.200 | rang 7.909
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : ONG-EUR | action LATENT_ACCELERATOR | opportunité 7.999 | entrée 5.750 | trend 8.000 | rang 7.461
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : THE-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.765 | entrée 6.550 | trend 8.700 | rang 8.053
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. THE-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.053
2. INIT-EUR — MEILLEURE_LIMITE_PASSIVE — PLACE_LIMITE_PASSIVE — rank 7.909
3. SOL-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.821

## Accélération indépendante

- CARV-EUR — CONFIRMED_ACCELERATION — score 8.967/10 — DETECTED_BUT_TOO_LATE
- NIL-EUR — CONFIRMED_ACCELERATION — score 7.880/10 — DETECTED_BUT_TOO_LATE
- AVA-EUR — CONFIRMED_ACCELERATION — score 7.729/10 — DETECTED_BUT_TOO_LATE
- TREAD-EUR — BUILDING_ACCELERATION — score 6.452/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- QKC-EUR — BUILDING_ACCELERATION — score 5.720/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- C98-EUR — BUILDING_ACCELERATION — score 5.555/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- LSK-EUR — BUILDING_ACCELERATION — score 5.468/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- MERL-EUR — BUILDING_ACCELERATION — score 5.074/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- ICX-EUR — BUILDING_ACCELERATION — score 4.929/10 — DETECTED_BUT_TOO_LATE
- GROVE-EUR — BUILDING_ACCELERATION — score 4.878/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- SAGA-EUR — MEMORY_24H — score mémoire 9.632/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- PHA-EUR — MEMORY_24H — score mémoire 9.177/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- GIGA-EUR — MEMORY_24H — score mémoire 9.062/10 — sources ACCELERATION — MEMORY_ONLY
- SWEAT-EUR — MEMORY_24H — score mémoire 9.062/10 — sources ACCELERATION — MEMORY_ONLY
- VELO-EUR — MEMORY_24H — score mémoire 9.000/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- CARV-EUR — ACTIVE_NOW — score mémoire 8.967/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- ZEUS-EUR — MEMORY_24H — score mémoire 8.781/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- MEW-EUR — MEMORY_24H — score mémoire 8.523/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- ZRC-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION — MEMORY_ONLY
- XMN-EUR — MEMORY_24H — score mémoire 8.438/10 — sources ACCELERATION — MEMORY_ONLY

## Audit des plus fortes hausses

- ICX-EUR +98.39% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- ZRC-EUR +98.09% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- AIOZ-EUR +52.05% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- PEPE-EUR +26.47% — DETECTED_EARLY — couche NONE — action NONE
- KERNEL-EUR +25.53% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- WIF-EUR +22.45% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- GRASS-EUR +21.89% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- SAGA-EUR +21.26% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- FORM-EUR +20.08% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- TAO-EUR +19.41% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
