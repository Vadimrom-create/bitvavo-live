# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-16T05:43:51.488717+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : aucun candidat matériel
- **MEILLEUR_LATENT_ACCELERATOR** : aucun candidat matériel
- **MEILLEUR_PULLBACK_REENTRY** : USELESS-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 7.975 | entrée 7.250 | trend 8.100 | rang 7.173
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. USELESS-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.173
2. FET-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.169

## Accélération indépendante

- SYN-EUR — BUILDING_ACCELERATION — score 5.081/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- LSK-EUR — MEMORY_24H — score mémoire 9.125/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- LDO-EUR — ACTIVE_NOW — score mémoire 8.540/10 — sources V4 — WATCH_ONLY
- NPC-EUR — ACTIVE_NOW — score mémoire 8.074/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- VTHO-EUR — ACTIVE_NOW — score mémoire 8.019/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- ICP-EUR — ACTIVE_NOW — score mémoire 7.975/10 — sources V4 — WATCH_ONLY
- ETHFI-EUR — ACTIVE_NOW — score mémoire 7.902/10 — sources V4 — WATCH_ONLY
- TIA-EUR — ACTIVE_NOW — score mémoire 7.898/10 — sources V4 — WATCH_ONLY
- SOMI-EUR — ACTIVE_NOW — score mémoire 7.777/10 — sources V4 — WATCH_ONLY
- VET-EUR — ACTIVE_NOW — score mémoire 7.759/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- XVG-EUR — ACTIVE_NOW — score mémoire 7.751/10 — sources V4 — WATCH_ONLY

## Audit des plus fortes hausses

- SYN-EUR +40.43% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- LSK-EUR +26.15% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- CNPY-EUR +20.60% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- ALIGN-EUR +16.06% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ARB-EUR +14.31% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- USELESS-EUR +12.30% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- LAPTOP-EUR +10.79% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- ACX-EUR +7.38% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- FOLD-EUR +6.45% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- IOST-EUR +5.85% — DETECTED_EARLY — couche NONE — action INTERPRETATION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
