# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-16T21:34:44.551268+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : aucun candidat matériel
- **MEILLEUR_LATENT_ACCELERATOR** : aucun candidat matériel
- **MEILLEUR_PULLBACK_REENTRY** : USELESS-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.172 | entrée 7.300 | trend 8.100 | rang 7.419
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. USELESS-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.419
2. NEAR-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.263

## Accélération indépendante

- TREAD-EUR — CONFIRMED_ACCELERATION — score 6.942/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- NPC-EUR — ACTIVE_NOW — score mémoire 8.146/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- LDO-EUR — ACTIVE_NOW — score mémoire 8.130/10 — sources V4 — WATCH_ONLY
- ICP-EUR — ACTIVE_NOW — score mémoire 8.075/10 — sources V4 — WATCH_ONLY
- VTHO-EUR — ACTIVE_NOW — score mémoire 8.072/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- SIGN-EUR — ACTIVE_NOW — score mémoire 8.061/10 — sources V4 — WATCH_ONLY
- FORM-EUR — ACTIVE_NOW — score mémoire 7.977/10 — sources V4 — WATCH_ONLY
- ETHFI-EUR — ACTIVE_NOW — score mémoire 7.954/10 — sources V4 — WATCH_ONLY
- AKT-EUR — ACTIVE_NOW — score mémoire 7.849/10 — sources DECISION_LAYER, V4 — WATCH_ONLY
- PEAQ-EUR — ACTIVE_NOW — score mémoire 7.795/10 — sources V4 — WATCH_ONLY
- PHA-EUR — ACTIVE_NOW — score mémoire 7.759/10 — sources V4 — WATCH_ONLY

## Audit des plus fortes hausses

- SYN-EUR +121.57% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- LSK-EUR +89.40% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- HEI-EUR +31.64% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- HNT-EUR +23.52% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- FOLD-EUR +21.70% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- IOST-EUR +17.38% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ARB-EUR +15.95% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- RAY-EUR +15.25% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- AGI-EUR +14.04% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- LIGHTER-EUR +11.30% — DETECTED_EARLY — couche NONE — action INTERPRETATION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
