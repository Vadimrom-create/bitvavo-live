# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-18T06:20:03.170236+00:00
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

- SYN-EUR — BUILDING_ACCELERATION — score 5.263/10 — REQUIRES_V4_ENTRY_AND_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- TREAD-EUR — MEMORY_24H — score mémoire 8.374/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- VTHO-EUR — ACTIVE_NOW — score mémoire 8.164/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- VET-EUR — ACTIVE_NOW — score mémoire 8.103/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- DRIFT-EUR — MEMORY_24H — score mémoire 7.980/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- LDO-EUR — ACTIVE_NOW — score mémoire 7.964/10 — sources V4 — WATCH_ONLY
- ETHFI-EUR — ACTIVE_NOW — score mémoire 7.923/10 — sources V4 — WATCH_ONLY
- ICP-EUR — ACTIVE_NOW — score mémoire 7.794/10 — sources V4 — WATCH_ONLY
- METIS-EUR — ACTIVE_NOW — score mémoire 7.792/10 — sources V4 — DETECTED_BUT_TOO_LATE
- KAS-EUR — ACTIVE_NOW — score mémoire 7.790/10 — sources DECISION_LAYER, V4 — WATCH_ONLY
- ARB-EUR — MEMORY_24H — score mémoire 7.749/10 — sources ACCELERATION, V4 — MEMORY_ONLY

## Audit des plus fortes hausses

- DRIFT-EUR +43.27% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- CNPY-EUR +31.26% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- COTI-EUR +31.08% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- NEAR-EUR +29.60% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- ARB-EUR +27.29% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- CROSS-EUR +26.31% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- UNI-EUR +26.30% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- MET-EUR +21.24% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE
- RAY-EUR +20.13% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- CHIP-EUR +19.37% — DETECTED_EARLY — couche NONE — action INTERPRETATION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
