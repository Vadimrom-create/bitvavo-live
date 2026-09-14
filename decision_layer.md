# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-14T00:51:11.378212+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : aucun candidat matériel
- **MEILLEUR_LATENT_ACCELERATOR** : aucun candidat matériel
- **MEILLEUR_PULLBACK_REENTRY** : WLD-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 7.424 | entrée 6.300 | trend 8.150 | rang 7.285
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. WLD-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.285
2. VTHO-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 6.690
3. SOLV-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 5.830

## Accélération indépendante

- LAPTOP-EUR — CONFIRMED_ACCELERATION — score 7.500/10 — REQUIRES_V4_ENTRY_AND_EXECUTION_VALIDATION
- SOLV-EUR — CONFIRMED_ACCELERATION — score 7.358/10 — DETECTED_BUT_TOO_LATE
- CVC-EUR — CONFIRMED_ACCELERATION — score 6.655/10 — DETECTED_BUT_TOO_LATE
- LSK-EUR — BUILDING_ACCELERATION — score 5.629/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- ETHFI-EUR — ACTIVE_NOW — score mémoire 8.012/10 — sources V4 — WATCH_ONLY
- SOMI-EUR — ACTIVE_NOW — score mémoire 7.809/10 — sources V4 — WATCH_ONLY
- VET-EUR — ACTIVE_NOW — score mémoire 7.807/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- LDO-EUR — ACTIVE_NOW — score mémoire 7.790/10 — sources V4 — WATCH_ONLY
- ZIL-EUR — ACTIVE_NOW — score mémoire 7.759/10 — sources DECISION_LAYER, V4 — WATCH_ONLY
- APT-EUR — MEMORY_24H — score mémoire 7.715/10 — sources V4 — MEMORY_ONLY
- ICP-EUR — ACTIVE_NOW — score mémoire 7.713/10 — sources V4 — WATCH_ONLY
- XVG-EUR — ACTIVE_NOW — score mémoire 7.637/10 — sources V4 — WATCH_ONLY
- ZIG-EUR — MEMORY_24H — score mémoire 7.576/10 — sources V4 — MEMORY_ONLY
- CAKE-EUR — ACTIVE_NOW — score mémoire 7.570/10 — sources V4 — WATCH_ONLY

## Audit des plus fortes hausses

- LSK-EUR +111.36% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- CVC-EUR +32.05% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- VTHO-EUR +28.67% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- FIL-EUR +21.79% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- SOLV-EUR +18.92% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- IQ-EUR +14.10% — DETECTED_TOO_LATE — couche NONE — action INTERPRETATION
- PUNDIX-EUR +13.65% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ZKJ-EUR +13.39% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- ZIL-EUR +9.99% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- REZ-EUR +9.57% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
