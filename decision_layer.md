# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-14T15:56:10.151774+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : aucun candidat matériel
- **MEILLEUR_LATENT_ACCELERATOR** : aucun candidat matériel
- **MEILLEUR_PULLBACK_REENTRY** : VTHO-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.162 | entrée 5.600 | trend 9.200 | rang 7.851
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. VTHO-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.851
2. USELESS-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.226
3. FET-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.185

## Accélération indépendante

- ARK-EUR — BUILDING_ACCELERATION — score 6.315/10 — DETECTED_BUT_TOO_LATE
- QKC-EUR — BUILDING_ACCELERATION — score 5.834/10 — REQUIRES_V4_ENTRY_AND_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- ICP-EUR — ACTIVE_NOW — score mémoire 8.379/10 — sources V4 — WATCH_ONLY
- VTHO-EUR — ACTIVE_NOW — score mémoire 7.851/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- ETHFI-EUR — ACTIVE_NOW — score mémoire 7.827/10 — sources V4 — WATCH_ONLY
- SPX-EUR — ACTIVE_NOW — score mémoire 7.675/10 — sources V4 — WATCH_ONLY
- WLD-EUR — ACTIVE_NOW — score mémoire 7.667/10 — sources DECISION_LAYER, V4 — WATCH_ONLY
- LDO-EUR — ACTIVE_NOW — score mémoire 7.657/10 — sources V4 — WATCH_ONLY
- VET-EUR — ACTIVE_NOW — score mémoire 7.656/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- SYRUP-EUR — ACTIVE_NOW — score mémoire 7.630/10 — sources V4 — WATCH_ONLY
- INJ-EUR — ACTIVE_NOW — score mémoire 7.582/10 — sources DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- AIOZ-EUR — ACTIVE_NOW — score mémoire 7.563/10 — sources V4 — WATCH_ONLY

## Audit des plus fortes hausses

- CPOOL-EUR +35.31% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- CAP-EUR +34.38% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- CNPY-EUR +25.87% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- ARK-EUR +18.07% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- MTL-EUR +15.60% — DETECTED_TOO_LATE — couche NONE — action INTERPRETATION
- T-EUR +14.24% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- NPC-EUR +13.28% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- QKC-EUR +11.83% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- WAXP-EUR +10.02% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- RON-EUR +10.00% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
