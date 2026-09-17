# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-17T04:54:17.541722+00:00
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

- TREAD-EUR — BUILDING_ACCELERATION — score 5.336/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- UNI-EUR — ACTIVE_NOW — score mémoire 8.112/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- CAKE-EUR — ACTIVE_NOW — score mémoire 8.112/10 — sources V4 — WATCH_ONLY
- VET-EUR — ACTIVE_NOW — score mémoire 8.057/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- COTI-EUR — ACTIVE_NOW — score mémoire 8.057/10 — sources V4 — DETECTED_BUT_TOO_LATE
- VTHO-EUR — ACTIVE_NOW — score mémoire 8.004/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- ETHFI-EUR — ACTIVE_NOW — score mémoire 7.925/10 — sources V4 — WATCH_ONLY
- LDO-EUR — ACTIVE_NOW — score mémoire 7.905/10 — sources V4 — WATCH_ONLY
- XVG-EUR — ACTIVE_NOW — score mémoire 7.868/10 — sources V4 — WATCH_ONLY
- S-EUR — ACTIVE_NOW — score mémoire 7.830/10 — sources V4 — WATCH_ONLY
- PEAQ-EUR — ACTIVE_NOW — score mémoire 7.811/10 — sources V4 — WATCH_ONLY

## Audit des plus fortes hausses

- SYN-EUR +73.60% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- FOLD-EUR +29.31% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- HNT-EUR +24.07% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- USELESS-EUR +20.71% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- QUID-EUR +19.40% — DETECTED_TOO_LATE — couche NONE — action INTERPRETATION
- LIGHTER-EUR +18.67% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- MOODENG-EUR +17.86% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- VVV-EUR +17.11% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- NEAR-EUR +15.20% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- IOST-EUR +13.04% — DETECTED_EARLY — couche NONE — action INTERPRETATION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
