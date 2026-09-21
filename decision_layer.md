# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-21T19:06:25.941427+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : TAO-EUR | action ACHETE_MAINTENANT | opportunité 8.405 | entrée 6.800 | trend 8.750 | rang 7.962
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : ATH-EUR | action PLACE_LIMITE_PASSIVE | opportunité 9.220 | entrée 6.050 | trend 8.150 | rang 8.019
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : WAL-EUR | action LATENT_ACCELERATOR | opportunité 7.720 | entrée 5.750 | trend 9.200 | rang 7.762
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : MERL-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.224 | entrée 5.900 | trend 8.950 | rang 7.883
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. ATH-EUR — MEILLEURE_LIMITE_PASSIVE — PLACE_LIMITE_PASSIVE — rank 8.019
2. TAO-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 7.962
3. MERL-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.883

## Accélération indépendante

- SYN-EUR — CONFIRMED_ACCELERATION — score 7.501/10 — DETECTED_BUT_TOO_LATE
- PROM-EUR — BUILDING_ACCELERATION — score 6.076/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- ZIG-EUR — BUILDING_ACCELERATION — score 5.612/10 — DETECTED_BUT_TOO_LATE
- PROVE-EUR — BUILDING_ACCELERATION — score 5.547/10 — DETECTED_BUT_TOO_LATE
- CPOOL-EUR — BUILDING_ACCELERATION — score 5.493/10 — DETECTED_BUT_TOO_LATE
- EPIC-EUR — BUILDING_ACCELERATION — score 5.345/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- SWEAT-EUR — BUILDING_ACCELERATION — score 5.286/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- PONKE-EUR — BUILDING_ACCELERATION — score 5.197/10 — DETECTED_BUT_TOO_LATE
- ALIGN-EUR — BUILDING_ACCELERATION — score 5.030/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- U-EUR — BUILDING_ACCELERATION — score 4.860/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- TAO-EUR — ACTIVE_NOW — score mémoire 7.962/10 — sources ACCELERATION, DECISION_LAYER, V4 — BUYABLE_NOW
- RON-EUR — MEMORY_24H — score mémoire 9.938/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- THQ-EUR — MEMORY_24H — score mémoire 9.062/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- ACU-EUR — MEMORY_24H — score mémoire 9.053/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- LUMIA-EUR — MEMORY_24H — score mémoire 8.655/10 — sources ACCELERATION — MEMORY_ONLY
- TRAC-EUR — MEMORY_24H — score mémoire 8.588/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- FTT-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- PUFFER-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- SFP-EUR — MEMORY_24H — score mémoire 8.323/10 — sources ACCELERATION — MEMORY_ONLY
- ZKJ-EUR — MEMORY_24H — score mémoire 8.224/10 — sources ACCELERATION, V4 — MEMORY_ONLY

## Audit des plus fortes hausses

- ZRC-EUR +110.08% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ICX-EUR +58.96% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- ZETA-EUR +58.46% — NOT_DETECTED — couche SCANNER_COVERAGE — action NOT_APPLICABLE
- FORM-EUR +40.99% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- PHA-EUR +38.59% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- PTB-EUR +31.20% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- SWELL-EUR +27.05% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- AIOZ-EUR +25.08% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- PEPE-EUR +23.93% — DETECTED_EARLY — couche NONE — action NONE
- SYN-EUR +23.34% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
