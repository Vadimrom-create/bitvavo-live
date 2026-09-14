# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-14T02:19:41.073941+00:00
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

- LAPTOP-EUR — CONFIRMED_ACCELERATION — score 8.013/10 — REQUIRES_V4_ENTRY_AND_EXECUTION_VALIDATION
- LSK-EUR — CONFIRMED_ACCELERATION — score 6.500/10 — DETECTED_BUT_TOO_LATE
- REZ-EUR — BUILDING_ACCELERATION — score 6.280/10 — REQUIRES_V4_ENTRY_AND_EXECUTION_VALIDATION
- USELESS-EUR — BUILDING_ACCELERATION — score 5.557/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- VET-EUR — ACTIVE_NOW — score mémoire 8.364/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- ICP-EUR — ACTIVE_NOW — score mémoire 8.197/10 — sources V4 — WATCH_ONLY
- LDO-EUR — ACTIVE_NOW — score mémoire 8.030/10 — sources V4 — WATCH_ONLY
- ETHFI-EUR — ACTIVE_NOW — score mémoire 8.019/10 — sources V4 — WATCH_ONLY
- LAPTOP-EUR — ACTIVE_NOW — score mémoire 8.013/10 — sources ACCELERATION, V4 — WATCH_ONLY
- SOMI-EUR — ACTIVE_NOW — score mémoire 7.993/10 — sources V4 — WATCH_ONLY
- UNI-EUR — ACTIVE_NOW — score mémoire 7.955/10 — sources V4 — WATCH_ONLY
- KAS-EUR — ACTIVE_NOW — score mémoire 7.892/10 — sources V4 — WATCH_ONLY
- YB-EUR — ACTIVE_NOW — score mémoire 7.884/10 — sources V4 — WATCH_ONLY
- XVG-EUR — ACTIVE_NOW — score mémoire 7.750/10 — sources V4 — WATCH_ONLY

## Audit des plus fortes hausses

- LSK-EUR +65.66% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- CVC-EUR +28.74% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- ZKJ-EUR +25.24% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- FIL-EUR +21.53% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- MTL-EUR +18.66% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- VTHO-EUR +16.00% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- CPOOL-EUR +14.21% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- IQ-EUR +12.72% — DETECTED_TOO_LATE — couche NONE — action INTERPRETATION
- ARK-EUR +11.02% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- REZ-EUR +9.99% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
