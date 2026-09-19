# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-19T19:37:28.538668+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : HYPE-EUR | action ACHETE_MAINTENANT | opportunité 8.115 | entrée 6.800 | trend 8.750 | rang 7.910
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : FIL-EUR | action PLACE_LIMITE_PASSIVE | opportunité 7.470 | entrée 6.550 | trend 8.050 | rang 6.720
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : NEAR-EUR | action LATENT_ACCELERATOR | opportunité 7.416 | entrée 4.500 | trend 7.550 | rang 6.789
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : SUI-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.479 | entrée 7.350 | trend 8.450 | rang 7.936
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. SUI-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.936
2. HYPE-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 7.910
3. VET-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.829

## Accélération indépendante

- NEAR-EUR — BUILDING_ACCELERATION — score 5.735/10 — DETECTED_BUT_TOO_LATE
- ZAMA-EUR — BUILDING_ACCELERATION — score 5.695/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- SENT-EUR — ACTIVE_NOW — score mémoire 8.167/10 — sources V4 — WATCH_ONLY
- IMX-EUR — ACTIVE_NOW — score mémoire 8.048/10 — sources V4 — WATCH_ONLY
- SUI-EUR — ACTIVE_NOW — score mémoire 7.936/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- HYPE-EUR — ACTIVE_NOW — score mémoire 7.910/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- PENDLE-EUR — ACTIVE_NOW — score mémoire 7.868/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- AAVE-EUR — ACTIVE_NOW — score mémoire 7.857/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- JUP-EUR — ACTIVE_NOW — score mémoire 7.848/10 — sources DECISION_LAYER, V4 — WATCH_ONLY
- ROSE-EUR — ACTIVE_NOW — score mémoire 7.831/10 — sources V4 — WATCH_ONLY
- VET-EUR — ACTIVE_NOW — score mémoire 7.829/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- APT-EUR — ACTIVE_NOW — score mémoire 7.829/10 — sources DECISION_LAYER, V4 — WATCH_ONLY

## Audit des plus fortes hausses

- ZAMA-EUR +45.82% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- CELR-EUR +40.06% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- EPIC-EUR +37.64% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- SYN-EUR +37.10% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- G-EUR +32.41% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- XTZ-EUR +30.14% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ENA-EUR +21.08% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- EDGE-EUR +20.63% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- INJ-EUR +19.22% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- AVAX-EUR +18.05% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
