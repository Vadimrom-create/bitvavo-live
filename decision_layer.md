# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-20T17:38:42.491565+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : HYPE-EUR | action ACHETE_MAINTENANT | opportunité 7.694 | entrée 7.600 | trend 8.250 | rang 7.584
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : aucun candidat matériel
- **MEILLEUR_LATENT_ACCELERATOR** : ZAMA-EUR | action LATENT_ACCELERATOR | opportunité 7.462 | entrée 4.500 | trend 7.700 | rang 6.679
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : INJ-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 7.707 | entrée 6.350 | trend 8.300 | rang 7.475
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. HYPE-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 7.584
2. INJ-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.475
3. ENA-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.070

## Accélération indépendante

- SAGA-EUR — CONFIRMED_ACCELERATION — score 9.730/10 — DETECTED_BUT_TOO_LATE
- PTB-EUR — CONFIRMED_ACCELERATION — score 8.518/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- XPL-EUR — ACTIVE_NOW — score mémoire 6.549/10 — sources V4 — BUYABLE_NOW
- SAGA-EUR — ACTIVE_NOW — score mémoire 9.730/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- PTB-EUR — ACTIVE_NOW — score mémoire 8.518/10 — sources ACCELERATION, V4 — DETECTED_BUT_TOO_LATE
- ACH-EUR — ACTIVE_NOW — score mémoire 8.067/10 — sources DECISION_LAYER, V4 — WATCH_ONLY
- STX-EUR — ACTIVE_NOW — score mémoire 8.004/10 — sources DECISION_LAYER, V4 — WATCH_ONLY
- WAL-EUR — ACTIVE_NOW — score mémoire 7.875/10 — sources DECISION_LAYER, V4 — WATCH_ONLY
- PROVE-EUR — ACTIVE_NOW — score mémoire 7.819/10 — sources V4 — WATCH_ONLY
- ARK-EUR — ACTIVE_NOW — score mémoire 7.809/10 — sources ACCELERATION, V4 — WATCH_ONLY
- W-EUR — ACTIVE_NOW — score mémoire 7.777/10 — sources V4 — WATCH_ONLY
- MERL-EUR — ACTIVE_NOW — score mémoire 7.724/10 — sources V4 — WATCH_ONLY

## Audit des plus fortes hausses

- CELR-EUR +50.19% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- SAGA-EUR +46.81% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- PTB-EUR +40.28% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- FTT-EUR +27.87% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- C-EUR +17.70% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- LUNA2-EUR +15.09% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- EPIC-EUR +14.67% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- NEAR-EUR +14.42% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- KMNO-EUR +14.03% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- AVAX-EUR +13.95% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
