# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-18T08:26:21.703460+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : aucun candidat matériel
- **MEILLEUR_LATENT_ACCELERATOR** : aucun candidat matériel
- **MEILLEUR_PULLBACK_REENTRY** : VTHO-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.501 | entrée 5.450 | trend 9.200 | rang 7.806
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. VTHO-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.806
2. AKT-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.591

## Accélération indépendante

- CNPY-EUR — BUILDING_ACCELERATION — score 5.049/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- YB-EUR — ACTIVE_NOW — score mémoire 8.218/10 — sources V4 — WATCH_ONLY
- ETHFI-EUR — ACTIVE_NOW — score mémoire 8.212/10 — sources V4 — DETECTED_BUT_TOO_LATE
- LDO-EUR — ACTIVE_NOW — score mémoire 8.126/10 — sources V4 — WATCH_ONLY
- ICP-EUR — ACTIVE_NOW — score mémoire 7.986/10 — sources V4 — WATCH_ONLY
- VET-EUR — ACTIVE_NOW — score mémoire 7.890/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- TAO-EUR — ACTIVE_NOW — score mémoire 7.829/10 — sources DECISION_LAYER, V4 — WATCH_ONLY
- VTHO-EUR — ACTIVE_NOW — score mémoire 7.806/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- ARB-EUR — MEMORY_24H — score mémoire 7.749/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- XVG-EUR — ACTIVE_NOW — score mémoire 7.727/10 — sources V4 — WATCH_ONLY
- ATOM-EUR — ACTIVE_NOW — score mémoire 7.692/10 — sources V4 — WATCH_ONLY

## Audit des plus fortes hausses

- G-EUR +79.67% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- DRIFT-EUR +41.64% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- CNPY-EUR +38.92% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- CROSS-EUR +29.00% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- UNI-EUR +27.67% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- NEAR-EUR +25.94% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- ARB-EUR +25.39% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- STRK-EUR +24.28% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- MET-EUR +22.46% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE
- COTI-EUR +18.76% — DETECTED_EARLY — couche NONE — action INTERPRETATION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
