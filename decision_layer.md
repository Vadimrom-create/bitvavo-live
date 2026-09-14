# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-14T15:38:39.267910+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : NEAR-EUR | action PLACE_LIMITE_PASSIVE | opportunité 7.557 | entrée 6.700 | trend 8.100 | rang 7.376
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : aucun candidat matériel
- **MEILLEUR_PULLBACK_REENTRY** : VTHO-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.603 | entrée 6.300 | trend 9.200 | rang 8.172
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. VTHO-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.172
2. NEAR-EUR — MEILLEURE_LIMITE_PASSIVE — PLACE_LIMITE_PASSIVE — rank 7.376
3. USELESS-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 6.983

## Accélération indépendante

- LSK-EUR — CONFIRMED_ACCELERATION — score 6.604/10 — REQUIRES_V4_ENTRY_AND_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- VTHO-EUR — ACTIVE_NOW — score mémoire 8.172/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- CAKE-EUR — ACTIVE_NOW — score mémoire 8.149/10 — sources V4 — WATCH_ONLY
- BNB-EUR — ACTIVE_NOW — score mémoire 7.857/10 — sources V4 — WATCH_ONLY
- WLD-EUR — ACTIVE_NOW — score mémoire 7.846/10 — sources DECISION_LAYER, V4 — WATCH_ONLY
- ETHFI-EUR — ACTIVE_NOW — score mémoire 7.744/10 — sources V4 — WATCH_ONLY
- VET-EUR — ACTIVE_NOW — score mémoire 7.707/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- LDO-EUR — ACTIVE_NOW — score mémoire 7.700/10 — sources V4 — WATCH_ONLY
- AIOZ-EUR — ACTIVE_NOW — score mémoire 7.598/10 — sources V4 — WATCH_ONLY
- ICP-EUR — ACTIVE_NOW — score mémoire 7.590/10 — sources V4 — WATCH_ONLY
- AERO-EUR — MEMORY_24H — score mémoire 7.561/10 — sources V4 — MEMORY_ONLY

## Audit des plus fortes hausses

- CAP-EUR +35.00% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- CPOOL-EUR +34.99% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- CNPY-EUR +24.63% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- T-EUR +16.17% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- MTL-EUR +13.82% — DETECTED_TOO_LATE — couche NONE — action INTERPRETATION
- ARK-EUR +13.15% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- NPC-EUR +11.53% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- RON-EUR +9.53% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- CAKE-EUR +9.17% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE
- WAXP-EUR +7.89% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
