# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-17T20:00:45.983851+00:00
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

- CROSS-EUR — BUILDING_ACCELERATION — score 5.751/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- CNPY-EUR — MEMORY_24H — score mémoire 9.527/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- ZRO-EUR — ACTIVE_NOW — score mémoire 7.906/10 — sources V4 — WATCH_ONLY
- LDO-EUR — ACTIVE_NOW — score mémoire 7.856/10 — sources V4 — WATCH_ONLY
- FORM-EUR — ACTIVE_NOW — score mémoire 7.853/10 — sources V4 — WATCH_ONLY
- VTHO-EUR — ACTIVE_NOW — score mémoire 7.816/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- VET-EUR — MEMORY_24H — score mémoire 7.796/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- ETHFI-EUR — ACTIVE_NOW — score mémoire 7.696/10 — sources V4 — WATCH_ONLY
- ICP-EUR — ACTIVE_NOW — score mémoire 7.678/10 — sources V4 — WATCH_ONLY
- ATOM-EUR — ACTIVE_NOW — score mémoire 7.621/10 — sources V4 — DETECTED_BUT_TOO_LATE
- INJ-EUR — ACTIVE_NOW — score mémoire 7.604/10 — sources DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE

## Audit des plus fortes hausses

- AVA-EUR +77.96% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- CNPY-EUR +58.49% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- CROSS-EUR +36.85% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- TREAD-EUR +33.56% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- COTI-EUR +32.00% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- AGI-EUR +22.76% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- QUID-EUR +22.55% — DETECTED_TOO_LATE — couche NONE — action INTERPRETATION
- UNI-EUR +20.68% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- NEAR-EUR +19.38% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE
- PEAQ-EUR +19.15% — DETECTED_EARLY — couche NONE — action INTERPRETATION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
