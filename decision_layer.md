# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-23T23:42:56.229397+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : LTC-EUR | action ACHETE_MAINTENANT | opportunité 8.313 | entrée 7.350 | trend 9.000 | rang 8.076
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : TREE-EUR | action PLACE_LIMITE_PASSIVE | opportunité 7.552 | entrée 6.000 | trend 7.950 | rang 7.248
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : LIGHTER-EUR | action LATENT_ACCELERATOR | opportunité 7.989 | entrée 5.400 | trend 8.650 | rang 7.647
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : EDEN-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.714 | entrée 5.900 | trend 8.100 | rang 7.685
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. LTC-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.076
2. EDEN-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.685
3. LIGHTER-EUR — MEILLEUR_LATENT_ACCELERATOR — LATENT_ACCELERATOR — rank 7.647

## Accélération indépendante

- LSK-EUR — CONFIRMED_ACCELERATION — score 7.867/10 — DETECTED_BUT_TOO_LATE
- ACX-EUR — BUILDING_ACCELERATION — score 4.927/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- AVA-EUR — BUILDING_ACCELERATION — score 4.828/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- AMP-EUR — MEMORY_24H — score mémoire 10.000/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- TREAD-EUR — MEMORY_24H — score mémoire 9.545/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- U-EUR — MEMORY_24H — score mémoire 9.175/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- NIL-EUR — MEMORY_24H — score mémoire 8.883/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- ZRC-EUR — MEMORY_24H — score mémoire 8.129/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- WIN-EUR — MEMORY_24H — score mémoire 8.088/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- LTC-EUR — ACTIVE_NOW — score mémoire 8.076/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- ZBCN-EUR — MEMORY_24H — score mémoire 8.056/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- LSK-EUR — ACTIVE_NOW — score mémoire 7.867/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- FIL-EUR — ACTIVE_NOW — score mémoire 7.814/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY

## Audit des plus fortes hausses

- NIL-EUR +53.12% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- CPOOL-EUR +25.83% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- DBR-EUR +21.21% — NOT_DETECTED — couche SCANNER_COVERAGE — action NOT_APPLICABLE
- SAGA-EUR +21.15% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- LSK-EUR +15.19% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- CAP-EUR +13.58% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- NOM-EUR +12.75% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- SUPER-EUR +10.08% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- RAY-EUR +9.96% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- SOSO-EUR +9.11% — NOT_DETECTED — couche SCANNER_COVERAGE — action NOT_APPLICABLE

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
