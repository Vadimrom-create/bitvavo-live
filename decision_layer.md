# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-16T00:00:21.445087+00:00
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

Aucune accélération indépendante confirmée ou en construction.

## Watchlist persistante 24–72 h

- LDO-EUR — ACTIVE_NOW — score mémoire 8.040/10 — sources V4 — WATCH_ONLY
- ZRO-EUR — ACTIVE_NOW — score mémoire 7.899/10 — sources V4 — WATCH_ONLY
- ICP-EUR — ACTIVE_NOW — score mémoire 7.895/10 — sources V4 — WATCH_ONLY
- ETHFI-EUR — ACTIVE_NOW — score mémoire 7.872/10 — sources V4 — WATCH_ONLY
- XPL-EUR — ACTIVE_NOW — score mémoire 7.854/10 — sources V4 — WATCH_ONLY
- XVG-EUR — ACTIVE_NOW — score mémoire 7.696/10 — sources V4 — WATCH_ONLY
- SOMI-EUR — ACTIVE_NOW — score mémoire 7.667/10 — sources V4 — WATCH_ONLY
- VET-EUR — ACTIVE_NOW — score mémoire 7.605/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- YB-EUR — ACTIVE_NOW — score mémoire 7.598/10 — sources V4 — WATCH_ONLY
- LIGHTER-EUR — ACTIVE_NOW — score mémoire 7.576/10 — sources V4 — WATCH_ONLY

## Audit des plus fortes hausses

- ALIGN-EUR +36.04% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- PUFFER-EUR +29.73% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- SAGA-EUR +28.52% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- CNPY-EUR +23.15% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- LAPTOP-EUR +21.91% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- SYN-EUR +20.43% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- VTHO-EUR +16.41% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- CROSS-EUR +15.97% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- ARB-EUR +14.27% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- G-EUR +12.32% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
