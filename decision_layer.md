# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-19T16:36:42.003697+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : PEPE-EUR | action ACHETE_MAINTENANT | opportunité 9.341 | entrée 7.950 | trend 8.450 | rang 8.334
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : aucun candidat matériel
- **MEILLEUR_LATENT_ACCELERATOR** : ONDO-EUR | action LATENT_ACCELERATOR | opportunité 7.471 | entrée 4.500 | trend 7.800 | rang 6.943
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : TAO-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 7.911 | entrée 7.150 | trend 8.050 | rang 7.544
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. PEPE-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.334
2. HYPE-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 7.908
3. TAO-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.544

## Accélération indépendante

- C-EUR — CONFIRMED_ACCELERATION — score 9.307/10 — DETECTED_BUT_TOO_LATE
- G-EUR — CONFIRMED_ACCELERATION — score 8.954/10 — DETECTED_BUT_TOO_LATE
- ZAMA-EUR — CONFIRMED_ACCELERATION — score 7.115/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- PEPE-EUR — ACTIVE_NOW — score mémoire 8.334/10 — sources ACCELERATION, DECISION_LAYER, V4 — BUYABLE_NOW
- C-EUR — ACTIVE_NOW — score mémoire 9.307/10 — sources ACCELERATION, V4 — DETECTED_BUT_TOO_LATE
- G-EUR — ACTIVE_NOW — score mémoire 8.954/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- GRT-EUR — ACTIVE_NOW — score mémoire 8.264/10 — sources V4 — WATCH_ONLY
- POWR-EUR — ACTIVE_NOW — score mémoire 8.057/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- AAVE-EUR — ACTIVE_NOW — score mémoire 8.008/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- HYPE-EUR — ACTIVE_NOW — score mémoire 7.908/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- IMX-EUR — ACTIVE_NOW — score mémoire 7.899/10 — sources V4 — WATCH_ONLY
- AERO-EUR — ACTIVE_NOW — score mémoire 7.866/10 — sources V4 — WATCH_ONLY
- ROSE-EUR — ACTIVE_NOW — score mémoire 7.856/10 — sources V4 — WATCH_ONLY

## Audit des plus fortes hausses

- ZAMA-EUR +42.50% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- G-EUR +31.20% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- XTZ-EUR +31.18% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- SYN-EUR +30.70% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- EPIC-EUR +24.76% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- EDGE-EUR +24.74% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- ENA-EUR +23.93% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- AIOZ-EUR +20.45% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- SAGA-EUR +20.21% — DETECTED_TOO_LATE — couche NONE — action INTERPRETATION
- AVAX-EUR +19.07% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
