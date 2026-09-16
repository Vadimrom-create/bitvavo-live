# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-16T23:56:09.622214+00:00
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

- LAPTOP-EUR — CONFIRMED_ACCELERATION — score 7.500/10 — REQUIRES_V4_ENTRY_AND_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- ATOM-EUR — ACTIVE_NOW — score mémoire 8.241/10 — sources V4 — DETECTED_BUT_TOO_LATE
- WLD-EUR — ACTIVE_NOW — score mémoire 8.232/10 — sources DECISION_LAYER, V4 — WATCH_ONLY
- DOT-EUR — ACTIVE_NOW — score mémoire 8.199/10 — sources DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- LDO-EUR — ACTIVE_NOW — score mémoire 8.195/10 — sources V4 — WATCH_ONLY
- RED-EUR — ACTIVE_NOW — score mémoire 8.174/10 — sources V4 — WATCH_ONLY
- VTHO-EUR — ACTIVE_NOW — score mémoire 8.083/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- ETHFI-EUR — ACTIVE_NOW — score mémoire 8.041/10 — sources V4 — WATCH_ONLY
- YB-EUR — ACTIVE_NOW — score mémoire 8.035/10 — sources V4 — WATCH_ONLY
- TAO-EUR — ACTIVE_NOW — score mémoire 7.992/10 — sources DECISION_LAYER, V4 — WATCH_ONLY
- AERO-EUR — ACTIVE_NOW — score mémoire 7.975/10 — sources V4 — WATCH_ONLY

## Audit des plus fortes hausses

- SYN-EUR +80.27% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- LSK-EUR +31.58% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- FOLD-EUR +25.47% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- HEI-EUR +18.40% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- HNT-EUR +17.18% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- DGB-EUR +17.17% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- LIGHTER-EUR +16.71% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- IOST-EUR +14.13% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- AGI-EUR +14.05% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- RAY-EUR +13.92% — DETECTED_EARLY — couche NONE — action INTERPRETATION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
