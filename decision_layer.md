# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-17T19:18:40.014837+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : aucun candidat matériel
- **MEILLEUR_LATENT_ACCELERATOR** : aucun candidat matériel
- **MEILLEUR_PULLBACK_REENTRY** : VVV-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 9.032 | entrée 7.150 | trend 7.600 | rang 7.582
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. VVV-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.582
2. LSK-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.138

## Accélération indépendante

- AVA-EUR — BUILDING_ACCELERATION — score 4.824/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- CNPY-EUR — MEMORY_24H — score mémoire 9.527/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- ARB-EUR — MEMORY_24H — score mémoire 8.911/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- VTHO-EUR — ACTIVE_NOW — score mémoire 8.037/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- PROM-EUR — ACTIVE_NOW — score mémoire 7.900/10 — sources V4 — WATCH_ONLY
- ICP-EUR — ACTIVE_NOW — score mémoire 7.895/10 — sources V4 — WATCH_ONLY
- LDO-EUR — ACTIVE_NOW — score mémoire 7.890/10 — sources V4 — WATCH_ONLY
- ETHFI-EUR — ACTIVE_NOW — score mémoire 7.871/10 — sources V4 — WATCH_ONLY
- FORM-EUR — ACTIVE_NOW — score mémoire 7.834/10 — sources V4 — WATCH_ONLY
- VET-EUR — ACTIVE_NOW — score mémoire 7.786/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- INJ-EUR — ACTIVE_NOW — score mémoire 7.738/10 — sources DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE

## Audit des plus fortes hausses

- AVA-EUR +90.47% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- TREAD-EUR +37.40% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- CROSS-EUR +26.37% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- COTI-EUR +23.89% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- KSM-EUR +23.76% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- AGI-EUR +23.54% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- FOLD-EUR +20.80% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- UNI-EUR +20.09% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- PEAQ-EUR +18.10% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- GALA-EUR +17.54% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
