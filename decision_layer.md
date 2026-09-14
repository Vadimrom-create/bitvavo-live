# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-14T02:37:14.184195+00:00
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

- ICP-EUR — ACTIVE_NOW — score mémoire 8.499/10 — sources V4 — WATCH_ONLY
- ETHFI-EUR — ACTIVE_NOW — score mémoire 8.483/10 — sources V4 — WATCH_ONLY
- VET-EUR — ACTIVE_NOW — score mémoire 8.154/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- LDO-EUR — ACTIVE_NOW — score mémoire 8.092/10 — sources V4 — WATCH_ONLY
- LAPTOP-EUR — MEMORY_24H — score mémoire 8.013/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- TAO-EUR — ACTIVE_NOW — score mémoire 7.978/10 — sources DECISION_LAYER, V4 — WATCH_ONLY
- SOMI-EUR — ACTIVE_NOW — score mémoire 7.978/10 — sources V4 — WATCH_ONLY
- ZORA-EUR — ACTIVE_NOW — score mémoire 7.957/10 — sources V4 — WATCH_ONLY
- KAS-EUR — ACTIVE_NOW — score mémoire 7.906/10 — sources V4 — WATCH_ONLY
- NEAR-EUR — ACTIVE_NOW — score mémoire 7.904/10 — sources DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE

## Audit des plus fortes hausses

- LSK-EUR +44.14% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- MTL-EUR +29.95% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- FIL-EUR +22.68% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- CVC-EUR +22.66% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- CPOOL-EUR +22.49% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- ZKJ-EUR +18.33% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- REZ-EUR +15.31% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- IQ-EUR +12.68% — DETECTED_TOO_LATE — couche NONE — action INTERPRETATION
- ARK-EUR +11.44% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ZIL-EUR +8.04% — DETECTED_EARLY — couche NONE — action INTERPRETATION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
