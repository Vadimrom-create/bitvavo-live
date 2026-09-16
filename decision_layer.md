# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-16T02:30:45.349807+00:00
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

- SYN-EUR — CONFIRMED_ACCELERATION — score 6.575/10 — DETECTED_BUT_TOO_LATE
- CNPY-EUR — BUILDING_ACCELERATION — score 5.641/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- DOT-EUR — ACTIVE_NOW — score mémoire 8.098/10 — sources DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- ZIL-EUR — ACTIVE_NOW — score mémoire 8.089/10 — sources DECISION_LAYER, V4 — WATCH_ONLY
- USELESS-EUR — ACTIVE_NOW — score mémoire 7.972/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- SIGN-EUR — ACTIVE_NOW — score mémoire 7.846/10 — sources V4 — WATCH_ONLY
- SOMI-EUR — ACTIVE_NOW — score mémoire 7.750/10 — sources V4 — WATCH_ONLY
- ICP-EUR — ACTIVE_NOW — score mémoire 7.695/10 — sources V4 — WATCH_ONLY
- VET-EUR — ACTIVE_NOW — score mémoire 7.677/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- LDO-EUR — ACTIVE_NOW — score mémoire 7.655/10 — sources V4 — WATCH_ONLY
- RED-EUR — ACTIVE_NOW — score mémoire 7.646/10 — sources V4 — WATCH_ONLY
- PENDLE-EUR — ACTIVE_NOW — score mémoire 7.610/10 — sources DECISION_LAYER, V4 — WATCH_ONLY

## Audit des plus fortes hausses

- PUFFER-EUR +35.08% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- CROSS-EUR +29.87% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- ALIGN-EUR +27.89% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- LAPTOP-EUR +27.00% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- SYN-EUR +21.86% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- VTHO-EUR +21.75% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- CNPY-EUR +19.60% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- SAGA-EUR +14.20% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- ARB-EUR +13.22% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- USELESS-EUR +10.11% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
