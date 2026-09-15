# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-15T14:42:10.617711+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : aucun candidat matériel
- **MEILLEUR_LATENT_ACCELERATOR** : aucun candidat matériel
- **MEILLEUR_PULLBACK_REENTRY** : USELESS-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 7.853 | entrée 6.250 | trend 8.100 | rang 7.278
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. USELESS-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.278
2. TAO-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 6.969
3. NEAR-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 6.913

## Accélération indépendante

Aucune accélération indépendante confirmée ou en construction.

## Watchlist persistante 24–72 h

- ICP-EUR — ACTIVE_NOW — score mémoire 8.441/10 — sources V4 — WATCH_ONLY
- UNI-EUR — MEMORY_24H — score mémoire 7.931/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- LDO-EUR — ACTIVE_NOW — score mémoire 7.835/10 — sources V4 — WATCH_ONLY
- CAKE-EUR — ACTIVE_NOW — score mémoire 7.816/10 — sources V4 — WATCH_ONLY
- TIA-EUR — MEMORY_24H — score mémoire 7.702/10 — sources V4 — MEMORY_ONLY
- ETHFI-EUR — ACTIVE_NOW — score mémoire 7.619/10 — sources V4 — WATCH_ONLY
- KAS-EUR — ACTIVE_NOW — score mémoire 7.547/10 — sources V4 — WATCH_ONLY
- WIF-EUR — MEMORY_24H — score mémoire 7.528/10 — sources V4 — MEMORY_ONLY
- VET-EUR — ACTIVE_NOW — score mémoire 7.505/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- VTHO-EUR — ACTIVE_NOW — score mémoire 7.438/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE

## Audit des plus fortes hausses

- ALIGN-EUR +36.96% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- CNPY-EUR +34.59% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- PUFFER-EUR +26.74% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- SAGA-EUR +18.18% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- ASTR-EUR +15.83% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- CROSS-EUR +15.55% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- GLMR-EUR +14.10% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- LAPTOP-EUR +11.32% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- VTHO-EUR +10.42% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- NES-EUR +6.22% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
