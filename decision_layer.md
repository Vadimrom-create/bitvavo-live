# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-14T02:53:48.029787+00:00
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

- LDO-EUR — ACTIVE_NOW — score mémoire 8.703/10 — sources V4 — WATCH_ONLY
- VET-EUR — ACTIVE_NOW — score mémoire 8.138/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- ETHFI-EUR — ACTIVE_NOW — score mémoire 8.120/10 — sources V4 — WATCH_ONLY
- ICP-EUR — ACTIVE_NOW — score mémoire 8.044/10 — sources V4 — WATCH_ONLY
- LAPTOP-EUR — MEMORY_24H — score mémoire 8.013/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- KAVA-EUR — ACTIVE_NOW — score mémoire 7.998/10 — sources V4 — WATCH_ONLY
- SOMI-EUR — ACTIVE_NOW — score mémoire 7.961/10 — sources V4 — WATCH_ONLY
- SYRUP-EUR — ACTIVE_NOW — score mémoire 7.948/10 — sources V4 — WATCH_ONLY
- TAO-EUR — ACTIVE_NOW — score mémoire 7.939/10 — sources DECISION_LAYER, V4 — WATCH_ONLY
- MEGA-EUR — ACTIVE_NOW — score mémoire 7.937/10 — sources V4 — WATCH_ONLY

## Audit des plus fortes hausses

- MTL-EUR +29.69% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- REZ-EUR +24.68% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- LSK-EUR +23.85% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- CVC-EUR +22.17% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- FIL-EUR +21.89% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- CPOOL-EUR +20.10% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- ZKJ-EUR +18.53% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- ARK-EUR +11.01% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- IQ-EUR +10.63% — DETECTED_TOO_LATE — couche NONE — action INTERPRETATION
- GLM-EUR +7.01% — DETECTED_EARLY — couche NONE — action INTERPRETATION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
