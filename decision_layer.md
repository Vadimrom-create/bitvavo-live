# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-14T09:59:08.156459+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : aucun candidat matériel
- **MEILLEUR_LATENT_ACCELERATOR** : aucun candidat matériel
- **MEILLEUR_PULLBACK_REENTRY** : VTHO-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 7.824 | entrée 5.500 | trend 9.200 | rang 7.811
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. VTHO-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.811
2. TAO-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.617
3. USELESS-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.410

## Accélération indépendante

- REZ-EUR — BUILDING_ACCELERATION — score 5.849/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- LDO-EUR — ACTIVE_NOW — score mémoire 8.221/10 — sources V4 — WATCH_ONLY
- PUMP-EUR — ACTIVE_NOW — score mémoire 8.027/10 — sources V4 — WATCH_ONLY
- LAPTOP-EUR — MEMORY_24H — score mémoire 8.013/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- ETHFI-EUR — ACTIVE_NOW — score mémoire 7.949/10 — sources V4 — WATCH_ONLY
- CAKE-EUR — ACTIVE_NOW — score mémoire 7.941/10 — sources V4 — WATCH_ONLY
- WLD-EUR — ACTIVE_NOW — score mémoire 7.937/10 — sources DECISION_LAYER, V4 — WATCH_ONLY
- ICP-EUR — ACTIVE_NOW — score mémoire 7.926/10 — sources V4 — WATCH_ONLY
- XVG-EUR — ACTIVE_NOW — score mémoire 7.868/10 — sources V4 — WATCH_ONLY
- VET-EUR — ACTIVE_NOW — score mémoire 7.850/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- ENS-EUR — ACTIVE_NOW — score mémoire 7.816/10 — sources V4 — WATCH_ONLY

## Audit des plus fortes hausses

- CPOOL-EUR +67.10% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- CVC-EUR +40.89% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- REZ-EUR +27.75% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- FIL-EUR +24.07% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- T-EUR +22.87% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- LSK-EUR +22.72% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- IQ-EUR +13.42% — DETECTED_TOO_LATE — couche NONE — action INTERPRETATION
- LIGHTER-EUR +11.50% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- CNPY-EUR +9.33% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- MTL-EUR +8.96% — DETECTED_TOO_LATE — couche NONE — action INTERPRETATION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
