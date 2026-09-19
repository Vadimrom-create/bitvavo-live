# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-19T13:59:00.702304+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : HYPE-EUR | action ACHETE_MAINTENANT | opportunité 8.150 | entrée 7.600 | trend 8.750 | rang 8.019
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : NPC-EUR | action PLACE_LIMITE_PASSIVE | opportunité 7.660 | entrée 6.250 | trend 8.000 | rang 7.254
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : SOL-EUR | action LATENT_ACCELERATOR | opportunité 7.551 | entrée 4.500 | trend 8.250 | rang 7.223
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : TAO-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.094 | entrée 6.650 | trend 8.300 | rang 7.691
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. HYPE-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.019
2. TAO-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.691
3. ONDO-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.625

## Accélération indépendante

- ZAMA-EUR — CONFIRMED_ACCELERATION — score 8.324/10 — DETECTED_BUT_TOO_LATE
- NPC-EUR — BUILDING_ACCELERATION — score 5.028/10 — REQUIRES_V4_ENTRY_AND_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- ZAMA-EUR — ACTIVE_NOW — score mémoire 8.324/10 — sources ACCELERATION, V4 — DETECTED_BUT_TOO_LATE
- ZRO-EUR — ACTIVE_NOW — score mémoire 8.252/10 — sources V4 — WATCH_ONLY
- LPT-EUR — ACTIVE_NOW — score mémoire 8.169/10 — sources ACCELERATION, V4 — WATCH_ONLY
- AAVE-EUR — ACTIVE_NOW — score mémoire 8.113/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- HYPE-EUR — ACTIVE_NOW — score mémoire 8.019/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- PROVE-EUR — ACTIVE_NOW — score mémoire 7.931/10 — sources V4 — WATCH_ONLY
- AIOZ-EUR — ACTIVE_NOW — score mémoire 7.908/10 — sources V4 — DETECTED_BUT_TOO_LATE
- AERO-EUR — ACTIVE_NOW — score mémoire 7.869/10 — sources V4 — WATCH_ONLY
- KMNO-EUR — ACTIVE_NOW — score mémoire 7.854/10 — sources V4 — WATCH_ONLY
- TIA-EUR — ACTIVE_NOW — score mémoire 7.774/10 — sources V4 — WATCH_ONLY

## Audit des plus fortes hausses

- ZAMA-EUR +44.55% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- SYN-EUR +33.91% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- EDGE-EUR +30.35% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- XTZ-EUR +29.84% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- SAGA-EUR +27.32% — DETECTED_TOO_LATE — couche NONE — action INTERPRETATION
- HEI-EUR +25.94% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- F-EUR +25.50% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- STRK-EUR +25.14% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ENA-EUR +22.44% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- EPIC-EUR +21.17% — DETECTED_EARLY — couche NONE — action INTERPRETATION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
