# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-20T03:31:41.349221+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : aucun candidat matériel
- **MEILLEUR_LATENT_ACCELERATOR** : INJ-EUR | action LATENT_ACCELERATOR | opportunité 8.045 | entrée 5.700 | trend 8.300 | rang 7.164
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : HYPE-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 7.636 | entrée 6.950 | trend 7.950 | rang 7.449
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. HYPE-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.449
2. INJ-EUR — MEILLEUR_LATENT_ACCELERATOR — LATENT_ACCELERATOR — rank 7.164
3. ENA-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.056

## Accélération indépendante

Aucune accélération indépendante confirmée ou en construction.

## Watchlist persistante 24–72 h

- CELR-EUR — MEMORY_24H — score mémoire 8.548/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- PENDLE-EUR — ACTIVE_NOW — score mémoire 8.108/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- GRASS-EUR — MEMORY_24H — score mémoire 7.955/10 — sources V4 — MEMORY_ONLY
- ZAMA-EUR — MEMORY_24H — score mémoire 7.949/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- G-EUR — MEMORY_24H — score mémoire 7.898/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- DOT-EUR — MEMORY_24H — score mémoire 7.831/10 — sources DECISION_LAYER, V4 — MEMORY_ONLY
- KMNO-EUR — ACTIVE_NOW — score mémoire 7.826/10 — sources V4 — WATCH_ONLY
- KAS-EUR — ACTIVE_NOW — score mémoire 7.801/10 — sources DECISION_LAYER, V4 — WATCH_ONLY
- RED-EUR — ACTIVE_NOW — score mémoire 7.776/10 — sources V4 — WATCH_ONLY
- ETC-EUR — MEMORY_24H — score mémoire 7.770/10 — sources V4 — MEMORY_ONLY

## Audit des plus fortes hausses

- CELR-EUR +96.56% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- G-EUR +50.03% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- ZAMA-EUR +33.22% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ZIL-EUR +23.34% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- C-EUR +18.57% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- SKL-EUR +15.25% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- HEI-EUR +14.91% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- CTSI-EUR +13.26% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- SOLV-EUR +13.23% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- EPIC-EUR +13.22% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
