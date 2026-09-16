# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-16T13:01:06.606083+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : aucun candidat matériel
- **MEILLEUR_LATENT_ACCELERATOR** : aucun candidat matériel
- **MEILLEUR_PULLBACK_REENTRY** : NEAR-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 7.650 | entrée 7.500 | trend 8.100 | rang 7.137
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. NEAR-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.137
2. USELESS-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 6.921

## Accélération indépendante

- IOST-EUR — CONFIRMED_ACCELERATION — score 8.811/10 — DETECTED_BUT_TOO_LATE
- SYN-EUR — BUILDING_ACCELERATION — score 5.500/10 — DETECTED_BUT_TOO_LATE
- USELESS-EUR — BUILDING_ACCELERATION — score 5.134/10 — DETECTED_BUT_TOO_LATE
- ARB-EUR — BUILDING_ACCELERATION — score 4.904/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- IOST-EUR — ACTIVE_NOW — score mémoire 8.811/10 — sources ACCELERATION, V4 — DETECTED_BUT_TOO_LATE
- KAS-EUR — ACTIVE_NOW — score mémoire 8.189/10 — sources V4 — WATCH_ONLY
- LDO-EUR — ACTIVE_NOW — score mémoire 8.018/10 — sources V4 — WATCH_ONLY
- ETHFI-EUR — ACTIVE_NOW — score mémoire 7.934/10 — sources V4 — WATCH_ONLY
- DOT-EUR — ACTIVE_NOW — score mémoire 7.911/10 — sources DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- XVG-EUR — ACTIVE_NOW — score mémoire 7.844/10 — sources V4 — WATCH_ONLY
- ICP-EUR — ACTIVE_NOW — score mémoire 7.832/10 — sources V4 — WATCH_ONLY
- VTHO-EUR — ACTIVE_NOW — score mémoire 7.768/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- SOMI-EUR — ACTIVE_NOW — score mémoire 7.752/10 — sources V4 — WATCH_ONLY
- CAKE-EUR — ACTIVE_NOW — score mémoire 7.735/10 — sources V4 — WATCH_ONLY

## Audit des plus fortes hausses

- SYN-EUR +115.07% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- LSK-EUR +63.44% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- CNPY-EUR +20.53% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ARB-EUR +19.76% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- FOLD-EUR +19.04% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- IOST-EUR +18.06% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- USELESS-EUR +13.08% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- HEI-EUR +12.85% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- ZKJ-EUR +11.17% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- G-EUR +7.13% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
