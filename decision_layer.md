# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-16T06:24:59.290594+00:00
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

- LSK-EUR — MEMORY_24H — score mémoire 9.125/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- ICP-EUR — ACTIVE_NOW — score mémoire 7.882/10 — sources V4 — WATCH_ONLY
- LDO-EUR — ACTIVE_NOW — score mémoire 7.877/10 — sources V4 — WATCH_ONLY
- VTHO-EUR — ACTIVE_NOW — score mémoire 7.776/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- SOMI-EUR — ACTIVE_NOW — score mémoire 7.770/10 — sources V4 — WATCH_ONLY
- CVC-EUR — MEMORY_24H — score mémoire 7.734/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- AIOZ-EUR — ACTIVE_NOW — score mémoire 7.679/10 — sources V4 — WATCH_ONLY
- NPC-EUR — ACTIVE_NOW — score mémoire 7.647/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- XVG-EUR — ACTIVE_NOW — score mémoire 7.623/10 — sources V4 — WATCH_ONLY
- ALGO-EUR — MEMORY_24H — score mémoire 7.613/10 — sources V4 — MEMORY_ONLY

## Audit des plus fortes hausses

- SYN-EUR +44.78% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- CNPY-EUR +21.44% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- FOLD-EUR +15.14% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- ALIGN-EUR +14.35% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ARB-EUR +13.59% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- USELESS-EUR +13.29% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- SAGA-EUR +9.43% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- G-EUR +7.94% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- LSK-EUR +7.65% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- ACX-EUR +7.38% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
