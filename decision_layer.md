# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-19T02:49:07.323695+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : ONDO-EUR | action ACHETE_MAINTENANT | opportunité 8.427 | entrée 7.350 | trend 7.650 | rang 7.607
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : aucun candidat matériel
- **MEILLEUR_LATENT_ACCELERATOR** : aucun candidat matériel
- **MEILLEUR_PULLBACK_REENTRY** : HYPE-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 7.984 | entrée 7.550 | trend 8.250 | rang 7.683
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. HYPE-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.683
2. ONDO-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 7.607
3. ENA-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.585

## Accélération indépendante

- ADA-EUR — BUILDING_ACCELERATION — score 5.011/10 — REQUIRES_V4_ENTRY_AND_EXECUTION_VALIDATION
- LSK-EUR — BUILDING_ACCELERATION — score 4.893/10 — DETECTED_BUT_TOO_LATE
- USELESS-EUR — BUILDING_ACCELERATION — score 4.752/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- ONDO-EUR — ACTIVE_NOW — score mémoire 7.607/10 — sources ACCELERATION, DECISION_LAYER, V4 — BUYABLE_NOW
- ADA-EUR — ACTIVE_NOW — score mémoire 7.192/10 — sources ACCELERATION, DECISION_LAYER, V4 — BUYABLE_NOW
- SYN-EUR — MEMORY_24H — score mémoire 8.620/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- VTHO-EUR — MEMORY_24H — score mémoire 8.268/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- PEPE-EUR — MEMORY_24H — score mémoire 8.255/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- NPC-EUR — ACTIVE_NOW — score mémoire 8.085/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- PYTH-EUR — ACTIVE_NOW — score mémoire 7.945/10 — sources V4 — WATCH_ONLY
- BEAM-EUR — ACTIVE_NOW — score mémoire 7.937/10 — sources V4 — WATCH_ONLY
- AAVE-EUR — ACTIVE_NOW — score mémoire 7.864/10 — sources ACCELERATION, V4 — WATCH_ONLY
- PROVE-EUR — ACTIVE_NOW — score mémoire 7.836/10 — sources V4 — DETECTED_BUT_TOO_LATE

## Audit des plus fortes hausses

- G-EUR +54.47% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- STRK-EUR +42.18% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- F-EUR +34.55% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- QKC-EUR +26.33% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- SYN-EUR +24.59% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- XTZ-EUR +24.39% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ZAMA-EUR +22.36% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- S-EUR +21.66% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ZIG-EUR +21.02% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- INJ-EUR +19.64% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
