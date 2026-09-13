# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-13T17:54:59.517558+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : aucun candidat matériel
- **MEILLEUR_LATENT_ACCELERATOR** : aucun candidat matériel
- **MEILLEUR_PULLBACK_REENTRY** : USELESS-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.403 | entrée 7.250 | trend 8.100 | rang 7.492
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. USELESS-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.492

## Accélération indépendante

- LAPTOP-EUR — BUILDING_ACCELERATION — score 4.894/10 — REQUIRES_V4_ENTRY_AND_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- KAS-EUR — ACTIVE_NOW — score mémoire 8.434/10 — sources V4 — WATCH_ONLY
- NEAR-EUR — ACTIVE_NOW — score mémoire 7.981/10 — sources DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- LDO-EUR — ACTIVE_NOW — score mémoire 7.963/10 — sources V4 — WATCH_ONLY
- ICP-EUR — ACTIVE_NOW — score mémoire 7.950/10 — sources V4 — WATCH_ONLY
- FET-EUR — ACTIVE_NOW — score mémoire 7.934/10 — sources DECISION_LAYER, V4 — WATCH_ONLY
- PORTAL-EUR — MEMORY_24H — score mémoire 7.868/10 — sources V4 — MEMORY_ONLY
- UNI-EUR — ACTIVE_NOW — score mémoire 7.829/10 — sources V4 — WATCH_ONLY
- ETHFI-EUR — ACTIVE_NOW — score mémoire 7.817/10 — sources V4 — WATCH_ONLY
- WLD-EUR — ACTIVE_NOW — score mémoire 7.754/10 — sources V4 — WATCH_ONLY
- VET-EUR — ACTIVE_NOW — score mémoire 7.738/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY

## Audit des plus fortes hausses

- LSK-EUR +284.02% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- CVC-EUR +57.79% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- REZ-EUR +26.26% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- VTHO-EUR +25.29% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- FIL-EUR +19.91% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ARK-EUR +16.85% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- XTZ-EUR +14.45% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- BAT-EUR +11.64% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ZIL-EUR +11.45% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE
- STRAX-EUR +10.67% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
