# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-13T13:45:11.383694+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : aucun candidat matériel
- **MEILLEUR_LATENT_ACCELERATOR** : aucun candidat matériel
- **MEILLEUR_PULLBACK_REENTRY** : VET-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 7.859 | entrée 7.150 | trend 8.650 | rang 7.801
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. VET-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.801
2. VTHO-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 6.966

## Accélération indépendante

Aucune accélération indépendante confirmée ou en construction.

## Watchlist persistante 24–72 h

- WLD-EUR — ACTIVE_NOW — score mémoire 8.155/10 — sources V4 — WATCH_ONLY
- YGG-EUR — ACTIVE_NOW — score mémoire 7.938/10 — sources V4 — WATCH_ONLY
- XVG-EUR — ACTIVE_NOW — score mémoire 7.917/10 — sources V4 — WATCH_ONLY
- LDO-EUR — ACTIVE_NOW — score mémoire 7.898/10 — sources V4 — WATCH_ONLY
- AIOZ-EUR — ACTIVE_NOW — score mémoire 7.852/10 — sources V4 — WATCH_ONLY
- VET-EUR — ACTIVE_NOW — score mémoire 7.801/10 — sources DECISION_LAYER, V4 — WATCH_ONLY
- F-EUR — ACTIVE_NOW — score mémoire 7.782/10 — sources V4 — WATCH_ONLY
- METIS-EUR — ACTIVE_NOW — score mémoire 7.731/10 — sources V4 — DETECTED_BUT_TOO_LATE
- ETHFI-EUR — ACTIVE_NOW — score mémoire 7.716/10 — sources V4 — WATCH_ONLY
- YB-EUR — ACTIVE_NOW — score mémoire 7.711/10 — sources V4 — WATCH_ONLY

## Audit des plus fortes hausses

- LSK-EUR +310.10% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- CVC-EUR +92.88% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- ARK-EUR +35.24% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- PUNDIX-EUR +26.13% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- POWR-EUR +21.61% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- GLM-EUR +16.79% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- VTHO-EUR +16.19% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- WAXP-EUR +13.63% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- STRAX-EUR +13.45% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- KNC-EUR +13.44% — DETECTED_EARLY — couche NONE — action INTERPRETATION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
