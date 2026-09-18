# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-18T21:36:48.688142+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : LSK-EUR | action PLACE_LIMITE_PASSIVE | opportunité 7.608 | entrée 6.000 | trend 8.400 | rang 7.467
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : aucun candidat matériel
- **MEILLEUR_PULLBACK_REENTRY** : DOT-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 7.934 | entrée 6.250 | trend 8.300 | rang 7.343
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. LSK-EUR — MEILLEURE_LIMITE_PASSIVE — PLACE_LIMITE_PASSIVE — rank 7.467
2. DOT-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.343
3. USELESS-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.064

## Accélération indépendante

- G-EUR — BUILDING_ACCELERATION — score 4.843/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- PEAQ-EUR — ACTIVE_NOW — score mémoire 8.236/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- ATOM-EUR — ACTIVE_NOW — score mémoire 8.071/10 — sources V4 — DETECTED_BUT_TOO_LATE
- CAKE-EUR — ACTIVE_NOW — score mémoire 8.006/10 — sources DECISION_LAYER, V4 — WATCH_ONLY
- ICP-EUR — ACTIVE_NOW — score mémoire 7.970/10 — sources DECISION_LAYER, V4 — WATCH_ONLY
- LDO-EUR — ACTIVE_NOW — score mémoire 7.918/10 — sources V4 — WATCH_ONLY
- VET-EUR — ACTIVE_NOW — score mémoire 7.868/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- ORCA-EUR — MEMORY_24H — score mémoire 7.810/10 — sources V4 — MEMORY_ONLY
- METIS-EUR — ACTIVE_NOW — score mémoire 7.795/10 — sources V4 — WATCH_ONLY
- YB-EUR — ACTIVE_NOW — score mémoire 7.784/10 — sources V4 — WATCH_ONLY
- SIGN-EUR — ACTIVE_NOW — score mémoire 7.706/10 — sources V4 — WATCH_ONLY

## Audit des plus fortes hausses

- STRK-EUR +54.05% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- G-EUR +45.76% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- F-EUR +40.54% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- ARB-EUR +27.96% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- APT-EUR +26.09% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ZAMA-EUR +23.52% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- NEAR-EUR +23.41% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- C-EUR +22.82% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- S-EUR +22.19% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ZIG-EUR +22.03% — DETECTED_EARLY — couche NONE — action INTERPRETATION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
