# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-17T10:47:41.412868+00:00
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

- AVA-EUR — CONFIRMED_ACCELERATION — score 8.996/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- AVA-EUR — ACTIVE_NOW — score mémoire 8.996/10 — sources ACCELERATION, V4 — DETECTED_BUT_TOO_LATE
- RED-EUR — ACTIVE_NOW — score mémoire 8.186/10 — sources V4 — WATCH_ONLY
- YB-EUR — ACTIVE_NOW — score mémoire 8.071/10 — sources V4 — WATCH_ONLY
- LDO-EUR — ACTIVE_NOW — score mémoire 7.937/10 — sources V4 — WATCH_ONLY
- ICP-EUR — ACTIVE_NOW — score mémoire 7.896/10 — sources V4 — WATCH_ONLY
- VTHO-EUR — MEMORY_24H — score mémoire 7.832/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- SOMI-EUR — ACTIVE_NOW — score mémoire 7.828/10 — sources V4 — WATCH_ONLY
- DOT-EUR — ACTIVE_NOW — score mémoire 7.777/10 — sources DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- VET-EUR — ACTIVE_NOW — score mémoire 7.691/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- LTC-EUR — MEMORY_24H — score mémoire 7.691/10 — sources V4 — MEMORY_ONLY

## Audit des plus fortes hausses

- AVA-EUR +80.46% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- FOLD-EUR +38.79% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- QUID-EUR +20.12% — DETECTED_TOO_LATE — couche NONE — action INTERPRETATION
- HNT-EUR +19.55% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- EDEN-EUR +17.26% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- PEAQ-EUR +17.12% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- NEAR-EUR +16.45% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- COTI-EUR +15.05% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- USELESS-EUR +14.83% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- SYN-EUR +14.52% — DETECTED_EARLY — couche NONE — action INTERPRETATION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
