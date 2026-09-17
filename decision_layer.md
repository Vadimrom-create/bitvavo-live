# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-17T02:31:48.461435+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : aucun candidat matériel
- **MEILLEUR_LATENT_ACCELERATOR** : aucun candidat matériel
- **MEILLEUR_PULLBACK_REENTRY** : NEAR-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 7.824 | entrée 8.300 | trend 8.100 | rang 7.215
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. NEAR-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.215
2. USELESS-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.102

## Accélération indépendante

- SYN-EUR — BUILDING_ACCELERATION — score 6.215/10 — DETECTED_BUT_TOO_LATE
- NEAR-EUR — BUILDING_ACCELERATION — score 4.828/10 — REQUIRES_V4_ENTRY_AND_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- LDO-EUR — ACTIVE_NOW — score mémoire 8.236/10 — sources V4 — WATCH_ONLY
- INJ-EUR — ACTIVE_NOW — score mémoire 8.155/10 — sources DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- ETHFI-EUR — ACTIVE_NOW — score mémoire 7.964/10 — sources V4 — WATCH_ONLY
- VTHO-EUR — ACTIVE_NOW — score mémoire 7.889/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- XPL-EUR — ACTIVE_NOW — score mémoire 7.889/10 — sources V4 — WATCH_ONLY
- YB-EUR — ACTIVE_NOW — score mémoire 7.850/10 — sources V4 — WATCH_ONLY
- KAS-EUR — ACTIVE_NOW — score mémoire 7.815/10 — sources DECISION_LAYER, V4 — WATCH_ONLY
- AIOZ-EUR — ACTIVE_NOW — score mémoire 7.815/10 — sources V4 — WATCH_ONLY
- ICP-EUR — ACTIVE_NOW — score mémoire 7.778/10 — sources V4 — WATCH_ONLY
- XVG-EUR — ACTIVE_NOW — score mémoire 7.776/10 — sources V4 — WATCH_ONLY

## Audit des plus fortes hausses

- SYN-EUR +59.73% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- LSK-EUR +31.55% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- FOLD-EUR +25.72% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- AVA-EUR +22.44% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE
- IOST-EUR +21.48% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- TRAC-EUR +19.44% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- AGI-EUR +18.97% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- QUID-EUR +17.44% — DETECTED_TOO_LATE — couche NONE — action INTERPRETATION
- RAY-EUR +16.43% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- HNT-EUR +15.66% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
