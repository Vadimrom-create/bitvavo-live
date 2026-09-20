# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-20T10:23:25.804826+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : aucun candidat matériel
- **MEILLEUR_LATENT_ACCELERATOR** : aucun candidat matériel
- **MEILLEUR_PULLBACK_REENTRY** : INJ-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.125 | entrée 6.500 | trend 8.300 | rang 7.386
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. INJ-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.386
2. ENA-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.332
3. HYPE-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.134

## Accélération indépendante

Aucune accélération indépendante confirmée ou en construction.

## Watchlist persistante 24–72 h

- STX-EUR — ACTIVE_NOW — score mémoire 7.931/10 — sources DECISION_LAYER, V4 — WATCH_ONLY
- COTI-EUR — MEMORY_24H — score mémoire 7.904/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- MERL-EUR — ACTIVE_NOW — score mémoire 7.878/10 — sources V4 — WATCH_ONLY
- KAS-EUR — ACTIVE_NOW — score mémoire 7.790/10 — sources DECISION_LAYER, V4 — WATCH_ONLY
- SENT-EUR — ACTIVE_NOW — score mémoire 7.772/10 — sources V4 — WATCH_ONLY
- BIGTIME-EUR — MEMORY_24H — score mémoire 7.662/10 — sources V4 — MEMORY_ONLY
- AIOZ-EUR — ACTIVE_NOW — score mémoire 7.597/10 — sources V4 — WATCH_ONLY
- PENDLE-EUR — ACTIVE_NOW — score mémoire 7.588/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- LPT-EUR — ACTIVE_NOW — score mémoire 7.533/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- XTZ-EUR — MEMORY_24H — score mémoire 7.479/10 — sources DECISION_LAYER, V4 — MEMORY_ONLY

## Audit des plus fortes hausses

- CELR-EUR +78.88% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- ZIL-EUR +18.67% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- SKL-EUR +17.09% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- CTSI-EUR +13.65% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- ZAMA-EUR +12.53% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- T-EUR +11.71% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- C-EUR +11.33% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- SOLV-EUR +11.23% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ONG-EUR +9.25% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- JTO-EUR +8.71% — DETECTED_EARLY — couche NONE — action INTERPRETATION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
