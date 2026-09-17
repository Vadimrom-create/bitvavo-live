# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-17T08:24:33.083221+00:00
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

- LAPTOP-EUR — BUILDING_ACCELERATION — score 4.994/10 — REQUIRES_V4_ENTRY_AND_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- LDO-EUR — ACTIVE_NOW — score mémoire 8.056/10 — sources V4 — WATCH_ONLY
- YB-EUR — ACTIVE_NOW — score mémoire 7.977/10 — sources V4 — WATCH_ONLY
- UNI-EUR — ACTIVE_NOW — score mémoire 7.900/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- ETHFI-EUR — MEMORY_24H — score mémoire 7.866/10 — sources V4 — MEMORY_ONLY
- MASK-EUR — ACTIVE_NOW — score mémoire 7.857/10 — sources V4 — WATCH_ONLY
- VTHO-EUR — MEMORY_24H — score mémoire 7.855/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- VET-EUR — ACTIVE_NOW — score mémoire 7.825/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- KAS-EUR — ACTIVE_NOW — score mémoire 7.794/10 — sources DECISION_LAYER, V4 — WATCH_ONLY
- TAO-EUR — ACTIVE_NOW — score mémoire 7.699/10 — sources DECISION_LAYER, V4 — WATCH_ONLY
- ASTR-EUR — ACTIVE_NOW — score mémoire 7.618/10 — sources DECISION_LAYER, V4 — WATCH_ONLY

## Audit des plus fortes hausses

- AVA-EUR +55.62% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- FOLD-EUR +35.32% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- HNT-EUR +24.30% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- QUID-EUR +21.78% — DETECTED_TOO_LATE — couche NONE — action INTERPRETATION
- PEAQ-EUR +18.91% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- NEAR-EUR +18.14% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- RAY-EUR +17.30% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- LIGHTER-EUR +16.23% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- TRAC-EUR +15.56% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- CNPY-EUR +14.98% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
