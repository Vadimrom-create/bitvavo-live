# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-16T15:51:23.562065+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : aucun candidat matériel
- **MEILLEUR_LATENT_ACCELERATOR** : aucun candidat matériel
- **MEILLEUR_PULLBACK_REENTRY** : VET-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 7.818 | entrée 6.250 | trend 8.650 | rang 7.700
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. VET-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.700
2. NEAR-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.669

## Accélération indépendante

- LSK-EUR — CONFIRMED_ACCELERATION — score 7.989/10 — DETECTED_BUT_TOO_LATE
- NEAR-EUR — BUILDING_ACCELERATION — score 5.573/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- HEI-EUR — MEMORY_24H — score mémoire 9.941/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- VTHO-EUR — ACTIVE_NOW — score mémoire 8.410/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- LSK-EUR — ACTIVE_NOW — score mémoire 7.989/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- LIGHTER-EUR — ACTIVE_NOW — score mémoire 7.981/10 — sources V4 — WATCH_ONLY
- ZORA-EUR — ACTIVE_NOW — score mémoire 7.896/10 — sources V4 — WATCH_ONLY
- LDO-EUR — ACTIVE_NOW — score mémoire 7.879/10 — sources V4 — WATCH_ONLY
- SYN-EUR — MEMORY_24H — score mémoire 7.850/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- XVG-EUR — ACTIVE_NOW — score mémoire 7.728/10 — sources V4 — WATCH_ONLY
- VET-EUR — ACTIVE_NOW — score mémoire 7.700/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- TRUST-EUR — ACTIVE_NOW — score mémoire 7.686/10 — sources V4 — WATCH_ONLY

## Audit des plus fortes hausses

- SYN-EUR +140.72% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- LSK-EUR +66.16% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- HEI-EUR +24.18% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- FOLD-EUR +15.91% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- SOSO-EUR +10.87% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE
- USELESS-EUR +10.86% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- CNPY-EUR +10.20% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- IOST-EUR +9.88% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ARB-EUR +7.50% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- SOMI-EUR +7.24% — DETECTED_EARLY — couche NONE — action INTERPRETATION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
