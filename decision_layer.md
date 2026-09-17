# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-17T04:37:41.071651+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : aucun candidat matériel
- **MEILLEUR_LATENT_ACCELERATOR** : USELESS-EUR | action LATENT_ACCELERATOR | opportunité 7.444 | entrée 5.300 | trend 8.100 | rang 6.173
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : aucun candidat matériel

## Top cross-sectionnel

1. USELESS-EUR — MEILLEUR_LATENT_ACCELERATOR — LATENT_ACCELERATOR — rank 6.173

## Accélération indépendante

- TREAD-EUR — CONFIRMED_ACCELERATION — score 9.550/10 — DETECTED_BUT_TOO_LATE
- USELESS-EUR — BUILDING_ACCELERATION — score 6.402/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- TREAD-EUR — ACTIVE_NOW — score mémoire 9.550/10 — sources ACCELERATION, V4 — DETECTED_BUT_TOO_LATE
- VET-EUR — ACTIVE_NOW — score mémoire 8.275/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- PHA-EUR — ACTIVE_NOW — score mémoire 8.133/10 — sources V4 — WATCH_ONLY
- CAKE-EUR — ACTIVE_NOW — score mémoire 8.092/10 — sources V4 — WATCH_ONLY
- UNI-EUR — ACTIVE_NOW — score mémoire 8.049/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- VTHO-EUR — ACTIVE_NOW — score mémoire 7.902/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- KAS-EUR — ACTIVE_NOW — score mémoire 7.893/10 — sources DECISION_LAYER, V4 — WATCH_ONLY
- PROM-EUR — ACTIVE_NOW — score mémoire 7.886/10 — sources V4 — WATCH_ONLY
- LDO-EUR — ACTIVE_NOW — score mémoire 7.864/10 — sources V4 — WATCH_ONLY
- XVG-EUR — ACTIVE_NOW — score mémoire 7.809/10 — sources V4 — WATCH_ONLY

## Audit des plus fortes hausses

- SYN-EUR +66.47% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- FOLD-EUR +30.05% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- HNT-EUR +22.74% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- QUID-EUR +17.66% — DETECTED_TOO_LATE — couche NONE — action INTERPRETATION
- USELESS-EUR +17.22% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- LIGHTER-EUR +17.04% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- IOST-EUR +16.24% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- VVV-EUR +15.97% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- NEAR-EUR +13.63% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- AVA-EUR +12.18% — DETECTED_EARLY — couche NONE — action INTERPRETATION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
