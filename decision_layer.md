# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-17T00:43:06.622564+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : aucun candidat matériel
- **MEILLEUR_LATENT_ACCELERATOR** : aucun candidat matériel
- **MEILLEUR_PULLBACK_REENTRY** : VTHO-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.448 | entrée 6.550 | trend 9.200 | rang 8.185
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. VTHO-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.185
2. NEAR-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.633

## Accélération indépendante

- VTHO-EUR — BUILDING_ACCELERATION — score 5.669/10 — REQUIRES_V4_ENTRY_AND_EXECUTION_VALIDATION
- LAPTOP-EUR — BUILDING_ACCELERATION — score 5.500/10 — DETECTED_BUT_TOO_LATE
- LSK-EUR — BUILDING_ACCELERATION — score 4.793/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- VTHO-EUR — ACTIVE_NOW — score mémoire 8.185/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- INJ-EUR — ACTIVE_NOW — score mémoire 8.170/10 — sources DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- LDO-EUR — ACTIVE_NOW — score mémoire 8.128/10 — sources V4 — WATCH_ONLY
- YB-EUR — ACTIVE_NOW — score mémoire 8.087/10 — sources V4 — WATCH_ONLY
- ATOM-EUR — ACTIVE_NOW — score mémoire 8.013/10 — sources V4 — DETECTED_BUT_TOO_LATE
- XVG-EUR — ACTIVE_NOW — score mémoire 8.012/10 — sources V4 — WATCH_ONLY
- NPC-EUR — ACTIVE_NOW — score mémoire 8.005/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- ICP-EUR — ACTIVE_NOW — score mémoire 8.004/10 — sources V4 — WATCH_ONLY
- ETHFI-EUR — ACTIVE_NOW — score mémoire 7.960/10 — sources V4 — WATCH_ONLY
- SOMI-EUR — ACTIVE_NOW — score mémoire 7.882/10 — sources V4 — WATCH_ONLY

## Audit des plus fortes hausses

- SYN-EUR +78.50% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- LSK-EUR +34.45% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- DGB-EUR +18.06% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- LIGHTER-EUR +16.66% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- FOLD-EUR +16.61% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- AGI-EUR +15.20% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- NEAR-EUR +15.19% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- RAY-EUR +15.04% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- TRAC-EUR +14.35% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE
- IOST-EUR +13.81% — DETECTED_EARLY — couche NONE — action INTERPRETATION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
