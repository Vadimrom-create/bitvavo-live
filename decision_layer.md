# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-16T22:03:00.773698+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : aucun candidat matériel
- **MEILLEUR_LATENT_ACCELERATOR** : aucun candidat matériel
- **MEILLEUR_PULLBACK_REENTRY** : USELESS-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 7.999 | entrée 7.050 | trend 8.100 | rang 7.277
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. USELESS-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.277
2. NEAR-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.087

## Accélération indépendante

Aucune accélération indépendante confirmée ou en construction.

## Watchlist persistante 24–72 h

- ETHFI-EUR — ACTIVE_NOW — score mémoire 8.355/10 — sources V4 — WATCH_ONLY
- SIGN-EUR — ACTIVE_NOW — score mémoire 8.035/10 — sources V4 — WATCH_ONLY
- ICP-EUR — ACTIVE_NOW — score mémoire 8.034/10 — sources V4 — WATCH_ONLY
- VTHO-EUR — ACTIVE_NOW — score mémoire 8.015/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- LDO-EUR — ACTIVE_NOW — score mémoire 8.007/10 — sources V4 — WATCH_ONLY
- FORM-EUR — ACTIVE_NOW — score mémoire 7.957/10 — sources V4 — WATCH_ONLY
- SPX-EUR — ACTIVE_NOW — score mémoire 7.855/10 — sources V4 — WATCH_ONLY
- AKT-EUR — MEMORY_24H — score mémoire 7.849/10 — sources DECISION_LAYER, V4 — MEMORY_ONLY
- KAS-EUR — ACTIVE_NOW — score mémoire 7.847/10 — sources DECISION_LAYER, V4 — WATCH_ONLY
- ZRX-EUR — ACTIVE_NOW — score mémoire 7.779/10 — sources V4 — WATCH_ONLY

## Audit des plus fortes hausses

- SYN-EUR +81.36% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- LSK-EUR +81.00% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- HNT-EUR +35.78% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- HEI-EUR +31.48% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- FOLD-EUR +21.39% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- AGI-EUR +16.57% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- IOST-EUR +15.83% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- DGB-EUR +15.19% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- RAY-EUR +14.29% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ARB-EUR +12.59% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
