# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-20T02:54:49.896413+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : SUI-EUR | action PLACE_LIMITE_PASSIVE | opportunité 8.077 | entrée 6.000 | trend 7.300 | rang 7.183
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : aucun candidat matériel
- **MEILLEUR_PULLBACK_REENTRY** : SOL-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 7.532 | entrée 6.350 | trend 7.900 | rang 7.311
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. SOL-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.311
2. SUI-EUR — MEILLEURE_LIMITE_PASSIVE — PLACE_LIMITE_PASSIVE — rank 7.183
3. HYPE-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.141

## Accélération indépendante

Aucune accélération indépendante confirmée ou en construction.

## Watchlist persistante 24–72 h

- CELR-EUR — MEMORY_24H — score mémoire 8.548/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- NPC-EUR — ACTIVE_NOW — score mémoire 8.114/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- KAS-EUR — ACTIVE_NOW — score mémoire 8.041/10 — sources DECISION_LAYER, V4 — WATCH_ONLY
- ZAMA-EUR — MEMORY_24H — score mémoire 7.949/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- G-EUR — MEMORY_24H — score mémoire 7.898/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- RED-EUR — ACTIVE_NOW — score mémoire 7.855/10 — sources V4 — WATCH_ONLY
- PROVE-EUR — MEMORY_24H — score mémoire 7.853/10 — sources V4 — MEMORY_ONLY
- DOT-EUR — MEMORY_24H — score mémoire 7.831/10 — sources DECISION_LAYER, V4 — MEMORY_ONLY
- WAL-EUR — MEMORY_24H — score mémoire 7.802/10 — sources V4 — MEMORY_ONLY
- ETC-EUR — MEMORY_24H — score mémoire 7.770/10 — sources V4 — MEMORY_ONLY

## Audit des plus fortes hausses

- CELR-EUR +89.63% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- G-EUR +65.17% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- ZAMA-EUR +30.07% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ZIL-EUR +18.32% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- SOLV-EUR +16.41% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- C-EUR +15.02% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- INJ-EUR +14.21% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- AGLD-EUR +13.57% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE
- SKL-EUR +13.34% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ENA-EUR +12.67% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
