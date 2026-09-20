# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-20T16:19:50.803487+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : SOL-EUR | action ACHETE_MAINTENANT | opportunité 8.911 | entrée 7.850 | trend 7.700 | rang 7.885
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : S-EUR | action PLACE_LIMITE_PASSIVE | opportunité 7.710 | entrée 6.100 | trend 8.400 | rang 7.338
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : aucun candidat matériel
- **MEILLEUR_PULLBACK_REENTRY** : ENA-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 9.293 | entrée 7.250 | trend 8.500 | rang 7.988
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. ENA-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.988
2. SOL-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 7.885
3. HYPE-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 7.810

## Accélération indépendante

- NEAR-EUR — CONFIRMED_ACCELERATION — score 6.695/10 — DETECTED_BUT_TOO_LATE
- EPIC-EUR — CONFIRMED_ACCELERATION — score 6.589/10 — DETECTED_BUT_TOO_LATE
- ZAMA-EUR — BUILDING_ACCELERATION — score 5.888/10 — DETECTED_BUT_TOO_LATE
- ENA-EUR — BUILDING_ACCELERATION — score 5.807/10 — DETECTED_BUT_TOO_LATE
- ONDO-EUR — BUILDING_ACCELERATION — score 4.959/10 — REQUIRES_V4_ENTRY_AND_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- SUI-EUR — ACTIVE_NOW — score mémoire 7.137/10 — sources ACCELERATION, DECISION_LAYER, V4 — BUYABLE_NOW
- ONDO-EUR — ACTIVE_NOW — score mémoire 7.053/10 — sources ACCELERATION, DECISION_LAYER, V4 — BUYABLE_NOW
- MERL-EUR — ACTIVE_NOW — score mémoire 8.466/10 — sources V4 — WATCH_ONLY
- WAL-EUR — ACTIVE_NOW — score mémoire 8.327/10 — sources DECISION_LAYER, V4 — WATCH_ONLY
- SENT-EUR — ACTIVE_NOW — score mémoire 8.232/10 — sources V4 — WATCH_ONLY
- RAY-EUR — ACTIVE_NOW — score mémoire 8.068/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- PROVE-EUR — ACTIVE_NOW — score mémoire 8.053/10 — sources V4 — WATCH_ONLY
- STX-EUR — ACTIVE_NOW — score mémoire 8.020/10 — sources DECISION_LAYER, V4 — WATCH_ONLY
- PENDLE-EUR — ACTIVE_NOW — score mémoire 8.015/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- ENA-EUR — ACTIVE_NOW — score mémoire 7.988/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE

## Audit des plus fortes hausses

- FTT-EUR +57.35% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE
- CELR-EUR +40.54% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- EPIC-EUR +23.82% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- SAGA-EUR +23.61% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- PTB-EUR +22.73% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- AVAX-EUR +18.14% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- LUNA2-EUR +14.11% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE
- ALGO-EUR +13.15% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- NEAR-EUR +13.09% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- C-EUR +10.70% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
