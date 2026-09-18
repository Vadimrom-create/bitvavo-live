# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-18T17:54:08.125870+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : WLD-EUR | action PLACE_LIMITE_PASSIVE | opportunité 7.490 | entrée 6.750 | trend 8.150 | rang 7.294
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : aucun candidat matériel
- **MEILLEUR_PULLBACK_REENTRY** : NPC-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.490 | entrée 6.300 | trend 7.750 | rang 7.505
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. NPC-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.505
2. WLD-EUR — MEILLEURE_LIMITE_PASSIVE — PLACE_LIMITE_PASSIVE — rank 7.294
3. TAO-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.205

## Accélération indépendante

- USELESS-EUR — CONFIRMED_ACCELERATION — score 9.581/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- USELESS-EUR — ACTIVE_NOW — score mémoire 9.581/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- CNPY-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- LDO-EUR — ACTIVE_NOW — score mémoire 8.466/10 — sources V4 — WATCH_ONLY
- AIOZ-EUR — ACTIVE_NOW — score mémoire 8.298/10 — sources V4 — DETECTED_BUT_TOO_LATE
- PHA-EUR — ACTIVE_NOW — score mémoire 8.211/10 — sources DECISION_LAYER, V4 — WATCH_ONLY
- ATOM-EUR — ACTIVE_NOW — score mémoire 8.098/10 — sources V4 — WATCH_ONLY
- METIS-EUR — ACTIVE_NOW — score mémoire 8.009/10 — sources V4 — WATCH_ONLY
- YB-EUR — ACTIVE_NOW — score mémoire 7.975/10 — sources V4 — WATCH_ONLY
- VTHO-EUR — ACTIVE_NOW — score mémoire 7.958/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- PORTAL-EUR — ACTIVE_NOW — score mémoire 7.899/10 — sources V4 — WATCH_ONLY

## Audit des plus fortes hausses

- G-EUR +89.29% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- F-EUR +47.83% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- CNPY-EUR +43.82% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- STRK-EUR +33.09% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- C-EUR +27.97% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- NEAR-EUR +24.35% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- SAGA-EUR +23.72% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ARB-EUR +22.18% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- APT-EUR +20.24% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- S-EUR +19.72% — DETECTED_EARLY — couche NONE — action INTERPRETATION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
