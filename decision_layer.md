# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-16T07:42:39.370782+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : aucun candidat matériel
- **MEILLEUR_LATENT_ACCELERATOR** : aucun candidat matériel
- **MEILLEUR_PULLBACK_REENTRY** : VTHO-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.105 | entrée 5.400 | trend 9.200 | rang 7.928
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. VTHO-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.928
2. TAO-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.050
3. USELESS-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 6.378

## Accélération indépendante

- SYN-EUR — CONFIRMED_ACCELERATION — score 9.400/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- SYN-EUR — ACTIVE_NOW — score mémoire 9.400/10 — sources ACCELERATION, V4 — DETECTED_BUT_TOO_LATE
- VET-EUR — ACTIVE_NOW — score mémoire 8.370/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- LDO-EUR — ACTIVE_NOW — score mémoire 8.032/10 — sources V4 — WATCH_ONLY
- NEAR-EUR — ACTIVE_NOW — score mémoire 8.002/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- XVG-EUR — ACTIVE_NOW — score mémoire 7.930/10 — sources V4 — WATCH_ONLY
- VTHO-EUR — ACTIVE_NOW — score mémoire 7.928/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- KAS-EUR — ACTIVE_NOW — score mémoire 7.928/10 — sources V4 — WATCH_ONLY
- ICP-EUR — ACTIVE_NOW — score mémoire 7.854/10 — sources V4 — WATCH_ONLY
- LIGHTER-EUR — ACTIVE_NOW — score mémoire 7.741/10 — sources V4 — WATCH_ONLY
- CVC-EUR — MEMORY_24H — score mémoire 7.734/10 — sources ACCELERATION, V4 — MEMORY_ONLY

## Audit des plus fortes hausses

- SYN-EUR +125.54% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- USELESS-EUR +20.80% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- ARB-EUR +15.83% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- CNPY-EUR +13.17% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- LMWR-EUR +13.07% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE
- FOLD-EUR +12.42% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- G-EUR +12.31% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- LSK-EUR +12.20% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- ALIGN-EUR +11.55% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- GLMR-EUR +9.33% — DETECTED_EARLY — couche NONE — action INTERPRETATION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
