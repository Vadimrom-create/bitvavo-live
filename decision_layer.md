# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-14T22:34:24.221549+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : aucun candidat matériel
- **MEILLEUR_LATENT_ACCELERATOR** : aucun candidat matériel
- **MEILLEUR_PULLBACK_REENTRY** : VTHO-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.156 | entrée 5.950 | trend 9.200 | rang 8.018
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. VTHO-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.018
2. LSK-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.171
3. NEAR-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.006

## Accélération indépendante

Aucune accélération indépendante confirmée ou en construction.

## Watchlist persistante 24–72 h

- CNPY-EUR — MEMORY_24H — score mémoire 8.734/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- LDO-EUR — ACTIVE_NOW — score mémoire 8.074/10 — sources V4 — WATCH_ONLY
- VTHO-EUR — ACTIVE_NOW — score mémoire 8.018/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- YB-EUR — ACTIVE_NOW — score mémoire 7.890/10 — sources V4 — WATCH_ONLY
- KAS-EUR — ACTIVE_NOW — score mémoire 7.809/10 — sources V4 — WATCH_ONLY
- VVV-EUR — MEMORY_24H — score mémoire 7.623/10 — sources V4 — MEMORY_ONLY
- ICP-EUR — ACTIVE_NOW — score mémoire 7.620/10 — sources V4 — WATCH_ONLY
- FORM-EUR — ACTIVE_NOW — score mémoire 7.569/10 — sources V4 — WATCH_ONLY
- ETHFI-EUR — ACTIVE_NOW — score mémoire 7.549/10 — sources V4 — WATCH_ONLY
- INJ-EUR — ACTIVE_NOW — score mémoire 7.534/10 — sources DECISION_LAYER, V4 — WATCH_ONLY

## Audit des plus fortes hausses

- CNPY-EUR +37.23% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- CPOOL-EUR +36.51% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- CAP-EUR +35.39% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- ARK-EUR +31.94% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- BOB-EUR +22.52% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- MTL-EUR +17.63% — DETECTED_TOO_LATE — couche NONE — action INTERPRETATION
- PENDLE-EUR +15.89% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE
- SENT-EUR +15.05% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- T-EUR +12.06% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- NPC-EUR +11.82% — DETECTED_EARLY — couche NONE — action INTERPRETATION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
