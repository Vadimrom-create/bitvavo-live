# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-18T22:03:40.890110+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : aucun candidat matériel
- **MEILLEUR_LATENT_ACCELERATOR** : aucun candidat matériel
- **MEILLEUR_PULLBACK_REENTRY** : DOT-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.221 | entrée 6.350 | trend 8.300 | rang 7.455
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. DOT-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.455
2. NEAR-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 6.107

## Accélération indépendante

Aucune accélération indépendante confirmée ou en construction.

## Watchlist persistante 24–72 h

- VET-EUR — ACTIVE_NOW — score mémoire 8.122/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- ATOM-EUR — ACTIVE_NOW — score mémoire 8.044/10 — sources V4 — DETECTED_BUT_TOO_LATE
- YB-EUR — ACTIVE_NOW — score mémoire 7.964/10 — sources V4 — WATCH_ONLY
- VTHO-EUR — ACTIVE_NOW — score mémoire 7.934/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- METIS-EUR — ACTIVE_NOW — score mémoire 7.895/10 — sources V4 — WATCH_ONLY
- ICP-EUR — ACTIVE_NOW — score mémoire 7.822/10 — sources DECISION_LAYER, V4 — WATCH_ONLY
- ORCA-EUR — MEMORY_24H — score mémoire 7.810/10 — sources V4 — MEMORY_ONLY
- XVG-EUR — ACTIVE_NOW — score mémoire 7.733/10 — sources V4 — WATCH_ONLY
- LDO-EUR — ACTIVE_NOW — score mémoire 7.721/10 — sources V4 — WATCH_ONLY
- PEAQ-EUR — ACTIVE_NOW — score mémoire 7.683/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY

## Audit des plus fortes hausses

- F-EUR +57.47% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- STRK-EUR +52.54% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- G-EUR +40.23% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- ARB-EUR +28.06% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- NEAR-EUR +24.35% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- APT-EUR +24.33% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ZAMA-EUR +23.44% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ZIG-EUR +21.67% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- CHIP-EUR +21.46% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- AIOZ-EUR +20.58% — DETECTED_EARLY — couche NONE — action INTERPRETATION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
