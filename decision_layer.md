# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-13T14:46:29.749603+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : aucun candidat matériel
- **MEILLEUR_LATENT_ACCELERATOR** : VTHO-EUR | action LATENT_ACCELERATOR | opportunité 7.836 | entrée 4.750 | trend 9.200 | rang 6.902
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : TAO-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.581 | entrée 7.000 | trend 7.650 | rang 7.697
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. TAO-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.697
2. NEAR-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.252
3. VTHO-EUR — MEILLEUR_LATENT_ACCELERATOR — LATENT_ACCELERATOR — rank 6.902

## Accélération indépendante

Aucune accélération indépendante confirmée ou en construction.

## Watchlist persistante 24–72 h

- LDO-EUR — ACTIVE_NOW — score mémoire 8.182/10 — sources V4 — WATCH_ONLY
- ATOM-EUR — ACTIVE_NOW — score mémoire 8.106/10 — sources V4 — DETECTED_BUT_TOO_LATE
- ICP-EUR — ACTIVE_NOW — score mémoire 8.073/10 — sources V4 — WATCH_ONLY
- VET-EUR — ACTIVE_NOW — score mémoire 8.033/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- ETHFI-EUR — ACTIVE_NOW — score mémoire 7.923/10 — sources V4 — WATCH_ONLY
- PENDLE-EUR — ACTIVE_NOW — score mémoire 7.919/10 — sources V4 — WATCH_ONLY
- UNI-EUR — ACTIVE_NOW — score mémoire 7.869/10 — sources V4 — WATCH_ONLY
- NPC-EUR — ACTIVE_NOW — score mémoire 7.840/10 — sources ACCELERATION, V4 — WATCH_ONLY
- FET-EUR — ACTIVE_NOW — score mémoire 7.839/10 — sources DECISION_LAYER, V4 — WATCH_ONLY
- INJ-EUR — ACTIVE_NOW — score mémoire 7.796/10 — sources V4 — DETECTED_BUT_TOO_LATE

## Audit des plus fortes hausses

- LSK-EUR +232.61% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- CVC-EUR +82.81% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- PUNDIX-EUR +30.32% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- ARK-EUR +26.96% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- STRAX-EUR +20.22% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- GLM-EUR +19.77% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- VTHO-EUR +17.16% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- POWR-EUR +15.55% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ZETA-EUR +13.74% — DETECTED_TOO_LATE — couche NONE — action INTERPRETATION
- BAT-EUR +12.65% — DETECTED_EARLY — couche NONE — action INTERPRETATION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
