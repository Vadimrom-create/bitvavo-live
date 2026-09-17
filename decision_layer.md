# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-17T05:12:14.929730+00:00
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

- USELESS-EUR — CONFIRMED_ACCELERATION — score 6.544/10 — DETECTED_BUT_TOO_LATE
- TREAD-EUR — BUILDING_ACCELERATION — score 5.105/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- VTHO-EUR — ACTIVE_NOW — score mémoire 8.649/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- INJ-EUR — ACTIVE_NOW — score mémoire 8.341/10 — sources DECISION_LAYER, V4 — WATCH_ONLY
- SYRUP-EUR — ACTIVE_NOW — score mémoire 8.116/10 — sources V4 — WATCH_ONLY
- LDO-EUR — ACTIVE_NOW — score mémoire 8.105/10 — sources V4 — WATCH_ONLY
- UNI-EUR — ACTIVE_NOW — score mémoire 8.019/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- VET-EUR — ACTIVE_NOW — score mémoire 7.998/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- XPL-EUR — ACTIVE_NOW — score mémoire 7.994/10 — sources V4 — WATCH_ONLY
- ETHFI-EUR — ACTIVE_NOW — score mémoire 7.900/10 — sources V4 — WATCH_ONLY
- KAS-EUR — ACTIVE_NOW — score mémoire 7.867/10 — sources DECISION_LAYER, V4 — WATCH_ONLY
- COTI-EUR — ACTIVE_NOW — score mémoire 7.799/10 — sources V4 — WATCH_ONLY

## Audit des plus fortes hausses

- SYN-EUR +67.36% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- FOLD-EUR +28.55% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- HNT-EUR +24.86% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- USELESS-EUR +22.23% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- AVA-EUR +21.81% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- QUID-EUR +20.28% — DETECTED_TOO_LATE — couche NONE — action INTERPRETATION
- VVV-EUR +16.77% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- LIGHTER-EUR +15.96% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- MOODENG-EUR +14.82% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- NEAR-EUR +14.48% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
