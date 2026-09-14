# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-14T01:42:57.148283+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : aucun candidat matériel
- **MEILLEUR_LATENT_ACCELERATOR** : VTHO-EUR | action LATENT_ACCELERATOR | opportunité 7.871 | entrée 5.650 | trend 9.200 | rang 7.093
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : SOLV-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 7.287 | entrée 5.600 | trend 7.950 | rang 6.444
  - Trend remains strong; candidate retained for re-entry instead of discarded.

## Top cross-sectionnel

1. VTHO-EUR — MEILLEUR_LATENT_ACCELERATOR — LATENT_ACCELERATOR — rank 7.093
2. SOLV-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 6.444

## Accélération indépendante

Aucune accélération indépendante confirmée ou en construction.

## Watchlist persistante 24–72 h

- SOMI-EUR — ACTIVE_NOW — score mémoire 8.434/10 — sources V4 — WATCH_ONLY
- CATI-EUR — ACTIVE_NOW — score mémoire 8.218/10 — sources V4 — WATCH_ONLY
- LAPTOP-EUR — MEMORY_24H — score mémoire 8.167/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- ETHFI-EUR — ACTIVE_NOW — score mémoire 8.033/10 — sources V4 — WATCH_ONLY
- VET-EUR — ACTIVE_NOW — score mémoire 8.011/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- LDO-EUR — MEMORY_24H — score mémoire 7.947/10 — sources V4 — MEMORY_ONLY
- BAT-EUR — ACTIVE_NOW — score mémoire 7.899/10 — sources V4 — WATCH_ONLY
- XVG-EUR — ACTIVE_NOW — score mémoire 7.721/10 — sources V4 — WATCH_ONLY
- APT-EUR — MEMORY_24H — score mémoire 7.715/10 — sources V4 — MEMORY_ONLY
- ZRX-EUR — ACTIVE_NOW — score mémoire 7.698/10 — sources V4 — WATCH_ONLY

## Audit des plus fortes hausses

- LSK-EUR +55.21% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- CVC-EUR +28.35% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- FIL-EUR +19.70% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- IQ-EUR +16.09% — DETECTED_TOO_LATE — couche NONE — action INTERPRETATION
- VTHO-EUR +16.09% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- SOLV-EUR +14.87% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ZKJ-EUR +13.47% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- ARK-EUR +12.20% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- PUNDIX-EUR +9.50% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- BIRB-EUR +9.40% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
