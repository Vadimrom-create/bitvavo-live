# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-13T21:06:02.906847+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : aucun candidat matériel
- **MEILLEUR_LATENT_ACCELERATOR** : VTHO-EUR | action LATENT_ACCELERATOR | opportunité 7.809 | entrée 4.950 | trend 9.200 | rang 6.672
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : aucun candidat matériel

## Top cross-sectionnel

1. VTHO-EUR — MEILLEUR_LATENT_ACCELERATOR — LATENT_ACCELERATOR — rank 6.672

## Accélération indépendante

Aucune accélération indépendante confirmée ou en construction.

## Watchlist persistante 24–72 h

- ETHFI-EUR — ACTIVE_NOW — score mémoire 8.399/10 — sources V4 — WATCH_ONLY
- PHA-EUR — ACTIVE_NOW — score mémoire 8.140/10 — sources V4 — WATCH_ONLY
- SYRUP-EUR — ACTIVE_NOW — score mémoire 7.976/10 — sources V4 — WATCH_ONLY
- LDO-EUR — ACTIVE_NOW — score mémoire 7.885/10 — sources V4 — WATCH_ONLY
- VET-EUR — ACTIVE_NOW — score mémoire 7.877/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- XVG-EUR — ACTIVE_NOW — score mémoire 7.810/10 — sources V4 — WATCH_ONLY
- APT-EUR — ACTIVE_NOW — score mémoire 7.715/10 — sources V4 — WATCH_ONLY
- ICP-EUR — ACTIVE_NOW — score mémoire 7.675/10 — sources V4 — WATCH_ONLY
- ATOM-EUR — ACTIVE_NOW — score mémoire 7.613/10 — sources V4 — WATCH_ONLY
- INJ-EUR — ACTIVE_NOW — score mémoire 7.602/10 — sources DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE

## Audit des plus fortes hausses

- LSK-EUR +315.42% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- CVC-EUR +63.10% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- FIL-EUR +22.89% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- VTHO-EUR +21.01% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- REZ-EUR +18.30% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- ARK-EUR +14.87% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- SOLV-EUR +14.56% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- XTZ-EUR +14.17% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ZIL-EUR +13.56% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- POWR-EUR +11.73% — DETECTED_EARLY — couche NONE — action INTERPRETATION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
