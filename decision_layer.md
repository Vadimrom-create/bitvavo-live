# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-13T17:09:05.441419+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : aucun candidat matériel
- **MEILLEUR_LATENT_ACCELERATOR** : aucun candidat matériel
- **MEILLEUR_PULLBACK_REENTRY** : USELESS-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.015 | entrée 6.950 | trend 8.100 | rang 7.208
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. USELESS-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.208
2. VTHO-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 6.655

## Accélération indépendante

Aucune accélération indépendante confirmée ou en construction.

## Watchlist persistante 24–72 h

- VET-EUR — ACTIVE_NOW — score mémoire 8.550/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- UNI-EUR — ACTIVE_NOW — score mémoire 8.092/10 — sources V4 — WATCH_ONLY
- ICP-EUR — ACTIVE_NOW — score mémoire 7.951/10 — sources V4 — WATCH_ONLY
- AERO-EUR — ACTIVE_NOW — score mémoire 7.874/10 — sources V4 — WATCH_ONLY
- PORTAL-EUR — MEMORY_24H — score mémoire 7.868/10 — sources V4 — MEMORY_ONLY
- KAS-EUR — ACTIVE_NOW — score mémoire 7.786/10 — sources V4 — WATCH_ONLY
- LDO-EUR — ACTIVE_NOW — score mémoire 7.729/10 — sources V4 — WATCH_ONLY
- CAKE-EUR — ACTIVE_NOW — score mémoire 7.699/10 — sources V4 — WATCH_ONLY
- AIOZ-EUR — ACTIVE_NOW — score mémoire 7.690/10 — sources V4 — WATCH_ONLY
- ETHFI-EUR — ACTIVE_NOW — score mémoire 7.657/10 — sources V4 — WATCH_ONLY

## Audit des plus fortes hausses

- LSK-EUR +300.33% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- CVC-EUR +51.80% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- FIL-EUR +26.27% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- VTHO-EUR +22.43% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- REZ-EUR +16.34% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ARK-EUR +16.09% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- STRAX-EUR +14.15% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- ZKJ-EUR +13.58% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- BAT-EUR +13.38% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- XTZ-EUR +13.29% — DETECTED_EARLY — couche NONE — action INTERPRETATION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
