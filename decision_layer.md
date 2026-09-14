# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-14T13:18:04.514388+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : aucun candidat matériel
- **MEILLEUR_LATENT_ACCELERATOR** : aucun candidat matériel
- **MEILLEUR_PULLBACK_REENTRY** : VTHO-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 7.945 | entrée 5.950 | trend 9.200 | rang 7.921
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. VTHO-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.921
2. NEAR-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.687
3. VET-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.619

## Accélération indépendante

- LSK-EUR — BUILDING_ACCELERATION — score 6.268/10 — REQUIRES_V4_ENTRY_AND_EXECUTION_VALIDATION
- T-EUR — BUILDING_ACCELERATION — score 6.034/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- VTHO-EUR — ACTIVE_NOW — score mémoire 7.921/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- LDO-EUR — ACTIVE_NOW — score mémoire 7.868/10 — sources V4 — WATCH_ONLY
- NEO-EUR — MEMORY_24H — score mémoire 7.738/10 — sources V4 — MEMORY_ONLY
- NEAR-EUR — ACTIVE_NOW — score mémoire 7.687/10 — sources DECISION_LAYER, V4 — WATCH_ONLY
- ETHFI-EUR — ACTIVE_NOW — score mémoire 7.652/10 — sources V4 — WATCH_ONLY
- SOMI-EUR — ACTIVE_NOW — score mémoire 7.633/10 — sources V4 — WATCH_ONLY
- AERO-EUR — MEMORY_24H — score mémoire 7.630/10 — sources V4 — MEMORY_ONLY
- VET-EUR — ACTIVE_NOW — score mémoire 7.619/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- PHA-EUR — ACTIVE_NOW — score mémoire 7.612/10 — sources V4 — WATCH_ONLY
- ZIL-EUR — ACTIVE_NOW — score mémoire 7.586/10 — sources DECISION_LAYER, V4 — WATCH_ONLY

## Audit des plus fortes hausses

- CAP-EUR +44.08% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- CPOOL-EUR +41.05% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- QKC-EUR +30.07% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- FIL-EUR +18.06% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- CNPY-EUR +17.18% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- T-EUR +16.50% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- REZ-EUR +14.27% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- MIOTA-EUR +11.57% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- NPC-EUR +10.59% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ZRC-EUR +8.85% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
