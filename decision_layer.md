# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-23T16:17:32.674036+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : NEWT-EUR | action PLACE_LIMITE_PASSIVE | opportunité 8.755 | entrée 6.000 | trend 8.150 | rang 7.615
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : API3-EUR | action LATENT_ACCELERATOR | opportunité 9.170 | entrée 5.300 | trend 8.150 | rang 8.028
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : WAL-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 7.882 | entrée 5.800 | trend 8.900 | rang 7.688
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. API3-EUR — MEILLEUR_LATENT_ACCELERATOR — LATENT_ACCELERATOR — rank 8.028
2. BEAM-EUR — MEILLEUR_LATENT_ACCELERATOR — LATENT_ACCELERATOR — rank 7.774
3. WAL-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.688

## Accélération indépendante

- SWELL-EUR — CONFIRMED_ACCELERATION — score 8.702/10 — DETECTED_BUT_TOO_LATE
- NOS-EUR — CONFIRMED_ACCELERATION — score 7.760/10 — DETECTED_BUT_TOO_LATE
- BCH-EUR — CONFIRMED_ACCELERATION — score 7.691/10 — DETECTED_BUT_TOO_LATE
- USELESS-EUR — CONFIRMED_ACCELERATION — score 7.674/10 — DETECTED_BUT_TOO_LATE
- CELR-EUR — CONFIRMED_ACCELERATION — score 6.676/10 — DETECTED_BUT_TOO_LATE
- CFG-EUR — CONFIRMED_ACCELERATION — score 6.634/10 — DETECTED_BUT_TOO_LATE
- KITE-EUR — CONFIRMED_ACCELERATION — score 6.515/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- ICX-EUR — BUILDING_ACCELERATION — score 6.487/10 — DETECTED_BUT_TOO_LATE
- CPOOL-EUR — BUILDING_ACCELERATION — score 6.400/10 — DETECTED_BUT_TOO_LATE
- ZRO-EUR — BUILDING_ACCELERATION — score 6.134/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- TRIA-EUR — MEMORY_24H — score mémoire 9.219/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- U-EUR — MEMORY_24H — score mémoire 9.175/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- SWELL-EUR — ACTIVE_NOW — score mémoire 8.702/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- WIN-EUR — MEMORY_24H — score mémoire 8.088/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- LINK-EUR — MEMORY_24H — score mémoire 8.056/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- API3-EUR — ACTIVE_NOW — score mémoire 8.028/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- PORTAL-EUR — MEMORY_24H — score mémoire 7.969/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- XRP-EUR — MEMORY_24H — score mémoire 7.855/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- BEAM-EUR — ACTIVE_NOW — score mémoire 7.774/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- NOS-EUR — ACTIVE_NOW — score mémoire 7.760/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE

## Audit des plus fortes hausses

- CPOOL-EUR +36.63% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- SAGA-EUR +33.56% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- MET-EUR +22.07% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- PROM-EUR +18.88% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- DBR-EUR +18.33% — NOT_DETECTED — couche SCANNER_COVERAGE — action NOT_APPLICABLE
- RAY-EUR +16.10% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- ZRO-EUR +16.06% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- SUPER-EUR +15.71% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- ALLO-EUR +15.16% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- NIL-EUR +14.49% — DETECTED_EARLY — couche NONE — action INTERPRETATION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
