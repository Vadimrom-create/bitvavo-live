# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-13T18:15:21.964187+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : aucun candidat matériel
- **MEILLEUR_LATENT_ACCELERATOR** : aucun candidat matériel
- **MEILLEUR_PULLBACK_REENTRY** : VET-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 7.848 | entrée 6.900 | trend 8.650 | rang 7.759
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. VET-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.759
2. USELESS-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.189
3. VTHO-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 6.920

## Accélération indépendante

Aucune accélération indépendante confirmée ou en construction.

## Watchlist persistante 24–72 h

- LDO-EUR — ACTIVE_NOW — score mémoire 7.972/10 — sources V4 — WATCH_ONLY
- PORTAL-EUR — MEMORY_24H — score mémoire 7.868/10 — sources V4 — MEMORY_ONLY
- FET-EUR — ACTIVE_NOW — score mémoire 7.855/10 — sources DECISION_LAYER, V4 — WATCH_ONLY
- NEAR-EUR — ACTIVE_NOW — score mémoire 7.833/10 — sources DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- ICP-EUR — ACTIVE_NOW — score mémoire 7.800/10 — sources V4 — WATCH_ONLY
- VET-EUR — ACTIVE_NOW — score mémoire 7.759/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- PHA-EUR — ACTIVE_NOW — score mémoire 7.755/10 — sources V4 — WATCH_ONLY
- METIS-EUR — ACTIVE_NOW — score mémoire 7.723/10 — sources V4 — DETECTED_BUT_TOO_LATE
- INJ-EUR — ACTIVE_NOW — score mémoire 7.702/10 — sources DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- ETHFI-EUR — ACTIVE_NOW — score mémoire 7.689/10 — sources V4 — WATCH_ONLY

## Audit des plus fortes hausses

- LSK-EUR +280.59% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- CVC-EUR +57.13% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- REZ-EUR +25.74% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- VTHO-EUR +23.80% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- FIL-EUR +22.27% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ARK-EUR +18.47% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ZIL-EUR +15.03% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- XTZ-EUR +13.67% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- STRAX-EUR +13.14% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- POWR-EUR +11.39% — DETECTED_EARLY — couche NONE — action INTERPRETATION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
