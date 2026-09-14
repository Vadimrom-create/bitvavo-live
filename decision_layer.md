# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-14T14:37:48.155341+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : aucun candidat matériel
- **MEILLEUR_LATENT_ACCELERATOR** : aucun candidat matériel
- **MEILLEUR_PULLBACK_REENTRY** : VTHO-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 7.725 | entrée 5.350 | trend 9.200 | rang 7.747
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. VTHO-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.747
2. USELESS-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 6.965
3. NPC-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 6.247

## Accélération indépendante

- LSK-EUR — CONFIRMED_ACCELERATION — score 7.130/10 — REQUIRES_V4_ENTRY_AND_EXECUTION_VALIDATION
- CPOOL-EUR — CONFIRMED_ACCELERATION — score 6.561/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- ZIL-EUR — ACTIVE_NOW — score mémoire 8.096/10 — sources DECISION_LAYER, V4 — WATCH_ONLY
- XVG-EUR — ACTIVE_NOW — score mémoire 7.926/10 — sources V4 — WATCH_ONLY
- VET-EUR — ACTIVE_NOW — score mémoire 7.910/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- ETHFI-EUR — ACTIVE_NOW — score mémoire 7.904/10 — sources V4 — WATCH_ONLY
- LDO-EUR — ACTIVE_NOW — score mémoire 7.886/10 — sources V4 — WATCH_ONLY
- PROM-EUR — ACTIVE_NOW — score mémoire 7.860/10 — sources V4 — WATCH_ONLY
- SOMI-EUR — ACTIVE_NOW — score mémoire 7.839/10 — sources V4 — WATCH_ONLY
- VTHO-EUR — ACTIVE_NOW — score mémoire 7.747/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- NEO-EUR — MEMORY_24H — score mémoire 7.738/10 — sources V4 — MEMORY_ONLY
- AERO-EUR — ACTIVE_NOW — score mémoire 7.691/10 — sources V4 — WATCH_ONLY

## Audit des plus fortes hausses

- CAP-EUR +48.99% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- CPOOL-EUR +41.44% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- T-EUR +21.62% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- REZ-EUR +19.01% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- NPC-EUR +17.07% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- CNPY-EUR +16.17% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- ARK-EUR +14.18% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- FIL-EUR +12.57% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- RED-EUR +11.55% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ZRC-EUR +9.57% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
