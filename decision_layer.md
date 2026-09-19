# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-19T01:57:35.477341+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : FET-EUR | action PLACE_LIMITE_PASSIVE | opportunité 7.409 | entrée 6.500 | trend 7.850 | rang 7.254
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : aucun candidat matériel
- **MEILLEUR_PULLBACK_REENTRY** : HYPE-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 7.810 | entrée 7.200 | trend 8.250 | rang 7.599
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. HYPE-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.599
2. FET-EUR — MEILLEURE_LIMITE_PASSIVE — PLACE_LIMITE_PASSIVE — rank 7.254
3. SOL-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.214

## Accélération indépendante

- NEAR-EUR — BUILDING_ACCELERATION — score 5.034/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- SYN-EUR — MEMORY_24H — score mémoire 8.311/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- VTHO-EUR — MEMORY_24H — score mémoire 8.268/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- PEPE-EUR — MEMORY_24H — score mémoire 8.255/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- YB-EUR — MEMORY_24H — score mémoire 7.953/10 — sources V4 — MEMORY_ONLY
- AAVE-EUR — ACTIVE_NOW — score mémoire 7.910/10 — sources ACCELERATION, V4 — WATCH_ONLY
- PROVE-EUR — ACTIVE_NOW — score mémoire 7.897/10 — sources V4 — WATCH_ONLY
- ENS-EUR — ACTIVE_NOW — score mémoire 7.864/10 — sources V4 — WATCH_ONLY
- PYTH-EUR — ACTIVE_NOW — score mémoire 7.836/10 — sources V4 — WATCH_ONLY
- JUP-EUR — ACTIVE_NOW — score mémoire 7.803/10 — sources V4 — DETECTED_BUT_TOO_LATE
- COW-EUR — MEMORY_24H — score mémoire 7.799/10 — sources V4 — MEMORY_ONLY

## Audit des plus fortes hausses

- G-EUR +45.67% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- STRK-EUR +42.97% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- F-EUR +35.94% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- ZAMA-EUR +27.05% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- QKC-EUR +23.99% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- SYN-EUR +22.48% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- S-EUR +20.95% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ZIG-EUR +20.63% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- SKY-EUR +20.35% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- APT-EUR +20.07% — DETECTED_EARLY — couche NONE — action INTERPRETATION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
