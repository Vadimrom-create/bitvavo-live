# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-19T19:50:19.912998+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : HYPE-EUR | action ACHETE_MAINTENANT | opportunité 8.054 | entrée 6.800 | trend 8.750 | rang 7.906
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : aucun candidat matériel
- **MEILLEUR_LATENT_ACCELERATOR** : TAO-EUR | action LATENT_ACCELERATOR | opportunité 7.531 | entrée 4.500 | trend 7.950 | rang 7.106
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : SUI-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.413 | entrée 7.950 | trend 8.450 | rang 7.897
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. HYPE-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 7.906
2. SUI-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.897
3. VET-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.248

## Accélération indépendante

- CNPY-EUR — CONFIRMED_ACCELERATION — score 7.714/10 — REQUIRES_V4_ENTRY_AND_EXECUTION_VALIDATION
- SUI-EUR — BUILDING_ACCELERATION — score 5.370/10 — REQUIRES_V4_ENTRY_AND_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- WAL-EUR — ACTIVE_NOW — score mémoire 8.365/10 — sources V4 — WATCH_ONLY
- AAVE-EUR — ACTIVE_NOW — score mémoire 7.997/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- APT-EUR — ACTIVE_NOW — score mémoire 7.968/10 — sources DECISION_LAYER, V4 — WATCH_ONLY
- KAS-EUR — ACTIVE_NOW — score mémoire 7.964/10 — sources DECISION_LAYER, V4 — WATCH_ONLY
- MIOTA-EUR — ACTIVE_NOW — score mémoire 7.922/10 — sources V4 — WATCH_ONLY
- HYPE-EUR — ACTIVE_NOW — score mémoire 7.906/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- SUI-EUR — ACTIVE_NOW — score mémoire 7.897/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- PENDLE-EUR — ACTIVE_NOW — score mémoire 7.875/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- ROSE-EUR — ACTIVE_NOW — score mémoire 7.818/10 — sources V4 — WATCH_ONLY
- DYDX-EUR — ACTIVE_NOW — score mémoire 7.813/10 — sources V4 — WATCH_ONLY

## Audit des plus fortes hausses

- ZAMA-EUR +49.90% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- EPIC-EUR +39.88% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- SYN-EUR +39.86% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- G-EUR +39.59% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- XTZ-EUR +28.21% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- CELR-EUR +26.94% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- ENA-EUR +22.83% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- EDGE-EUR +21.80% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- INJ-EUR +20.72% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- CROSS-EUR +18.05% — DETECTED_EARLY — couche NONE — action INTERPRETATION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
