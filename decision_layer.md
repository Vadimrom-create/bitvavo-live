# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-16T03:00:50.000331+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : aucun candidat matériel
- **MEILLEUR_LATENT_ACCELERATOR** : VTHO-EUR | action LATENT_ACCELERATOR | opportunité 7.605 | entrée 4.950 | trend 9.200 | rang 6.787
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : USELESS-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 9.261 | entrée 7.750 | trend 8.100 | rang 8.081
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. USELESS-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.081
2. VTHO-EUR — MEILLEUR_LATENT_ACCELERATOR — LATENT_ACCELERATOR — rank 6.787

## Accélération indépendante

Aucune accélération indépendante confirmée ou en construction.

## Watchlist persistante 24–72 h

- USELESS-EUR — ACTIVE_NOW — score mémoire 8.081/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- SOMI-EUR — ACTIVE_NOW — score mémoire 7.833/10 — sources V4 — WATCH_ONLY
- SIGN-EUR — ACTIVE_NOW — score mémoire 7.813/10 — sources V4 — WATCH_ONLY
- AERO-EUR — ACTIVE_NOW — score mémoire 7.792/10 — sources V4 — WATCH_ONLY
- AIOZ-EUR — ACTIVE_NOW — score mémoire 7.697/10 — sources V4 — WATCH_ONLY
- VET-EUR — ACTIVE_NOW — score mémoire 7.682/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- DOT-EUR — ACTIVE_NOW — score mémoire 7.682/10 — sources DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- ICP-EUR — ACTIVE_NOW — score mémoire 7.680/10 — sources V4 — WATCH_ONLY
- ETHFI-EUR — ACTIVE_NOW — score mémoire 7.669/10 — sources V4 — WATCH_ONLY
- LDO-EUR — ACTIVE_NOW — score mémoire 7.654/10 — sources V4 — WATCH_ONLY

## Audit des plus fortes hausses

- PUFFER-EUR +42.37% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- ALIGN-EUR +29.23% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- LAPTOP-EUR +23.81% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- SYN-EUR +21.33% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- CNPY-EUR +19.85% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- CROSS-EUR +17.74% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- VTHO-EUR +17.68% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- SAGA-EUR +15.04% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- FOLD-EUR +14.09% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- ARB-EUR +12.94% — DETECTED_EARLY — couche NONE — action INTERPRETATION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
