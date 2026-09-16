# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-16T12:20:17.228482+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : aucun candidat matériel
- **MEILLEUR_LATENT_ACCELERATOR** : aucun candidat matériel
- **MEILLEUR_PULLBACK_REENTRY** : TAO-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.990 | entrée 7.050 | trend 7.650 | rang 7.894
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. TAO-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.894
2. NEAR-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.294
3. USELESS-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 6.803

## Accélération indépendante

- SYN-EUR — CONFIRMED_ACCELERATION — score 8.500/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- SYN-EUR — ACTIVE_NOW — score mémoire 8.500/10 — sources ACCELERATION, V4 — DETECTED_BUT_TOO_LATE
- DOT-EUR — ACTIVE_NOW — score mémoire 8.062/10 — sources DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- ETHFI-EUR — ACTIVE_NOW — score mémoire 7.963/10 — sources V4 — WATCH_ONLY
- VET-EUR — ACTIVE_NOW — score mémoire 7.939/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- LDO-EUR — ACTIVE_NOW — score mémoire 7.913/10 — sources V4 — WATCH_ONLY
- TAO-EUR — ACTIVE_NOW — score mémoire 7.894/10 — sources DECISION_LAYER, V4 — WATCH_ONLY
- XVG-EUR — ACTIVE_NOW — score mémoire 7.825/10 — sources V4 — WATCH_ONLY
- ICP-EUR — ACTIVE_NOW — score mémoire 7.770/10 — sources V4 — WATCH_ONLY
- KAS-EUR — ACTIVE_NOW — score mémoire 7.757/10 — sources V4 — WATCH_ONLY
- VTHO-EUR — ACTIVE_NOW — score mémoire 7.732/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY

## Audit des plus fortes hausses

- SYN-EUR +152.72% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- LSK-EUR +69.35% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- FOLD-EUR +26.41% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- CNPY-EUR +23.73% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ARB-EUR +20.64% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- HEI-EUR +17.51% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- USELESS-EUR +13.75% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- IOST-EUR +8.55% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- G-EUR +8.11% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- SOMI-EUR +6.18% — DETECTED_EARLY — couche NONE — action INTERPRETATION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
