# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-20T03:48:01.879399+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : aucun candidat matériel
- **MEILLEUR_LATENT_ACCELERATOR** : INJ-EUR | action LATENT_ACCELERATOR | opportunité 7.540 | entrée 5.700 | trend 8.300 | rang 6.981
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : HYPE-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 7.391 | entrée 6.700 | trend 7.950 | rang 7.287
  - Trend remains strong; candidate retained for re-entry instead of discarded.

## Top cross-sectionnel

1. HYPE-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.287
2. INJ-EUR — MEILLEUR_LATENT_ACCELERATOR — LATENT_ACCELERATOR — rank 6.981
3. RAY-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 6.821

## Accélération indépendante

- G-EUR — BUILDING_ACCELERATION — score 6.400/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- CELR-EUR — MEMORY_24H — score mémoire 8.548/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- ZAMA-EUR — MEMORY_24H — score mémoire 7.949/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- DOT-EUR — MEMORY_24H — score mémoire 7.831/10 — sources DECISION_LAYER, V4 — MEMORY_ONLY
- ETC-EUR — MEMORY_24H — score mémoire 7.770/10 — sources V4 — MEMORY_ONLY
- PENDLE-EUR — ACTIVE_NOW — score mémoire 7.767/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- XTZ-EUR — ACTIVE_NOW — score mémoire 7.744/10 — sources DECISION_LAYER, V4 — WATCH_ONLY
- WAL-EUR — MEMORY_24H — score mémoire 7.737/10 — sources V4 — MEMORY_ONLY
- BIGTIME-EUR — MEMORY_24H — score mémoire 7.714/10 — sources V4 — MEMORY_ONLY
- JUP-EUR — MEMORY_24H — score mémoire 7.694/10 — sources DECISION_LAYER, V4 — MEMORY_ONLY
- KAS-EUR — ACTIVE_NOW — score mémoire 7.684/10 — sources DECISION_LAYER, V4 — WATCH_ONLY

## Audit des plus fortes hausses

- CELR-EUR +89.51% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- G-EUR +51.81% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- ZAMA-EUR +33.81% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ZIL-EUR +24.06% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- C-EUR +17.36% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- AVA-EUR +15.37% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- CTSI-EUR +14.41% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- SKL-EUR +13.89% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- EPIC-EUR +13.45% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- HEI-EUR +13.31% — DETECTED_EARLY — couche NONE — action INTERPRETATION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
