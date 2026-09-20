# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-20T14:11:48.521919+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : ALGO-EUR | action ACHETE_MAINTENANT | opportunité 8.091 | entrée 7.550 | trend 8.100 | rang 7.572
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : aucun candidat matériel
- **MEILLEUR_LATENT_ACCELERATOR** : ZAMA-EUR | action LATENT_ACCELERATOR | opportunité 7.404 | entrée 5.250 | trend 8.250 | rang 6.596
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : WAL-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 7.918 | entrée 5.450 | trend 8.700 | rang 7.668
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. WAL-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.668
2. ALGO-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 7.572
3. STRK-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.455

## Accélération indépendante

- CELR-EUR — CONFIRMED_ACCELERATION — score 7.831/10 — DETECTED_BUT_TOO_LATE
- HBAR-EUR — CONFIRMED_ACCELERATION — score 7.704/10 — DETECTED_BUT_TOO_LATE
- ALGO-EUR — CONFIRMED_ACCELERATION — score 6.555/10 — REQUIRES_V4_ENTRY_AND_EXECUTION_VALIDATION
- EPIC-EUR — BUILDING_ACCELERATION — score 5.703/10 — DETECTED_BUT_TOO_LATE
- AVAX-EUR — BUILDING_ACCELERATION — score 4.975/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- ALGO-EUR — ACTIVE_NOW — score mémoire 7.572/10 — sources ACCELERATION, DECISION_LAYER, V4 — BUYABLE_NOW
- CAKE-EUR — ACTIVE_NOW — score mémoire 8.134/10 — sources DECISION_LAYER, V4 — WATCH_ONLY
- NPC-EUR — ACTIVE_NOW — score mémoire 7.849/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- CELR-EUR — ACTIVE_NOW — score mémoire 7.831/10 — sources ACCELERATION, V4 — DETECTED_BUT_TOO_LATE
- AERO-EUR — ACTIVE_NOW — score mémoire 7.782/10 — sources V4 — WATCH_ONLY
- STX-EUR — ACTIVE_NOW — score mémoire 7.769/10 — sources DECISION_LAYER, V4 — WATCH_ONLY
- HBAR-EUR — ACTIVE_NOW — score mémoire 7.704/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- WAL-EUR — ACTIVE_NOW — score mémoire 7.668/10 — sources DECISION_LAYER, V4 — WATCH_ONLY
- BIGTIME-EUR — MEMORY_24H — score mémoire 7.662/10 — sources V4 — MEMORY_ONLY
- SENT-EUR — ACTIVE_NOW — score mémoire 7.648/10 — sources V4 — WATCH_ONLY

## Audit des plus fortes hausses

- CELR-EUR +82.81% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- EPIC-EUR +24.14% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- AVAX-EUR +15.49% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- C-EUR +15.18% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- CTSI-EUR +10.59% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- ZAMA-EUR +10.59% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- PTB-EUR +10.23% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- HBAR-EUR +8.15% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- STRK-EUR +7.84% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- S-EUR +7.48% — DETECTED_EARLY — couche NONE — action INTERPRETATION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
