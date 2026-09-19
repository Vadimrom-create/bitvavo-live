# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-19T13:17:40.565194+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : ONDO-EUR | action ACHETE_MAINTENANT | opportunité 8.259 | entrée 7.750 | trend 8.450 | rang 7.838
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : ACH-EUR | action PLACE_LIMITE_PASSIVE | opportunité 7.818 | entrée 5.900 | trend 9.200 | rang 7.429
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : TAO-EUR | action LATENT_ACCELERATOR | opportunité 7.583 | entrée 4.500 | trend 8.300 | rang 7.182
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : HYPE-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 7.874 | entrée 6.700 | trend 8.750 | rang 7.816
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. ONDO-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 7.838
2. HYPE-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.816
3. RAY-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.719

## Accélération indépendante

Aucune accélération indépendante confirmée ou en construction.

## Watchlist persistante 24–72 h

- XLM-EUR — ACTIVE_NOW — score mémoire 7.122/10 — sources ACCELERATION, DECISION_LAYER, V4 — BUYABLE_NOW
- ZAMA-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- LPT-EUR — ACTIVE_NOW — score mémoire 8.408/10 — sources ACCELERATION, V4 — WATCH_ONLY
- AIOZ-EUR — ACTIVE_NOW — score mémoire 8.247/10 — sources V4 — DETECTED_BUT_TOO_LATE
- AAVE-EUR — ACTIVE_NOW — score mémoire 8.179/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- KMNO-EUR — ACTIVE_NOW — score mémoire 8.116/10 — sources V4 — WATCH_ONLY
- LSK-EUR — MEMORY_24H — score mémoire 8.067/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- W-EUR — ACTIVE_NOW — score mémoire 8.001/10 — sources V4 — WATCH_ONLY
- AERO-EUR — ACTIVE_NOW — score mémoire 8.001/10 — sources V4 — WATCH_ONLY
- PROVE-EUR — ACTIVE_NOW — score mémoire 7.981/10 — sources V4 — WATCH_ONLY

## Audit des plus fortes hausses

- SYN-EUR +41.22% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- ZAMA-EUR +41.20% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- SAGA-EUR +30.99% — DETECTED_TOO_LATE — couche NONE — action INTERPRETATION
- STRK-EUR +30.41% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- HEI-EUR +29.01% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- EDGE-EUR +28.76% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- F-EUR +26.92% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- XTZ-EUR +24.35% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- CAP-EUR +23.73% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ENA-EUR +22.95% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
