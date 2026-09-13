# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-13T19:05:37.076612+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : VTHO-EUR | action PLACE_LIMITE_PASSIVE | opportunité 7.554 | entrée 6.300 | trend 9.200 | rang 6.680
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : aucun candidat matériel
- **MEILLEUR_PULLBACK_REENTRY** : FET-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 7.588 | entrée 7.200 | trend 7.650 | rang 7.205
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. FET-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.205
2. USELESS-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.188
3. VTHO-EUR — MEILLEURE_LIMITE_PASSIVE — PLACE_LIMITE_PASSIVE — rank 6.680

## Accélération indépendante

- REZ-EUR — BUILDING_ACCELERATION — score 4.752/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- VET-EUR — ACTIVE_NOW — score mémoire 8.133/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- CAKE-EUR — ACTIVE_NOW — score mémoire 7.920/10 — sources V4 — WATCH_ONLY
- ETHFI-EUR — ACTIVE_NOW — score mémoire 7.911/10 — sources V4 — WATCH_ONLY
- PORTAL-EUR — MEMORY_24H — score mémoire 7.868/10 — sources V4 — MEMORY_ONLY
- PROM-EUR — ACTIVE_NOW — score mémoire 7.835/10 — sources V4 — WATCH_ONLY
- LDO-EUR — ACTIVE_NOW — score mémoire 7.787/10 — sources V4 — WATCH_ONLY
- W-EUR — ACTIVE_NOW — score mémoire 7.777/10 — sources V4 — WATCH_ONLY
- ICP-EUR — ACTIVE_NOW — score mémoire 7.752/10 — sources V4 — WATCH_ONLY
- QKC-EUR — MEMORY_24H — score mémoire 7.588/10 — sources V4 — MEMORY_ONLY
- SYRUP-EUR — ACTIVE_NOW — score mémoire 7.569/10 — sources V4 — WATCH_ONLY

## Audit des plus fortes hausses

- LSK-EUR +262.34% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- CVC-EUR +55.07% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- REZ-EUR +24.08% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- FIL-EUR +23.75% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- VTHO-EUR +21.60% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- ZIL-EUR +19.88% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ARK-EUR +17.28% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- POWR-EUR +13.61% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- XTZ-EUR +13.30% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- STRAX-EUR +12.64% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
