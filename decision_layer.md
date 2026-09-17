# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-17T19:48:03.685301+00:00
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

- NPC-EUR — CONFIRMED_ACCELERATION — score 9.183/10 — DETECTED_BUT_TOO_LATE
- COTI-EUR — BUILDING_ACCELERATION — score 5.766/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- CNPY-EUR — MEMORY_24H — score mémoire 9.527/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- NPC-EUR — ACTIVE_NOW — score mémoire 9.183/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- FORM-EUR — ACTIVE_NOW — score mémoire 8.264/10 — sources V4 — WATCH_ONLY
- ICP-EUR — ACTIVE_NOW — score mémoire 8.030/10 — sources V4 — WATCH_ONLY
- SUPER-EUR — ACTIVE_NOW — score mémoire 7.954/10 — sources V4 — WATCH_ONLY
- LDO-EUR — ACTIVE_NOW — score mémoire 7.928/10 — sources V4 — WATCH_ONLY
- VTHO-EUR — ACTIVE_NOW — score mémoire 7.914/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- ATOM-EUR — ACTIVE_NOW — score mémoire 7.820/10 — sources V4 — WATCH_ONLY
- ZRO-EUR — ACTIVE_NOW — score mémoire 7.817/10 — sources V4 — WATCH_ONLY
- VET-EUR — ACTIVE_NOW — score mémoire 7.796/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY

## Audit des plus fortes hausses

- AVA-EUR +84.15% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- CNPY-EUR +51.57% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- TREAD-EUR +37.92% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- COTI-EUR +32.82% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- CROSS-EUR +31.19% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- QUID-EUR +23.51% — DETECTED_TOO_LATE — couche NONE — action INTERPRETATION
- AGI-EUR +22.05% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- UNI-EUR +20.19% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- DGB-EUR +19.12% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- PEAQ-EUR +18.73% — DETECTED_EARLY — couche NONE — action INTERPRETATION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
