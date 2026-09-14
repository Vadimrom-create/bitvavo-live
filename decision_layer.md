# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-14T12:33:34.756236+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : aucun candidat matériel
- **MEILLEUR_LATENT_ACCELERATOR** : aucun candidat matériel
- **MEILLEUR_PULLBACK_REENTRY** : VTHO-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.036 | entrée 5.750 | trend 9.200 | rang 7.939
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. VTHO-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.939
2. NEAR-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.746
3. LSK-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.158

## Accélération indépendante

Aucune accélération indépendante confirmée ou en construction.

## Watchlist persistante 24–72 h

- ETHFI-EUR — ACTIVE_NOW — score mémoire 8.014/10 — sources V4 — WATCH_ONLY
- VTHO-EUR — ACTIVE_NOW — score mémoire 7.939/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- LDO-EUR — ACTIVE_NOW — score mémoire 7.881/10 — sources V4 — WATCH_ONLY
- VET-EUR — ACTIVE_NOW — score mémoire 7.752/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- NEAR-EUR — ACTIVE_NOW — score mémoire 7.746/10 — sources DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- NEO-EUR — MEMORY_24H — score mémoire 7.738/10 — sources V4 — MEMORY_ONLY
- PEAQ-EUR — ACTIVE_NOW — score mémoire 7.703/10 — sources V4 — DETECTED_BUT_TOO_LATE
- WLD-EUR — ACTIVE_NOW — score mémoire 7.702/10 — sources DECISION_LAYER, V4 — WATCH_ONLY
- NPC-EUR — ACTIVE_NOW — score mémoire 7.672/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- ICP-EUR — ACTIVE_NOW — score mémoire 7.598/10 — sources V4 — WATCH_ONLY

## Audit des plus fortes hausses

- CPOOL-EUR +50.36% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- QKC-EUR +36.41% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- CAP-EUR +32.12% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- FIL-EUR +20.01% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- T-EUR +15.41% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- MIOTA-EUR +15.20% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- CNPY-EUR +12.79% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- LIGHTER-EUR +11.12% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- REZ-EUR +10.52% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ZRC-EUR +10.22% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
