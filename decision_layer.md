# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-20T19:10:43.100639+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : HYPE-EUR | action ACHETE_MAINTENANT | opportunité 8.074 | entrée 7.200 | trend 8.500 | rang 7.826
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : ENA-EUR | action PLACE_LIMITE_PASSIVE | opportunité 7.410 | entrée 6.000 | trend 7.950 | rang 6.546
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : aucun candidat matériel
- **MEILLEUR_PULLBACK_REENTRY** : WAL-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 7.857 | entrée 6.650 | trend 8.700 | rang 7.714
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. HYPE-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 7.826
2. WAL-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.714
3. RENDER-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.499

## Accélération indépendante

Aucune accélération indépendante confirmée ou en construction.

## Watchlist persistante 24–72 h

- PTB-EUR — MEMORY_24H — score mémoire 8.518/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- C-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- CAKE-EUR — ACTIVE_NOW — score mémoire 8.297/10 — sources DECISION_LAYER, V4 — WATCH_ONLY
- STX-EUR — ACTIVE_NOW — score mémoire 8.170/10 — sources DECISION_LAYER, V4 — WATCH_ONLY
- AIOZ-EUR — ACTIVE_NOW — score mémoire 8.081/10 — sources V4 — WATCH_ONLY
- COW-EUR — ACTIVE_NOW — score mémoire 8.029/10 — sources V4 — WATCH_ONLY
- PHA-EUR — ACTIVE_NOW — score mémoire 7.958/10 — sources DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- HYPE-EUR — ACTIVE_NOW — score mémoire 7.826/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- W-EUR — ACTIVE_NOW — score mémoire 7.814/10 — sources V4 — WATCH_ONLY
- T-EUR — ACTIVE_NOW — score mémoire 7.742/10 — sources ACCELERATION, V4 — WATCH_ONLY

## Audit des plus fortes hausses

- SAGA-EUR +50.38% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- CELR-EUR +26.91% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- PTB-EUR +24.07% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- FTT-EUR +20.83% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- NIL-EUR +18.28% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- LUNA2-EUR +18.25% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- NEAR-EUR +17.17% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- STRK-EUR +16.17% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- S-EUR +16.03% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- AVAX-EUR +13.69% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
