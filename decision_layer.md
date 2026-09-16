# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-16T01:03:59.644222+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : aucun candidat matériel
- **MEILLEUR_LATENT_ACCELERATOR** : aucun candidat matériel
- **MEILLEUR_PULLBACK_REENTRY** : aucun candidat matériel

## Top cross-sectionnel

Aucun candidat ne remplit actuellement un bucket décisionnel.

## Accélération indépendante

- LSK-EUR — BUILDING_ACCELERATION — score 6.000/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- ETHFI-EUR — ACTIVE_NOW — score mémoire 7.991/10 — sources V4 — WATCH_ONLY
- SOMI-EUR — ACTIVE_NOW — score mémoire 7.861/10 — sources V4 — WATCH_ONLY
- VET-EUR — ACTIVE_NOW — score mémoire 7.857/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- ICP-EUR — ACTIVE_NOW — score mémoire 7.817/10 — sources V4 — WATCH_ONLY
- XVG-EUR — ACTIVE_NOW — score mémoire 7.730/10 — sources V4 — WATCH_ONLY
- RED-EUR — ACTIVE_NOW — score mémoire 7.651/10 — sources V4 — WATCH_ONLY
- ZRX-EUR — ACTIVE_NOW — score mémoire 7.567/10 — sources V4 — WATCH_ONLY
- WLD-EUR — ACTIVE_NOW — score mémoire 7.539/10 — sources DECISION_LAYER, V4 — WATCH_ONLY
- PENDLE-EUR — ACTIVE_NOW — score mémoire 7.534/10 — sources DECISION_LAYER, V4 — WATCH_ONLY
- ORCA-EUR — MEMORY_24H — score mémoire 7.513/10 — sources V4 — MEMORY_ONLY

## Audit des plus fortes hausses

- ALIGN-EUR +28.30% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- PUFFER-EUR +25.12% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- SAGA-EUR +24.95% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- CNPY-EUR +24.60% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- LAPTOP-EUR +22.37% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- SYN-EUR +18.10% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- VTHO-EUR +17.14% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- CROSS-EUR +16.74% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- G-EUR +15.72% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- ARB-EUR +12.06% — DETECTED_EARLY — couche NONE — action INTERPRETATION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
