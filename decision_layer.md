# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-18T09:36:13.816900+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : aucun candidat matériel
- **MEILLEUR_LATENT_ACCELERATOR** : VTHO-EUR | action LATENT_ACCELERATOR | opportunité 8.372 | entrée 5.000 | trend 9.200 | rang 7.453
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : VET-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.133 | entrée 7.000 | trend 8.650 | rang 7.876
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. VET-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.876
2. VTHO-EUR — MEILLEUR_LATENT_ACCELERATOR — LATENT_ACCELERATOR — rank 7.453
3. TAO-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.168

## Accélération indépendante

Aucune accélération indépendante confirmée ou en construction.

## Watchlist persistante 24–72 h

- RAY-EUR — MEMORY_24H — score mémoire 9.566/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- LDO-EUR — ACTIVE_NOW — score mémoire 8.711/10 — sources V4 — WATCH_ONLY
- YB-EUR — ACTIVE_NOW — score mémoire 7.973/10 — sources V4 — WATCH_ONLY
- VET-EUR — ACTIVE_NOW — score mémoire 7.876/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- AIOZ-EUR — ACTIVE_NOW — score mémoire 7.854/10 — sources V4 — WATCH_ONLY
- KAS-EUR — ACTIVE_NOW — score mémoire 7.780/10 — sources DECISION_LAYER, V4 — WATCH_ONLY
- ETHFI-EUR — ACTIVE_NOW — score mémoire 7.752/10 — sources V4 — DETECTED_BUT_TOO_LATE
- ARB-EUR — MEMORY_24H — score mémoire 7.749/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- ZIL-EUR — ACTIVE_NOW — score mémoire 7.729/10 — sources DECISION_LAYER, V4 — WATCH_ONLY
- METIS-EUR — ACTIVE_NOW — score mémoire 7.717/10 — sources V4 — DETECTED_BUT_TOO_LATE

## Audit des plus fortes hausses

- G-EUR +76.70% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- DRIFT-EUR +39.94% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- CNPY-EUR +37.13% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- CROSS-EUR +35.64% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- UNI-EUR +30.35% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- STRK-EUR +29.68% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ARB-EUR +24.80% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- RAY-EUR +23.60% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- NEAR-EUR +21.64% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- MET-EUR +17.71% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
