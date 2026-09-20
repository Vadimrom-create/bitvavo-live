# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-20T17:21:04.436584+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : SOL-EUR | action ACHETE_MAINTENANT | opportunité 8.548 | entrée 7.600 | trend 7.700 | rang 7.773
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : aucun candidat matériel
- **MEILLEUR_LATENT_ACCELERATOR** : ZAMA-EUR | action LATENT_ACCELERATOR | opportunité 7.422 | entrée 4.500 | trend 7.700 | rang 6.726
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : RAY-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 7.537 | entrée 4.500 | trend 8.000 | rang 6.919
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. SOL-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 7.773
2. HYPE-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 7.680
3. ADA-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 6.958

## Accélération indépendante

- CELR-EUR — CONFIRMED_ACCELERATION — score 6.575/10 — DETECTED_BUT_TOO_LATE
- PTB-EUR — BUILDING_ACCELERATION — score 5.165/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- ADA-EUR — ACTIVE_NOW — score mémoire 6.958/10 — sources ACCELERATION, DECISION_LAYER, V4 — BUYABLE_NOW
- LTC-EUR — ACTIVE_NOW — score mémoire 6.825/10 — sources DECISION_LAYER, V4 — BUYABLE_NOW
- SAGA-EUR — MEMORY_24H — score mémoire 8.151/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- ACH-EUR — ACTIVE_NOW — score mémoire 8.032/10 — sources DECISION_LAYER, V4 — WATCH_ONLY
- PROVE-EUR — ACTIVE_NOW — score mémoire 8.010/10 — sources V4 — WATCH_ONLY
- STX-EUR — ACTIVE_NOW — score mémoire 7.976/10 — sources DECISION_LAYER, V4 — WATCH_ONLY
- PENDLE-EUR — ACTIVE_NOW — score mémoire 7.941/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- WAL-EUR — ACTIVE_NOW — score mémoire 7.904/10 — sources DECISION_LAYER, V4 — WATCH_ONLY
- AIOZ-EUR — ACTIVE_NOW — score mémoire 7.900/10 — sources V4 — WATCH_ONLY
- COW-EUR — ACTIVE_NOW — score mémoire 7.839/10 — sources V4 — WATCH_ONLY

## Audit des plus fortes hausses

- CELR-EUR +53.56% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- SAGA-EUR +38.66% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- FTT-EUR +26.29% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- PTB-EUR +25.52% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- LUNA2-EUR +19.54% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- EPIC-EUR +18.40% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- C-EUR +16.24% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- KMNO-EUR +15.81% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- NEAR-EUR +14.60% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- AVAX-EUR +14.05% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
