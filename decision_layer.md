# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-14T04:04:28.936807+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : aucun candidat matériel
- **MEILLEUR_LATENT_ACCELERATOR** : aucun candidat matériel
- **MEILLEUR_PULLBACK_REENTRY** : VTHO-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.153 | entrée 6.250 | trend 9.200 | rang 8.052
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. VTHO-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.052
2. UNI-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.372
3. NEAR-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.151

## Accélération indépendante

Aucune accélération indépendante confirmée ou en construction.

## Watchlist persistante 24–72 h

- NPC-EUR — ACTIVE_NOW — score mémoire 8.143/10 — sources ACCELERATION, V4 — WATCH_ONLY
- LDO-EUR — ACTIVE_NOW — score mémoire 8.119/10 — sources V4 — WATCH_ONLY
- VTHO-EUR — ACTIVE_NOW — score mémoire 8.052/10 — sources DECISION_LAYER, V4 — WATCH_ONLY
- LAPTOP-EUR — MEMORY_24H — score mémoire 8.013/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- ETHFI-EUR — ACTIVE_NOW — score mémoire 7.987/10 — sources V4 — WATCH_ONLY
- ICP-EUR — ACTIVE_NOW — score mémoire 7.960/10 — sources V4 — WATCH_ONLY
- INJ-EUR — ACTIVE_NOW — score mémoire 7.945/10 — sources DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- YB-EUR — ACTIVE_NOW — score mémoire 7.938/10 — sources V4 — WATCH_ONLY
- VET-EUR — ACTIVE_NOW — score mémoire 7.851/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- CAKE-EUR — ACTIVE_NOW — score mémoire 7.804/10 — sources V4 — WATCH_ONLY

## Audit des plus fortes hausses

- REZ-EUR +30.97% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- CPOOL-EUR +23.37% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- CVC-EUR +22.60% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- ZKJ-EUR +20.99% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- FIL-EUR +17.69% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- IQ-EUR +15.34% — DETECTED_TOO_LATE — couche NONE — action INTERPRETATION
- MTL-EUR +15.02% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- LIGHTER-EUR +10.18% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- NPC-EUR +9.97% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE
- BABY-EUR +7.07% — DETECTED_EARLY — couche NONE — action INTERPRETATION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
