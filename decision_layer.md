# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-19T16:50:14.540245+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : PEPE-EUR | action ACHETE_MAINTENANT | opportunité 8.642 | entrée 7.550 | trend 8.450 | rang 7.848
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : aucun candidat matériel
- **MEILLEUR_LATENT_ACCELERATOR** : TAO-EUR | action LATENT_ACCELERATOR | opportunité 7.413 | entrée 4.500 | trend 8.050 | rang 6.988
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : HYPE-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 7.874 | entrée 6.550 | trend 8.750 | rang 7.782
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. PEPE-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 7.848
2. HYPE-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.782
3. SOL-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.233

## Accélération indépendante

- G-EUR — CONFIRMED_ACCELERATION — score 6.994/10 — DETECTED_BUT_TOO_LATE
- FIL-EUR — CONFIRMED_ACCELERATION — score 6.940/10 — DETECTED_BUT_TOO_LATE
- SYN-EUR — BUILDING_ACCELERATION — score 6.030/10 — DETECTED_BUT_TOO_LATE
- PEPE-EUR — BUILDING_ACCELERATION — score 5.671/10 — REQUIRES_V4_ENTRY_AND_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- PEPE-EUR — ACTIVE_NOW — score mémoire 7.848/10 — sources ACCELERATION, DECISION_LAYER, V4 — BUYABLE_NOW
- C-EUR — MEMORY_24H — score mémoire 9.307/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- LPT-EUR — ACTIVE_NOW — score mémoire 8.254/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- ROSE-EUR — ACTIVE_NOW — score mémoire 8.112/10 — sources V4 — WATCH_ONLY
- AAVE-EUR — ACTIVE_NOW — score mémoire 8.041/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- KAS-EUR — ACTIVE_NOW — score mémoire 7.988/10 — sources DECISION_LAYER, V4 — WATCH_ONLY
- ZIL-EUR — ACTIVE_NOW — score mémoire 7.936/10 — sources DECISION_LAYER, V4 — WATCH_ONLY
- ATH-EUR — ACTIVE_NOW — score mémoire 7.929/10 — sources V4 — WATCH_ONLY
- ZK-EUR — ACTIVE_NOW — score mémoire 7.884/10 — sources V4 — WATCH_ONLY
- WAL-EUR — ACTIVE_NOW — score mémoire 7.871/10 — sources V4 — WATCH_ONLY

## Audit des plus fortes hausses

- G-EUR +41.92% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ZAMA-EUR +38.50% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- SYN-EUR +34.78% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- XTZ-EUR +30.28% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- EPIC-EUR +26.86% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ENA-EUR +22.67% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- SAGA-EUR +22.38% — DETECTED_TOO_LATE — couche NONE — action INTERPRETATION
- AIOZ-EUR +21.53% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- EDGE-EUR +21.39% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- STRK-EUR +20.89% — DETECTED_EARLY — couche NONE — action INTERPRETATION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
