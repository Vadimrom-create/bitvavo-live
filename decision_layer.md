# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-20T04:00:38.068198+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : aucun candidat matériel
- **MEILLEUR_LATENT_ACCELERATOR** : SKL-EUR | action LATENT_ACCELERATOR | opportunité 7.631 | entrée 4.850 | trend 8.200 | rang 6.568
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : HYPE-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 7.569 | entrée 6.700 | trend 7.950 | rang 7.324
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. HYPE-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.324
2. RAY-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 6.718
3. SKL-EUR — MEILLEUR_LATENT_ACCELERATOR — LATENT_ACCELERATOR — rank 6.568

## Accélération indépendante

- PEPE-EUR — BUILDING_ACCELERATION — score 5.042/10 — REQUIRES_V4_ENTRY_AND_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- CELR-EUR — MEMORY_24H — score mémoire 8.548/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- ZAMA-EUR — MEMORY_24H — score mémoire 7.949/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- DOT-EUR — MEMORY_24H — score mémoire 7.831/10 — sources DECISION_LAYER, V4 — MEMORY_ONLY
- ATH-EUR — ACTIVE_NOW — score mémoire 7.829/10 — sources V4 — WATCH_ONLY
- PENDLE-EUR — ACTIVE_NOW — score mémoire 7.776/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- ETC-EUR — MEMORY_24H — score mémoire 7.770/10 — sources V4 — MEMORY_ONLY
- XTZ-EUR — ACTIVE_NOW — score mémoire 7.733/10 — sources DECISION_LAYER, V4 — WATCH_ONLY
- BIGTIME-EUR — MEMORY_24H — score mémoire 7.714/10 — sources V4 — MEMORY_ONLY
- AIOZ-EUR — ACTIVE_NOW — score mémoire 7.700/10 — sources V4 — WATCH_ONLY
- WAL-EUR — ACTIVE_NOW — score mémoire 7.669/10 — sources V4 — WATCH_ONLY

## Audit des plus fortes hausses

- CELR-EUR +82.81% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- G-EUR +55.92% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- ZAMA-EUR +36.73% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ZIL-EUR +25.09% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- C-EUR +20.58% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- CTSI-EUR +16.68% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- SKL-EUR +15.42% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- AVA-EUR +14.99% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- EPIC-EUR +14.14% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- SYN-EUR +14.01% — DETECTED_EARLY — couche NONE — action INTERPRETATION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
