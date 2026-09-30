# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-30T19:46:25.713566+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : HBAR-EUR | action ACHETE_MAINTENANT | opportunité 9.339 | entrée 8.050 | trend 8.400 | rang 8.448
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : AVNT-EUR | action PLACE_LIMITE_PASSIVE | opportunité 8.074 | entrée 6.100 | trend 8.450 | rang 7.678
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : KSM-EUR | action LATENT_ACCELERATOR | opportunité 8.133 | entrée 5.450 | trend 9.200 | rang 7.856
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : ICP-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 9.385 | entrée 7.150 | trend 8.900 | rang 8.560
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Tous les achats immédiats

1. HBAR-EUR — ACHETE_MAINTENANT — rank 8.448 — opportunité 9.339 — entrée 8.050 — trend 8.400
2. FET-EUR — ACHETE_MAINTENANT — rank 8.125 — opportunité 9.214 — entrée 7.400 — trend 7.900
3. XLM-EUR — ACHETE_MAINTENANT — rank 8.074 — opportunité 8.364 — entrée 7.850 — trend 8.700
4. CRV-EUR — ACHETE_MAINTENANT — rank 7.691 — opportunité 8.285 — entrée 6.950 — trend 8.050

## Top cross-sectionnel — aperçu non exhaustif

Ce top est une vue courte multi-buckets. Il ne doit jamais être utilisé comme liste exhaustive des achats immédiats.
1. ICP-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.560
2. HBAR-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.448
3. FET-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.125

## Accélération indépendante

- AUDIO-EUR — CONFIRMED_ACCELERATION — score 9.472/10 — DETECTED_BUT_TOO_LATE
- CRV-EUR — CONFIRMED_ACCELERATION — score 6.771/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- ARX-EUR — BUILDING_ACCELERATION — score 6.246/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- LRC-EUR — BUILDING_ACCELERATION — score 6.137/10 — DETECTED_BUT_TOO_LATE
- NOS-EUR — BUILDING_ACCELERATION — score 6.078/10 — DETECTED_BUT_TOO_LATE
- MOVR-EUR — BUILDING_ACCELERATION — score 5.474/10 — DETECTED_BUT_TOO_LATE
- CAP-EUR — BUILDING_ACCELERATION — score 5.368/10 — DETECTED_BUT_TOO_LATE
- DYDX-EUR — BUILDING_ACCELERATION — score 5.236/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- VSN-EUR — BUILDING_ACCELERATION — score 4.754/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- AUDIO-EUR — ACTIVE_NOW — score mémoire 9.472/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- CT-EUR — MEMORY_24H — score mémoire 9.221/10 — sources ACCELERATION — MEMORY_ONLY
- CTR-EUR — MEMORY_24H — score mémoire 8.902/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- DGB-EUR — MEMORY_24H — score mémoire 8.670/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- ARPA-EUR — MEMORY_24H — score mémoire 8.595/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- CVC-EUR — MEMORY_24H — score mémoire 8.565/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- ICP-EUR — ACTIVE_NOW — score mémoire 8.560/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- HBAR-EUR — ACTIVE_NOW — score mémoire 8.448/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- PONKE-EUR — MEMORY_24H — score mémoire 8.400/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- GWEI-EUR — MEMORY_24H — score mémoire 8.214/10 — sources ACCELERATION, V4 — MEMORY_ONLY

## Audit des plus fortes hausses

- CT-EUR +54.10% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- MOVR-EUR +49.55% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- SOON-EUR +17.62% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- NOS-EUR +17.57% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- GLMR-EUR +16.59% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- AUDIO-EUR +16.31% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- UP-EUR +14.90% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- CAP-EUR +13.70% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE
- TRAC-EUR +13.13% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- REZ-EUR +12.67% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION

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
