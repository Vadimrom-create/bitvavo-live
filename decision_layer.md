# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-15T18:03:37.805107+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : aucun candidat matériel
- **MEILLEUR_LATENT_ACCELERATOR** : aucun candidat matériel
- **MEILLEUR_PULLBACK_REENTRY** : UNI-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.431 | entrée 7.150 | trend 7.750 | rang 7.677
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. UNI-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.677
2. VTHO-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.668
3. USELESS-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.046

## Accélération indépendante

Aucune accélération indépendante confirmée ou en construction.

## Watchlist persistante 24–72 h

- ARB-EUR — MEMORY_24H — score mémoire 9.147/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- ALIGN-EUR — MEMORY_24H — score mémoire 8.942/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- VET-EUR — ACTIVE_NOW — score mémoire 8.011/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- LDO-EUR — ACTIVE_NOW — score mémoire 7.977/10 — sources V4 — WATCH_ONLY
- WLD-EUR — ACTIVE_NOW — score mémoire 7.904/10 — sources DECISION_LAYER, V4 — WATCH_ONLY
- XVG-EUR — ACTIVE_NOW — score mémoire 7.842/10 — sources V4 — WATCH_ONLY
- ICP-EUR — ACTIVE_NOW — score mémoire 7.712/10 — sources V4 — WATCH_ONLY
- UNI-EUR — ACTIVE_NOW — score mémoire 7.677/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- VTHO-EUR — ACTIVE_NOW — score mémoire 7.668/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- ETHFI-EUR — ACTIVE_NOW — score mémoire 7.649/10 — sources V4 — WATCH_ONLY

## Audit des plus fortes hausses

- ALIGN-EUR +41.35% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- SAGA-EUR +30.22% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- PUFFER-EUR +18.96% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- CNPY-EUR +18.59% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- NES-EUR +15.77% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- ASTR-EUR +15.27% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- LAPTOP-EUR +12.33% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- VTHO-EUR +11.08% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- ZKJ-EUR +10.27% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- G-EUR +9.45% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
