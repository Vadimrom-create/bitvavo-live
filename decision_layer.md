# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-14T23:04:48.949815+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : aucun candidat matériel
- **MEILLEUR_LATENT_ACCELERATOR** : aucun candidat matériel
- **MEILLEUR_PULLBACK_REENTRY** : VTHO-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.111 | entrée 6.050 | trend 9.200 | rang 7.980
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. VTHO-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.980
2. USELESS-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 6.896

## Accélération indépendante

- CPOOL-EUR — BUILDING_ACCELERATION — score 5.234/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- CNPY-EUR — MEMORY_24H — score mémoire 8.734/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- KAS-EUR — ACTIVE_NOW — score mémoire 7.989/10 — sources V4 — WATCH_ONLY
- VTHO-EUR — ACTIVE_NOW — score mémoire 7.980/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- LDO-EUR — ACTIVE_NOW — score mémoire 7.964/10 — sources V4 — WATCH_ONLY
- YB-EUR — ACTIVE_NOW — score mémoire 7.870/10 — sources V4 — WATCH_ONLY
- COTI-EUR — ACTIVE_NOW — score mémoire 7.671/10 — sources V4 — DETECTED_BUT_TOO_LATE
- VET-EUR — ACTIVE_NOW — score mémoire 7.661/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- VVV-EUR — MEMORY_24H — score mémoire 7.623/10 — sources V4 — MEMORY_ONLY
- ETHFI-EUR — ACTIVE_NOW — score mémoire 7.615/10 — sources V4 — WATCH_ONLY
- SOMI-EUR — ACTIVE_NOW — score mémoire 7.553/10 — sources V4 — WATCH_ONLY

## Audit des plus fortes hausses

- CNPY-EUR +40.87% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- CPOOL-EUR +38.00% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- CAP-EUR +32.56% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- ARK-EUR +27.06% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- STRAX-EUR +17.78% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- BOB-EUR +16.03% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- PENDLE-EUR +14.83% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE
- MTL-EUR +14.58% — DETECTED_TOO_LATE — couche NONE — action INTERPRETATION
- SENT-EUR +13.74% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- RED-EUR +11.43% — DETECTED_EARLY — couche NONE — action INTERPRETATION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
