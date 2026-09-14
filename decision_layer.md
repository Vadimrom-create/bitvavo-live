# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-14T15:19:53.632246+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : aucun candidat matériel
- **MEILLEUR_LATENT_ACCELERATOR** : aucun candidat matériel
- **MEILLEUR_PULLBACK_REENTRY** : VTHO-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.057 | entrée 6.200 | trend 9.200 | rang 7.873
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. VTHO-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.873
2. NPC-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 6.993
3. USELESS-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 6.987

## Accélération indépendante

- RAY-EUR — BUILDING_ACCELERATION — score 5.525/10 — REQUIRES_V4_ENTRY_AND_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- ETHFI-EUR — ACTIVE_NOW — score mémoire 8.066/10 — sources V4 — WATCH_ONLY
- VET-EUR — ACTIVE_NOW — score mémoire 7.887/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- VTHO-EUR — ACTIVE_NOW — score mémoire 7.873/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- NEO-EUR — MEMORY_24H — score mémoire 7.738/10 — sources V4 — MEMORY_ONLY
- LDO-EUR — ACTIVE_NOW — score mémoire 7.701/10 — sources V4 — WATCH_ONLY
- XVG-EUR — ACTIVE_NOW — score mémoire 7.654/10 — sources V4 — WATCH_ONLY
- AERO-EUR — ACTIVE_NOW — score mémoire 7.561/10 — sources V4 — WATCH_ONLY
- ZIG-EUR — MEMORY_24H — score mémoire 7.547/10 — sources V4 — MEMORY_ONLY
- YB-EUR — ACTIVE_NOW — score mémoire 7.541/10 — sources V4 — WATCH_ONLY
- PUMP-EUR — MEMORY_24H — score mémoire 7.533/10 — sources V4 — MEMORY_ONLY

## Audit des plus fortes hausses

- CPOOL-EUR +44.23% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- CAP-EUR +41.06% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- CNPY-EUR +23.36% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- T-EUR +20.31% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- MTL-EUR +12.64% — DETECTED_TOO_LATE — couche NONE — action INTERPRETATION
- NPC-EUR +11.69% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- REZ-EUR +11.58% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- CAKE-EUR +8.90% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE
- QKC-EUR +8.61% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- ARK-EUR +8.45% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
