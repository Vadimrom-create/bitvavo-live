# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-10-01T01:58:03.455911+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : ICP-EUR | action ACHETE_MAINTENANT | opportunité 9.261 | entrée 7.600 | trend 8.700 | rang 8.437
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : ALICE-EUR | action PLACE_LIMITE_PASSIVE | opportunité 7.532 | entrée 6.400 | trend 8.700 | rang 7.571
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : HUMA-EUR | action LATENT_ACCELERATOR | opportunité 8.376 | entrée 5.550 | trend 8.900 | rang 7.838
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : GALA-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.326 | entrée 6.200 | trend 8.650 | rang 7.811
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Tous les achats immédiats

1. ICP-EUR — ACHETE_MAINTENANT — rank 8.437 — opportunité 9.261 — entrée 7.600 — trend 8.700
2. CRV-EUR — ACHETE_MAINTENANT — rank 7.913 — opportunité 9.024 — entrée 6.900 — trend 7.600
3. AAVE-EUR — ACHETE_MAINTENANT — rank 7.805 — opportunité 8.415 — entrée 6.850 — trend 8.250
4. DOT-EUR — ACHETE_MAINTENANT — rank 7.752 — opportunité 8.190 — entrée 6.950 — trend 8.100
5. XLM-EUR — ACHETE_MAINTENANT — rank 7.608 — opportunité 8.561 — entrée 7.450 — trend 7.100
6. SUI-EUR — ACHETE_MAINTENANT — rank 7.586 — opportunité 7.812 — entrée 7.550 — trend 8.150
7. ONDO-EUR — ACHETE_MAINTENANT — rank 6.980 — opportunité 8.311 — entrée 7.400 — trend 5.900

## Top cross-sectionnel — aperçu non exhaustif

Ce top est une vue courte multi-buckets. Il ne doit jamais être utilisé comme liste exhaustive des achats immédiats.
1. ICP-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.437
2. CRV-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 7.913
3. HUMA-EUR — MEILLEUR_LATENT_ACCELERATOR — LATENT_ACCELERATOR — rank 7.838

## Accélération indépendante

- KITE-EUR — BUILDING_ACCELERATION — score 5.675/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- DRV-EUR — BUILDING_ACCELERATION — score 5.558/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- POND-EUR — BUILDING_ACCELERATION — score 5.025/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- LMWR-EUR — MEMORY_24H — score mémoire 9.685/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- CT-EUR — MEMORY_24H — score mémoire 9.156/10 — sources ACCELERATION — MEMORY_ONLY
- CTR-EUR — MEMORY_24H — score mémoire 8.902/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- ACU-EUR — MEMORY_24H — score mémoire 8.894/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- MOVE-EUR — MEMORY_24H — score mémoire 8.660/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- ARPA-EUR — MEMORY_24H — score mémoire 8.595/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- ICP-EUR — ACTIVE_NOW — score mémoire 8.437/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- MOVR-EUR — MEMORY_24H — score mémoire 8.404/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- PONKE-EUR — MEMORY_24H — score mémoire 8.400/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- GWEI-EUR — MEMORY_24H — score mémoire 8.214/10 — sources ACCELERATION, V4 — MEMORY_ONLY

## Audit des plus fortes hausses

- MOVR-EUR +83.39% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- CT-EUR +54.44% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- TRAC-EUR +29.98% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- SOON-EUR +27.91% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- GLMR-EUR +24.70% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- STX-EUR +18.23% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- MON-EUR +17.68% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- ZBCN-EUR +14.28% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- CAP-EUR +14.19% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE
- ICX-EUR +12.23% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE

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
