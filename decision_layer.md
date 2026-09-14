# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-14T16:16:53.546209+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : NPC-EUR | action PLACE_LIMITE_PASSIVE | opportunité 7.580 | entrée 6.750 | trend 7.750 | rang 6.692
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : aucun candidat matériel
- **MEILLEUR_PULLBACK_REENTRY** : VTHO-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.221 | entrée 5.850 | trend 9.200 | rang 8.036
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. VTHO-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.036
2. NEAR-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.499
3. NPC-EUR — MEILLEURE_LIMITE_PASSIVE — PLACE_LIMITE_PASSIVE — rank 6.692

## Accélération indépendante

Aucune accélération indépendante confirmée ou en construction.

## Watchlist persistante 24–72 h

- VTHO-EUR — ACTIVE_NOW — score mémoire 8.036/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- ICP-EUR — ACTIVE_NOW — score mémoire 7.999/10 — sources V4 — WATCH_ONLY
- SUPER-EUR — ACTIVE_NOW — score mémoire 7.841/10 — sources V4 — WATCH_ONLY
- LDO-EUR — ACTIVE_NOW — score mémoire 7.705/10 — sources V4 — WATCH_ONLY
- SPX-EUR — MEMORY_24H — score mémoire 7.675/10 — sources V4 — MEMORY_ONLY
- KAS-EUR — ACTIVE_NOW — score mémoire 7.604/10 — sources V4 — WATCH_ONLY
- XVG-EUR — ACTIVE_NOW — score mémoire 7.594/10 — sources V4 — WATCH_ONLY
- VET-EUR — ACTIVE_NOW — score mémoire 7.594/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- ETHFI-EUR — ACTIVE_NOW — score mémoire 7.578/10 — sources V4 — WATCH_ONLY
- WLD-EUR — ACTIVE_NOW — score mémoire 7.575/10 — sources DECISION_LAYER, V4 — WATCH_ONLY

## Audit des plus fortes hausses

- CPOOL-EUR +34.91% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- CNPY-EUR +26.88% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- CAP-EUR +24.73% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- ARK-EUR +15.98% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- MTL-EUR +14.58% — DETECTED_TOO_LATE — couche NONE — action INTERPRETATION
- NPC-EUR +13.37% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- T-EUR +12.87% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- QKC-EUR +11.53% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- RON-EUR +10.63% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- WAXP-EUR +9.53% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
