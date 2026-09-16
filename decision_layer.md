# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-16T16:45:34.429878+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : aucun candidat matériel
- **MEILLEUR_LATENT_ACCELERATOR** : aucun candidat matériel
- **MEILLEUR_PULLBACK_REENTRY** : VTHO-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.238 | entrée 5.400 | trend 9.200 | rang 7.894
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. VTHO-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.894
2. NEAR-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.483

## Accélération indépendante

- LSK-EUR — CONFIRMED_ACCELERATION — score 9.258/10 — DETECTED_BUT_TOO_LATE
- LAPTOP-EUR — BUILDING_ACCELERATION — score 4.890/10 — REQUIRES_V4_ENTRY_AND_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- HEI-EUR — MEMORY_24H — score mémoire 9.941/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- LSK-EUR — ACTIVE_NOW — score mémoire 9.258/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- LDO-EUR — ACTIVE_NOW — score mémoire 8.673/10 — sources V4 — WATCH_ONLY
- PHA-EUR — MEMORY_24H — score mémoire 8.040/10 — sources V4 — MEMORY_ONLY
- VTHO-EUR — ACTIVE_NOW — score mémoire 7.894/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- SYN-EUR — MEMORY_24H — score mémoire 7.850/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- XVG-EUR — ACTIVE_NOW — score mémoire 7.734/10 — sources V4 — WATCH_ONLY
- ASTR-EUR — ACTIVE_NOW — score mémoire 7.707/10 — sources DECISION_LAYER, V4 — WATCH_ONLY
- ETHFI-EUR — ACTIVE_NOW — score mémoire 7.690/10 — sources V4 — WATCH_ONLY
- VET-EUR — ACTIVE_NOW — score mémoire 7.659/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY

## Audit des plus fortes hausses

- SYN-EUR +111.92% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- LSK-EUR +92.27% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- HEI-EUR +26.95% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- CNPY-EUR +17.97% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- FOLD-EUR +16.20% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- SOSO-EUR +9.81% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- USELESS-EUR +9.08% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- AGI-EUR +7.92% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE
- RAY-EUR +7.24% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE
- IOST-EUR +7.12% — DETECTED_EARLY — couche NONE — action INTERPRETATION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
