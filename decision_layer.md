# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-13T16:53:09.850639+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : aucun candidat matériel
- **MEILLEUR_LATENT_ACCELERATOR** : aucun candidat matériel
- **MEILLEUR_PULLBACK_REENTRY** : USELESS-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 7.753 | entrée 6.200 | trend 8.100 | rang 7.072
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. USELESS-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.072
2. VTHO-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 6.728

## Accélération indépendante

- REZ-EUR — BUILDING_ACCELERATION — score 5.523/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- AIOZ-EUR — ACTIVE_NOW — score mémoire 8.153/10 — sources V4 — WATCH_ONLY
- ICP-EUR — ACTIVE_NOW — score mémoire 7.921/10 — sources V4 — WATCH_ONLY
- AERO-EUR — ACTIVE_NOW — score mémoire 7.909/10 — sources V4 — WATCH_ONLY
- PORTAL-EUR — MEMORY_24H — score mémoire 7.868/10 — sources V4 — MEMORY_ONLY
- LIGHTER-EUR — ACTIVE_NOW — score mémoire 7.838/10 — sources V4 — WATCH_ONLY
- ETHFI-EUR — ACTIVE_NOW — score mémoire 7.819/10 — sources V4 — WATCH_ONLY
- VET-EUR — ACTIVE_NOW — score mémoire 7.709/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- LDO-EUR — ACTIVE_NOW — score mémoire 7.695/10 — sources V4 — WATCH_ONLY
- RED-EUR — MEMORY_24H — score mémoire 7.652/10 — sources V4 — MEMORY_ONLY
- XVG-EUR — ACTIVE_NOW — score mémoire 7.635/10 — sources V4 — WATCH_ONLY

## Audit des plus fortes hausses

- LSK-EUR +313.63% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- CVC-EUR +52.48% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- VTHO-EUR +25.68% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- FIL-EUR +20.57% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ARK-EUR +19.05% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- REZ-EUR +18.00% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- XTZ-EUR +15.01% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- BAT-EUR +13.12% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- STRAX-EUR +12.51% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- SCR-EUR +11.36% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
