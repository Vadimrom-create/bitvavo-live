# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-14T23:36:28.235055+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : aucun candidat matériel
- **MEILLEUR_LATENT_ACCELERATOR** : aucun candidat matériel
- **MEILLEUR_PULLBACK_REENTRY** : VTHO-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 7.905 | entrée 5.500 | trend 9.200 | rang 7.848
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. VTHO-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.848
2. NEAR-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.133
3. FET-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.086

## Accélération indépendante

- CAP-EUR — BUILDING_ACCELERATION — score 5.389/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- CNPY-EUR — MEMORY_24H — score mémoire 8.734/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- LDO-EUR — ACTIVE_NOW — score mémoire 7.965/10 — sources V4 — WATCH_ONLY
- PORTAL-EUR — ACTIVE_NOW — score mémoire 7.935/10 — sources V4 — WATCH_ONLY
- KAS-EUR — ACTIVE_NOW — score mémoire 7.886/10 — sources V4 — WATCH_ONLY
- VTHO-EUR — ACTIVE_NOW — score mémoire 7.848/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- YB-EUR — ACTIVE_NOW — score mémoire 7.774/10 — sources V4 — WATCH_ONLY
- ETHFI-EUR — ACTIVE_NOW — score mémoire 7.769/10 — sources V4 — WATCH_ONLY
- VET-EUR — ACTIVE_NOW — score mémoire 7.753/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- COTI-EUR — ACTIVE_NOW — score mémoire 7.724/10 — sources V4 — DETECTED_BUT_TOO_LATE
- WLD-EUR — ACTIVE_NOW — score mémoire 7.623/10 — sources DECISION_LAYER, V4 — WATCH_ONLY

## Audit des plus fortes hausses

- CNPY-EUR +39.80% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- CAP-EUR +36.00% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- CPOOL-EUR +34.92% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- ARK-EUR +23.22% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- MTL-EUR +15.78% — DETECTED_TOO_LATE — couche NONE — action INTERPRETATION
- STRAX-EUR +15.38% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- PENDLE-EUR +14.58% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE
- T-EUR +13.98% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- SENT-EUR +13.48% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- NPC-EUR +10.34% — DETECTED_EARLY — couche NONE — action INTERPRETATION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
