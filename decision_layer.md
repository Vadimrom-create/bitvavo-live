# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-13T22:27:59.667400+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : aucun candidat matériel
- **MEILLEUR_LATENT_ACCELERATOR** : VTHO-EUR | action LATENT_ACCELERATOR | opportunité 7.555 | entrée 4.750 | trend 9.200 | rang 6.686
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : FET-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 7.177 | entrée 6.250 | trend 7.650 | rang 6.985
  - Trend remains strong; candidate retained for re-entry instead of discarded.

## Top cross-sectionnel

1. FET-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 6.985
2. VTHO-EUR — MEILLEUR_LATENT_ACCELERATOR — LATENT_ACCELERATOR — rank 6.686
3. LSK-EUR — MEILLEUR_LATENT_ACCELERATOR — LATENT_ACCELERATOR — rank -3.736

## Accélération indépendante

Aucune accélération indépendante confirmée ou en construction.

## Watchlist persistante 24–72 h

- LDO-EUR — ACTIVE_NOW — score mémoire 8.083/10 — sources V4 — WATCH_ONLY
- WLD-EUR — ACTIVE_NOW — score mémoire 7.982/10 — sources V4 — WATCH_ONLY
- VET-EUR — ACTIVE_NOW — score mémoire 7.866/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- APT-EUR — MEMORY_24H — score mémoire 7.715/10 — sources V4 — MEMORY_ONLY
- ETHFI-EUR — ACTIVE_NOW — score mémoire 7.689/10 — sources V4 — WATCH_ONLY
- YB-EUR — ACTIVE_NOW — score mémoire 7.661/10 — sources V4 — WATCH_ONLY
- INJ-EUR — ACTIVE_NOW — score mémoire 7.591/10 — sources DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- ZIG-EUR — MEMORY_24H — score mémoire 7.576/10 — sources V4 — MEMORY_ONLY
- KAS-EUR — ACTIVE_NOW — score mémoire 7.520/10 — sources V4 — WATCH_ONLY
- XVG-EUR — ACTIVE_NOW — score mémoire 7.482/10 — sources V4 — WATCH_ONLY

## Audit des plus fortes hausses

- LSK-EUR +310.30% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- CVC-EUR +49.15% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- VTHO-EUR +18.53% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- FIL-EUR +18.49% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ZKJ-EUR +17.76% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- REZ-EUR +13.03% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- SOLV-EUR +12.79% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- IQ-EUR +12.00% — DETECTED_TOO_LATE — couche NONE — action INTERPRETATION
- POWR-EUR +9.20% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- XTZ-EUR +8.96% — DETECTED_EARLY — couche NONE — action INTERPRETATION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
