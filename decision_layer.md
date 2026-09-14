# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-14T18:00:42.671077+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : aucun candidat matériel
- **MEILLEUR_LATENT_ACCELERATOR** : aucun candidat matériel
- **MEILLEUR_PULLBACK_REENTRY** : TAO-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.587 | entrée 7.250 | trend 7.650 | rang 7.731
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. TAO-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.731
2. FET-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.279
3. NEAR-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 6.854

## Accélération indépendante

- NEAR-EUR — BUILDING_ACCELERATION — score 4.870/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- ETHFI-EUR — ACTIVE_NOW — score mémoire 8.485/10 — sources V4 — WATCH_ONLY
- XVG-EUR — ACTIVE_NOW — score mémoire 8.370/10 — sources V4 — WATCH_ONLY
- ICP-EUR — ACTIVE_NOW — score mémoire 8.311/10 — sources V4 — WATCH_ONLY
- VET-EUR — ACTIVE_NOW — score mémoire 8.056/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- YB-EUR — ACTIVE_NOW — score mémoire 8.017/10 — sources V4 — WATCH_ONLY
- LDO-EUR — ACTIVE_NOW — score mémoire 8.008/10 — sources V4 — WATCH_ONLY
- WLD-EUR — ACTIVE_NOW — score mémoire 7.963/10 — sources DECISION_LAYER, V4 — WATCH_ONLY
- VTHO-EUR — ACTIVE_NOW — score mémoire 7.892/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- GRT-EUR — ACTIVE_NOW — score mémoire 7.799/10 — sources V4 — WATCH_ONLY
- INJ-EUR — ACTIVE_NOW — score mémoire 7.749/10 — sources DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE

## Audit des plus fortes hausses

- CPOOL-EUR +33.16% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- CNPY-EUR +31.04% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- CAP-EUR +22.86% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- SENT-EUR +15.67% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- MTL-EUR +13.97% — DETECTED_TOO_LATE — couche NONE — action INTERPRETATION
- ARK-EUR +13.76% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- NPC-EUR +11.71% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- QKC-EUR +11.25% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- NOT-EUR +10.43% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE
- NEAR-EUR +10.05% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
