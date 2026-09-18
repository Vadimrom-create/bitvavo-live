# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-18T17:40:57.074090+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : WLD-EUR | action PLACE_LIMITE_PASSIVE | opportunité 7.489 | entrée 6.300 | trend 8.150 | rang 7.189
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : aucun candidat matériel
- **MEILLEUR_PULLBACK_REENTRY** : USELESS-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 7.831 | entrée 7.050 | trend 8.100 | rang 7.211
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. USELESS-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.211
2. WLD-EUR — MEILLEURE_LIMITE_PASSIVE — PLACE_LIMITE_PASSIVE — rank 7.189
3. FET-EUR — MEILLEURE_LIMITE_PASSIVE — PLACE_LIMITE_PASSIVE — rank 6.956

## Accélération indépendante

Aucune accélération indépendante confirmée ou en construction.

## Watchlist persistante 24–72 h

- CNPY-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- LDO-EUR — ACTIVE_NOW — score mémoire 8.337/10 — sources V4 — WATCH_ONLY
- METIS-EUR — ACTIVE_NOW — score mémoire 8.081/10 — sources V4 — WATCH_ONLY
- CATI-EUR — ACTIVE_NOW — score mémoire 8.004/10 — sources V4 — WATCH_ONLY
- YB-EUR — ACTIVE_NOW — score mémoire 7.998/10 — sources V4 — WATCH_ONLY
- VTHO-EUR — ACTIVE_NOW — score mémoire 7.952/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- VET-EUR — ACTIVE_NOW — score mémoire 7.776/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- NPC-EUR — MEMORY_24H — score mémoire 7.759/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- XVG-EUR — ACTIVE_NOW — score mémoire 7.756/10 — sources V4 — WATCH_ONLY
- AIOZ-EUR — ACTIVE_NOW — score mémoire 7.679/10 — sources V4 — WATCH_ONLY

## Audit des plus fortes hausses

- G-EUR +80.00% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- F-EUR +53.18% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- CNPY-EUR +48.00% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- STRK-EUR +33.10% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- SAGA-EUR +29.86% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- C-EUR +28.08% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- NEAR-EUR +25.87% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- A-EUR +23.23% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ARB-EUR +23.22% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- APT-EUR +18.94% — DETECTED_EARLY — couche NONE — action INTERPRETATION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
