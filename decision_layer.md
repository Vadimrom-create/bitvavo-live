# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-16T02:47:57.065725+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : aucun candidat matériel
- **MEILLEUR_LATENT_ACCELERATOR** : VTHO-EUR | action LATENT_ACCELERATOR | opportunité 7.658 | entrée 4.750 | trend 9.200 | rang 6.771
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : USELESS-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 9.261 | entrée 7.750 | trend 8.100 | rang 8.062
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. USELESS-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.062
2. VTHO-EUR — MEILLEUR_LATENT_ACCELERATOR — LATENT_ACCELERATOR — rank 6.771

## Accélération indépendante

Aucune accélération indépendante confirmée ou en construction.

## Watchlist persistante 24–72 h

- USELESS-EUR — ACTIVE_NOW — score mémoire 8.062/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- ETHFI-EUR — ACTIVE_NOW — score mémoire 7.990/10 — sources V4 — WATCH_ONLY
- SIGN-EUR — ACTIVE_NOW — score mémoire 7.864/10 — sources V4 — WATCH_ONLY
- DOT-EUR — ACTIVE_NOW — score mémoire 7.805/10 — sources DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- AERO-EUR — ACTIVE_NOW — score mémoire 7.772/10 — sources V4 — WATCH_ONLY
- SOMI-EUR — ACTIVE_NOW — score mémoire 7.770/10 — sources V4 — WATCH_ONLY
- ICP-EUR — ACTIVE_NOW — score mémoire 7.732/10 — sources V4 — WATCH_ONLY
- ZIL-EUR — ACTIVE_NOW — score mémoire 7.725/10 — sources DECISION_LAYER, V4 — WATCH_ONLY
- LDO-EUR — ACTIVE_NOW — score mémoire 7.707/10 — sources V4 — WATCH_ONLY
- VET-EUR — ACTIVE_NOW — score mémoire 7.653/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY

## Audit des plus fortes hausses

- PUFFER-EUR +48.13% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- ALIGN-EUR +29.09% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- CROSS-EUR +26.71% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- LAPTOP-EUR +24.95% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- SYN-EUR +22.42% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- VTHO-EUR +17.94% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- CNPY-EUR +17.66% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- SAGA-EUR +14.64% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- ARB-EUR +13.58% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- USELESS-EUR +9.48% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
