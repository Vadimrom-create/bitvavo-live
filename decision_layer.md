# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-16T06:48:15.596415+00:00
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

- SYN-EUR — CONFIRMED_ACCELERATION — score 8.500/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- LSK-EUR — MEMORY_24H — score mémoire 9.125/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- SYN-EUR — ACTIVE_NOW — score mémoire 8.500/10 — sources ACCELERATION, V4 — DETECTED_BUT_TOO_LATE
- XVG-EUR — ACTIVE_NOW — score mémoire 7.867/10 — sources V4 — WATCH_ONLY
- VTHO-EUR — ACTIVE_NOW — score mémoire 7.795/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- LDO-EUR — ACTIVE_NOW — score mémoire 7.793/10 — sources V4 — WATCH_ONLY
- ICP-EUR — ACTIVE_NOW — score mémoire 7.771/10 — sources V4 — WATCH_ONLY
- NPC-EUR — ACTIVE_NOW — score mémoire 7.749/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- CVC-EUR — MEMORY_24H — score mémoire 7.734/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- YB-EUR — ACTIVE_NOW — score mémoire 7.713/10 — sources V4 — WATCH_ONLY
- SOMI-EUR — ACTIVE_NOW — score mémoire 7.668/10 — sources V4 — WATCH_ONLY

## Audit des plus fortes hausses

- SYN-EUR +75.16% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- CNPY-EUR +24.06% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- FOLD-EUR +15.92% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- ALIGN-EUR +14.48% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- USELESS-EUR +14.18% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- ARB-EUR +12.65% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- CROSS-EUR +12.23% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- G-EUR +8.86% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- LMWR-EUR +8.38% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE
- SAGA-EUR +7.94% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
