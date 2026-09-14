# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-14T21:03:47.032897+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : aucun candidat matériel
- **MEILLEUR_LATENT_ACCELERATOR** : aucun candidat matériel
- **MEILLEUR_PULLBACK_REENTRY** : LSK-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 7.570 | entrée 5.550 | trend 8.400 | rang 7.352
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. LSK-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.352
2. NEAR-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.234

## Accélération indépendante

- CAP-EUR — BUILDING_ACCELERATION — score 6.074/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- CNPY-EUR — MEMORY_24H — score mémoire 8.734/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- LDO-EUR — ACTIVE_NOW — score mémoire 8.042/10 — sources V4 — WATCH_ONLY
- ETHFI-EUR — ACTIVE_NOW — score mémoire 7.902/10 — sources V4 — WATCH_ONLY
- VTHO-EUR — MEMORY_24H — score mémoire 7.899/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- SYRUP-EUR — ACTIVE_NOW — score mémoire 7.767/10 — sources V4 — WATCH_ONLY
- ICP-EUR — ACTIVE_NOW — score mémoire 7.751/10 — sources V4 — WATCH_ONLY
- ENS-EUR — MEMORY_24H — score mémoire 7.700/10 — sources V4 — MEMORY_ONLY
- PEAQ-EUR — MEMORY_24H — score mémoire 7.694/10 — sources V4 — MEMORY_ONLY
- YB-EUR — ACTIVE_NOW — score mémoire 7.664/10 — sources V4 — WATCH_ONLY
- AERO-EUR — ACTIVE_NOW — score mémoire 7.642/10 — sources V4 — WATCH_ONLY

## Audit des plus fortes hausses

- CPOOL-EUR +46.97% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- CNPY-EUR +45.37% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- CAP-EUR +25.02% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- ARK-EUR +21.88% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- BOB-EUR +19.91% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE
- MTL-EUR +15.97% — DETECTED_TOO_LATE — couche NONE — action INTERPRETATION
- SYN-EUR +12.73% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- PENDLE-EUR +12.02% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE
- RED-EUR +10.95% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- SENT-EUR +10.70% — DETECTED_EARLY — couche NONE — action INTERPRETATION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
