# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-16T00:51:15.476349+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : LSK-EUR | action PLACE_LIMITE_PASSIVE | opportunité 8.215 | entrée 6.700 | trend 8.400 | rang 7.409
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : aucun candidat matériel
- **MEILLEUR_PULLBACK_REENTRY** : aucun candidat matériel

## Top cross-sectionnel

1. LSK-EUR — MEILLEURE_LIMITE_PASSIVE — PLACE_LIMITE_PASSIVE — rank 7.409

## Accélération indépendante

- LSK-EUR — CONFIRMED_ACCELERATION — score 8.500/10 — REQUIRES_V4_ENTRY_AND_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- LSK-EUR — ACTIVE_NOW — score mémoire 8.500/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- ETHFI-EUR — ACTIVE_NOW — score mémoire 7.975/10 — sources V4 — WATCH_ONLY
- VET-EUR — ACTIVE_NOW — score mémoire 7.955/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- ICP-EUR — ACTIVE_NOW — score mémoire 7.811/10 — sources V4 — WATCH_ONLY
- SOMI-EUR — ACTIVE_NOW — score mémoire 7.786/10 — sources V4 — WATCH_ONLY
- LDO-EUR — ACTIVE_NOW — score mémoire 7.673/10 — sources V4 — WATCH_ONLY
- KAS-EUR — ACTIVE_NOW — score mémoire 7.571/10 — sources V4 — WATCH_ONLY
- YB-EUR — ACTIVE_NOW — score mémoire 7.563/10 — sources V4 — WATCH_ONLY
- ZRX-EUR — ACTIVE_NOW — score mémoire 7.525/10 — sources V4 — WATCH_ONLY
- ORCA-EUR — MEMORY_24H — score mémoire 7.513/10 — sources V4 — MEMORY_ONLY

## Audit des plus fortes hausses

- ALIGN-EUR +32.90% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- SAGA-EUR +27.67% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- CNPY-EUR +27.52% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- PUFFER-EUR +23.29% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- LAPTOP-EUR +21.76% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- SYN-EUR +18.02% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- CROSS-EUR +17.61% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- VTHO-EUR +15.24% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- G-EUR +13.49% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- ARB-EUR +12.67% — DETECTED_EARLY — couche NONE — action INTERPRETATION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
