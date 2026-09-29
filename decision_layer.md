# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-29T12:00:00.888713+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : HBAR-EUR | action ACHETE_MAINTENANT | opportunité 9.233 | entrée 7.800 | trend 8.400 | rang 8.383
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : ROSE-EUR | action PLACE_LIMITE_PASSIVE | opportunité 8.023 | entrée 6.100 | trend 8.500 | rang 7.525
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : AZTEC-EUR | action LATENT_ACCELERATOR | opportunité 8.091 | entrée 5.550 | trend 8.400 | rang 7.625
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : XLM-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 9.198 | entrée 8.050 | trend 8.650 | rang 8.381
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Tous les achats immédiats

1. HBAR-EUR — ACHETE_MAINTENANT — rank 8.383 — opportunité 9.233 — entrée 7.800 — trend 8.400
2. LINK-EUR — ACHETE_MAINTENANT — rank 8.214 — opportunité 8.438 — entrée 7.500 — trend 9.200
3. ALGO-EUR — ACHETE_MAINTENANT — rank 8.143 — opportunité 8.449 — entrée 7.400 — trend 8.900
4. VIRTUAL-EUR — ACHETE_MAINTENANT — rank 8.091 — opportunité 9.101 — entrée 7.150 — trend 8.100
5. SUI-EUR — ACHETE_MAINTENANT — rank 7.829 — opportunité 8.590 — entrée 7.850 — trend 7.900
6. NEAR-EUR — ACHETE_MAINTENANT — rank 7.687 — opportunité 9.077 — entrée 7.850 — trend 7.300
7. ICP-EUR — ACHETE_MAINTENANT — rank 7.651 — opportunité 8.482 — entrée 6.850 — trend 9.000
8. SOL-EUR — ACHETE_MAINTENANT — rank 7.309 — opportunité 8.787 — entrée 7.850 — trend 6.250
9. XPL-EUR — ACHETE_MAINTENANT — rank 7.298 — opportunité 8.750 — entrée 7.350 — trend 6.650
10. DOT-EUR — ACHETE_MAINTENANT — rank 7.227 — opportunité 8.799 — entrée 7.500 — trend 6.300
11. ETH-EUR — ACHETE_MAINTENANT — rank 6.821 — opportunité 8.581 — entrée 7.850 — trend 5.350

## Top cross-sectionnel — aperçu non exhaustif

Ce top est une vue courte multi-buckets. Il ne doit jamais être utilisé comme liste exhaustive des achats immédiats.
1. HBAR-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.383
2. XLM-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.381
3. RUNE-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.221

## Accélération indépendante

- PUMP-EUR — CONFIRMED_ACCELERATION — score 9.896/10 — DETECTED_BUT_TOO_LATE
- SPK-EUR — CONFIRMED_ACCELERATION — score 8.782/10 — DETECTED_BUT_TOO_LATE
- IKA-EUR — CONFIRMED_ACCELERATION — score 8.504/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- JASMY-EUR — CONFIRMED_ACCELERATION — score 8.396/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- XDC-EUR — CONFIRMED_ACCELERATION — score 6.968/10 — DETECTED_BUT_TOO_LATE
- USELESS-EUR — BUILDING_ACCELERATION — score 6.277/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- XAI-EUR — BUILDING_ACCELERATION — score 6.251/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- CTC-EUR — BUILDING_ACCELERATION — score 6.189/10 — DETECTED_BUT_TOO_LATE
- VIRTUAL-EUR — BUILDING_ACCELERATION — score 5.933/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- RED-EUR — BUILDING_ACCELERATION — score 5.715/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- NEAR-EUR — ACTIVE_NOW — score mémoire 7.687/10 — sources ACCELERATION, DECISION_LAYER, V4 — BUYABLE_NOW
- XPL-EUR — ACTIVE_NOW — score mémoire 7.298/10 — sources ACCELERATION, DECISION_LAYER, V4 — BUYABLE_NOW
- GIGA-EUR — MEMORY_24H — score mémoire 10.000/10 — sources ACCELERATION — MEMORY_ONLY
- PUMP-EUR — ACTIVE_NOW — score mémoire 9.896/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- BTT-EUR — MEMORY_24H — score mémoire 9.062/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- QUID-EUR — MEMORY_24H — score mémoire 9.062/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- SWELL-EUR — MEMORY_24H — score mémoire 9.000/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- DGB-EUR — MEMORY_24H — score mémoire 8.836/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- SPK-EUR — ACTIVE_NOW — score mémoire 8.782/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- DYDX-EUR — MEMORY_24H — score mémoire 8.690/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY

## Audit des plus fortes hausses

- POND-EUR +54.63% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- 0G-EUR +30.75% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- CELO-EUR +27.80% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ZBCN-EUR +22.65% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- GRASS-EUR +22.15% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- CRV-EUR +19.04% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- SYRUP-EUR +18.90% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- CVX-EUR +16.89% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE
- AAVE-EUR +16.40% — DETECTED_EARLY — couche NONE — action NONE
- INIT-EUR +13.74% — DETECTED_EARLY — couche NONE — action INTERPRETATION

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
