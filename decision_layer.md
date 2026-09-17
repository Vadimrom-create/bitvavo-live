# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-17T10:09:34.465788+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : aucun candidat matériel
- **MEILLEUR_LATENT_ACCELERATOR** : aucun candidat matériel
- **MEILLEUR_PULLBACK_REENTRY** : TAO-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 7.312 | entrée 7.000 | trend 7.650 | rang 7.171
  - Trend remains strong; candidate retained for re-entry instead of discarded.

## Top cross-sectionnel

1. TAO-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.171
2. NEAR-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 6.864

## Accélération indépendante

- SYN-EUR — BUILDING_ACCELERATION — score 6.000/10 — DETECTED_BUT_TOO_LATE
- TREAD-EUR — BUILDING_ACCELERATION — score 5.366/10 — REQUIRES_V4_ENTRY_AND_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- ICP-EUR — ACTIVE_NOW — score mémoire 8.481/10 — sources V4 — WATCH_ONLY
- AERO-EUR — ACTIVE_NOW — score mémoire 8.247/10 — sources V4 — WATCH_ONLY
- VTHO-EUR — ACTIVE_NOW — score mémoire 8.104/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- LDO-EUR — ACTIVE_NOW — score mémoire 8.088/10 — sources V4 — WATCH_ONLY
- YB-EUR — ACTIVE_NOW — score mémoire 7.985/10 — sources V4 — WATCH_ONLY
- VET-EUR — ACTIVE_NOW — score mémoire 7.918/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- PHA-EUR — ACTIVE_NOW — score mémoire 7.912/10 — sources V4 — WATCH_ONLY
- CAKE-EUR — ACTIVE_NOW — score mémoire 7.851/10 — sources V4 — DETECTED_BUT_TOO_LATE
- NPC-EUR — MEMORY_24H — score mémoire 7.770/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- ETHFI-EUR — ACTIVE_NOW — score mémoire 7.750/10 — sources V4 — WATCH_ONLY

## Audit des plus fortes hausses

- AVA-EUR +59.07% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- FOLD-EUR +44.72% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- SYN-EUR +23.97% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- 0G-EUR +18.57% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- PEAQ-EUR +18.00% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- QUID-EUR +17.90% — DETECTED_TOO_LATE — couche NONE — action INTERPRETATION
- HNT-EUR +17.58% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- NEAR-EUR +15.12% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- LIGHTER-EUR +14.96% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- USELESS-EUR +14.70% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
