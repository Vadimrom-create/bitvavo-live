# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-17T21:26:12.212228+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : aucun candidat matériel
- **MEILLEUR_LATENT_ACCELERATOR** : aucun candidat matériel
- **MEILLEUR_PULLBACK_REENTRY** : FET-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 7.294 | entrée 6.350 | trend 7.650 | rang 7.018
  - Trend remains strong; candidate retained for re-entry instead of discarded.

## Top cross-sectionnel

1. FET-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.018

## Accélération indépendante

- CROSS-EUR — CONFIRMED_ACCELERATION — score 6.864/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- CNPY-EUR — MEMORY_24H — score mémoire 9.527/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- VTHO-EUR — ACTIVE_NOW — score mémoire 8.185/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- ETHFI-EUR — ACTIVE_NOW — score mémoire 8.038/10 — sources V4 — WATCH_ONLY
- LDO-EUR — ACTIVE_NOW — score mémoire 8.021/10 — sources V4 — WATCH_ONLY
- XPL-EUR — ACTIVE_NOW — score mémoire 7.949/10 — sources V4 — WATCH_ONLY
- METIS-EUR — ACTIVE_NOW — score mémoire 7.829/10 — sources V4 — WATCH_ONLY
- VET-EUR — ACTIVE_NOW — score mémoire 7.810/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- ICP-EUR — ACTIVE_NOW — score mémoire 7.722/10 — sources V4 — WATCH_ONLY
- XVG-EUR — ACTIVE_NOW — score mémoire 7.615/10 — sources V4 — WATCH_ONLY
- FORM-EUR — ACTIVE_NOW — score mémoire 7.598/10 — sources V4 — WATCH_ONLY

## Audit des plus fortes hausses

- AVA-EUR +82.27% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- CROSS-EUR +43.21% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- CNPY-EUR +38.20% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- COTI-EUR +35.64% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- TREAD-EUR +31.97% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- AGI-EUR +27.17% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- G-EUR +20.69% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- DRIFT-EUR +20.40% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- PEAQ-EUR +20.10% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- UNI-EUR +19.02% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
