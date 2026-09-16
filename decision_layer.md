# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-16T13:42:37.584851+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : aucun candidat matériel
- **MEILLEUR_LATENT_ACCELERATOR** : aucun candidat matériel
- **MEILLEUR_PULLBACK_REENTRY** : NPC-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.203 | entrée 7.250 | trend 7.750 | rang 7.553
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. NPC-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.553
2. NEAR-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.371
3. USELESS-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 6.734

## Accélération indépendante

- LSK-EUR — BUILDING_ACCELERATION — score 5.331/10 — DETECTED_BUT_TOO_LATE
- RAY-EUR — BUILDING_ACCELERATION — score 5.227/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- SYRUP-EUR — ACTIVE_NOW — score mémoire 8.063/10 — sources V4 — WATCH_ONLY
- LDO-EUR — ACTIVE_NOW — score mémoire 7.986/10 — sources V4 — WATCH_ONLY
- GRT-EUR — ACTIVE_NOW — score mémoire 7.982/10 — sources V4 — WATCH_ONLY
- ZORA-EUR — ACTIVE_NOW — score mémoire 7.913/10 — sources V4 — WATCH_ONLY
- VTHO-EUR — ACTIVE_NOW — score mémoire 7.864/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- ETHFI-EUR — ACTIVE_NOW — score mémoire 7.768/10 — sources V4 — WATCH_ONLY
- WLD-EUR — ACTIVE_NOW — score mémoire 7.694/10 — sources DECISION_LAYER, V4 — WATCH_ONLY
- KAS-EUR — ACTIVE_NOW — score mémoire 7.661/10 — sources V4 — WATCH_ONLY
- UNI-EUR — MEMORY_24H — score mémoire 7.629/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- BLUR-EUR — ACTIVE_NOW — score mémoire 7.617/10 — sources V4 — WATCH_ONLY

## Audit des plus fortes hausses

- SYN-EUR +116.63% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- LSK-EUR +54.33% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- FOLD-EUR +22.22% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- ARB-EUR +20.94% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- HEI-EUR +15.19% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- USELESS-EUR +14.77% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- CNPY-EUR +12.55% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- IOST-EUR +11.56% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- TAI-EUR +8.63% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- G-EUR +8.31% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
