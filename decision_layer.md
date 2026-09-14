# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-14T03:50:37.485263+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : aucun candidat matériel
- **MEILLEUR_LATENT_ACCELERATOR** : aucun candidat matériel
- **MEILLEUR_PULLBACK_REENTRY** : VTHO-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 7.747 | entrée 5.500 | trend 9.200 | rang 7.767
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. VTHO-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.767
2. NEAR-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.462
3. FET-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.269

## Accélération indépendante

- LSK-EUR — BUILDING_ACCELERATION — score 5.857/10 — REQUIRES_V4_ENTRY_AND_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- LDO-EUR — ACTIVE_NOW — score mémoire 8.119/10 — sources V4 — WATCH_ONLY
- ETHFI-EUR — ACTIVE_NOW — score mémoire 8.061/10 — sources V4 — WATCH_ONLY
- LAPTOP-EUR — MEMORY_24H — score mémoire 8.013/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- ICP-EUR — ACTIVE_NOW — score mémoire 7.933/10 — sources V4 — WATCH_ONLY
- YB-EUR — ACTIVE_NOW — score mémoire 7.908/10 — sources V4 — WATCH_ONLY
- XPL-EUR — ACTIVE_NOW — score mémoire 7.888/10 — sources V4 — WATCH_ONLY
- WLD-EUR — ACTIVE_NOW — score mémoire 7.874/10 — sources DECISION_LAYER, V4 — WATCH_ONLY
- VET-EUR — ACTIVE_NOW — score mémoire 7.822/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- ZIL-EUR — ACTIVE_NOW — score mémoire 7.793/10 — sources DECISION_LAYER, V4 — WATCH_ONLY
- KAS-EUR — ACTIVE_NOW — score mémoire 7.793/10 — sources V4 — WATCH_ONLY

## Audit des plus fortes hausses

- REZ-EUR +31.09% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- CPOOL-EUR +27.88% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- ZKJ-EUR +19.13% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- CVC-EUR +19.07% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- FIL-EUR +18.61% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- IQ-EUR +15.04% — DETECTED_TOO_LATE — couche NONE — action INTERPRETATION
- MTL-EUR +13.08% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- LIGHTER-EUR +10.70% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- NPC-EUR +9.39% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE
- BABY-EUR +7.56% — DETECTED_EARLY — couche NONE — action INTERPRETATION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
