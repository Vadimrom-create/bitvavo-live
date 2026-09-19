# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-19T14:47:03.797372+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : HYPE-EUR | action ACHETE_MAINTENANT | opportunité 8.453 | entrée 7.700 | trend 8.750 | rang 8.145
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : INJ-EUR | action PLACE_LIMITE_PASSIVE | opportunité 7.745 | entrée 6.250 | trend 8.550 | rang 6.989
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : NPC-EUR | action LATENT_ACCELERATOR | opportunité 7.615 | entrée 4.500 | trend 8.250 | rang 7.146
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : TAO-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.017 | entrée 7.150 | trend 8.300 | rang 7.674
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. HYPE-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.145
2. AAVE-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.047
3. SOL-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 7.757

## Accélération indépendante

Aucune accélération indépendante confirmée ou en construction.

## Watchlist persistante 24–72 h

- USELESS-EUR — ACTIVE_NOW — score mémoire 7.630/10 — sources ACCELERATION, DECISION_LAYER, V4 — BUYABLE_NOW
- ZAMA-EUR — MEMORY_24H — score mémoire 8.324/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- APT-EUR — ACTIVE_NOW — score mémoire 8.190/10 — sources DECISION_LAYER, V4 — WATCH_ONLY
- HYPE-EUR — ACTIVE_NOW — score mémoire 8.145/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- ATH-EUR — ACTIVE_NOW — score mémoire 8.121/10 — sources V4 — WATCH_ONLY
- JUP-EUR — ACTIVE_NOW — score mémoire 8.071/10 — sources DECISION_LAYER, V4 — WATCH_ONLY
- AAVE-EUR — ACTIVE_NOW — score mémoire 8.047/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- EIGEN-EUR — ACTIVE_NOW — score mémoire 7.953/10 — sources V4 — WATCH_ONLY
- SSV-EUR — ACTIVE_NOW — score mémoire 7.946/10 — sources V4 — WATCH_ONLY
- SUPER-EUR — ACTIVE_NOW — score mémoire 7.930/10 — sources V4 — WATCH_ONLY

## Audit des plus fortes hausses

- ZAMA-EUR +44.93% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- XTZ-EUR +40.01% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- SYN-EUR +34.71% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- SAGA-EUR +26.50% — DETECTED_TOO_LATE — couche NONE — action INTERPRETATION
- STRK-EUR +25.80% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- EDGE-EUR +21.35% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- C-EUR +20.91% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- F-EUR +20.53% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- ENA-EUR +20.50% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- EPIC-EUR +20.21% — DETECTED_EARLY — couche NONE — action INTERPRETATION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
