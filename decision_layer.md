# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-19T17:03:55.605951+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : HYPE-EUR | action ACHETE_MAINTENANT | opportunité 8.842 | entrée 8.200 | trend 8.750 | rang 8.406
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : aucun candidat matériel
- **MEILLEUR_LATENT_ACCELERATOR** : TAO-EUR | action LATENT_ACCELERATOR | opportunité 7.452 | entrée 4.500 | trend 8.050 | rang 7.000
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : INJ-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.118 | entrée 7.200 | trend 8.550 | rang 7.290
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. HYPE-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.406
2. PEPE-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 7.533
3. INJ-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.290

## Accélération indépendante

- FIL-EUR — CONFIRMED_ACCELERATION — score 9.667/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- PEPE-EUR — ACTIVE_NOW — score mémoire 7.533/10 — sources ACCELERATION, DECISION_LAYER, V4 — BUYABLE_NOW
- FIL-EUR — ACTIVE_NOW — score mémoire 9.667/10 — sources ACCELERATION, V4 — DETECTED_BUT_TOO_LATE
- C-EUR — MEMORY_24H — score mémoire 9.307/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- LPT-EUR — ACTIVE_NOW — score mémoire 8.413/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- HYPE-EUR — ACTIVE_NOW — score mémoire 8.406/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- BIGTIME-EUR — ACTIVE_NOW — score mémoire 8.221/10 — sources V4 — WATCH_ONLY
- AAVE-EUR — ACTIVE_NOW — score mémoire 8.207/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- ATH-EUR — ACTIVE_NOW — score mémoire 8.073/10 — sources V4 — WATCH_ONLY
- MANA-EUR — ACTIVE_NOW — score mémoire 8.072/10 — sources V4 — WATCH_ONLY
- GALA-EUR — ACTIVE_NOW — score mémoire 8.066/10 — sources V4 — WATCH_ONLY

## Audit des plus fortes hausses

- ZAMA-EUR +42.37% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- SYN-EUR +37.45% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- G-EUR +31.58% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- XTZ-EUR +29.13% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ENA-EUR +24.84% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- EPIC-EUR +24.63% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- FIL-EUR +22.19% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- AVAX-EUR +20.35% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE
- EDGE-EUR +20.20% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- AIOZ-EUR +18.13% — DETECTED_EARLY — couche NONE — action INTERPRETATION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
