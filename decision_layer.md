# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-13T17:26:06.137480+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : VTHO-EUR | action PLACE_LIMITE_PASSIVE | opportunité 7.752 | entrée 6.150 | trend 9.200 | rang 6.742
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : aucun candidat matériel
- **MEILLEUR_PULLBACK_REENTRY** : USELESS-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 9.238 | entrée 7.350 | trend 8.100 | rang 7.835
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. USELESS-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.835
2. TAO-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.555
3. VTHO-EUR — MEILLEURE_LIMITE_PASSIVE — PLACE_LIMITE_PASSIVE — rank 6.742

## Accélération indépendante

- REZ-EUR — BUILDING_ACCELERATION — score 4.928/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- WLD-EUR — ACTIVE_NOW — score mémoire 8.263/10 — sources V4 — WATCH_ONLY
- ICP-EUR — ACTIVE_NOW — score mémoire 8.241/10 — sources V4 — WATCH_ONLY
- VET-EUR — ACTIVE_NOW — score mémoire 8.168/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- UNI-EUR — ACTIVE_NOW — score mémoire 8.061/10 — sources V4 — WATCH_ONLY
- KAS-EUR — ACTIVE_NOW — score mémoire 8.058/10 — sources V4 — WATCH_ONLY
- NEAR-EUR — ACTIVE_NOW — score mémoire 7.911/10 — sources DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- PORTAL-EUR — MEMORY_24H — score mémoire 7.868/10 — sources V4 — MEMORY_ONLY
- USELESS-EUR — ACTIVE_NOW — score mémoire 7.835/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- AERO-EUR — ACTIVE_NOW — score mémoire 7.783/10 — sources V4 — WATCH_ONLY
- FET-EUR — ACTIVE_NOW — score mémoire 7.776/10 — sources DECISION_LAYER, V4 — WATCH_ONLY

## Audit des plus fortes hausses

- LSK-EUR +294.17% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- CVC-EUR +48.34% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- FIL-EUR +28.88% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- VTHO-EUR +21.78% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- REZ-EUR +18.42% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ARK-EUR +17.46% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ZKJ-EUR +16.84% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- XTZ-EUR +14.71% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- STRAX-EUR +13.01% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- SCR-EUR +12.96% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
