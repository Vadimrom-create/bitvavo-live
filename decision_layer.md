# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-14T07:59:24.367468+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : aucun candidat matériel
- **MEILLEUR_LATENT_ACCELERATOR** : aucun candidat matériel
- **MEILLEUR_PULLBACK_REENTRY** : WLD-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 9.197 | entrée 6.500 | trend 8.150 | rang 8.185
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. WLD-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.185
2. VET-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.943
3. VTHO-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.883

## Accélération indépendante

Aucune accélération indépendante confirmée ou en construction.

## Watchlist persistante 24–72 h

- CVC-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION — MEMORY_ONLY
- LSK-EUR — MEMORY_24H — score mémoire 8.317/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- WLD-EUR — ACTIVE_NOW — score mémoire 8.185/10 — sources DECISION_LAYER, V4 — WATCH_ONLY
- S-EUR — ACTIVE_NOW — score mémoire 8.150/10 — sources V4 — WATCH_ONLY
- SYRUP-EUR — ACTIVE_NOW — score mémoire 8.114/10 — sources V4 — WATCH_ONLY
- LAPTOP-EUR — MEMORY_24H — score mémoire 8.013/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- LDO-EUR — ACTIVE_NOW — score mémoire 7.993/10 — sources V4 — WATCH_ONLY
- ETHFI-EUR — MEMORY_24H — score mémoire 7.951/10 — sources V4 — MEMORY_ONLY
- VET-EUR — ACTIVE_NOW — score mémoire 7.943/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- XVG-EUR — ACTIVE_NOW — score mémoire 7.914/10 — sources V4 — WATCH_ONLY

## Audit des plus fortes hausses

- CVC-EUR +47.20% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- REZ-EUR +27.11% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- LSK-EUR +25.86% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- FIL-EUR +24.87% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- CPOOL-EUR +22.44% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- IQ-EUR +13.87% — DETECTED_TOO_LATE — couche NONE — action INTERPRETATION
- MTL-EUR +13.58% — DETECTED_TOO_LATE — couche NONE — action INTERPRETATION
- LIGHTER-EUR +11.54% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- MOVR-EUR +11.08% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ZKJ-EUR +10.31% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
