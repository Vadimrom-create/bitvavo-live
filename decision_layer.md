# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-10-01T05:45:56.718900+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : ENA-EUR | action ACHETE_MAINTENANT | opportunité 8.697 | entrée 7.400 | trend 8.650 | rang 8.004
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : REZ-EUR | action PLACE_LIMITE_PASSIVE | opportunité 8.044 | entrée 6.200 | trend 8.650 | rang 7.523
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : ETHFI-EUR | action LATENT_ACCELERATOR | opportunité 7.519 | entrée 4.500 | trend 8.650 | rang 7.353
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : KSM-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 9.074 | entrée 6.450 | trend 8.950 | rang 8.281
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Tous les achats immédiats

1. ENA-EUR — ACHETE_MAINTENANT — rank 8.004 — opportunité 8.697 — entrée 7.400 — trend 8.650
2. NEAR-EUR — ACHETE_MAINTENANT — rank 7.906 — opportunité 8.853 — entrée 7.500 — trend 8.300
3. AAVE-EUR — ACHETE_MAINTENANT — rank 7.807 — opportunité 8.171 — entrée 7.000 — trend 8.700
4. ALGO-EUR — ACHETE_MAINTENANT — rank 7.736 — opportunité 8.327 — entrée 7.000 — trend 8.150
5. AERO-EUR — ACHETE_MAINTENANT — rank 7.733 — opportunité 8.784 — entrée 6.800 — trend 7.750
6. HBAR-EUR — ACHETE_MAINTENANT — rank 7.605 — opportunité 8.053 — entrée 6.900 — trend 8.150
7. TAO-EUR — ACHETE_MAINTENANT — rank 7.491 — opportunité 8.548 — entrée 7.450 — trend 7.050
8. FET-EUR — ACHETE_MAINTENANT — rank 7.424 — opportunité 8.160 — entrée 7.650 — trend 7.550
9. RENDER-EUR — ACHETE_MAINTENANT — rank 7.361 — opportunité 8.021 — entrée 7.450 — trend 7.300
10. ADA-EUR — ACHETE_MAINTENANT — rank 7.073 — opportunité 8.231 — entrée 7.350 — trend 6.350
11. ETH-EUR — ACHETE_MAINTENANT — rank 6.992 — opportunité 8.581 — entrée 7.850 — trend 5.350
12. SOL-EUR — ACHETE_MAINTENANT — rank 6.952 — opportunité 8.211 — entrée 7.600 — trend 5.800
13. BTC-EUR — ACHETE_MAINTENANT — rank 6.850 — opportunité 8.309 — entrée 7.600 — trend 5.350

## Top cross-sectionnel — aperçu non exhaustif

Ce top est une vue courte multi-buckets. Il ne doit jamais être utilisé comme liste exhaustive des achats immédiats.
1. KSM-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.281
2. CELO-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.124
3. ENA-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.004

## Accélération indépendante

- HUMA-EUR — CONFIRMED_ACCELERATION — score 6.921/10 — DETECTED_BUT_TOO_LATE
- HFT-EUR — BUILDING_ACCELERATION — score 5.935/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- NOM-EUR — BUILDING_ACCELERATION — score 5.808/10 — DETECTED_BUT_TOO_LATE
- ICX-EUR — BUILDING_ACCELERATION — score 5.544/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- INJ-EUR — BUILDING_ACCELERATION — score 5.518/10 — DETECTED_BUT_TOO_LATE
- TREAD-EUR — BUILDING_ACCELERATION — score 5.260/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- USELESS-EUR — BUILDING_ACCELERATION — score 5.202/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- CT-EUR — BUILDING_ACCELERATION — score 4.956/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- CTR-EUR — MEMORY_24H — score mémoire 8.902/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- ACU-EUR — MEMORY_24H — score mémoire 8.894/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- ARPA-EUR — MEMORY_24H — score mémoire 8.595/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- PONKE-EUR — MEMORY_24H — score mémoire 8.400/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- MOVR-EUR — MEMORY_24H — score mémoire 8.346/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- KSM-EUR — ACTIVE_NOW — score mémoire 8.281/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- CELO-EUR — ACTIVE_NOW — score mémoire 8.124/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- ENA-EUR — ACTIVE_NOW — score mémoire 8.004/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- PYTH-EUR — ACTIVE_NOW — score mémoire 7.963/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- 0G-EUR — ACTIVE_NOW — score mémoire 7.913/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY

## Audit des plus fortes hausses

- MOVR-EUR +85.89% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- CT-EUR +44.31% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- TRAC-EUR +29.12% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- GLMR-EUR +27.20% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- STX-EUR +26.64% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- MON-EUR +24.69% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- CAP-EUR +17.96% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- RED-EUR +15.02% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- PLUME-EUR +14.43% — DETECTED_EARLY — couche NONE — action NONE
- ESP-EUR +14.24% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE

## Gestion des positions détenues

Policy : STAGED_10_20_RUNNER_V1
- +10% : prise partielle 35%.
- +20% : seconde prise 35%.
- Runner conservé : 30%.
- Revue coût d'opportunité après 72 h ; sortie seulement avant la première partielle, proche/sous le PRU et avec momentum 15m affaibli.
- Pas de stop serré mécaniquement après une petite hausse ; le stop reste lié à l'invalidation structurelle.

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
