# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-17T12:58:09.922554+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : aucun candidat matériel
- **MEILLEUR_LATENT_ACCELERATOR** : aucun candidat matériel
- **MEILLEUR_PULLBACK_REENTRY** : LSK-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 7.738 | entrée 6.350 | trend 8.400 | rang 7.585
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. LSK-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.585

## Accélération indépendante

- AVA-EUR — BUILDING_ACCELERATION — score 5.784/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- LDO-EUR — ACTIVE_NOW — score mémoire 8.329/10 — sources V4 — WATCH_ONLY
- ETHFI-EUR — ACTIVE_NOW — score mémoire 8.275/10 — sources V4 — WATCH_ONLY
- INJ-EUR — ACTIVE_NOW — score mémoire 8.227/10 — sources DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- PHA-EUR — ACTIVE_NOW — score mémoire 8.176/10 — sources V4 — DETECTED_BUT_TOO_LATE
- METIS-EUR — ACTIVE_NOW — score mémoire 8.101/10 — sources V4 — DETECTED_BUT_TOO_LATE
- FORM-EUR — ACTIVE_NOW — score mémoire 8.018/10 — sources V4 — WATCH_ONLY
- FET-EUR — ACTIVE_NOW — score mémoire 7.802/10 — sources DECISION_LAYER, V4 — WATCH_ONLY
- DOT-EUR — ACTIVE_NOW — score mémoire 7.794/10 — sources DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- VTHO-EUR — ACTIVE_NOW — score mémoire 7.789/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- PUMP-EUR — ACTIVE_NOW — score mémoire 7.747/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE

## Audit des plus fortes hausses

- AVA-EUR +97.70% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- QUID-EUR +21.84% — DETECTED_TOO_LATE — couche NONE — action INTERPRETATION
- AGI-EUR +21.29% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- PEAQ-EUR +19.47% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- NEAR-EUR +16.59% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- EDEN-EUR +16.28% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- LIGHTER-EUR +16.20% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- FOLD-EUR +15.20% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- DGB-EUR +14.53% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- SYN-EUR +13.78% — DETECTED_EARLY — couche NONE — action INTERPRETATION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
