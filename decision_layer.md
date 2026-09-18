# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-18T13:36:44.994875+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : WLD-EUR | action PLACE_LIMITE_PASSIVE | opportunité 7.463 | entrée 6.550 | trend 8.150 | rang 6.587
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : FET-EUR | action LATENT_ACCELERATOR | opportunité 7.564 | entrée 5.700 | trend 7.650 | rang 6.361
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : TAO-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 7.965 | entrée 7.050 | trend 7.650 | rang 7.351
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. TAO-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.351
2. SYRUP-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.162
3. LSK-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.046

## Accélération indépendante

- NEAR-EUR — CONFIRMED_ACCELERATION — score 9.739/10 — DETECTED_BUT_TOO_LATE
- TREAD-EUR — BUILDING_ACCELERATION — score 5.560/10 — DETECTED_BUT_TOO_LATE
- G-EUR — BUILDING_ACCELERATION — score 5.449/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- NEAR-EUR — ACTIVE_NOW — score mémoire 9.739/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- AERO-EUR — ACTIVE_NOW — score mémoire 8.172/10 — sources V4 — WATCH_ONLY
- VTHO-EUR — MEMORY_24H — score mémoire 8.124/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- LDO-EUR — ACTIVE_NOW — score mémoire 8.047/10 — sources V4 — WATCH_ONLY
- PEAQ-EUR — ACTIVE_NOW — score mémoire 7.882/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- KAS-EUR — ACTIVE_NOW — score mémoire 7.846/10 — sources DECISION_LAYER, V4 — WATCH_ONLY
- ICP-EUR — ACTIVE_NOW — score mémoire 7.827/10 — sources V4 — DETECTED_BUT_TOO_LATE
- SOMI-EUR — ACTIVE_NOW — score mémoire 7.806/10 — sources V4 — WATCH_ONLY
- ATOM-EUR — ACTIVE_NOW — score mémoire 7.757/10 — sources V4 — DETECTED_BUT_TOO_LATE
- VET-EUR — ACTIVE_NOW — score mémoire 7.756/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY

## Audit des plus fortes hausses

- G-EUR +94.43% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- CNPY-EUR +41.97% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- NEAR-EUR +31.59% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- ARB-EUR +30.71% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- UNI-EUR +24.68% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- DRIFT-EUR +24.19% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- STRK-EUR +22.28% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- S-EUR +20.07% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- APT-EUR +19.94% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- INJ-EUR +17.51% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
