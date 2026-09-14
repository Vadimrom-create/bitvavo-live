# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-14T22:50:37.587288+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : aucun candidat matériel
- **MEILLEUR_LATENT_ACCELERATOR** : aucun candidat matériel
- **MEILLEUR_PULLBACK_REENTRY** : VTHO-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.156 | entrée 5.800 | trend 9.200 | rang 7.965
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. VTHO-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.965
2. NPC-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 6.692
3. PENDLE-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 6.600

## Accélération indépendante

- CPOOL-EUR — BUILDING_ACCELERATION — score 5.146/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- CNPY-EUR — MEMORY_24H — score mémoire 8.734/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- LDO-EUR — ACTIVE_NOW — score mémoire 8.001/10 — sources V4 — WATCH_ONLY
- KAS-EUR — ACTIVE_NOW — score mémoire 7.985/10 — sources V4 — WATCH_ONLY
- VTHO-EUR — ACTIVE_NOW — score mémoire 7.965/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- LIGHTER-EUR — ACTIVE_NOW — score mémoire 7.954/10 — sources V4 — WATCH_ONLY
- YGG-EUR — ACTIVE_NOW — score mémoire 7.852/10 — sources V4 — WATCH_ONLY
- YB-EUR — ACTIVE_NOW — score mémoire 7.809/10 — sources V4 — WATCH_ONLY
- SOMI-EUR — ACTIVE_NOW — score mémoire 7.719/10 — sources V4 — WATCH_ONLY
- AERO-EUR — ACTIVE_NOW — score mémoire 7.686/10 — sources V4 — WATCH_ONLY
- COTI-EUR — ACTIVE_NOW — score mémoire 7.669/10 — sources V4 — DETECTED_BUT_TOO_LATE

## Audit des plus fortes hausses

- CNPY-EUR +41.29% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- CPOOL-EUR +39.06% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- CAP-EUR +33.09% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- ARK-EUR +31.04% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- BOB-EUR +16.48% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- MTL-EUR +16.33% — DETECTED_TOO_LATE — couche NONE — action INTERPRETATION
- PENDLE-EUR +15.15% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE
- SENT-EUR +13.82% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- T-EUR +11.64% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- SAGA-EUR +11.48% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
