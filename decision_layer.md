# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-15T15:53:09.398762+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : aucun candidat matériel
- **MEILLEUR_LATENT_ACCELERATOR** : aucun candidat matériel
- **MEILLEUR_PULLBACK_REENTRY** : VTHO-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.562 | entrée 5.700 | trend 9.200 | rang 7.797
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. VTHO-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.797
2. AKT-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.482
3. USELESS-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.280

## Accélération indépendante

Aucune accélération indépendante confirmée ou en construction.

## Watchlist persistante 24–72 h

- LDO-EUR — ACTIVE_NOW — score mémoire 7.851/10 — sources V4 — WATCH_ONLY
- VTHO-EUR — ACTIVE_NOW — score mémoire 7.797/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- YB-EUR — ACTIVE_NOW — score mémoire 7.763/10 — sources V4 — WATCH_ONLY
- VET-EUR — ACTIVE_NOW — score mémoire 7.757/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- ETHFI-EUR — ACTIVE_NOW — score mémoire 7.736/10 — sources V4 — WATCH_ONLY
- TIA-EUR — MEMORY_24H — score mémoire 7.702/10 — sources V4 — MEMORY_ONLY
- ICP-EUR — ACTIVE_NOW — score mémoire 7.686/10 — sources V4 — WATCH_ONLY
- SOMI-EUR — ACTIVE_NOW — score mémoire 7.570/10 — sources V4 — WATCH_ONLY
- KAS-EUR — ACTIVE_NOW — score mémoire 7.548/10 — sources V4 — WATCH_ONLY
- WIF-EUR — MEMORY_24H — score mémoire 7.528/10 — sources V4 — MEMORY_ONLY

## Audit des plus fortes hausses

- ALIGN-EUR +36.55% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- CNPY-EUR +26.61% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- PUFFER-EUR +22.96% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- SAGA-EUR +20.27% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- ASTR-EUR +16.26% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- LAPTOP-EUR +11.63% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- CROSS-EUR +11.47% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- VTHO-EUR +10.96% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- ARB-EUR +9.95% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- NES-EUR +9.29% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
