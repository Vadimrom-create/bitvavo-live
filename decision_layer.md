# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-16T23:27:11.170617+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : aucun candidat matériel
- **MEILLEUR_LATENT_ACCELERATOR** : aucun candidat matériel
- **MEILLEUR_PULLBACK_REENTRY** : NEAR-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 7.839 | entrée 7.950 | trend 8.100 | rang 7.190
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. NEAR-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.190

## Accélération indépendante

- SYN-EUR — CONFIRMED_ACCELERATION — score 7.335/10 — DETECTED_BUT_TOO_LATE
- NEAR-EUR — BUILDING_ACCELERATION — score 5.773/10 — DETECTED_BUT_TOO_LATE
- TREAD-EUR — BUILDING_ACCELERATION — score 5.714/10 — REQUIRES_V4_ENTRY_AND_EXECUTION_VALIDATION
- ONDO-EUR — BUILDING_ACCELERATION — score 5.024/10 — REQUIRES_V4_ENTRY_AND_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- VTHO-EUR — ACTIVE_NOW — score mémoire 8.121/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- LDO-EUR — ACTIVE_NOW — score mémoire 8.119/10 — sources V4 — WATCH_ONLY
- VET-EUR — ACTIVE_NOW — score mémoire 8.102/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- YB-EUR — ACTIVE_NOW — score mémoire 8.019/10 — sources V4 — WATCH_ONLY
- SOMI-EUR — ACTIVE_NOW — score mémoire 7.980/10 — sources V4 — WATCH_ONLY
- ICP-EUR — ACTIVE_NOW — score mémoire 7.957/10 — sources V4 — WATCH_ONLY
- ETHFI-EUR — ACTIVE_NOW — score mémoire 7.935/10 — sources V4 — WATCH_ONLY
- CAKE-EUR — ACTIVE_NOW — score mémoire 7.905/10 — sources V4 — WATCH_ONLY
- ATOM-EUR — ACTIVE_NOW — score mémoire 7.846/10 — sources V4 — DETECTED_BUT_TOO_LATE
- AKT-EUR — ACTIVE_NOW — score mémoire 7.823/10 — sources DECISION_LAYER, V4 — WATCH_ONLY

## Audit des plus fortes hausses

- SYN-EUR +81.62% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- LSK-EUR +35.33% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- HEI-EUR +26.88% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- FOLD-EUR +24.67% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- HNT-EUR +22.44% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- DGB-EUR +16.96% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- AGI-EUR +15.40% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- IOST-EUR +13.03% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- NEAR-EUR +12.38% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- RAY-EUR +11.81% — DETECTED_EARLY — couche NONE — action INTERPRETATION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
