# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-30T08:58:42.608588+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : ICP-EUR | action ACHETE_MAINTENANT | opportunité 9.444 | entrée 7.850 | trend 8.900 | rang 8.655
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : WOO-EUR | action PLACE_LIMITE_PASSIVE | opportunité 9.187 | entrée 6.100 | trend 8.200 | rang 7.990
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : ETHFI-EUR | action LATENT_ACCELERATOR | opportunité 7.839 | entrée 5.250 | trend 8.650 | rang 7.590
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : COMP-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.364 | entrée 6.650 | trend 9.200 | rang 8.188
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Tous les achats immédiats

1. ICP-EUR — ACHETE_MAINTENANT — rank 8.655 — opportunité 9.444 — entrée 7.850 — trend 8.900
2. DOT-EUR — ACHETE_MAINTENANT — rank 8.153 — opportunité 9.131 — entrée 7.200 — trend 7.950
3. NEAR-EUR — ACHETE_MAINTENANT — rank 7.833 — opportunité 8.961 — entrée 7.850 — trend 7.500
4. CRV-EUR — ACHETE_MAINTENANT — rank 7.812 — opportunité 8.274 — entrée 6.950 — trend 8.400
5. PUMP-EUR — ACHETE_MAINTENANT — rank 7.154 — opportunité 8.083 — entrée 7.200 — trend 8.350

## Top cross-sectionnel — aperçu non exhaustif

Ce top est une vue courte multi-buckets. Il ne doit jamais être utilisé comme liste exhaustive des achats immédiats.
1. ICP-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.655
2. COMP-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.188
3. DOT-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.153

## Accélération indépendante

- MOVR-EUR — CONFIRMED_ACCELERATION — score 8.377/10 — DETECTED_BUT_TOO_LATE
- GLMR-EUR — CONFIRMED_ACCELERATION — score 7.366/10 — DETECTED_BUT_TOO_LATE
- LIGHTER-EUR — BUILDING_ACCELERATION — score 6.444/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- GMT-EUR — BUILDING_ACCELERATION — score 5.864/10 — DETECTED_BUT_TOO_LATE
- SOON-EUR — BUILDING_ACCELERATION — score 5.803/10 — DETECTED_BUT_TOO_LATE
- GNS-EUR — BUILDING_ACCELERATION — score 5.717/10 — DETECTED_BUT_TOO_LATE
- GRASS-EUR — BUILDING_ACCELERATION — score 5.508/10 — DETECTED_BUT_TOO_LATE
- YFI-EUR — BUILDING_ACCELERATION — score 5.488/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- SOMI-EUR — BUILDING_ACCELERATION — score 5.396/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- GWEI-EUR — BUILDING_ACCELERATION — score 5.232/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- NEAR-EUR — ACTIVE_NOW — score mémoire 7.833/10 — sources ACCELERATION, DECISION_LAYER, V4 — BUYABLE_NOW
- TREAD-EUR — MEMORY_24H — score mémoire 9.983/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- SWELL-EUR — MEMORY_DECAY_24_72H — score mémoire 8.895/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- ICP-EUR — ACTIVE_NOW — score mémoire 8.655/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- WMTX-EUR — MEMORY_24H — score mémoire 8.460/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- MOVR-EUR — ACTIVE_NOW — score mémoire 8.377/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- AGI-EUR — MEMORY_24H — score mémoire 8.300/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- COMP-EUR — ACTIVE_NOW — score mémoire 8.188/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- DOT-EUR — ACTIVE_NOW — score mémoire 8.153/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- ENA-EUR — ACTIVE_NOW — score mémoire 8.051/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY

## Audit des plus fortes hausses

- MOVR-EUR +96.33% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- GTC-EUR +35.51% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- GLMR-EUR +27.69% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- SOON-EUR +24.27% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- PHA-EUR +24.12% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- ARK-EUR +19.48% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- 0G-EUR +15.21% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- ZBCN-EUR +14.91% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- PUMP-EUR +14.75% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- MEW-EUR +14.54% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE

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
