# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-20T04:53:46.480704+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : aucun candidat matériel
- **MEILLEUR_LATENT_ACCELERATOR** : SKL-EUR | action LATENT_ACCELERATOR | opportunité 7.900 | entrée 5.350 | trend 8.200 | rang 6.536
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : HYPE-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 7.498 | entrée 6.100 | trend 7.950 | rang 7.275
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. HYPE-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.275
2. UNI-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.010
3. SKL-EUR — MEILLEUR_LATENT_ACCELERATOR — LATENT_ACCELERATOR — rank 6.536

## Accélération indépendante

- SKL-EUR — CONFIRMED_ACCELERATION — score 8.467/10 — DETECTED_BUT_TOO_LATE
- G-EUR — CONFIRMED_ACCELERATION — score 8.197/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- SKL-EUR — ACTIVE_NOW — score mémoire 8.467/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- G-EUR — ACTIVE_NOW — score mémoire 8.197/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- C-EUR — MEMORY_24H — score mémoire 8.029/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- PENDLE-EUR — ACTIVE_NOW — score mémoire 7.956/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- ZAMA-EUR — MEMORY_24H — score mémoire 7.949/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- NPC-EUR — ACTIVE_NOW — score mémoire 7.903/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- DOT-EUR — MEMORY_24H — score mémoire 7.831/10 — sources DECISION_LAYER, V4 — MEMORY_ONLY
- ETC-EUR — MEMORY_24H — score mémoire 7.770/10 — sources V4 — MEMORY_ONLY
- AIOZ-EUR — MEMORY_24H — score mémoire 7.700/10 — sources V4 — MEMORY_ONLY
- SENT-EUR — ACTIVE_NOW — score mémoire 7.679/10 — sources V4 — WATCH_ONLY

## Audit des plus fortes hausses

- CELR-EUR +110.36% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- G-EUR +62.37% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ZAMA-EUR +33.43% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- CTSI-EUR +29.93% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- ZIL-EUR +25.22% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- C-EUR +22.29% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- EPIC-EUR +19.33% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- SKL-EUR +18.88% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- SOLV-EUR +16.87% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- HEI-EUR +15.26% — DETECTED_EARLY — couche NONE — action INTERPRETATION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
