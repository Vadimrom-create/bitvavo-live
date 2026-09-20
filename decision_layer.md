# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-20T15:16:38.504237+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : HYPE-EUR | action ACHETE_MAINTENANT | opportunité 8.895 | entrée 6.950 | trend 7.950 | rang 7.995
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : aucun candidat matériel
- **MEILLEUR_LATENT_ACCELERATOR** : aucun candidat matériel
- **MEILLEUR_PULLBACK_REENTRY** : WAL-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 7.986 | entrée 5.700 | trend 8.700 | rang 7.695
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. HYPE-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 7.995
2. WAL-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.695
3. S-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.269

## Accélération indépendante

- SAGA-EUR — CONFIRMED_ACCELERATION — score 8.500/10 — DETECTED_BUT_TOO_LATE
- HBAR-EUR — BUILDING_ACCELERATION — score 5.481/10 — DETECTED_BUT_TOO_LATE
- AVAX-EUR — BUILDING_ACCELERATION — score 5.057/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- SAGA-EUR — ACTIVE_NOW — score mémoire 8.500/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- KAS-EUR — ACTIVE_NOW — score mémoire 8.335/10 — sources DECISION_LAYER, V4 — WATCH_ONLY
- XTZ-EUR — ACTIVE_NOW — score mémoire 8.138/10 — sources DECISION_LAYER, V4 — WATCH_ONLY
- CAKE-EUR — ACTIVE_NOW — score mémoire 8.061/10 — sources DECISION_LAYER, V4 — WATCH_ONLY
- AIOZ-EUR — MEMORY_24H — score mémoire 8.044/10 — sources V4 — MEMORY_ONLY
- HYPE-EUR — ACTIVE_NOW — score mémoire 7.995/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- SIGN-EUR — ACTIVE_NOW — score mémoire 7.899/10 — sources V4 — WATCH_ONLY
- CELR-EUR — MEMORY_24H — score mémoire 7.831/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- ZIL-EUR — ACTIVE_NOW — score mémoire 7.769/10 — sources DECISION_LAYER, V4 — WATCH_ONLY
- WAL-EUR — ACTIVE_NOW — score mémoire 7.695/10 — sources DECISION_LAYER, V4 — WATCH_ONLY

## Audit des plus fortes hausses

- CELR-EUR +62.89% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- C-EUR +21.49% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- SAGA-EUR +18.66% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- AVAX-EUR +17.84% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- PTB-EUR +17.42% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- ALGO-EUR +12.18% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- EPIC-EUR +12.17% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- GNO-EUR +11.77% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE
- HBAR-EUR +11.34% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- CTSI-EUR +10.08% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
