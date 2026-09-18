# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-18T23:23:39.432741+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : MEGA-EUR | action PLACE_LIMITE_PASSIVE | opportunité 7.486 | entrée 6.650 | trend 7.950 | rang 6.587
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : aucun candidat matériel
- **MEILLEUR_PULLBACK_REENTRY** : USELESS-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 7.528 | entrée 7.000 | trend 8.100 | rang 7.155
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. USELESS-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.155
2. NEAR-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 6.617
3. MEGA-EUR — MEILLEURE_LIMITE_PASSIVE — PLACE_LIMITE_PASSIVE — rank 6.587

## Accélération indépendante

- TREAD-EUR — BUILDING_ACCELERATION — score 5.769/10 — REQUIRES_V4_ENTRY_AND_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- VTHO-EUR — ACTIVE_NOW — score mémoire 8.268/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- PHA-EUR — ACTIVE_NOW — score mémoire 8.019/10 — sources DECISION_LAYER, V4 — WATCH_ONLY
- YB-EUR — ACTIVE_NOW — score mémoire 7.953/10 — sources V4 — WATCH_ONLY
- ICP-EUR — ACTIVE_NOW — score mémoire 7.888/10 — sources DECISION_LAYER, V4 — WATCH_ONLY
- GRT-EUR — ACTIVE_NOW — score mémoire 7.887/10 — sources V4 — WATCH_ONLY
- XVG-EUR — ACTIVE_NOW — score mémoire 7.857/10 — sources V4 — WATCH_ONLY
- VET-EUR — ACTIVE_NOW — score mémoire 7.733/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- LDO-EUR — ACTIVE_NOW — score mémoire 7.664/10 — sources V4 — WATCH_ONLY
- METIS-EUR — ACTIVE_NOW — score mémoire 7.584/10 — sources V4 — WATCH_ONLY
- CVX-EUR — MEMORY_24H — score mémoire 7.542/10 — sources V4 — MEMORY_ONLY

## Audit des plus fortes hausses

- F-EUR +67.01% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- G-EUR +56.89% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- STRK-EUR +52.31% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- C-EUR +28.49% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- ARB-EUR +25.03% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- APT-EUR +22.43% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ZIG-EUR +22.16% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ZK-EUR +21.93% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE
- NEAR-EUR +21.40% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- RAY-EUR +21.29% — DETECTED_EARLY — couche NONE — action INTERPRETATION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
