# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-30T01:05:22.899489+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : ICP-EUR | action ACHETE_MAINTENANT | opportunité 8.282 | entrée 7.200 | trend 9.200 | rang 7.787
  - V4 buy-ready with acceptable current entry; no structural veto. High extension/chase is retained as risk context, not an automatic veto.
- **MEILLEURE_LIMITE_PASSIVE** : HUMA-EUR | action PLACE_LIMITE_PASSIVE | opportunité 7.901 | entrée 5.800 | trend 8.400 | rang 7.553
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : CRV-EUR | action LATENT_ACCELERATOR | opportunité 7.922 | entrée 5.400 | trend 8.200 | rang 7.484
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : XDC-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 9.143 | entrée 6.250 | trend 8.000 | rang 8.075
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Tous les achats immédiats

1. ICP-EUR — ACHETE_MAINTENANT — rank 7.787 — opportunité 8.282 — entrée 7.200 — trend 9.200

## Top cross-sectionnel — aperçu non exhaustif

Ce top est une vue courte multi-buckets. Il ne doit jamais être utilisé comme liste exhaustive des achats immédiats.
1. XDC-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.075
2. ROSE-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.840
3. ALGO-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.809

## Accélération indépendante

- KSM-EUR — BUILDING_ACCELERATION — score 5.898/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- GNS-EUR — BUILDING_ACCELERATION — score 5.676/10 — DETECTED_BUT_TOO_LATE
- SAGA-EUR — BUILDING_ACCELERATION — score 5.520/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- 0G-EUR — BUILDING_ACCELERATION — score 5.384/10 — DETECTED_BUT_TOO_LATE
- BIO-EUR — BUILDING_ACCELERATION — score 5.211/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- CNPY-EUR — BUILDING_ACCELERATION — score 5.187/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- ZRC-EUR — BUILDING_ACCELERATION — score 4.967/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- QUID-EUR — MEMORY_24H — score mémoire 9.062/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- SWELL-EUR — MEMORY_24H — score mémoire 9.000/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- IMU-EUR — MEMORY_24H — score mémoire 8.866/10 — sources ACCELERATION — MEMORY_ONLY
- MEW-EUR — MEMORY_24H — score mémoire 8.720/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- EDGE-EUR — MEMORY_24H — score mémoire 8.544/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- XDC-EUR — ACTIVE_NOW — score mémoire 8.075/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- SOLV-EUR — MEMORY_24H — score mémoire 8.017/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- ROSE-EUR — ACTIVE_NOW — score mémoire 7.840/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- ZIG-EUR — MEMORY_24H — score mémoire 7.836/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- GTC-EUR — MEMORY_24H — score mémoire 7.830/10 — sources ACCELERATION, V4 — MEMORY_ONLY

## Audit des plus fortes hausses

- SOON-EUR +47.76% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- POND-EUR +31.69% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- MOVR-EUR +31.30% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- GRASS-EUR +26.33% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- QNT-EUR +22.92% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- PUMP-EUR +18.82% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- TRIA-EUR +16.04% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE
- INIT-EUR +15.67% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- ZBCN-EUR +15.13% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- ZRO-EUR +14.99% — DETECTED_EARLY — couche NONE — action NONE

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
