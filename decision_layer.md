# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-13T16:38:10.788129+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : aucun candidat matériel
- **MEILLEUR_LATENT_ACCELERATOR** : aucun candidat matériel
- **MEILLEUR_PULLBACK_REENTRY** : USELESS-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 7.468 | entrée 6.600 | trend 8.100 | rang 7.055
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. USELESS-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.055
2. VTHO-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 6.950

## Accélération indépendante

- ARK-EUR — BUILDING_ACCELERATION — score 5.617/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- REZ-EUR — MEMORY_24H — score mémoire 9.305/10 — sources ACCELERATION — MEMORY_ONLY
- ICP-EUR — ACTIVE_NOW — score mémoire 8.526/10 — sources V4 — WATCH_ONLY
- LSK-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION — MEMORY_ONLY
- PORTAL-EUR — MEMORY_24H — score mémoire 7.868/10 — sources V4 — MEMORY_ONLY
- ETHFI-EUR — MEMORY_24H — score mémoire 7.778/10 — sources V4 — MEMORY_ONLY
- AIOZ-EUR — ACTIVE_NOW — score mémoire 7.763/10 — sources V4 — WATCH_ONLY
- LDO-EUR — ACTIVE_NOW — score mémoire 7.717/10 — sources V4 — WATCH_ONLY
- XVG-EUR — ACTIVE_NOW — score mémoire 7.709/10 — sources V4 — WATCH_ONLY
- PEAQ-EUR — ACTIVE_NOW — score mémoire 7.692/10 — sources V4 — DETECTED_BUT_TOO_LATE
- DOT-EUR — ACTIVE_NOW — score mémoire 7.661/10 — sources V4 — WATCH_ONLY

## Audit des plus fortes hausses

- LSK-EUR +337.23% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- CVC-EUR +61.36% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- VTHO-EUR +23.80% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- ARK-EUR +21.68% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- REZ-EUR +20.48% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- FIL-EUR +19.60% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- STRAX-EUR +18.45% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- BAT-EUR +14.14% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- XTZ-EUR +13.04% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- SCR-EUR +11.98% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
