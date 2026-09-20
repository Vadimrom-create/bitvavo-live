# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-20T06:56:03.922879+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : INJ-EUR | action PLACE_LIMITE_PASSIVE | opportunité 7.529 | entrée 6.150 | trend 8.050 | rang 7.339
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : aucun candidat matériel
- **MEILLEUR_PULLBACK_REENTRY** : HYPE-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 7.581 | entrée 6.950 | trend 7.950 | rang 7.419
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. HYPE-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.419
2. INJ-EUR — MEILLEURE_LIMITE_PASSIVE — PLACE_LIMITE_PASSIVE — rank 7.339
3. STX-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.333

## Accélération indépendante

- C-EUR — BUILDING_ACCELERATION — score 5.776/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- PROVE-EUR — ACTIVE_NOW — score mémoire 8.230/10 — sources V4 — WATCH_ONLY
- ZAMA-EUR — MEMORY_24H — score mémoire 7.960/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- NPC-EUR — MEMORY_24H — score mémoire 7.903/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- DOT-EUR — MEMORY_24H — score mémoire 7.831/10 — sources DECISION_LAYER, V4 — MEMORY_ONLY
- KAS-EUR — ACTIVE_NOW — score mémoire 7.783/10 — sources DECISION_LAYER, V4 — WATCH_ONLY
- ETC-EUR — MEMORY_24H — score mémoire 7.770/10 — sources V4 — MEMORY_ONLY
- AIOZ-EUR — ACTIVE_NOW — score mémoire 7.701/10 — sources V4 — WATCH_ONLY
- WAL-EUR — ACTIVE_NOW — score mémoire 7.678/10 — sources V4 — WATCH_ONLY
- JUP-EUR — ACTIVE_NOW — score mémoire 7.608/10 — sources DECISION_LAYER, V4 — WATCH_ONLY
- S-EUR — ACTIVE_NOW — score mémoire 7.593/10 — sources DECISION_LAYER, V4 — WATCH_ONLY

## Audit des plus fortes hausses

- CELR-EUR +112.72% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- G-EUR +98.29% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- C-EUR +39.49% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ZAMA-EUR +37.68% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- SKL-EUR +27.00% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- CTSI-EUR +25.09% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- ZIL-EUR +20.59% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ARK-EUR +16.44% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE
- AVAX-EUR +14.99% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- STX-EUR +14.44% — DETECTED_EARLY — couche NONE — action INTERPRETATION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
