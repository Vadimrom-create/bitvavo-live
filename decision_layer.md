# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-20T05:43:17.610481+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : aucun candidat matériel
- **MEILLEUR_LATENT_ACCELERATOR** : ZAMA-EUR | action LATENT_ACCELERATOR | opportunité 7.625 | entrée 5.250 | trend 7.700 | rang 5.384
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : UNI-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.366 | entrée 7.500 | trend 7.650 | rang 7.537
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. UNI-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.537
2. HYPE-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.236
3. NEAR-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 6.995

## Accélération indépendante

- CELR-EUR — BUILDING_ACCELERATION — score 5.495/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- C-EUR — MEMORY_24H — score mémoire 8.647/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- S-EUR — ACTIVE_NOW — score mémoire 8.223/10 — sources DECISION_LAYER, V4 — WATCH_ONLY
- VVV-EUR — ACTIVE_NOW — score mémoire 8.001/10 — sources DECISION_LAYER, V4 — WATCH_ONLY
- NPC-EUR — MEMORY_24H — score mémoire 7.903/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- WAL-EUR — ACTIVE_NOW — score mémoire 7.878/10 — sources V4 — WATCH_ONLY
- DOT-EUR — MEMORY_24H — score mémoire 7.831/10 — sources DECISION_LAYER, V4 — MEMORY_ONLY
- ETC-EUR — MEMORY_24H — score mémoire 7.770/10 — sources V4 — MEMORY_ONLY
- PENDLE-EUR — ACTIVE_NOW — score mémoire 7.758/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- COW-EUR — ACTIVE_NOW — score mémoire 7.714/10 — sources V4 — WATCH_ONLY
- KAS-EUR — ACTIVE_NOW — score mémoire 7.704/10 — sources DECISION_LAYER, V4 — WATCH_ONLY

## Audit des plus fortes hausses

- CELR-EUR +113.04% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- G-EUR +76.34% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ZAMA-EUR +37.87% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- CTSI-EUR +30.82% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- ZIL-EUR +23.66% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- C-EUR +22.43% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- SKL-EUR +21.88% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- STX-EUR +16.24% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ONG-EUR +13.74% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- HEI-EUR +13.61% — DETECTED_EARLY — couche NONE — action INTERPRETATION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
