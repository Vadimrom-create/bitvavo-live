# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-15T02:08:53.467797+00:00
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

- CAP-EUR — CONFIRMED_ACCELERATION — score 9.037/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- CAP-EUR — ACTIVE_NOW — score mémoire 9.037/10 — sources ACCELERATION — DETECTED_BUT_TOO_LATE
- CNPY-EUR — MEMORY_24H — score mémoire 8.734/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- SYRUP-EUR — ACTIVE_NOW — score mémoire 8.108/10 — sources V4 — WATCH_ONLY
- ATOM-EUR — ACTIVE_NOW — score mémoire 7.996/10 — sources V4 — DETECTED_BUT_TOO_LATE
- SOMI-EUR — ACTIVE_NOW — score mémoire 7.965/10 — sources V4 — WATCH_ONLY
- ZIL-EUR — ACTIVE_NOW — score mémoire 7.880/10 — sources DECISION_LAYER, V4 — WATCH_ONLY
- VTHO-EUR — ACTIVE_NOW — score mémoire 7.839/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- ETHFI-EUR — ACTIVE_NOW — score mémoire 7.769/10 — sources V4 — WATCH_ONLY
- YB-EUR — ACTIVE_NOW — score mémoire 7.758/10 — sources V4 — WATCH_ONLY
- AIOZ-EUR — ACTIVE_NOW — score mémoire 7.736/10 — sources V4 — WATCH_ONLY

## Audit des plus fortes hausses

- CAP-EUR +60.09% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- CNPY-EUR +38.15% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- CPOOL-EUR +31.34% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- ASTR-EUR +16.16% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- T-EUR +15.63% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- PENDLE-EUR +13.26% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE
- KAVA-EUR +11.77% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE
- PUFFER-EUR +10.13% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- RED-EUR +9.73% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- NPC-EUR +9.43% — DETECTED_EARLY — couche NONE — action INTERPRETATION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
