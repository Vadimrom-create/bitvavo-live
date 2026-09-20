# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-20T11:07:57.206254+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : aucun candidat matériel
- **MEILLEUR_LATENT_ACCELERATOR** : aucun candidat matériel
- **MEILLEUR_PULLBACK_REENTRY** : ENA-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 7.627 | entrée 6.700 | trend 8.500 | rang 7.244
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. ENA-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.244
2. VET-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.078
3. SAGA-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 6.723

## Accélération indépendante

- SAGA-EUR — CONFIRMED_ACCELERATION — score 8.977/10 — DETECTED_BUT_TOO_LATE
- ENSO-EUR — BUILDING_ACCELERATION — score 5.272/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- SAGA-EUR — ACTIVE_NOW — score mémoire 8.977/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- STX-EUR — ACTIVE_NOW — score mémoire 8.180/10 — sources DECISION_LAYER, V4 — WATCH_ONLY
- PENDLE-EUR — ACTIVE_NOW — score mémoire 8.082/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- MERL-EUR — ACTIVE_NOW — score mémoire 7.919/10 — sources V4 — WATCH_ONLY
- COTI-EUR — MEMORY_24H — score mémoire 7.904/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- NPC-EUR — ACTIVE_NOW — score mémoire 7.774/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- KAS-EUR — ACTIVE_NOW — score mémoire 7.710/10 — sources DECISION_LAYER, V4 — WATCH_ONLY
- WAL-EUR — ACTIVE_NOW — score mémoire 7.677/10 — sources V4 — WATCH_ONLY
- BIGTIME-EUR — MEMORY_24H — score mémoire 7.662/10 — sources V4 — MEMORY_ONLY
- PROVE-EUR — ACTIVE_NOW — score mémoire 7.617/10 — sources V4 — WATCH_ONLY

## Audit des plus fortes hausses

- CELR-EUR +75.71% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- ALLO-EUR +18.61% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ZIL-EUR +15.78% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ZAMA-EUR +13.97% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ENSO-EUR +12.11% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- SKL-EUR +11.18% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- CTSI-EUR +10.48% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- S-EUR +10.45% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- C-EUR +9.95% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- JTO-EUR +8.16% — DETECTED_EARLY — couche NONE — action INTERPRETATION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
