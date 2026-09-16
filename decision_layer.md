# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-16T10:08:49.034302+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : aucun candidat matériel
- **MEILLEUR_LATENT_ACCELERATOR** : aucun candidat matériel
- **MEILLEUR_PULLBACK_REENTRY** : NEAR-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 7.991 | entrée 8.000 | trend 8.100 | rang 7.312
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. NEAR-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.312

## Accélération indépendante

Aucune accélération indépendante confirmée ou en construction.

## Watchlist persistante 24–72 h

- LSK-EUR — MEMORY_24H — score mémoire 8.468/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- ETHFI-EUR — ACTIVE_NOW — score mémoire 8.119/10 — sources V4 — WATCH_ONLY
- VET-EUR — ACTIVE_NOW — score mémoire 7.982/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- FORM-EUR — ACTIVE_NOW — score mémoire 7.953/10 — sources V4 — WATCH_ONLY
- PENDLE-EUR — ACTIVE_NOW — score mémoire 7.840/10 — sources DECISION_LAYER, V4 — WATCH_ONLY
- LDO-EUR — ACTIVE_NOW — score mémoire 7.774/10 — sources V4 — WATCH_ONLY
- PUMP-EUR — ACTIVE_NOW — score mémoire 7.771/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- VTHO-EUR — ACTIVE_NOW — score mémoire 7.736/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- CVC-EUR — MEMORY_24H — score mémoire 7.734/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- ICP-EUR — ACTIVE_NOW — score mémoire 7.721/10 — sources V4 — WATCH_ONLY

## Audit des plus fortes hausses

- SYN-EUR +118.95% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- LSK-EUR +31.73% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- ARB-EUR +17.24% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- USELESS-EUR +17.02% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- CNPY-EUR +12.97% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ALIGN-EUR +10.98% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- G-EUR +9.71% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- FOLD-EUR +7.35% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- PUNDIX-EUR +7.23% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- XNO-EUR +7.04% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
