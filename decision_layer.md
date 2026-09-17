# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-17T11:00:39.629381+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : UNI-EUR | action PLACE_LIMITE_PASSIVE | opportunité 7.418 | entrée 6.700 | trend 7.750 | rang 7.138
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : aucun candidat matériel
- **MEILLEUR_PULLBACK_REENTRY** : FET-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 7.478 | entrée 7.250 | trend 7.650 | rang 7.304
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. FET-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.304
2. TAO-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.201
3. UNI-EUR — MEILLEURE_LIMITE_PASSIVE — PLACE_LIMITE_PASSIVE — rank 7.138

## Accélération indépendante

- AVA-EUR — BUILDING_ACCELERATION — score 5.369/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- LDO-EUR — ACTIVE_NOW — score mémoire 8.611/10 — sources V4 — WATCH_ONLY
- VTHO-EUR — ACTIVE_NOW — score mémoire 8.234/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- XVG-EUR — ACTIVE_NOW — score mémoire 8.155/10 — sources V4 — WATCH_ONLY
- ICP-EUR — ACTIVE_NOW — score mémoire 7.957/10 — sources V4 — WATCH_ONLY
- YB-EUR — ACTIVE_NOW — score mémoire 7.875/10 — sources V4 — WATCH_ONLY
- SOMI-EUR — ACTIVE_NOW — score mémoire 7.871/10 — sources V4 — DETECTED_BUT_TOO_LATE
- DOT-EUR — ACTIVE_NOW — score mémoire 7.781/10 — sources DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- VET-EUR — ACTIVE_NOW — score mémoire 7.718/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- LTC-EUR — MEMORY_24H — score mémoire 7.691/10 — sources V4 — MEMORY_ONLY
- INIT-EUR — MEMORY_24H — score mémoire 7.668/10 — sources V4 — MEMORY_ONLY

## Audit des plus fortes hausses

- AVA-EUR +82.24% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- FOLD-EUR +28.01% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- QUID-EUR +19.03% — DETECTED_TOO_LATE — couche NONE — action INTERPRETATION
- EDEN-EUR +17.86% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- HNT-EUR +17.58% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- SYN-EUR +16.86% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- PEAQ-EUR +16.55% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- NEAR-EUR +16.06% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- USELESS-EUR +15.45% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- COTI-EUR +14.64% — DETECTED_EARLY — couche NONE — action INTERPRETATION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
