# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-18T02:38:43.955000+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : aucun candidat matériel
- **MEILLEUR_LATENT_ACCELERATOR** : aucun candidat matériel
- **MEILLEUR_PULLBACK_REENTRY** : DOT-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.058 | entrée 7.000 | trend 8.300 | rang 7.368
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. DOT-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.368
2. UNI-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 6.559

## Accélération indépendante

- NEAR-EUR — CONFIRMED_ACCELERATION — score 6.525/10 — DETECTED_BUT_TOO_LATE
- ADA-EUR — BUILDING_ACCELERATION — score 6.003/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- CNPY-EUR — MEMORY_24H — score mémoire 9.527/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- LDO-EUR — ACTIVE_NOW — score mémoire 8.611/10 — sources V4 — WATCH_ONLY
- VET-EUR — ACTIVE_NOW — score mémoire 8.523/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- ICP-EUR — ACTIVE_NOW — score mémoire 8.450/10 — sources V4 — WATCH_ONLY
- AERO-EUR — ACTIVE_NOW — score mémoire 8.382/10 — sources V4 — WATCH_ONLY
- YB-EUR — ACTIVE_NOW — score mémoire 8.305/10 — sources V4 — WATCH_ONLY
- PENDLE-EUR — ACTIVE_NOW — score mémoire 8.216/10 — sources DECISION_LAYER, V4 — WATCH_ONLY
- NPC-EUR — ACTIVE_NOW — score mémoire 8.193/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- METIS-EUR — ACTIVE_NOW — score mémoire 8.084/10 — sources V4 — DETECTED_BUT_TOO_LATE
- ETHFI-EUR — ACTIVE_NOW — score mémoire 8.081/10 — sources V4 — WATCH_ONLY

## Audit des plus fortes hausses

- TREAD-EUR +58.79% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- CNPY-EUR +44.28% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- AVA-EUR +41.11% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- DRIFT-EUR +40.82% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- COTI-EUR +31.54% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- CROSS-EUR +26.66% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- NEAR-EUR +25.26% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- ARB-EUR +22.00% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- UNI-EUR +18.03% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- APT-EUR +16.89% — DETECTED_EARLY — couche NONE — action INTERPRETATION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
