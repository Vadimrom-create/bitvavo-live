# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-29T00:02:36.981256+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : VIRTUAL-EUR | action ACHETE_MAINTENANT | opportunité 9.027 | entrée 7.200 | trend 9.000 | rang 8.387
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : AZTEC-EUR | action PLACE_LIMITE_PASSIVE | opportunité 8.183 | entrée 6.050 | trend 8.400 | rang 7.671
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : MON-EUR | action LATENT_ACCELERATOR | opportunité 7.520 | entrée 4.500 | trend 7.900 | rang 7.037
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : LINK-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.683 | entrée 7.200 | trend 8.650 | rang 8.040
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Tous les achats immédiats

1. VIRTUAL-EUR — ACHETE_MAINTENANT — rank 8.387 — opportunité 9.027 — entrée 7.200 — trend 9.000
2. XDC-EUR — ACHETE_MAINTENANT — rank 8.255 — opportunité 8.604 — entrée 7.100 — trend 9.000
3. XLM-EUR — ACHETE_MAINTENANT — rank 8.088 — opportunité 8.611 — entrée 7.500 — trend 8.800
4. RENDER-EUR — ACHETE_MAINTENANT — rank 7.971 — opportunité 8.975 — entrée 7.500 — trend 7.850
5. BCH-EUR — ACHETE_MAINTENANT — rank 7.353 — opportunité 7.834 — entrée 6.950 — trend 7.550
6. AAVE-EUR — ACHETE_MAINTENANT — rank 7.003 — opportunité 8.397 — entrée 7.200 — trend 6.450

## Top cross-sectionnel — aperçu non exhaustif

Ce top est une vue courte multi-buckets. Il ne doit jamais être utilisé comme liste exhaustive des achats immédiats.
1. VIRTUAL-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.387
2. XDC-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.255
3. XLM-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.088

## Accélération indépendante

- AIXBT-EUR — CONFIRMED_ACCELERATION — score 7.962/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- MLN-EUR — CONFIRMED_ACCELERATION — score 6.500/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- BNT-EUR — BUILDING_ACCELERATION — score 6.442/10 — DETECTED_BUT_TOO_LATE
- STRK-EUR — BUILDING_ACCELERATION — score 6.265/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- AEVO-EUR — BUILDING_ACCELERATION — score 6.213/10 — DETECTED_BUT_TOO_LATE
- XDP-EUR — BUILDING_ACCELERATION — score 6.202/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- TRB-EUR — BUILDING_ACCELERATION — score 6.150/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- XTZ-EUR — BUILDING_ACCELERATION — score 5.765/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- CROSS-EUR — BUILDING_ACCELERATION — score 5.327/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- ASTR-EUR — BUILDING_ACCELERATION — score 5.245/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- XLM-EUR — ACTIVE_NOW — score mémoire 8.088/10 — sources ACCELERATION, DECISION_LAYER, V4 — BUYABLE_NOW
- ZRC-EUR — MEMORY_24H — score mémoire 9.275/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- PUFFER-EUR — MEMORY_24H — score mémoire 9.062/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- ZEUS-EUR — MEMORY_24H — score mémoire 8.844/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- VIRTUAL-EUR — ACTIVE_NOW — score mémoire 8.387/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- XDC-EUR — ACTIVE_NOW — score mémoire 8.255/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- LINK-EUR — ACTIVE_NOW — score mémoire 8.040/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- RENDER-EUR — ACTIVE_NOW — score mémoire 7.971/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- AIXBT-EUR — ACTIVE_NOW — score mémoire 7.962/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- SUPER-EUR — ACTIVE_NOW — score mémoire 7.864/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY

## Audit des plus fortes hausses

- NMR-EUR +34.36% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- HBAR-EUR +27.56% — DETECTED_EARLY — couche NONE — action NONE
- ALGO-EUR +13.83% — DETECTED_EARLY — couche NONE — action NONE
- LINK-EUR +10.55% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- 0G-EUR +10.34% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- IKA-EUR +8.86% — DETECTED_TOO_LATE — couche NONE — action INTERPRETATION
- CRV-EUR +7.87% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- XLM-EUR +7.82% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- MIOTA-EUR +7.51% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- NPC-EUR +6.45% — DETECTED_EARLY — couche NONE — action INTERPRETATION

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
