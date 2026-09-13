# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-13T18:35:10.123915+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : aucun candidat matériel
- **MEILLEUR_LATENT_ACCELERATOR** : VTHO-EUR | action LATENT_ACCELERATOR | opportunité 7.958 | entrée 5.750 | trend 9.200 | rang 6.811
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : VET-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 7.839 | entrée 7.400 | trend 8.650 | rang 7.804
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. VET-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.804
2. USELESS-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.029
3. VTHO-EUR — MEILLEUR_LATENT_ACCELERATOR — LATENT_ACCELERATOR — rank 6.811

## Accélération indépendante

Aucune accélération indépendante confirmée ou en construction.

## Watchlist persistante 24–72 h

- LDO-EUR — ACTIVE_NOW — score mémoire 7.889/10 — sources V4 — WATCH_ONLY
- S-EUR — ACTIVE_NOW — score mémoire 7.886/10 — sources V4 — WATCH_ONLY
- ICP-EUR — ACTIVE_NOW — score mémoire 7.884/10 — sources V4 — WATCH_ONLY
- SPX-EUR — ACTIVE_NOW — score mémoire 7.882/10 — sources V4 — WATCH_ONLY
- PORTAL-EUR — MEMORY_24H — score mémoire 7.868/10 — sources V4 — MEMORY_ONLY
- VET-EUR — ACTIVE_NOW — score mémoire 7.804/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- PEAQ-EUR — ACTIVE_NOW — score mémoire 7.754/10 — sources V4 — DETECTED_BUT_TOO_LATE
- YGG-EUR — ACTIVE_NOW — score mémoire 7.707/10 — sources V4 — WATCH_ONLY
- W-EUR — ACTIVE_NOW — score mémoire 7.671/10 — sources V4 — WATCH_ONLY
- CHILLGUY-EUR — ACTIVE_NOW — score mémoire 7.663/10 — sources V4 — WATCH_ONLY

## Audit des plus fortes hausses

- LSK-EUR +263.32% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- CVC-EUR +54.17% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- FIL-EUR +23.26% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- REZ-EUR +23.00% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- VTHO-EUR +21.43% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- ZIL-EUR +19.27% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ARK-EUR +16.34% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- XTZ-EUR +13.26% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- POWR-EUR +12.61% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- BAT-EUR +11.17% — DETECTED_EARLY — couche NONE — action INTERPRETATION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
