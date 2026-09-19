# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-19T18:40:26.477538+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : SUI-EUR | action ACHETE_MAINTENANT | opportunité 8.239 | entrée 7.750 | trend 8.450 | rang 7.939
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : HYPE-EUR | action PLACE_LIMITE_PASSIVE | opportunité 8.022 | entrée 6.000 | trend 8.750 | rang 7.800
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : aucun candidat matériel
- **MEILLEUR_PULLBACK_REENTRY** : VET-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 7.906 | entrée 6.600 | trend 8.150 | rang 7.373
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. SUI-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 7.939
2. HYPE-EUR — MEILLEURE_LIMITE_PASSIVE — PLACE_LIMITE_PASSIVE — rank 7.800
3. VET-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.373

## Accélération indépendante

- G-EUR — BUILDING_ACCELERATION — score 5.748/10 — DETECTED_BUT_TOO_LATE
- INJ-EUR — BUILDING_ACCELERATION — score 5.319/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- SENT-EUR — ACTIVE_NOW — score mémoire 8.425/10 — sources V4 — WATCH_ONLY
- TRB-EUR — ACTIVE_NOW — score mémoire 8.018/10 — sources V4 — WATCH_ONLY
- AAVE-EUR — ACTIVE_NOW — score mémoire 8.007/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- JUP-EUR — ACTIVE_NOW — score mémoire 7.984/10 — sources DECISION_LAYER, V4 — WATCH_ONLY
- STX-EUR — ACTIVE_NOW — score mémoire 7.975/10 — sources V4 — DETECTED_BUT_TOO_LATE
- SUI-EUR — ACTIVE_NOW — score mémoire 7.939/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- PROVE-EUR — ACTIVE_NOW — score mémoire 7.919/10 — sources V4 — WATCH_ONLY
- RED-EUR — ACTIVE_NOW — score mémoire 7.896/10 — sources V4 — WATCH_ONLY
- KAS-EUR — ACTIVE_NOW — score mémoire 7.888/10 — sources DECISION_LAYER, V4 — WATCH_ONLY
- HYPE-EUR — ACTIVE_NOW — score mémoire 7.800/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY

## Audit des plus fortes hausses

- ZAMA-EUR +45.78% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- SYN-EUR +36.22% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- EPIC-EUR +32.62% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- XTZ-EUR +32.08% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- G-EUR +28.71% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- EDGE-EUR +21.35% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- FIL-EUR +20.25% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ENA-EUR +19.79% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- CROSS-EUR +18.14% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- AVAX-EUR +17.97% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
