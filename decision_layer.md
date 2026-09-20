# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-20T05:10:29.937311+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : aucun candidat matériel
- **MEILLEUR_LATENT_ACCELERATOR** : aucun candidat matériel
- **MEILLEUR_PULLBACK_REENTRY** : HYPE-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 7.591 | entrée 6.450 | trend 7.950 | rang 7.368
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. HYPE-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.368
2. UNI-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 6.730

## Accélération indépendante

- C-EUR — CONFIRMED_ACCELERATION — score 8.647/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- C-EUR — ACTIVE_NOW — score mémoire 8.647/10 — sources ACCELERATION, V4 — DETECTED_BUT_TOO_LATE
- WAL-EUR — ACTIVE_NOW — score mémoire 8.303/10 — sources V4 — WATCH_ONLY
- G-EUR — MEMORY_24H — score mémoire 8.197/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- ZAMA-EUR — MEMORY_24H — score mémoire 7.949/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- NPC-EUR — MEMORY_24H — score mémoire 7.903/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- DOT-EUR — MEMORY_24H — score mémoire 7.831/10 — sources DECISION_LAYER, V4 — MEMORY_ONLY
- PROVE-EUR — ACTIVE_NOW — score mémoire 7.796/10 — sources V4 — WATCH_ONLY
- ETC-EUR — MEMORY_24H — score mémoire 7.770/10 — sources V4 — MEMORY_ONLY
- PENDLE-EUR — ACTIVE_NOW — score mémoire 7.741/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- AAVE-EUR — MEMORY_24H — score mémoire 7.654/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY

## Audit des plus fortes hausses

- CELR-EUR +114.24% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- G-EUR +64.66% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ZAMA-EUR +31.60% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- CTSI-EUR +29.96% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- ZIL-EUR +25.31% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- C-EUR +22.92% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- SKL-EUR +19.36% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- HEI-EUR +15.30% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- SOLV-EUR +13.93% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- STX-EUR +13.91% — DETECTED_EARLY — couche NONE — action INTERPRETATION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
