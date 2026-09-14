# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-14T07:43:37.897588+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : aucun candidat matériel
- **MEILLEUR_LATENT_ACCELERATOR** : aucun candidat matériel
- **MEILLEUR_PULLBACK_REENTRY** : VTHO-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.168 | entrée 6.250 | trend 9.200 | rang 8.055
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. VTHO-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.055
2. VET-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.886
3. USELESS-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.761

## Accélération indépendante

- LSK-EUR — CONFIRMED_ACCELERATION — score 8.317/10 — DETECTED_BUT_TOO_LATE
- REZ-EUR — CONFIRMED_ACCELERATION — score 7.129/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- CVC-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION — MEMORY_ONLY
- LSK-EUR — ACTIVE_NOW — score mémoire 8.317/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- VTHO-EUR — ACTIVE_NOW — score mémoire 8.055/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- LAPTOP-EUR — MEMORY_24H — score mémoire 8.013/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- ETHFI-EUR — MEMORY_24H — score mémoire 7.951/10 — sources V4 — MEMORY_ONLY
- LDO-EUR — ACTIVE_NOW — score mémoire 7.950/10 — sources V4 — WATCH_ONLY
- XVG-EUR — ACTIVE_NOW — score mémoire 7.936/10 — sources V4 — WATCH_ONLY
- WAXP-EUR — ACTIVE_NOW — score mémoire 7.909/10 — sources V4 — WATCH_ONLY
- VET-EUR — ACTIVE_NOW — score mémoire 7.886/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- SOMI-EUR — ACTIVE_NOW — score mémoire 7.882/10 — sources V4 — WATCH_ONLY

## Audit des plus fortes hausses

- CVC-EUR +52.25% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- LSK-EUR +31.86% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- REZ-EUR +27.16% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- FIL-EUR +24.09% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- CPOOL-EUR +22.27% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- MTL-EUR +14.75% — DETECTED_TOO_LATE — couche NONE — action INTERPRETATION
- IQ-EUR +14.41% — DETECTED_TOO_LATE — couche NONE — action INTERPRETATION
- LIGHTER-EUR +11.99% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- CNPY-EUR +10.06% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- ZKJ-EUR +9.38% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
