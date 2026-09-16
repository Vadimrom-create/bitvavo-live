# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-16T09:16:52.805011+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : aucun candidat matériel
- **MEILLEUR_LATENT_ACCELERATOR** : aucun candidat matériel
- **MEILLEUR_PULLBACK_REENTRY** : TAO-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 7.342 | entrée 6.700 | trend 7.650 | rang 7.102
  - Trend remains strong; candidate retained for re-entry instead of discarded.

## Top cross-sectionnel

1. TAO-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.102
2. USELESS-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 6.374

## Accélération indépendante

- SYN-EUR — BUILDING_ACCELERATION — score 6.189/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- ZIL-EUR — ACTIVE_NOW — score mémoire 8.271/10 — sources DECISION_LAYER, V4 — WATCH_ONLY
- AIOZ-EUR — ACTIVE_NOW — score mémoire 8.153/10 — sources V4 — WATCH_ONLY
- VTHO-EUR — ACTIVE_NOW — score mémoire 8.102/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- PENDLE-EUR — ACTIVE_NOW — score mémoire 7.922/10 — sources DECISION_LAYER, V4 — WATCH_ONLY
- ICP-EUR — ACTIVE_NOW — score mémoire 7.862/10 — sources V4 — WATCH_ONLY
- CVC-EUR — MEMORY_24H — score mémoire 7.734/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- COTI-EUR — ACTIVE_NOW — score mémoire 7.682/10 — sources V4 — DETECTED_BUT_TOO_LATE
- ETHFI-EUR — ACTIVE_NOW — score mémoire 7.649/10 — sources V4 — WATCH_ONLY
- LDO-EUR — ACTIVE_NOW — score mémoire 7.631/10 — sources V4 — WATCH_ONLY
- YB-EUR — ACTIVE_NOW — score mémoire 7.630/10 — sources V4 — WATCH_ONLY

## Audit des plus fortes hausses

- SYN-EUR +127.04% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- LSK-EUR +26.36% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- USELESS-EUR +21.74% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- LMWR-EUR +20.65% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- ARB-EUR +15.57% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ALIGN-EUR +11.16% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- FOLD-EUR +10.90% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- CNPY-EUR +10.67% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- G-EUR +7.14% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- SIGN-EUR +5.65% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
