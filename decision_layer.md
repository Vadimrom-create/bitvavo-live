# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-18T05:55:52.973549+00:00
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

- TREAD-EUR — CONFIRMED_ACCELERATION — score 8.374/10 — DETECTED_BUT_TOO_LATE
- DRIFT-EUR — CONFIRMED_ACCELERATION — score 7.980/10 — DETECTED_BUT_TOO_LATE
- USELESS-EUR — BUILDING_ACCELERATION — score 5.134/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- VTHO-EUR — ACTIVE_NOW — score mémoire 8.591/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- TREAD-EUR — ACTIVE_NOW — score mémoire 8.374/10 — sources ACCELERATION, V4 — DETECTED_BUT_TOO_LATE
- ETHFI-EUR — ACTIVE_NOW — score mémoire 7.986/10 — sources V4 — WATCH_ONLY
- DRIFT-EUR — ACTIVE_NOW — score mémoire 7.980/10 — sources ACCELERATION, V4 — DETECTED_BUT_TOO_LATE
- BNB-EUR — ACTIVE_NOW — score mémoire 7.951/10 — sources V4 — WATCH_ONLY
- XTZ-EUR — ACTIVE_NOW — score mémoire 7.934/10 — sources V4 — WATCH_ONLY
- LDO-EUR — ACTIVE_NOW — score mémoire 7.925/10 — sources V4 — WATCH_ONLY
- ICP-EUR — ACTIVE_NOW — score mémoire 7.898/10 — sources V4 — WATCH_ONLY
- KMNO-EUR — ACTIVE_NOW — score mémoire 7.876/10 — sources V4 — WATCH_ONLY
- VET-EUR — ACTIVE_NOW — score mémoire 7.864/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY

## Audit des plus fortes hausses

- DRIFT-EUR +39.77% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- NEAR-EUR +29.90% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- COTI-EUR +29.50% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- CNPY-EUR +26.99% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- UNI-EUR +25.77% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- CROSS-EUR +25.54% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ARB-EUR +24.82% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- TREAD-EUR +21.34% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- RAY-EUR +20.09% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- MET-EUR +19.55% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
