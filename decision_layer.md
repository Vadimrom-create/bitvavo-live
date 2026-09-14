# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-14T14:56:39.148672+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : aucun candidat matériel
- **MEILLEUR_LATENT_ACCELERATOR** : aucun candidat matériel
- **MEILLEUR_PULLBACK_REENTRY** : VTHO-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 7.833 | entrée 5.350 | trend 9.200 | rang 7.797
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. VTHO-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.797
2. NEAR-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.311
3. LSK-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.073

## Accélération indépendante

Aucune accélération indépendante confirmée ou en construction.

## Watchlist persistante 24–72 h

- ETHFI-EUR — ACTIVE_NOW — score mémoire 8.043/10 — sources V4 — WATCH_ONLY
- PROM-EUR — MEMORY_24H — score mémoire 7.860/10 — sources V4 — MEMORY_ONLY
- VET-EUR — ACTIVE_NOW — score mémoire 7.836/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- VTHO-EUR — ACTIVE_NOW — score mémoire 7.797/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- NEO-EUR — MEMORY_24H — score mémoire 7.738/10 — sources V4 — MEMORY_ONLY
- LDO-EUR — ACTIVE_NOW — score mémoire 7.712/10 — sources V4 — WATCH_ONLY
- XVG-EUR — ACTIVE_NOW — score mémoire 7.642/10 — sources V4 — WATCH_ONLY
- ZIL-EUR — ACTIVE_NOW — score mémoire 7.630/10 — sources DECISION_LAYER, V4 — WATCH_ONLY
- ICP-EUR — ACTIVE_NOW — score mémoire 7.609/10 — sources V4 — WATCH_ONLY
- ZIG-EUR — MEMORY_24H — score mémoire 7.547/10 — sources V4 — MEMORY_ONLY

## Audit des plus fortes hausses

- CPOOL-EUR +44.44% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- CAP-EUR +37.49% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- T-EUR +20.50% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- CNPY-EUR +18.61% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- MTL-EUR +13.16% — DETECTED_TOO_LATE — couche NONE — action INTERPRETATION
- REZ-EUR +12.67% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ARK-EUR +12.23% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- NPC-EUR +10.57% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ZRC-EUR +9.47% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- CAKE-EUR +9.35% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
