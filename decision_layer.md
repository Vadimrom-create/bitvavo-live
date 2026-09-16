# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-16T23:09:15.500493+00:00
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

- CAKE-EUR — ACTIVE_NOW — score mémoire 8.243/10 — sources V4 — WATCH_ONLY
- SIGN-EUR — ACTIVE_NOW — score mémoire 8.166/10 — sources V4 — WATCH_ONLY
- YB-EUR — ACTIVE_NOW — score mémoire 8.045/10 — sources V4 — WATCH_ONLY
- VET-EUR — ACTIVE_NOW — score mémoire 7.942/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- LDO-EUR — ACTIVE_NOW — score mémoire 7.936/10 — sources V4 — WATCH_ONLY
- ICP-EUR — ACTIVE_NOW — score mémoire 7.923/10 — sources V4 — WATCH_ONLY
- AKT-EUR — MEMORY_24H — score mémoire 7.849/10 — sources DECISION_LAYER, V4 — MEMORY_ONLY
- SOMI-EUR — ACTIVE_NOW — score mémoire 7.806/10 — sources V4 — WATCH_ONLY
- VTHO-EUR — ACTIVE_NOW — score mémoire 7.793/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- METIS-EUR — ACTIVE_NOW — score mémoire 7.773/10 — sources V4 — DETECTED_BUT_TOO_LATE

## Audit des plus fortes hausses

- SYN-EUR +77.14% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- HNT-EUR +32.23% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- LSK-EUR +31.48% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- HEI-EUR +28.30% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- FOLD-EUR +24.02% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- IOST-EUR +13.23% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- AGI-EUR +12.95% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- DGB-EUR +12.65% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- RAY-EUR +11.35% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- LIGHTER-EUR +11.09% — DETECTED_EARLY — couche NONE — action INTERPRETATION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
