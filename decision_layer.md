# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-15T16:30:20.903696+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : aucun candidat matériel
- **MEILLEUR_LATENT_ACCELERATOR** : VTHO-EUR | action LATENT_ACCELERATOR | opportunité 8.417 | entrée 5.750 | trend 9.200 | rang 7.623
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : USELESS-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 7.508 | entrée 5.750 | trend 8.100 | rang 7.016
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. VTHO-EUR — MEILLEUR_LATENT_ACCELERATOR — LATENT_ACCELERATOR — rank 7.623
2. USELESS-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.016
3. UNI-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 6.967

## Accélération indépendante

- ARB-EUR — CONFIRMED_ACCELERATION — score 9.147/10 — DETECTED_BUT_TOO_LATE
- USELESS-EUR — BUILDING_ACCELERATION — score 5.032/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- ARB-EUR — ACTIVE_NOW — score mémoire 9.147/10 — sources ACCELERATION, V4 — DETECTED_BUT_TOO_LATE
- ATOM-EUR — ACTIVE_NOW — score mémoire 7.921/10 — sources V4 — DETECTED_BUT_TOO_LATE
- SIGN-EUR — ACTIVE_NOW — score mémoire 7.770/10 — sources V4 — WATCH_ONLY
- LDO-EUR — ACTIVE_NOW — score mémoire 7.738/10 — sources V4 — WATCH_ONLY
- VET-EUR — ACTIVE_NOW — score mémoire 7.735/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- TIA-EUR — MEMORY_24H — score mémoire 7.702/10 — sources V4 — MEMORY_ONLY
- VTHO-EUR — ACTIVE_NOW — score mémoire 7.623/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- YB-EUR — ACTIVE_NOW — score mémoire 7.610/10 — sources V4 — WATCH_ONLY
- ICP-EUR — ACTIVE_NOW — score mémoire 7.601/10 — sources V4 — WATCH_ONLY
- ETHFI-EUR — ACTIVE_NOW — score mémoire 7.591/10 — sources V4 — WATCH_ONLY

## Audit des plus fortes hausses

- ALIGN-EUR +38.81% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- SAGA-EUR +20.32% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- PUFFER-EUR +18.38% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- ARB-EUR +14.09% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- CNPY-EUR +13.08% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- ASTR-EUR +12.88% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- VTHO-EUR +12.77% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- CROSS-EUR +12.74% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- NES-EUR +11.46% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- LAPTOP-EUR +10.77% — DETECTED_EARLY — couche NONE — action INTERPRETATION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
