# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-29T12:28:23.719118+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : LINK-EUR | action ACHETE_MAINTENANT | opportunité 8.036 | entrée 7.700 | trend 9.200 | rang 8.168
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : W-EUR | action PLACE_LIMITE_PASSIVE | opportunité 7.797 | entrée 6.750 | trend 8.650 | rang 7.624
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : AZTEC-EUR | action LATENT_ACCELERATOR | opportunité 7.724 | entrée 4.500 | trend 8.400 | rang 7.301
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : ZRO-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 9.255 | entrée 7.100 | trend 8.400 | rang 8.115
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Tous les achats immédiats

1. LINK-EUR — ACHETE_MAINTENANT — rank 8.168 — opportunité 8.036 — entrée 7.700 — trend 9.200
2. XLM-EUR — ACHETE_MAINTENANT — rank 8.166 — opportunité 8.322 — entrée 7.950 — trend 9.000
3. EIGEN-EUR — ACHETE_MAINTENANT — rank 7.795 — opportunité 8.904 — entrée 6.900 — trend 7.850
4. NEAR-EUR — ACHETE_MAINTENANT — rank 7.759 — opportunité 9.089 — entrée 7.800 — trend 7.300
5. SUI-EUR — ACHETE_MAINTENANT — rank 7.659 — opportunité 8.066 — entrée 7.400 — trend 8.150
6. ETHFI-EUR — ACHETE_MAINTENANT — rank 7.443 — opportunité 8.162 — entrée 7.050 — trend 8.500
7. AVAX-EUR — ACHETE_MAINTENANT — rank 7.290 — opportunité 8.040 — entrée 7.700 — trend 8.100
8. APT-EUR — ACHETE_MAINTENANT — rank 7.177 — opportunité 8.374 — entrée 6.850 — trend 7.100
9. ETH-EUR — ACHETE_MAINTENANT — rank 6.680 — opportunité 8.181 — entrée 7.600 — trend 5.350

## Top cross-sectionnel — aperçu non exhaustif

Ce top est une vue courte multi-buckets. Il ne doit jamais être utilisé comme liste exhaustive des achats immédiats.
1. LINK-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.168
2. XLM-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.166
3. ZRO-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.115

## Accélération indépendante

- QUID-EUR — CONFIRMED_ACCELERATION — score 9.062/10 — DETECTED_BUT_TOO_LATE
- ICX-EUR — CONFIRMED_ACCELERATION — score 7.500/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- IKA-EUR — CONFIRMED_ACCELERATION — score 7.023/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- MOCA-EUR — CONFIRMED_ACCELERATION — score 6.704/10 — DETECTED_BUT_TOO_LATE
- GRASS-EUR — BUILDING_ACCELERATION — score 6.243/10 — DETECTED_BUT_TOO_LATE
- VERONA-EUR — BUILDING_ACCELERATION — score 6.121/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- PROVE-EUR — BUILDING_ACCELERATION — score 5.679/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- EDEN-EUR — BUILDING_ACCELERATION — score 5.113/10 — DETECTED_BUT_TOO_LATE
- CRV-EUR — BUILDING_ACCELERATION — score 5.112/10 — DETECTED_BUT_TOO_LATE
- DOS-EUR — BUILDING_ACCELERATION — score 4.862/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- GIGA-EUR — MEMORY_24H — score mémoire 10.000/10 — sources ACCELERATION — MEMORY_ONLY
- BTT-EUR — MEMORY_24H — score mémoire 9.062/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- QUID-EUR — ACTIVE_NOW — score mémoire 9.062/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- SWELL-EUR — MEMORY_24H — score mémoire 9.000/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- DGB-EUR — MEMORY_24H — score mémoire 8.836/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- DYDX-EUR — MEMORY_24H — score mémoire 8.690/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- IMU-EUR — MEMORY_24H — score mémoire 8.632/10 — sources ACCELERATION — MEMORY_ONLY
- U-EUR — MEMORY_24H — score mémoire 8.582/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- ZRC-EUR — MEMORY_24H — score mémoire 8.185/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- LINK-EUR — ACTIVE_NOW — score mémoire 8.168/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY

## Audit des plus fortes hausses

- POND-EUR +42.82% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- 0G-EUR +34.48% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- CELO-EUR +22.89% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- CRV-EUR +19.44% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- SYRUP-EUR +19.00% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ZBCN-EUR +18.32% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- GRASS-EUR +17.93% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- AAVE-EUR +15.98% — DETECTED_EARLY — couche NONE — action NONE
- CVX-EUR +15.61% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE
- NMR-EUR +14.54% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION

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
