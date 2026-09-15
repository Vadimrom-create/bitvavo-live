# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-15T10:24:09.016995+00:00
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

- CAP-EUR — MEMORY_24H — score mémoire 8.685/10 — sources ACCELERATION — MEMORY_ONLY
- LAPTOP-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- VTHO-EUR — MEMORY_24H — score mémoire 8.054/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- XVG-EUR — ACTIVE_NOW — score mémoire 8.051/10 — sources V4 — WATCH_ONLY
- ETHFI-EUR — ACTIVE_NOW — score mémoire 8.026/10 — sources V4 — WATCH_ONLY
- LDO-EUR — ACTIVE_NOW — score mémoire 7.769/10 — sources V4 — WATCH_ONLY
- AIOZ-EUR — ACTIVE_NOW — score mémoire 7.676/10 — sources V4 — WATCH_ONLY
- ICP-EUR — ACTIVE_NOW — score mémoire 7.655/10 — sources V4 — WATCH_ONLY
- XPL-EUR — ACTIVE_NOW — score mémoire 7.595/10 — sources V4 — WATCH_ONLY
- YB-EUR — ACTIVE_NOW — score mémoire 7.595/10 — sources V4 — WATCH_ONLY

## Audit des plus fortes hausses

- PUFFER-EUR +27.81% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- CNPY-EUR +25.81% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- SAGA-EUR +22.10% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- CAP-EUR +21.70% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- ACX-EUR +12.90% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- ASTR-EUR +12.24% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- CROSS-EUR +9.89% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- LRC-EUR +8.13% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- ACE-EUR +7.21% — DETECTED_TOO_LATE — couche NONE — action INTERPRETATION
- COTI-EUR +6.82% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
