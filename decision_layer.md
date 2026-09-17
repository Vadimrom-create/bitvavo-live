# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-17T09:36:06.434467+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : aucun candidat matériel
- **MEILLEUR_LATENT_ACCELERATOR** : aucun candidat matériel
- **MEILLEUR_PULLBACK_REENTRY** : FET-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.211 | entrée 7.850 | trend 7.650 | rang 7.624
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. FET-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.624
2. NEAR-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 6.736

## Accélération indépendante

- SYN-EUR — CONFIRMED_ACCELERATION — score 9.383/10 — DETECTED_BUT_TOO_LATE
- AVA-EUR — CONFIRMED_ACCELERATION — score 6.688/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- SYN-EUR — ACTIVE_NOW — score mémoire 9.383/10 — sources ACCELERATION, V4 — DETECTED_BUT_TOO_LATE
- VET-EUR — ACTIVE_NOW — score mémoire 8.197/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- ENS-EUR — ACTIVE_NOW — score mémoire 8.165/10 — sources V4 — WATCH_ONLY
- GRT-EUR — ACTIVE_NOW — score mémoire 8.147/10 — sources V4 — WATCH_ONLY
- KAS-EUR — ACTIVE_NOW — score mémoire 8.085/10 — sources DECISION_LAYER, V4 — WATCH_ONLY
- ICP-EUR — ACTIVE_NOW — score mémoire 7.972/10 — sources V4 — WATCH_ONLY
- ETHFI-EUR — ACTIVE_NOW — score mémoire 7.924/10 — sources V4 — WATCH_ONLY
- VTHO-EUR — MEMORY_24H — score mémoire 7.860/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- LDO-EUR — ACTIVE_NOW — score mémoire 7.819/10 — sources V4 — WATCH_ONLY
- ATOM-EUR — ACTIVE_NOW — score mémoire 7.800/10 — sources V4 — WATCH_ONLY

## Audit des plus fortes hausses

- AVA-EUR +62.31% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- FOLD-EUR +47.00% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- HNT-EUR +18.53% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- NEAR-EUR +18.05% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- QUID-EUR +17.14% — DETECTED_TOO_LATE — couche NONE — action INTERPRETATION
- 0G-EUR +16.50% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- PEAQ-EUR +16.24% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- LIGHTER-EUR +15.71% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- VVV-EUR +15.54% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- COTI-EUR +12.52% — DETECTED_EARLY — couche NONE — action INTERPRETATION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
