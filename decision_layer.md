# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-17T09:17:49.367064+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : aucun candidat matériel
- **MEILLEUR_LATENT_ACCELERATOR** : aucun candidat matériel
- **MEILLEUR_PULLBACK_REENTRY** : WLD-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 7.795 | entrée 7.050 | trend 8.150 | rang 7.557
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. WLD-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.557
2. LSK-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.421
3. TAO-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.244

## Accélération indépendante

- TREAD-EUR — CONFIRMED_ACCELERATION — score 6.500/10 — REQUIRES_V4_ENTRY_AND_EXECUTION_VALIDATION
- SYN-EUR — BUILDING_ACCELERATION — score 5.855/10 — REQUIRES_V4_ENTRY_AND_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- ETHFI-EUR — ACTIVE_NOW — score mémoire 8.421/10 — sources V4 — WATCH_ONLY
- VET-EUR — ACTIVE_NOW — score mémoire 8.239/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- DOT-EUR — ACTIVE_NOW — score mémoire 8.141/10 — sources DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- SYRUP-EUR — ACTIVE_NOW — score mémoire 8.135/10 — sources V4 — WATCH_ONLY
- KAS-EUR — ACTIVE_NOW — score mémoire 8.100/10 — sources DECISION_LAYER, V4 — WATCH_ONLY
- ICP-EUR — ACTIVE_NOW — score mémoire 7.917/10 — sources V4 — WATCH_ONLY
- LDO-EUR — ACTIVE_NOW — score mémoire 7.897/10 — sources V4 — WATCH_ONLY
- SOMI-EUR — ACTIVE_NOW — score mémoire 7.876/10 — sources V4 — WATCH_ONLY
- VTHO-EUR — ACTIVE_NOW — score mémoire 7.860/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- YB-EUR — ACTIVE_NOW — score mémoire 7.821/10 — sources V4 — WATCH_ONLY

## Audit des plus fortes hausses

- AVA-EUR +52.64% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- FOLD-EUR +36.82% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- HNT-EUR +21.95% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- PEAQ-EUR +18.41% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- NEAR-EUR +17.63% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- LIGHTER-EUR +17.49% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- SAGA-EUR +15.34% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- VVV-EUR +14.83% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- QUID-EUR +14.77% — DETECTED_TOO_LATE — couche NONE — action INTERPRETATION
- USELESS-EUR +13.86% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
