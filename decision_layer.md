# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-20T18:41:03.841538+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : ARB-EUR | action PLACE_LIMITE_PASSIVE | opportunité 7.584 | entrée 6.650 | trend 7.300 | rang 6.691
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : aucun candidat matériel
- **MEILLEUR_PULLBACK_REENTRY** : HYPE-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 7.984 | entrée 7.700 | trend 8.500 | rang 7.824
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. HYPE-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.824
2. APT-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.575
3. ENSO-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.501

## Accélération indépendante

Aucune accélération indépendante confirmée ou en construction.

## Watchlist persistante 24–72 h

- PTB-EUR — MEMORY_24H — score mémoire 8.518/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- C-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- AIOZ-EUR — ACTIVE_NOW — score mémoire 8.339/10 — sources V4 — WATCH_ONLY
- STX-EUR — ACTIVE_NOW — score mémoire 8.266/10 — sources DECISION_LAYER, V4 — WATCH_ONLY
- 0G-EUR — ACTIVE_NOW — score mémoire 8.165/10 — sources V4 — WATCH_ONLY
- CAKE-EUR — ACTIVE_NOW — score mémoire 8.084/10 — sources DECISION_LAYER, V4 — WATCH_ONLY
- COW-EUR — ACTIVE_NOW — score mémoire 8.023/10 — sources V4 — WATCH_ONLY
- ETHFI-EUR — ACTIVE_NOW — score mémoire 7.879/10 — sources V4 — WATCH_ONLY
- KAS-EUR — ACTIVE_NOW — score mémoire 7.861/10 — sources DECISION_LAYER, V4 — WATCH_ONLY
- HYPE-EUR — ACTIVE_NOW — score mémoire 7.824/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY

## Audit des plus fortes hausses

- SAGA-EUR +42.54% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- CELR-EUR +35.98% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- PTB-EUR +26.55% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- FTT-EUR +24.51% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- STRK-EUR +18.77% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- LUNA2-EUR +16.04% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- AVA-EUR +15.05% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- S-EUR +14.16% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- NIL-EUR +14.16% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- AVAX-EUR +13.65% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
