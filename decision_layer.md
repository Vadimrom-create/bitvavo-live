# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-17T09:53:00.621098+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : aucun candidat matériel
- **MEILLEUR_LATENT_ACCELERATOR** : aucun candidat matériel
- **MEILLEUR_PULLBACK_REENTRY** : FET-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 7.624 | entrée 7.150 | trend 7.650 | rang 7.261
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. FET-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.261
2. NEAR-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.130

## Accélération indépendante

- SYN-EUR — CONFIRMED_ACCELERATION — score 10.000/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- SYN-EUR — ACTIVE_NOW — score mémoire 10.000/10 — sources ACCELERATION, V4 — DETECTED_BUT_TOO_LATE
- LDO-EUR — ACTIVE_NOW — score mémoire 8.791/10 — sources V4 — WATCH_ONLY
- CAKE-EUR — ACTIVE_NOW — score mémoire 8.138/10 — sources V4 — DETECTED_BUT_TOO_LATE
- AERO-EUR — ACTIVE_NOW — score mémoire 8.052/10 — sources V4 — WATCH_ONLY
- ETHFI-EUR — ACTIVE_NOW — score mémoire 7.973/10 — sources V4 — WATCH_ONLY
- KAS-EUR — ACTIVE_NOW — score mémoire 7.910/10 — sources DECISION_LAYER, V4 — WATCH_ONLY
- VET-EUR — ACTIVE_NOW — score mémoire 7.778/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- NPC-EUR — ACTIVE_NOW — score mémoire 7.770/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- VTHO-EUR — ACTIVE_NOW — score mémoire 7.747/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- PORTAL-EUR — ACTIVE_NOW — score mémoire 7.744/10 — sources V4 — WATCH_ONLY

## Audit des plus fortes hausses

- AVA-EUR +55.42% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- FOLD-EUR +44.26% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- SYN-EUR +41.73% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- 0G-EUR +18.10% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- HNT-EUR +17.82% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- NEAR-EUR +17.55% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- QUID-EUR +17.43% — DETECTED_TOO_LATE — couche NONE — action INTERPRETATION
- PEAQ-EUR +17.04% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- USELESS-EUR +16.19% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- LIGHTER-EUR +14.61% — DETECTED_EARLY — couche NONE — action INTERPRETATION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
