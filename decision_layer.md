# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-16T21:49:49.234597+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : aucun candidat matériel
- **MEILLEUR_LATENT_ACCELERATOR** : aucun candidat matériel
- **MEILLEUR_PULLBACK_REENTRY** : USELESS-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.326 | entrée 7.250 | trend 8.100 | rang 7.516
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. USELESS-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.516

## Accélération indépendante

Aucune accélération indépendante confirmée ou en construction.

## Watchlist persistante 24–72 h

- VTHO-EUR — ACTIVE_NOW — score mémoire 8.165/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- ICP-EUR — ACTIVE_NOW — score mémoire 8.098/10 — sources V4 — WATCH_ONLY
- FORM-EUR — ACTIVE_NOW — score mémoire 8.060/10 — sources V4 — WATCH_ONLY
- PHA-EUR — ACTIVE_NOW — score mémoire 8.047/10 — sources V4 — WATCH_ONLY
- SIGN-EUR — ACTIVE_NOW — score mémoire 8.035/10 — sources V4 — WATCH_ONLY
- LDO-EUR — ACTIVE_NOW — score mémoire 7.998/10 — sources V4 — WATCH_ONLY
- ETHFI-EUR — ACTIVE_NOW — score mémoire 7.972/10 — sources V4 — WATCH_ONLY
- NPC-EUR — ACTIVE_NOW — score mémoire 7.961/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- AKT-EUR — MEMORY_24H — score mémoire 7.849/10 — sources DECISION_LAYER, V4 — MEMORY_ONLY
- XVG-EUR — ACTIVE_NOW — score mémoire 7.721/10 — sources V4 — WATCH_ONLY

## Audit des plus fortes hausses

- SYN-EUR +121.62% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- LSK-EUR +89.41% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- HEI-EUR +33.98% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- HNT-EUR +30.87% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- FOLD-EUR +20.63% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- AGI-EUR +18.17% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- IOST-EUR +16.48% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- RAY-EUR +14.57% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ARB-EUR +14.43% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- DGB-EUR +13.39% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
