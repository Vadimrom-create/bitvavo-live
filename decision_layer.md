# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-14T05:00:16.735948+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : aucun candidat matériel
- **MEILLEUR_LATENT_ACCELERATOR** : aucun candidat matériel
- **MEILLEUR_PULLBACK_REENTRY** : VTHO-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.372 | entrée 5.950 | trend 9.200 | rang 7.928
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. VTHO-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.928

## Accélération indépendante

- LSK-EUR — BUILDING_ACCELERATION — score 5.176/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- ETHFI-EUR — ACTIVE_NOW — score mémoire 8.206/10 — sources V4 — WATCH_ONLY
- LDO-EUR — ACTIVE_NOW — score mémoire 8.135/10 — sources V4 — WATCH_ONLY
- YB-EUR — ACTIVE_NOW — score mémoire 8.072/10 — sources V4 — WATCH_ONLY
- LAPTOP-EUR — MEMORY_24H — score mémoire 8.013/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- DOT-EUR — ACTIVE_NOW — score mémoire 7.967/10 — sources V4 — WATCH_ONLY
- VTHO-EUR — ACTIVE_NOW — score mémoire 7.928/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- VET-EUR — ACTIVE_NOW — score mémoire 7.877/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- SOMI-EUR — ACTIVE_NOW — score mémoire 7.717/10 — sources V4 — WATCH_ONLY
- KAVA-EUR — ACTIVE_NOW — score mémoire 7.698/10 — sources V4 — WATCH_ONLY
- KAS-EUR — ACTIVE_NOW — score mémoire 7.687/10 — sources V4 — WATCH_ONLY

## Audit des plus fortes hausses

- CPOOL-EUR +30.11% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- REZ-EUR +29.88% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- MTL-EUR +26.61% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- CVC-EUR +22.70% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- FIL-EUR +19.03% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- IQ-EUR +14.24% — DETECTED_TOO_LATE — couche NONE — action INTERPRETATION
- ZKJ-EUR +13.64% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- LIGHTER-EUR +10.64% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- BABY-EUR +10.17% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- NPC-EUR +9.14% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
