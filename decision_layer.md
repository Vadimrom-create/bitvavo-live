# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-20T00:28:09.157351+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : VET-EUR | action ACHETE_MAINTENANT | opportunité 8.015 | entrée 7.900 | trend 8.700 | rang 7.754
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : aucun candidat matériel
- **MEILLEUR_LATENT_ACCELERATOR** : ONDO-EUR | action LATENT_ACCELERATOR | opportunité 7.491 | entrée 4.500 | trend 8.450 | rang 7.268
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : SUI-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 7.664 | entrée 7.450 | trend 8.450 | rang 7.701
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. VET-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 7.754
2. SUI-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.701
3. TAO-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.543

## Accélération indépendante

- AVAX-EUR — BUILDING_ACCELERATION — score 5.698/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- HYPE-EUR — ACTIVE_NOW — score mémoire 8.333/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- APT-EUR — ACTIVE_NOW — score mémoire 8.191/10 — sources DECISION_LAYER, V4 — WATCH_ONLY
- ZK-EUR — ACTIVE_NOW — score mémoire 8.178/10 — sources V4 — WATCH_ONLY
- S-EUR — MEMORY_24H — score mémoire 8.059/10 — sources DECISION_LAYER, V4 — MEMORY_ONLY
- JUP-EUR — ACTIVE_NOW — score mémoire 7.997/10 — sources DECISION_LAYER, V4 — WATCH_ONLY
- MIOTA-EUR — ACTIVE_NOW — score mémoire 7.981/10 — sources V4 — WATCH_ONLY
- PROVE-EUR — ACTIVE_NOW — score mémoire 7.968/10 — sources V4 — WATCH_ONLY
- SUPER-EUR — ACTIVE_NOW — score mémoire 7.917/10 — sources V4 — WATCH_ONLY
- IMX-EUR — ACTIVE_NOW — score mémoire 7.834/10 — sources V4 — WATCH_ONLY
- BIGTIME-EUR — ACTIVE_NOW — score mémoire 7.827/10 — sources V4 — WATCH_ONLY

## Audit des plus fortes hausses

- G-EUR +60.33% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- CELR-EUR +42.65% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- ZAMA-EUR +34.01% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- AVAX-EUR +26.46% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- XTZ-EUR +23.73% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ENA-EUR +21.91% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- INJ-EUR +18.29% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- ZIL-EUR +17.22% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- EDGE-EUR +17.00% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- SOLV-EUR +15.36% — DETECTED_EARLY — couche NONE — action INTERPRETATION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
