# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-16T22:38:46.404080+00:00
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

- SYN-EUR — BUILDING_ACCELERATION — score 5.923/10 — DETECTED_BUT_TOO_LATE
- HNT-EUR — BUILDING_ACCELERATION — score 5.369/10 — DETECTED_BUT_TOO_LATE
- LAPTOP-EUR — BUILDING_ACCELERATION — score 5.149/10 — REQUIRES_V4_ENTRY_AND_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- VET-EUR — ACTIVE_NOW — score mémoire 8.064/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- ETHFI-EUR — ACTIVE_NOW — score mémoire 8.014/10 — sources V4 — WATCH_ONLY
- VTHO-EUR — ACTIVE_NOW — score mémoire 8.013/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- LDO-EUR — ACTIVE_NOW — score mémoire 7.935/10 — sources V4 — WATCH_ONLY
- AKT-EUR — MEMORY_24H — score mémoire 7.849/10 — sources DECISION_LAYER, V4 — MEMORY_ONLY
- SOMI-EUR — ACTIVE_NOW — score mémoire 7.824/10 — sources V4 — WATCH_ONLY
- STRK-EUR — ACTIVE_NOW — score mémoire 7.769/10 — sources V4 — WATCH_ONLY
- ICP-EUR — ACTIVE_NOW — score mémoire 7.761/10 — sources V4 — WATCH_ONLY
- SIGN-EUR — ACTIVE_NOW — score mémoire 7.698/10 — sources V4 — WATCH_ONLY
- LINEA-EUR — MEMORY_24H — score mémoire 7.666/10 — sources V4 — MEMORY_ONLY

## Audit des plus fortes hausses

- SYN-EUR +78.62% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- LSK-EUR +43.81% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- HNT-EUR +37.03% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- HEI-EUR +31.22% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- FOLD-EUR +24.91% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- DGB-EUR +17.68% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- AGI-EUR +13.86% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- IOST-EUR +13.78% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- RAY-EUR +12.47% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- LIGHTER-EUR +11.96% — DETECTED_EARLY — couche NONE — action INTERPRETATION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
