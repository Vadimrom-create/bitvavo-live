# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-14T10:54:47.362952+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : aucun candidat matériel
- **MEILLEUR_LATENT_ACCELERATOR** : aucun candidat matériel
- **MEILLEUR_PULLBACK_REENTRY** : VTHO-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.297 | entrée 5.750 | trend 9.200 | rang 8.059
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. VTHO-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.059
2. USELESS-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.341

## Accélération indépendante

- CPOOL-EUR — BUILDING_ACCELERATION — score 6.094/10 — DETECTED_BUT_TOO_LATE
- USELESS-EUR — BUILDING_ACCELERATION — score 4.945/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- VTHO-EUR — ACTIVE_NOW — score mémoire 8.059/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- LAPTOP-EUR — MEMORY_24H — score mémoire 8.013/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- LDO-EUR — ACTIVE_NOW — score mémoire 7.893/10 — sources V4 — WATCH_ONLY
- ETHFI-EUR — ACTIVE_NOW — score mémoire 7.821/10 — sources V4 — WATCH_ONLY
- AKT-EUR — ACTIVE_NOW — score mémoire 7.753/10 — sources V4 — WATCH_ONLY
- NEO-EUR — MEMORY_24H — score mémoire 7.738/10 — sources V4 — MEMORY_ONLY
- VET-EUR — ACTIVE_NOW — score mémoire 7.681/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- APT-EUR — MEMORY_24H — score mémoire 7.661/10 — sources V4 — MEMORY_ONLY
- KAS-EUR — ACTIVE_NOW — score mémoire 7.657/10 — sources V4 — WATCH_ONLY
- CAKE-EUR — ACTIVE_NOW — score mémoire 7.611/10 — sources V4 — DETECTED_BUT_TOO_LATE

## Audit des plus fortes hausses

- CPOOL-EUR +58.61% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- CVC-EUR +39.12% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- T-EUR +35.37% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- FIL-EUR +24.82% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- REZ-EUR +23.96% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- CAP-EUR +16.04% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- QKC-EUR +14.63% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- CNPY-EUR +13.80% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- WAXP-EUR +13.18% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- IQ-EUR +13.07% — DETECTED_TOO_LATE — couche NONE — action INTERPRETATION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
