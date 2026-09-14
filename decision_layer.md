# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-14T05:53:57.429416+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : aucun candidat matériel
- **MEILLEUR_LATENT_ACCELERATOR** : LSK-EUR | action LATENT_ACCELERATOR | opportunité 7.443 | entrée 5.250 | trend 8.400 | rang 6.768
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : VTHO-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.434 | entrée 6.350 | trend 9.200 | rang 8.064
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. VTHO-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.064
2. USELESS-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.321
3. LSK-EUR — MEILLEUR_LATENT_ACCELERATOR — LATENT_ACCELERATOR — rank 6.768

## Accélération indépendante

- CVC-EUR — CONFIRMED_ACCELERATION — score 8.123/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- LDO-EUR — ACTIVE_NOW — score mémoire 8.150/10 — sources V4 — WATCH_ONLY
- CVC-EUR — ACTIVE_NOW — score mémoire 8.123/10 — sources ACCELERATION — DETECTED_BUT_TOO_LATE
- VET-EUR — ACTIVE_NOW — score mémoire 8.122/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- VTHO-EUR — ACTIVE_NOW — score mémoire 8.064/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- ETHFI-EUR — ACTIVE_NOW — score mémoire 8.024/10 — sources V4 — WATCH_ONLY
- LAPTOP-EUR — MEMORY_24H — score mémoire 8.013/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- ZETA-EUR — ACTIVE_NOW — score mémoire 8.002/10 — sources V4 — WATCH_ONLY
- SYRUP-EUR — MEMORY_24H — score mémoire 7.941/10 — sources V4 — MEMORY_ONLY
- VELO-EUR — ACTIVE_NOW — score mémoire 7.901/10 — sources V4 — WATCH_ONLY
- ICP-EUR — ACTIVE_NOW — score mémoire 7.894/10 — sources V4 — WATCH_ONLY

## Audit des plus fortes hausses

- CVC-EUR +41.34% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- REZ-EUR +30.26% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- CPOOL-EUR +21.46% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- FIL-EUR +18.58% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- MTL-EUR +18.52% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- ARK-EUR +15.37% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- IQ-EUR +14.51% — DETECTED_TOO_LATE — couche NONE — action INTERPRETATION
- ZKJ-EUR +12.73% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- BABY-EUR +9.11% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- LIGHTER-EUR +8.84% — DETECTED_EARLY — couche NONE — action INTERPRETATION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
