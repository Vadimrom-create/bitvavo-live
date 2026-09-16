# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-16T00:27:35.478579+00:00
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

- ICP-EUR — ACTIVE_NOW — score mémoire 8.366/10 — sources V4 — WATCH_ONLY
- USELESS-EUR — ACTIVE_NOW — score mémoire 8.028/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- ETHFI-EUR — ACTIVE_NOW — score mémoire 7.946/10 — sources V4 — WATCH_ONLY
- VET-EUR — ACTIVE_NOW — score mémoire 7.819/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- SOMI-EUR — ACTIVE_NOW — score mémoire 7.774/10 — sources V4 — WATCH_ONLY
- LDO-EUR — ACTIVE_NOW — score mémoire 7.743/10 — sources V4 — WATCH_ONLY
- UNI-EUR — ACTIVE_NOW — score mémoire 7.658/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- CAKE-EUR — ACTIVE_NOW — score mémoire 7.642/10 — sources V4 — WATCH_ONLY
- AIOZ-EUR — ACTIVE_NOW — score mémoire 7.612/10 — sources V4 — WATCH_ONLY
- ZIL-EUR — ACTIVE_NOW — score mémoire 7.592/10 — sources DECISION_LAYER, V4 — WATCH_ONLY

## Audit des plus fortes hausses

- ALIGN-EUR +30.12% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- CNPY-EUR +27.56% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- SAGA-EUR +25.42% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- LAPTOP-EUR +23.44% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- PUFFER-EUR +22.56% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- CROSS-EUR +17.13% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- SYN-EUR +16.13% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- G-EUR +14.25% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- VTHO-EUR +13.56% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- ARB-EUR +13.42% — DETECTED_EARLY — couche NONE — action INTERPRETATION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
