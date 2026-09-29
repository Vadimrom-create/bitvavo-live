# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-29T04:55:36.444961+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : ICP-EUR | action ACHETE_MAINTENANT | opportunité 8.656 | entrée 7.450 | trend 7.950 | rang 7.784
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : AZTEC-EUR | action PLACE_LIMITE_PASSIVE | opportunité 7.763 | entrée 6.200 | trend 8.400 | rang 7.579
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : ARX-EUR | action LATENT_ACCELERATOR | opportunité 7.783 | entrée 5.150 | trend 8.250 | rang 7.069
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : W-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.598 | entrée 7.150 | trend 8.650 | rang 7.936
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Tous les achats immédiats

1. ICP-EUR — ACHETE_MAINTENANT — rank 7.784 — opportunité 8.656 — entrée 7.450 — trend 7.950
2. POL-EUR — ACHETE_MAINTENANT — rank 7.237 — opportunité 8.099 — entrée 7.200 — trend 6.850

## Top cross-sectionnel — aperçu non exhaustif

Ce top est une vue courte multi-buckets. Il ne doit jamais être utilisé comme liste exhaustive des achats immédiats.
1. W-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.936
2. LINK-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.893
3. ICP-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 7.784

## Accélération indépendante

- ROBO-EUR — CONFIRMED_ACCELERATION — score 7.405/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- ICX-EUR — CONFIRMED_ACCELERATION — score 7.062/10 — DETECTED_BUT_TOO_LATE
- GWEI-EUR — BUILDING_ACCELERATION — score 6.187/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- WMTX-EUR — BUILDING_ACCELERATION — score 5.616/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- 0G-EUR — BUILDING_ACCELERATION — score 5.581/10 — DETECTED_BUT_TOO_LATE
- ICP-EUR — BUILDING_ACCELERATION — score 5.433/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- ICP-EUR — ACTIVE_NOW — score mémoire 7.784/10 — sources ACCELERATION, DECISION_LAYER, V4 — BUYABLE_NOW
- PUFFER-EUR — MEMORY_24H — score mémoire 9.062/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- ZRC-EUR — MEMORY_24H — score mémoire 9.000/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- ZEUS-EUR — MEMORY_24H — score mémoire 8.844/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- IMU-EUR — MEMORY_24H — score mémoire 8.632/10 — sources ACCELERATION — MEMORY_ONLY
- QUID-EUR — MEMORY_24H — score mémoire 8.100/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- OSMO-EUR — MEMORY_24H — score mémoire 7.990/10 — sources ACCELERATION — MEMORY_ONLY
- W-EUR — ACTIVE_NOW — score mémoire 7.936/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- LINK-EUR — ACTIVE_NOW — score mémoire 7.893/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- U-EUR — MEMORY_24H — score mémoire 7.773/10 — sources ACCELERATION, V4 — MEMORY_ONLY

## Audit des plus fortes hausses

- NMR-EUR +33.36% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- HBAR-EUR +26.70% — DETECTED_EARLY — couche NONE — action NONE
- 0G-EUR +18.82% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- ALGO-EUR +17.96% — DETECTED_EARLY — couche NONE — action NONE
- CRV-EUR +16.62% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- CELO-EUR +11.38% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- GRASS-EUR +9.46% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- MIOTA-EUR +8.87% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- IKA-EUR +7.08% — DETECTED_TOO_LATE — couche NONE — action INTERPRETATION
- XLM-EUR +6.84% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION

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
