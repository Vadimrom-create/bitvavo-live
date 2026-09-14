# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-14T16:54:40.937808+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : aucun candidat matériel
- **MEILLEUR_LATENT_ACCELERATOR** : aucun candidat matériel
- **MEILLEUR_PULLBACK_REENTRY** : VTHO-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.830 | entrée 6.300 | trend 9.200 | rang 8.370
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. VTHO-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.370
2. NEAR-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.018
3. TAO-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.639

## Accélération indépendante

- LSK-EUR — CONFIRMED_ACCELERATION — score 7.153/10 — REQUIRES_V4_ENTRY_AND_EXECUTION_VALIDATION
- ARK-EUR — BUILDING_ACCELERATION — score 5.501/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- CNPY-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- VTHO-EUR — ACTIVE_NOW — score mémoire 8.370/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- KAS-EUR — ACTIVE_NOW — score mémoire 8.203/10 — sources V4 — WATCH_ONLY
- VET-EUR — ACTIVE_NOW — score mémoire 8.195/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- NEAR-EUR — ACTIVE_NOW — score mémoire 8.018/10 — sources DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- LDO-EUR — ACTIVE_NOW — score mémoire 8.010/10 — sources V4 — WATCH_ONLY
- ICP-EUR — ACTIVE_NOW — score mémoire 7.968/10 — sources V4 — WATCH_ONLY
- JUP-EUR — ACTIVE_NOW — score mémoire 7.916/10 — sources V4 — WATCH_ONLY
- ETHFI-EUR — ACTIVE_NOW — score mémoire 7.915/10 — sources V4 — WATCH_ONLY
- ZORA-EUR — ACTIVE_NOW — score mémoire 7.892/10 — sources V4 — WATCH_ONLY

## Audit des plus fortes hausses

- CNPY-EUR +38.76% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- CPOOL-EUR +36.03% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- CAP-EUR +25.71% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- ARK-EUR +17.70% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- MTL-EUR +17.05% — DETECTED_TOO_LATE — couche NONE — action INTERPRETATION
- T-EUR +12.82% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- NPC-EUR +11.76% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- SENT-EUR +11.06% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE
- QKC-EUR +9.96% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- XLM-EUR +9.45% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
