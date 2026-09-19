# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-19T04:43:22.522962+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : aucun candidat matériel
- **MEILLEUR_LATENT_ACCELERATOR** : aucun candidat matériel
- **MEILLEUR_PULLBACK_REENTRY** : HYPE-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.205 | entrée 6.500 | trend 8.250 | rang 7.739
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. HYPE-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.739
2. SOL-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.680
3. INJ-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.399

## Accélération indépendante

Aucune accélération indépendante confirmée ou en construction.

## Watchlist persistante 24–72 h

- AERO-EUR — ACTIVE_NOW — score mémoire 8.514/10 — sources V4 — WATCH_ONLY
- WAL-EUR — ACTIVE_NOW — score mémoire 7.976/10 — sources V4 — DETECTED_BUT_TOO_LATE
- AAVE-EUR — ACTIVE_NOW — score mémoire 7.866/10 — sources ACCELERATION, V4 — WATCH_ONLY
- BEAM-EUR — ACTIVE_NOW — score mémoire 7.856/10 — sources V4 — WATCH_ONLY
- RENDER-EUR — ACTIVE_NOW — score mémoire 7.745/10 — sources V4 — WATCH_ONLY
- ZRO-EUR — MEMORY_24H — score mémoire 7.741/10 — sources V4 — MEMORY_ONLY
- HYPE-EUR — ACTIVE_NOW — score mémoire 7.739/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- NPC-EUR — ACTIVE_NOW — score mémoire 7.710/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- PENDLE-EUR — MEMORY_24H — score mémoire 7.704/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- PYTH-EUR — ACTIVE_NOW — score mémoire 7.703/10 — sources V4 — WATCH_ONLY

## Audit des plus fortes hausses

- G-EUR +70.83% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- F-EUR +34.70% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- STRK-EUR +33.11% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- XTZ-EUR +26.23% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- CPOOL-EUR +24.53% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE
- SYN-EUR +23.53% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- ZAMA-EUR +20.44% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ZIG-EUR +19.47% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- MORPHO-EUR +17.87% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- QKC-EUR +17.15% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
