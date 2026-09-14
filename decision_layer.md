# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-14T01:58:13.379874+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : aucun candidat matériel
- **MEILLEUR_LATENT_ACCELERATOR** : VTHO-EUR | action LATENT_ACCELERATOR | opportunité 7.929 | entrée 5.400 | trend 9.200 | rang 6.855
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : aucun candidat matériel

## Top cross-sectionnel

1. VTHO-EUR — MEILLEUR_LATENT_ACCELERATOR — LATENT_ACCELERATOR — rank 6.855

## Accélération indépendante

Aucune accélération indépendante confirmée ou en construction.

## Watchlist persistante 24–72 h

- LAPTOP-EUR — MEMORY_24H — score mémoire 8.167/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- SOMI-EUR — ACTIVE_NOW — score mémoire 8.012/10 — sources V4 — WATCH_ONLY
- VET-EUR — ACTIVE_NOW — score mémoire 8.007/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- ETHFI-EUR — ACTIVE_NOW — score mémoire 7.992/10 — sources V4 — WATCH_ONLY
- ZORA-EUR — ACTIVE_NOW — score mémoire 7.937/10 — sources V4 — WATCH_ONLY
- LDO-EUR — ACTIVE_NOW — score mémoire 7.784/10 — sources V4 — WATCH_ONLY
- ICP-EUR — ACTIVE_NOW — score mémoire 7.782/10 — sources V4 — WATCH_ONLY
- CATI-EUR — ACTIVE_NOW — score mémoire 7.729/10 — sources V4 — WATCH_ONLY
- APT-EUR — MEMORY_24H — score mémoire 7.715/10 — sources V4 — MEMORY_ONLY
- ZRX-EUR — ACTIVE_NOW — score mémoire 7.692/10 — sources V4 — WATCH_ONLY

## Audit des plus fortes hausses

- LSK-EUR +61.09% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- CVC-EUR +27.24% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- FIL-EUR +21.19% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- VTHO-EUR +19.84% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- ZKJ-EUR +18.37% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- IQ-EUR +13.62% — DETECTED_TOO_LATE — couche NONE — action INTERPRETATION
- SOLV-EUR +11.57% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- CPOOL-EUR +11.30% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- MTL-EUR +9.24% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- ZIL-EUR +8.80% — DETECTED_EARLY — couche NONE — action INTERPRETATION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
