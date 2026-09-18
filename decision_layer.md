# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-18T22:18:25.682900+00:00
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

Aucune accélération indépendante confirmée ou en construction.

## Watchlist persistante 24–72 h

- VTHO-EUR — ACTIVE_NOW — score mémoire 8.300/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- ICP-EUR — ACTIVE_NOW — score mémoire 7.971/10 — sources DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- VET-EUR — ACTIVE_NOW — score mémoire 7.962/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- METIS-EUR — ACTIVE_NOW — score mémoire 7.883/10 — sources V4 — WATCH_ONLY
- YB-EUR — ACTIVE_NOW — score mémoire 7.849/10 — sources V4 — WATCH_ONLY
- SIGN-EUR — ACTIVE_NOW — score mémoire 7.827/10 — sources V4 — WATCH_ONLY
- LDO-EUR — ACTIVE_NOW — score mémoire 7.822/10 — sources V4 — WATCH_ONLY
- PEAQ-EUR — ACTIVE_NOW — score mémoire 7.819/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- KSM-EUR — ACTIVE_NOW — score mémoire 7.767/10 — sources V4 — WATCH_ONLY
- XVG-EUR — ACTIVE_NOW — score mémoire 7.671/10 — sources V4 — WATCH_ONLY

## Audit des plus fortes hausses

- F-EUR +67.22% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- STRK-EUR +56.54% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- G-EUR +48.84% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- ARB-EUR +29.47% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- APT-EUR +24.00% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- CHIP-EUR +22.82% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ZIG-EUR +22.71% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ZAMA-EUR +22.64% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- C-EUR +22.20% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- NEAR-EUR +21.95% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
