# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-17T01:21:01.407332+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : aucun candidat matériel
- **MEILLEUR_LATENT_ACCELERATOR** : aucun candidat matériel
- **MEILLEUR_PULLBACK_REENTRY** : VTHO-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.393 | entrée 6.150 | trend 9.200 | rang 7.963
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. VTHO-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.963
2. UNI-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.098
3. NEAR-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 6.931

## Accélération indépendante

- LSK-EUR — BUILDING_ACCELERATION — score 5.783/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- LDO-EUR — ACTIVE_NOW — score mémoire 8.344/10 — sources V4 — WATCH_ONLY
- XVG-EUR — ACTIVE_NOW — score mémoire 8.088/10 — sources V4 — WATCH_ONLY
- YB-EUR — ACTIVE_NOW — score mémoire 8.017/10 — sources V4 — WATCH_ONLY
- VET-EUR — ACTIVE_NOW — score mémoire 7.999/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- VTHO-EUR — ACTIVE_NOW — score mémoire 7.963/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- ETHFI-EUR — ACTIVE_NOW — score mémoire 7.962/10 — sources V4 — WATCH_ONLY
- ICP-EUR — ACTIVE_NOW — score mémoire 7.805/10 — sources V4 — WATCH_ONLY
- KAS-EUR — ACTIVE_NOW — score mémoire 7.726/10 — sources DECISION_LAYER, V4 — WATCH_ONLY
- SOMI-EUR — ACTIVE_NOW — score mémoire 7.608/10 — sources V4 — DETECTED_BUT_TOO_LATE
- USELESS-EUR — ACTIVE_NOW — score mémoire 7.599/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE

## Audit des plus fortes hausses

- SYN-EUR +76.41% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- FOLD-EUR +32.70% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- LSK-EUR +28.68% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- DGB-EUR +18.39% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- IOST-EUR +18.18% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- TRAC-EUR +17.66% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- LIGHTER-EUR +17.44% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- RAY-EUR +15.47% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- AGI-EUR +15.23% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- VVV-EUR +14.70% — DETECTED_EARLY — couche NONE — action INTERPRETATION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
