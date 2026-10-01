# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-10-01T00:58:25.711480+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : ONDO-EUR | action ACHETE_MAINTENANT | opportunité 9.190 | entrée 7.850 | trend 8.000 | rang 8.172
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : HUMA-EUR | action PLACE_LIMITE_PASSIVE | opportunité 7.980 | entrée 6.050 | trend 8.850 | rang 7.583
  - Strong structure but imperfect current entry; prefer passive execution. High extension/chase reduces rank but does not erase the setup.
- **MEILLEUR_LATENT_ACCELERATOR** : DIA-EUR | action LATENT_ACCELERATOR | opportunité 8.359 | entrée 5.500 | trend 8.750 | rang 7.729
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : W-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 9.252 | entrée 7.150 | trend 8.150 | rang 8.227
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Tous les achats immédiats

1. ONDO-EUR — ACHETE_MAINTENANT — rank 8.172 — opportunité 9.190 — entrée 7.850 — trend 8.000
2. SUI-EUR — ACHETE_MAINTENANT — rank 8.104 — opportunité 9.026 — entrée 8.050 — trend 7.900
3. XLM-EUR — ACHETE_MAINTENANT — rank 8.017 — opportunité 8.139 — entrée 7.600 — trend 8.700
4. WLD-EUR — ACHETE_MAINTENANT — rank 7.307 — opportunité 8.074 — entrée 7.600 — trend 7.800

## Top cross-sectionnel — aperçu non exhaustif

Ce top est une vue courte multi-buckets. Il ne doit jamais être utilisé comme liste exhaustive des achats immédiats.
1. W-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.227
2. ONDO-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.172
3. SUI-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.104

## Accélération indépendante

- NOS-EUR — CONFIRMED_ACCELERATION — score 9.683/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- ZBCN-EUR — CONFIRMED_ACCELERATION — score 8.054/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- FET-EUR — BUILDING_ACCELERATION — score 5.910/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- CFG-EUR — BUILDING_ACCELERATION — score 5.256/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- MOCA-EUR — BUILDING_ACCELERATION — score 5.043/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- LMWR-EUR — MEMORY_24H — score mémoire 9.685/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- NOS-EUR — ACTIVE_NOW — score mémoire 9.683/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- CTR-EUR — MEMORY_24H — score mémoire 8.902/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- ARPA-EUR — MEMORY_24H — score mémoire 8.595/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- HNT-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- MOVR-EUR — MEMORY_24H — score mémoire 8.404/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- PONKE-EUR — MEMORY_24H — score mémoire 8.400/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- W-EUR — ACTIVE_NOW — score mémoire 8.227/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- GWEI-EUR — MEMORY_24H — score mémoire 8.214/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- ONDO-EUR — ACTIVE_NOW — score mémoire 8.172/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY

## Audit des plus fortes hausses

- MOVR-EUR +88.02% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- CT-EUR +49.63% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- GLMR-EUR +22.34% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- TRAC-EUR +20.56% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- STX-EUR +19.01% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- MON-EUR +18.15% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- SOON-EUR +16.21% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- CAP-EUR +14.37% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE
- NOM-EUR +12.82% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- SOMI-EUR +11.15% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION

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
