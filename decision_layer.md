# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-19T08:37:46.874630+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : TAO-EUR | action ACHETE_MAINTENANT | opportunité 8.486 | entrée 7.000 | trend 7.200 | rang 7.513
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : aucun candidat matériel
- **MEILLEUR_LATENT_ACCELERATOR** : aucun candidat matériel
- **MEILLEUR_PULLBACK_REENTRY** : HYPE-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 7.982 | entrée 8.000 | trend 8.500 | rang 7.906
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. HYPE-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.906
2. AVAX-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.759
3. SOL-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.625

## Accélération indépendante

- SYN-EUR — CONFIRMED_ACCELERATION — score 8.915/10 — DETECTED_BUT_TOO_LATE
- ENA-EUR — BUILDING_ACCELERATION — score 5.878/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- SYN-EUR — ACTIVE_NOW — score mémoire 8.915/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- AAVE-EUR — ACTIVE_NOW — score mémoire 8.508/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- PENDLE-EUR — ACTIVE_NOW — score mémoire 8.078/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- LSK-EUR — MEMORY_24H — score mémoire 8.067/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- ACH-EUR — ACTIVE_NOW — score mémoire 8.031/10 — sources V4 — DETECTED_BUT_TOO_LATE
- ARX-EUR — ACTIVE_NOW — score mémoire 8.030/10 — sources V4 — WATCH_ONLY
- AERO-EUR — ACTIVE_NOW — score mémoire 7.976/10 — sources V4 — WATCH_ONLY
- WAL-EUR — ACTIVE_NOW — score mémoire 7.970/10 — sources V4 — WATCH_ONLY
- VVV-EUR — ACTIVE_NOW — score mémoire 7.922/10 — sources DECISION_LAYER, V4 — WATCH_ONLY
- HYPE-EUR — ACTIVE_NOW — score mémoire 7.906/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY

## Audit des plus fortes hausses

- EDGE-EUR +46.08% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- HEI-EUR +41.51% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- SYN-EUR +39.61% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- ZAMA-EUR +33.34% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- XTZ-EUR +27.76% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- F-EUR +27.16% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- INJ-EUR +23.95% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- STRK-EUR +23.56% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ZIG-EUR +23.00% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- EPIC-EUR +20.21% — DETECTED_EARLY — couche NONE — action INTERPRETATION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
