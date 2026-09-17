# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-17T13:38:52.785987+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : aucun candidat matériel
- **MEILLEUR_LATENT_ACCELERATOR** : PEAQ-EUR | action LATENT_ACCELERATOR | opportunité 7.432 | entrée 5.750 | trend 8.550 | rang 6.494
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : UNI-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 7.804 | entrée 7.000 | trend 7.750 | rang 7.119
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. UNI-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.119
2. NEAR-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 6.563
3. PEAQ-EUR — MEILLEUR_LATENT_ACCELERATOR — LATENT_ACCELERATOR — rank 6.494

## Accélération indépendante

Aucune accélération indépendante confirmée ou en construction.

## Watchlist persistante 24–72 h

- ICP-EUR — ACTIVE_NOW — score mémoire 8.373/10 — sources V4 — WATCH_ONLY
- XVG-EUR — ACTIVE_NOW — score mémoire 8.138/10 — sources V4 — WATCH_ONLY
- VTHO-EUR — ACTIVE_NOW — score mémoire 8.121/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- WLD-EUR — ACTIVE_NOW — score mémoire 8.053/10 — sources DECISION_LAYER, V4 — WATCH_ONLY
- ETHFI-EUR — ACTIVE_NOW — score mémoire 7.998/10 — sources V4 — WATCH_ONLY
- LDO-EUR — ACTIVE_NOW — score mémoire 7.894/10 — sources V4 — WATCH_ONLY
- INJ-EUR — ACTIVE_NOW — score mémoire 7.749/10 — sources DECISION_LAYER, V4 — WATCH_ONLY
- YGG-EUR — ACTIVE_NOW — score mémoire 7.705/10 — sources V4 — WATCH_ONLY
- YB-EUR — ACTIVE_NOW — score mémoire 7.693/10 — sources V4 — WATCH_ONLY
- BNB-EUR — ACTIVE_NOW — score mémoire 7.634/10 — sources V4 — WATCH_ONLY

## Audit des plus fortes hausses

- AVA-EUR +86.95% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- AGI-EUR +33.97% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- FOLD-EUR +19.51% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- PEAQ-EUR +18.89% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- QUID-EUR +18.86% — DETECTED_TOO_LATE — couche NONE — action INTERPRETATION
- DGB-EUR +18.73% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- NEAR-EUR +17.02% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- LIGHTER-EUR +16.39% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- COTI-EUR +14.75% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- EDEN-EUR +14.49% — DETECTED_EARLY — couche NONE — action INTERPRETATION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
