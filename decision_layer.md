# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-17T05:30:38.087873+00:00
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

- TREAD-EUR — CONFIRMED_ACCELERATION — score 8.990/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- TREAD-EUR — ACTIVE_NOW — score mémoire 8.990/10 — sources ACCELERATION, V4 — DETECTED_BUT_TOO_LATE
- VTHO-EUR — ACTIVE_NOW — score mémoire 8.324/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- ETHFI-EUR — ACTIVE_NOW — score mémoire 8.144/10 — sources V4 — WATCH_ONLY
- S-EUR — ACTIVE_NOW — score mémoire 8.090/10 — sources V4 — WATCH_ONLY
- LDO-EUR — ACTIVE_NOW — score mémoire 8.027/10 — sources V4 — WATCH_ONLY
- ICP-EUR — ACTIVE_NOW — score mémoire 7.898/10 — sources V4 — WATCH_ONLY
- SYRUP-EUR — ACTIVE_NOW — score mémoire 7.867/10 — sources V4 — WATCH_ONLY
- SPX-EUR — ACTIVE_NOW — score mémoire 7.842/10 — sources V4 — WATCH_ONLY
- VET-EUR — ACTIVE_NOW — score mémoire 7.813/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- AIOZ-EUR — ACTIVE_NOW — score mémoire 7.792/10 — sources V4 — WATCH_ONLY

## Audit des plus fortes hausses

- SYN-EUR +58.97% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- FOLD-EUR +29.41% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- AVA-EUR +26.30% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- USELESS-EUR +23.90% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- HNT-EUR +22.54% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- QUID-EUR +21.25% — DETECTED_TOO_LATE — couche NONE — action INTERPRETATION
- VVV-EUR +16.50% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- LIGHTER-EUR +15.70% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- HEI-EUR +15.32% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- MOODENG-EUR +14.63% — DETECTED_EARLY — couche NONE — action INTERPRETATION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
