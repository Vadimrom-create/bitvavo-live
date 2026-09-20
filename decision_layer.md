# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-20T10:39:15.825733+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : SAGA-EUR | action PLACE_LIMITE_PASSIVE | opportunité 7.502 | entrée 6.300 | trend 7.800 | rang 6.869
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : aucun candidat matériel
- **MEILLEUR_PULLBACK_REENTRY** : ENA-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.119 | entrée 6.150 | trend 8.500 | rang 7.358
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. ENA-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.358
2. INJ-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.317
3. VET-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.296

## Accélération indépendante

- ENSO-EUR — CONFIRMED_ACCELERATION — score 9.734/10 — REQUIRES_V4_ENTRY_AND_EXECUTION_VALIDATION
- ZAMA-EUR — CONFIRMED_ACCELERATION — score 8.196/10 — DETECTED_BUT_TOO_LATE
- ONDO-EUR — BUILDING_ACCELERATION — score 5.483/10 — REQUIRES_V4_ENTRY_AND_EXECUTION_VALIDATION
- LAPTOP-EUR — BUILDING_ACCELERATION — score 4.860/10 — REQUIRES_V4_ENTRY_AND_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- ENSO-EUR — ACTIVE_NOW — score mémoire 9.734/10 — sources ACCELERATION, V4 — WATCH_ONLY
- ZAMA-EUR — ACTIVE_NOW — score mémoire 8.196/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- MERL-EUR — ACTIVE_NOW — score mémoire 7.932/10 — sources V4 — WATCH_ONLY
- COTI-EUR — MEMORY_24H — score mémoire 7.904/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- PENDLE-EUR — ACTIVE_NOW — score mémoire 7.895/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- STX-EUR — ACTIVE_NOW — score mémoire 7.783/10 — sources DECISION_LAYER, V4 — WATCH_ONLY
- COW-EUR — ACTIVE_NOW — score mémoire 7.703/10 — sources V4 — WATCH_ONLY
- KAS-EUR — ACTIVE_NOW — score mémoire 7.692/10 — sources DECISION_LAYER, V4 — WATCH_ONLY
- PROVE-EUR — ACTIVE_NOW — score mémoire 7.668/10 — sources V4 — WATCH_ONLY
- BIGTIME-EUR — MEMORY_24H — score mémoire 7.662/10 — sources V4 — MEMORY_ONLY

## Audit des plus fortes hausses

- CELR-EUR +74.28% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- ZIL-EUR +20.11% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- SKL-EUR +14.97% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- CTSI-EUR +13.98% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- ALLO-EUR +11.46% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ZAMA-EUR +11.29% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- T-EUR +10.03% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- C-EUR +9.35% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ONG-EUR +8.90% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- SOLV-EUR +8.37% — DETECTED_EARLY — couche NONE — action INTERPRETATION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
