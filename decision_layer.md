# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-18T17:11:29.527921+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : TAO-EUR | action PLACE_LIMITE_PASSIVE | opportunité 8.483 | entrée 6.200 | trend 7.650 | rang 7.513
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : aucun candidat matériel
- **MEILLEUR_PULLBACK_REENTRY** : NPC-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.974 | entrée 7.050 | trend 7.750 | rang 7.673
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. NPC-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.673
2. TAO-EUR — MEILLEURE_LIMITE_PASSIVE — PLACE_LIMITE_PASSIVE — rank 7.513
3. ICP-EUR — MEILLEURE_LIMITE_PASSIVE — PLACE_LIMITE_PASSIVE — rank 7.495

## Accélération indépendante

Aucune accélération indépendante confirmée ou en construction.

## Watchlist persistante 24–72 h

- CNPY-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- VTHO-EUR — ACTIVE_NOW — score mémoire 8.146/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- YB-EUR — ACTIVE_NOW — score mémoire 8.124/10 — sources V4 — WATCH_ONLY
- KAS-EUR — ACTIVE_NOW — score mémoire 7.952/10 — sources DECISION_LAYER, V4 — WATCH_ONLY
- XVG-EUR — ACTIVE_NOW — score mémoire 7.828/10 — sources V4 — WATCH_ONLY
- LDO-EUR — ACTIVE_NOW — score mémoire 7.808/10 — sources V4 — WATCH_ONLY
- AERO-EUR — ACTIVE_NOW — score mémoire 7.769/10 — sources V4 — WATCH_ONLY
- NPC-EUR — ACTIVE_NOW — score mémoire 7.673/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- SOMI-EUR — ACTIVE_NOW — score mémoire 7.669/10 — sources V4 — DETECTED_BUT_TOO_LATE
- ENA-EUR — MEMORY_24H — score mémoire 7.668/10 — sources ACCELERATION, V4 — MEMORY_ONLY

## Audit des plus fortes hausses

- G-EUR +91.34% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- F-EUR +55.58% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- CNPY-EUR +50.77% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- SAGA-EUR +37.85% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- C-EUR +32.93% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- STRK-EUR +30.12% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ARB-EUR +23.84% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- NEAR-EUR +21.61% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- DRIFT-EUR +18.27% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ZIG-EUR +17.70% — DETECTED_EARLY — couche NONE — action INTERPRETATION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
