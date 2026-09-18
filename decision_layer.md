# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-18T20:49:34.604993+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : aucun candidat matériel
- **MEILLEUR_LATENT_ACCELERATOR** : aucun candidat matériel
- **MEILLEUR_PULLBACK_REENTRY** : LSK-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.147 | entrée 6.550 | trend 8.400 | rang 7.794
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. LSK-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.794
2. KAS-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.460

## Accélération indépendante

- STRK-EUR — BUILDING_ACCELERATION — score 5.679/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- ICP-EUR — ACTIVE_NOW — score mémoire 8.200/10 — sources DECISION_LAYER, V4 — WATCH_ONLY
- LDO-EUR — ACTIVE_NOW — score mémoire 8.163/10 — sources V4 — WATCH_ONLY
- VTHO-EUR — ACTIVE_NOW — score mémoire 8.011/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- COTI-EUR — ACTIVE_NOW — score mémoire 7.979/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- METIS-EUR — ACTIVE_NOW — score mémoire 7.951/10 — sources V4 — DETECTED_BUT_TOO_LATE
- VET-EUR — ACTIVE_NOW — score mémoire 7.876/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- FORM-EUR — ACTIVE_NOW — score mémoire 7.850/10 — sources V4 — WATCH_ONLY
- ORCA-EUR — ACTIVE_NOW — score mémoire 7.810/10 — sources V4 — WATCH_ONLY
- YB-EUR — ACTIVE_NOW — score mémoire 7.802/10 — sources V4 — WATCH_ONLY
- LSK-EUR — ACTIVE_NOW — score mémoire 7.794/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY

## Audit des plus fortes hausses

- G-EUR +59.77% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- STRK-EUR +49.01% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- F-EUR +39.26% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- APT-EUR +26.15% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ARB-EUR +26.05% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- NEAR-EUR +22.12% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- ZAMA-EUR +21.19% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- C-EUR +21.02% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- S-EUR +20.78% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ZK-EUR +20.41% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
