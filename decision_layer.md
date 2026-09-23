# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-23T11:36:44.771868+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : LTC-EUR | action PLACE_LIMITE_PASSIVE | opportunité 7.896 | entrée 6.050 | trend 9.000 | rang 7.838
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : ARX-EUR | action LATENT_ACCELERATOR | opportunité 8.324 | entrée 4.900 | trend 8.550 | rang 7.675
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : ICP-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.261 | entrée 7.000 | trend 8.200 | rang 7.731
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. LTC-EUR — MEILLEURE_LIMITE_PASSIVE — PLACE_LIMITE_PASSIVE — rank 7.838
2. ICP-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.731
3. API3-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.716

## Accélération indépendante

- MAVIA-EUR — BUILDING_ACCELERATION — score 5.039/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- TRIA-EUR — MEMORY_24H — score mémoire 9.219/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- ZRC-EUR — MEMORY_24H — score mémoire 9.216/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- WIN-EUR — MEMORY_24H — score mémoire 8.088/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- LINK-EUR — MEMORY_24H — score mémoire 8.056/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- PORTAL-EUR — MEMORY_24H — score mémoire 7.969/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- PHA-EUR — MEMORY_24H — score mémoire 7.915/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- SAFE-EUR — ACTIVE_NOW — score mémoire 7.862/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- LTC-EUR — ACTIVE_NOW — score mémoire 7.838/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- TURBO-EUR — MEMORY_24H — score mémoire 7.783/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- BICO-EUR — ACTIVE_NOW — score mémoire 7.763/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY

## Audit des plus fortes hausses

- CPOOL-EUR +39.03% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- MET-EUR +38.92% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- BCH-EUR +30.04% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- ALLO-EUR +27.60% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ZRO-EUR +25.22% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- NIL-EUR +25.02% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- CHR-EUR +24.57% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- SUPER-EUR +20.37% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- SAGA-EUR +20.06% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- SENT-EUR +19.59% — DETECTED_EARLY — couche NONE — action INTERPRETATION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
