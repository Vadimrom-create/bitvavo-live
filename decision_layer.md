# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-16T05:07:24.877093+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : aucun candidat matériel
- **MEILLEUR_LATENT_ACCELERATOR** : aucun candidat matériel
- **MEILLEUR_PULLBACK_REENTRY** : VTHO-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.205 | entrée 5.500 | trend 9.200 | rang 7.815
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. VTHO-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.815
2. USELESS-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.404

## Accélération indépendante

- LSK-EUR — CONFIRMED_ACCELERATION — score 9.125/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- LSK-EUR — ACTIVE_NOW — score mémoire 9.125/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- VET-EUR — ACTIVE_NOW — score mémoire 8.499/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- LDO-EUR — ACTIVE_NOW — score mémoire 8.434/10 — sources V4 — WATCH_ONLY
- ICP-EUR — ACTIVE_NOW — score mémoire 8.058/10 — sources V4 — WATCH_ONLY
- INJ-EUR — ACTIVE_NOW — score mémoire 7.918/10 — sources DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- VTHO-EUR — ACTIVE_NOW — score mémoire 7.815/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- BNB-EUR — ACTIVE_NOW — score mémoire 7.774/10 — sources V4 — WATCH_ONLY
- XVG-EUR — ACTIVE_NOW — score mémoire 7.745/10 — sources V4 — WATCH_ONLY
- AERO-EUR — ACTIVE_NOW — score mémoire 7.741/10 — sources V4 — WATCH_ONLY
- NPC-EUR — ACTIVE_NOW — score mémoire 7.736/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY

## Audit des plus fortes hausses

- LSK-EUR +43.52% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- SYN-EUR +32.12% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- CNPY-EUR +22.35% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- ARB-EUR +15.53% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ALIGN-EUR +13.34% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- FOLD-EUR +13.27% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- LAPTOP-EUR +11.25% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- USELESS-EUR +11.18% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- G-EUR +9.78% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- GLMR-EUR +9.28% — DETECTED_EARLY — couche NONE — action INTERPRETATION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
