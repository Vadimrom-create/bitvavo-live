# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-20T11:25:01.952036+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : aucun candidat matériel
- **MEILLEUR_LATENT_ACCELERATOR** : SAGA-EUR | action LATENT_ACCELERATOR | opportunité 7.856 | entrée 5.650 | trend 7.800 | rang 6.685
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : ENA-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 7.995 | entrée 6.950 | trend 8.500 | rang 7.421
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. ENA-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.421
2. AVAX-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 6.949
3. VET-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 6.821

## Accélération indépendante

- G-EUR — CONFIRMED_ACCELERATION — score 7.379/10 — REQUIRES_V4_ENTRY_AND_EXECUTION_VALIDATION
- AVAX-EUR — BUILDING_ACCELERATION — score 6.055/10 — DETECTED_BUT_TOO_LATE
- CELR-EUR — BUILDING_ACCELERATION — score 5.244/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- PENDLE-EUR — ACTIVE_NOW — score mémoire 8.229/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- AIOZ-EUR — ACTIVE_NOW — score mémoire 7.977/10 — sources V4 — WATCH_ONLY
- STX-EUR — ACTIVE_NOW — score mémoire 7.966/10 — sources DECISION_LAYER, V4 — WATCH_ONLY
- COTI-EUR — MEMORY_24H — score mémoire 7.904/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- MERL-EUR — ACTIVE_NOW — score mémoire 7.887/10 — sources V4 — WATCH_ONLY
- WAL-EUR — ACTIVE_NOW — score mémoire 7.817/10 — sources V4 — WATCH_ONLY
- KAS-EUR — ACTIVE_NOW — score mémoire 7.676/10 — sources DECISION_LAYER, V4 — WATCH_ONLY
- BIGTIME-EUR — MEMORY_24H — score mémoire 7.662/10 — sources V4 — MEMORY_ONLY
- PROVE-EUR — ACTIVE_NOW — score mémoire 7.521/10 — sources V4 — WATCH_ONLY
- SENT-EUR — ACTIVE_NOW — score mémoire 7.521/10 — sources V4 — WATCH_ONLY

## Audit des plus fortes hausses

- CELR-EUR +76.40% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- ZAMA-EUR +14.48% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ZIL-EUR +13.39% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ENSO-EUR +12.33% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- SKL-EUR +11.65% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- S-EUR +11.20% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- CTSI-EUR +9.76% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- ALLO-EUR +8.66% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- C-EUR +8.60% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- JTO-EUR +8.17% — DETECTED_EARLY — couche NONE — action INTERPRETATION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
