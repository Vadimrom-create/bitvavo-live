# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-10-01T04:46:19.150352+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : HBAR-EUR | action ACHETE_MAINTENANT | opportunité 9.160 | entrée 7.600 | trend 8.150 | rang 8.188
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : REZ-EUR | action PLACE_LIMITE_PASSIVE | opportunité 7.654 | entrée 6.000 | trend 8.650 | rang 7.387
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : KSM-EUR | action LATENT_ACCELERATOR | opportunité 7.808 | entrée 4.500 | trend 8.900 | rang 7.576
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : DYDX-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 9.245 | entrée 6.250 | trend 8.250 | rang 8.175
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Tous les achats immédiats

1. HBAR-EUR — ACHETE_MAINTENANT — rank 8.188 — opportunité 9.160 — entrée 7.600 — trend 8.150
2. KAS-EUR — ACHETE_MAINTENANT — rank 7.968 — opportunité 9.075 — entrée 7.050 — trend 7.700
3. AVAX-EUR — ACHETE_MAINTENANT — rank 7.894 — opportunité 8.133 — entrée 7.350 — trend 8.700
4. ENA-EUR — ACHETE_MAINTENANT — rank 7.756 — opportunité 8.288 — entrée 7.250 — trend 8.400
5. ALGO-EUR — ACHETE_MAINTENANT — rank 7.755 — opportunité 8.163 — entrée 7.200 — trend 8.400
6. XLM-EUR — ACHETE_MAINTENANT — rank 7.729 — opportunité 8.983 — entrée 7.950 — trend 7.100
7. NEAR-EUR — ACHETE_MAINTENANT — rank 7.662 — opportunité 8.051 — entrée 7.600 — trend 8.250
8. ADA-EUR — ACHETE_MAINTENANT — rank 7.399 — opportunité 8.870 — entrée 7.600 — trend 6.350
9. UNI-EUR — ACHETE_MAINTENANT — rank 7.125 — opportunité 8.741 — entrée 7.400 — trend 6.100
10. PEPE-EUR — ACHETE_MAINTENANT — rank 6.947 — opportunité 8.167 — entrée 6.900 — trend 6.150
11. SHIB-EUR — ACHETE_MAINTENANT — rank 6.438 — opportunité 8.122 — entrée 7.000 — trend 5.050

## Top cross-sectionnel — aperçu non exhaustif

Ce top est une vue courte multi-buckets. Il ne doit jamais être utilisé comme liste exhaustive des achats immédiats.
1. HBAR-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.188
2. DYDX-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.175
3. KAS-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 7.968

## Accélération indépendante

- MOVE-EUR — CONFIRMED_ACCELERATION — score 6.591/10 — DETECTED_BUT_TOO_LATE
- DRIFT-EUR — BUILDING_ACCELERATION — score 6.479/10 — DETECTED_BUT_TOO_LATE
- IO-EUR — BUILDING_ACCELERATION — score 4.793/10 — DETECTED_BUT_TOO_LATE
- U-EUR — BUILDING_ACCELERATION — score 4.777/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- NEAR-EUR — ACTIVE_NOW — score mémoire 7.662/10 — sources ACCELERATION, DECISION_LAYER, V4 — BUYABLE_NOW
- CT-EUR — MEMORY_24H — score mémoire 9.156/10 — sources ACCELERATION — MEMORY_ONLY
- CTR-EUR — MEMORY_24H — score mémoire 8.902/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- ACU-EUR — MEMORY_24H — score mémoire 8.894/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- ARPA-EUR — MEMORY_24H — score mémoire 8.595/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- GLMR-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- PONKE-EUR — MEMORY_24H — score mémoire 8.400/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- GWEI-EUR — MEMORY_24H — score mémoire 8.214/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- HBAR-EUR — ACTIVE_NOW — score mémoire 8.188/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- DYDX-EUR — ACTIVE_NOW — score mémoire 8.175/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY

## Audit des plus fortes hausses

- MOVR-EUR +71.32% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- CT-EUR +48.31% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- TRAC-EUR +27.86% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- GLMR-EUR +26.71% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- STX-EUR +24.96% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- MON-EUR +21.24% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- PLUME-EUR +17.32% — DETECTED_EARLY — couche NONE — action NONE
- CAP-EUR +16.48% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- SAFE-EUR +15.21% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- MOVE-EUR +14.06% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE

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
