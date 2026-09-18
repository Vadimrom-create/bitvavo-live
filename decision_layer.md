# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-18T01:16:14.699656+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : aucun candidat matériel
- **MEILLEUR_LATENT_ACCELERATOR** : aucun candidat matériel
- **MEILLEUR_PULLBACK_REENTRY** : DOT-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.031 | entrée 7.000 | trend 8.300 | rang 7.470
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. DOT-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.470
2. TAO-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.307

## Accélération indépendante

Aucune accélération indépendante confirmée ou en construction.

## Watchlist persistante 24–72 h

- CNPY-EUR — MEMORY_24H — score mémoire 9.527/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- LDO-EUR — ACTIVE_NOW — score mémoire 8.694/10 — sources V4 — WATCH_ONLY
- KAS-EUR — ACTIVE_NOW — score mémoire 8.437/10 — sources DECISION_LAYER, V4 — WATCH_ONLY
- ETHFI-EUR — ACTIVE_NOW — score mémoire 8.251/10 — sources V4 — WATCH_ONLY
- YB-EUR — ACTIVE_NOW — score mémoire 8.083/10 — sources V4 — WATCH_ONLY
- XVG-EUR — ACTIVE_NOW — score mémoire 8.051/10 — sources V4 — WATCH_ONLY
- ICP-EUR — ACTIVE_NOW — score mémoire 7.918/10 — sources V4 — WATCH_ONLY
- SOMI-EUR — ACTIVE_NOW — score mémoire 7.890/10 — sources V4 — WATCH_ONLY
- VTHO-EUR — MEMORY_24H — score mémoire 7.881/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- DRIFT-EUR — MEMORY_24H — score mémoire 7.782/10 — sources ACCELERATION, V4 — MEMORY_ONLY

## Audit des plus fortes hausses

- AVA-EUR +63.22% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- DRIFT-EUR +47.45% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- CNPY-EUR +43.85% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- COTI-EUR +35.90% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- CROSS-EUR +31.72% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- TREAD-EUR +31.11% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- AGI-EUR +19.76% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- NEAR-EUR +19.53% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- UNI-EUR +16.18% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- PEAQ-EUR +15.34% — DETECTED_EARLY — couche NONE — action INTERPRETATION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
