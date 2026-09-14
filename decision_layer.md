# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-14T22:16:05.548252+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : aucun candidat matériel
- **MEILLEUR_LATENT_ACCELERATOR** : aucun candidat matériel
- **MEILLEUR_PULLBACK_REENTRY** : VTHO-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.006 | entrée 5.750 | trend 9.200 | rang 7.925
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. VTHO-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.925
2. NEAR-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.293
3. FET-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.168

## Accélération indépendante

- CPOOL-EUR — BUILDING_ACCELERATION — score 5.500/10 — DETECTED_BUT_TOO_LATE
- CAP-EUR — BUILDING_ACCELERATION — score 4.785/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- CNPY-EUR — MEMORY_24H — score mémoire 8.734/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- LDO-EUR — ACTIVE_NOW — score mémoire 8.014/10 — sources V4 — WATCH_ONLY
- PUMP-EUR — ACTIVE_NOW — score mémoire 7.956/10 — sources V4 — WATCH_ONLY
- VTHO-EUR — ACTIVE_NOW — score mémoire 7.925/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- KAS-EUR — ACTIVE_NOW — score mémoire 7.920/10 — sources V4 — WATCH_ONLY
- YB-EUR — ACTIVE_NOW — score mémoire 7.784/10 — sources V4 — WATCH_ONLY
- INJ-EUR — ACTIVE_NOW — score mémoire 7.685/10 — sources DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- ETHFI-EUR — ACTIVE_NOW — score mémoire 7.650/10 — sources V4 — WATCH_ONLY
- VVV-EUR — MEMORY_24H — score mémoire 7.623/10 — sources V4 — MEMORY_ONLY
- ICP-EUR — MEMORY_24H — score mémoire 7.596/10 — sources V4 — MEMORY_ONLY

## Audit des plus fortes hausses

- CPOOL-EUR +40.64% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- CNPY-EUR +37.27% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- CAP-EUR +35.74% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- ARK-EUR +27.25% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- BOB-EUR +20.41% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- MTL-EUR +17.96% — DETECTED_TOO_LATE — couche NONE — action INTERPRETATION
- PENDLE-EUR +15.69% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE
- SENT-EUR +15.15% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- T-EUR +14.28% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- SAGA-EUR +13.62% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
