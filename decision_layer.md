# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-20T14:56:48.743336+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : SUI-EUR | action ACHETE_MAINTENANT | opportunité 7.360 | entrée 7.400 | trend 6.500 | rang 6.723
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : aucun candidat matériel
- **MEILLEUR_LATENT_ACCELERATOR** : aucun candidat matériel
- **MEILLEUR_PULLBACK_REENTRY** : WAL-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 7.840 | entrée 5.100 | trend 8.700 | rang 7.590
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. WAL-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.590
2. ALGO-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.522
3. HYPE-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.354

## Accélération indépendante

- ALGO-EUR — CONFIRMED_ACCELERATION — score 8.599/10 — REQUIRES_V4_ENTRY_AND_EXECUTION_VALIDATION
- C-EUR — CONFIRMED_ACCELERATION — score 7.237/10 — DETECTED_BUT_TOO_LATE
- SAGA-EUR — BUILDING_ACCELERATION — score 6.436/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- ALGO-EUR — ACTIVE_NOW — score mémoire 8.599/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- KAS-EUR — ACTIVE_NOW — score mémoire 8.119/10 — sources DECISION_LAYER, V4 — WATCH_ONLY
- AIOZ-EUR — ACTIVE_NOW — score mémoire 8.044/10 — sources V4 — WATCH_ONLY
- SIGN-EUR — ACTIVE_NOW — score mémoire 8.033/10 — sources V4 — WATCH_ONLY
- COW-EUR — ACTIVE_NOW — score mémoire 8.000/10 — sources V4 — WATCH_ONLY
- STX-EUR — ACTIVE_NOW — score mémoire 7.965/10 — sources DECISION_LAYER, V4 — WATCH_ONLY
- CAKE-EUR — MEMORY_24H — score mémoire 7.877/10 — sources DECISION_LAYER, V4 — MEMORY_ONLY
- CELR-EUR — MEMORY_24H — score mémoire 7.831/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- BIGTIME-EUR — MEMORY_24H — score mémoire 7.662/10 — sources V4 — MEMORY_ONLY
- ZIL-EUR — ACTIVE_NOW — score mémoire 7.644/10 — sources DECISION_LAYER, V4 — WATCH_ONLY

## Audit des plus fortes hausses

- CELR-EUR +83.97% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- C-EUR +27.58% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- PTB-EUR +18.25% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- EPIC-EUR +16.20% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- AVAX-EUR +15.80% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- CTSI-EUR +12.08% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- SAGA-EUR +11.71% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ALGO-EUR +9.40% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- S-EUR +9.04% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- HBAR-EUR +8.56% — DETECTED_EARLY — couche NONE — action INTERPRETATION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
