# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-20T17:33:18.799354+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : HYPE-EUR | action ACHETE_MAINTENANT | opportunité 7.663 | entrée 7.600 | trend 8.250 | rang 7.570
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : aucun candidat matériel
- **MEILLEUR_LATENT_ACCELERATOR** : INJ-EUR | action LATENT_ACCELERATOR | opportunité 7.473 | entrée 4.500 | trend 8.300 | rang 7.086
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : ENA-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.125 | entrée 6.250 | trend 8.500 | rang 7.112
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. HYPE-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 7.570
2. ENA-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.112
3. INJ-EUR — MEILLEUR_LATENT_ACCELERATOR — LATENT_ACCELERATOR — rank 7.086

## Accélération indépendante

- SAGA-EUR — CONFIRMED_ACCELERATION — score 7.407/10 — DETECTED_BUT_TOO_LATE
- PTB-EUR — BUILDING_ACCELERATION — score 6.177/10 — DETECTED_BUT_TOO_LATE
- CELR-EUR — BUILDING_ACCELERATION — score 5.814/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- XPL-EUR — ACTIVE_NOW — score mémoire 6.472/10 — sources V4 — BUYABLE_NOW
- STX-EUR — ACTIVE_NOW — score mémoire 8.035/10 — sources DECISION_LAYER, V4 — WATCH_ONLY
- ACH-EUR — ACTIVE_NOW — score mémoire 8.004/10 — sources DECISION_LAYER, V4 — WATCH_ONLY
- AIOZ-EUR — ACTIVE_NOW — score mémoire 7.922/10 — sources V4 — WATCH_ONLY
- PENDLE-EUR — ACTIVE_NOW — score mémoire 7.919/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- PROVE-EUR — ACTIVE_NOW — score mémoire 7.819/10 — sources V4 — WATCH_ONLY
- COW-EUR — ACTIVE_NOW — score mémoire 7.809/10 — sources V4 — WATCH_ONLY
- KAS-EUR — ACTIVE_NOW — score mémoire 7.783/10 — sources DECISION_LAYER, V4 — WATCH_ONLY
- ARK-EUR — ACTIVE_NOW — score mémoire 7.772/10 — sources ACCELERATION, V4 — WATCH_ONLY
- MERL-EUR — ACTIVE_NOW — score mémoire 7.750/10 — sources V4 — WATCH_ONLY

## Audit des plus fortes hausses

- CELR-EUR +51.25% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- SAGA-EUR +47.32% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- PTB-EUR +36.52% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- FTT-EUR +29.60% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- EPIC-EUR +18.42% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- C-EUR +17.95% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- KMNO-EUR +14.94% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- LUNA2-EUR +14.35% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- AVAX-EUR +14.33% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- S-EUR +13.80% — DETECTED_EARLY — couche NONE — action INTERPRETATION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
