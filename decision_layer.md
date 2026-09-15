# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-15T09:48:34.202286+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : aucun candidat matériel
- **MEILLEUR_LATENT_ACCELERATOR** : aucun candidat matériel
- **MEILLEUR_PULLBACK_REENTRY** : VTHO-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.602 | entrée 6.350 | trend 9.200 | rang 8.054
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. VTHO-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.054
2. VET-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.555
3. USELESS-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.075

## Accélération indépendante

- CAP-EUR — CONFIRMED_ACCELERATION — score 8.685/10 — DETECTED_BUT_TOO_LATE
- UNI-EUR — BUILDING_ACCELERATION — score 5.788/10 — REQUIRES_V4_ENTRY_AND_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- CAP-EUR — ACTIVE_NOW — score mémoire 8.685/10 — sources ACCELERATION — DETECTED_BUT_TOO_LATE
- LAPTOP-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- AIOZ-EUR — ACTIVE_NOW — score mémoire 8.239/10 — sources V4 — WATCH_ONLY
- VTHO-EUR — ACTIVE_NOW — score mémoire 8.054/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- ETHFI-EUR — ACTIVE_NOW — score mémoire 7.895/10 — sources V4 — WATCH_ONLY
- LDO-EUR — ACTIVE_NOW — score mémoire 7.795/10 — sources V4 — WATCH_ONLY
- SOMI-EUR — ACTIVE_NOW — score mémoire 7.726/10 — sources V4 — WATCH_ONLY
- ICP-EUR — ACTIVE_NOW — score mémoire 7.667/10 — sources V4 — WATCH_ONLY
- KAS-EUR — ACTIVE_NOW — score mémoire 7.602/10 — sources V4 — WATCH_ONLY
- YB-EUR — ACTIVE_NOW — score mémoire 7.590/10 — sources V4 — WATCH_ONLY

## Audit des plus fortes hausses

- CAP-EUR +37.07% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- CNPY-EUR +27.16% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- PUFFER-EUR +26.35% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- SAGA-EUR +17.02% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- ASTR-EUR +14.32% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- LAPTOP-EUR +13.84% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ACX-EUR +11.82% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- CROSS-EUR +8.82% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- ACE-EUR +6.99% — DETECTED_TOO_LATE — couche NONE — action INTERPRETATION
- LRC-EUR +6.29% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
