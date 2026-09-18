# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-18T16:06:35.274617+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : aucun candidat matériel
- **MEILLEUR_LATENT_ACCELERATOR** : aucun candidat matériel
- **MEILLEUR_PULLBACK_REENTRY** : VET-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 7.906 | entrée 7.150 | trend 8.650 | rang 7.677
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. VET-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.677
2. DOT-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.391
3. INJ-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 6.855

## Accélération indépendante

- PUMP-EUR — CONFIRMED_ACCELERATION — score 6.679/10 — REQUIRES_V4_ENTRY_AND_EXECUTION_VALIDATION
- ENA-EUR — BUILDING_ACCELERATION — score 4.836/10 — REQUIRES_V4_ENTRY_AND_EXECUTION_VALIDATION
- ZIG-EUR — BUILDING_ACCELERATION — score 4.777/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- YB-EUR — ACTIVE_NOW — score mémoire 8.193/10 — sources V4 — WATCH_ONLY
- LDO-EUR — ACTIVE_NOW — score mémoire 8.110/10 — sources V4 — DETECTED_BUT_TOO_LATE
- VTHO-EUR — ACTIVE_NOW — score mémoire 8.052/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- ICP-EUR — ACTIVE_NOW — score mémoire 7.970/10 — sources V4 — DETECTED_BUT_TOO_LATE
- PEAQ-EUR — ACTIVE_NOW — score mémoire 7.955/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- XVG-EUR — ACTIVE_NOW — score mémoire 7.926/10 — sources V4 — WATCH_ONLY
- ZORA-EUR — ACTIVE_NOW — score mémoire 7.899/10 — sources V4 — WATCH_ONLY
- RED-EUR — ACTIVE_NOW — score mémoire 7.888/10 — sources V4 — DETECTED_BUT_TOO_LATE
- LPT-EUR — MEMORY_24H — score mémoire 7.863/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- METIS-EUR — ACTIVE_NOW — score mémoire 7.834/10 — sources V4 — DETECTED_BUT_TOO_LATE

## Audit des plus fortes hausses

- G-EUR +89.55% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- F-EUR +58.15% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- CNPY-EUR +43.29% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- STRK-EUR +32.77% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- NEAR-EUR +24.96% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- ARB-EUR +22.98% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- UNI-EUR +21.57% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- S-EUR +21.14% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ZIG-EUR +20.21% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- AZTEC-EUR +19.76% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
