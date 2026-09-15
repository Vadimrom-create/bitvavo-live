# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-15T23:19:34.688572+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : aucun candidat matériel
- **MEILLEUR_LATENT_ACCELERATOR** : VTHO-EUR | action LATENT_ACCELERATOR | opportunité 8.050 | entrée 5.500 | trend 9.200 | rang 6.963
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : aucun candidat matériel

## Top cross-sectionnel

1. VTHO-EUR — MEILLEUR_LATENT_ACCELERATOR — LATENT_ACCELERATOR — rank 6.963

## Accélération indépendante

Aucune accélération indépendante confirmée ou en construction.

## Watchlist persistante 24–72 h

- ETHFI-EUR — ACTIVE_NOW — score mémoire 8.038/10 — sources V4 — WATCH_ONLY
- LDO-EUR — ACTIVE_NOW — score mémoire 7.992/10 — sources V4 — WATCH_ONLY
- CAKE-EUR — ACTIVE_NOW — score mémoire 7.867/10 — sources V4 — WATCH_ONLY
- XVG-EUR — ACTIVE_NOW — score mémoire 7.850/10 — sources V4 — WATCH_ONLY
- XPL-EUR — ACTIVE_NOW — score mémoire 7.775/10 — sources V4 — WATCH_ONLY
- ICP-EUR — ACTIVE_NOW — score mémoire 7.750/10 — sources V4 — WATCH_ONLY
- VET-EUR — ACTIVE_NOW — score mémoire 7.740/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- NEO-EUR — MEMORY_24H — score mémoire 7.694/10 — sources V4 — MEMORY_ONLY
- YB-EUR — ACTIVE_NOW — score mémoire 7.693/10 — sources V4 — WATCH_ONLY
- FORM-EUR — ACTIVE_NOW — score mémoire 7.638/10 — sources V4 — WATCH_ONLY

## Audit des plus fortes hausses

- ALIGN-EUR +35.29% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- PUFFER-EUR +32.24% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- SAGA-EUR +31.90% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- LAPTOP-EUR +21.54% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- CNPY-EUR +20.36% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- VTHO-EUR +19.20% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- SYN-EUR +16.43% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ARB-EUR +11.82% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ASTR-EUR +11.71% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- USELESS-EUR +11.64% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
