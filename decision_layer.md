# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-20T03:14:07.309180+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : aucun candidat matériel
- **MEILLEUR_LATENT_ACCELERATOR** : INJ-EUR | action LATENT_ACCELERATOR | opportunité 7.518 | entrée 4.700 | trend 8.300 | rang 6.557
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : HYPE-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 7.848 | entrée 6.250 | trend 7.950 | rang 7.462
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. HYPE-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.462
2. RAY-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.161
3. INJ-EUR — MEILLEUR_LATENT_ACCELERATOR — LATENT_ACCELERATOR — rank 6.557

## Accélération indépendante

Aucune accélération indépendante confirmée ou en construction.

## Watchlist persistante 24–72 h

- CELR-EUR — MEMORY_24H — score mémoire 8.548/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- KAS-EUR — MEMORY_24H — score mémoire 8.041/10 — sources DECISION_LAYER, V4 — MEMORY_ONLY
- GRASS-EUR — ACTIVE_NOW — score mémoire 7.955/10 — sources V4 — WATCH_ONLY
- ZAMA-EUR — MEMORY_24H — score mémoire 7.949/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- G-EUR — MEMORY_24H — score mémoire 7.898/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- WAL-EUR — ACTIVE_NOW — score mémoire 7.893/10 — sources V4 — WATCH_ONLY
- RED-EUR — MEMORY_24H — score mémoire 7.855/10 — sources V4 — MEMORY_ONLY
- DOT-EUR — MEMORY_24H — score mémoire 7.831/10 — sources DECISION_LAYER, V4 — MEMORY_ONLY
- ETC-EUR — MEMORY_24H — score mémoire 7.770/10 — sources V4 — MEMORY_ONLY
- BIGTIME-EUR — MEMORY_24H — score mémoire 7.714/10 — sources V4 — MEMORY_ONLY

## Audit des plus fortes hausses

- CELR-EUR +102.07% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- G-EUR +60.89% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- ZAMA-EUR +30.01% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ZIL-EUR +18.37% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- AGLD-EUR +15.84% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE
- C-EUR +15.49% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- INJ-EUR +15.05% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- SKL-EUR +13.91% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- HEI-EUR +12.37% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- EPIC-EUR +12.19% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
