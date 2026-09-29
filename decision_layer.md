# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-29T09:02:13.629763+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : LINK-EUR | action ACHETE_MAINTENANT | opportunité 8.712 | entrée 7.600 | trend 9.200 | rang 8.038
  - V4 buy-ready with acceptable current entry; no structural veto. High extension/chase is retained as risk context, not an automatic veto.
- **MEILLEURE_LIMITE_PASSIVE** : SUPER-EUR | action PLACE_LIMITE_PASSIVE | opportunité 8.400 | entrée 6.450 | trend 7.500 | rang 7.445
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : W-EUR | action LATENT_ACCELERATOR | opportunité 7.644 | entrée 4.500 | trend 8.650 | rang 7.410
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : MIOTA-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.123 | entrée 6.550 | trend 9.200 | rang 7.849
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Tous les achats immédiats

1. LINK-EUR — ACHETE_MAINTENANT — rank 8.038 — opportunité 8.712 — entrée 7.600 — trend 9.200
2. XDC-EUR — ACHETE_MAINTENANT — rank 8.000 — opportunité 8.780 — entrée 6.900 — trend 8.700
3. VIRTUAL-EUR — ACHETE_MAINTENANT — rank 7.571 — opportunité 8.009 — entrée 6.900 — trend 8.100
4. SYRUP-EUR — ACHETE_MAINTENANT — rank 7.368 — opportunité 7.888 — entrée 7.650 — trend 8.500
5. NEAR-EUR — ACHETE_MAINTENANT — rank 7.284 — opportunité 7.960 — entrée 7.250 — trend 7.300
6. UNI-EUR — ACHETE_MAINTENANT — rank 6.494 — opportunité 7.738 — entrée 7.400 — trend 5.650

## Top cross-sectionnel — aperçu non exhaustif

Ce top est une vue courte multi-buckets. Il ne doit jamais être utilisé comme liste exhaustive des achats immédiats.
1. LINK-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.038
2. XDC-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.000
3. MIOTA-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.849

## Accélération indépendante

- GIGA-EUR — CONFIRMED_ACCELERATION — score 10.000/10 — DETECTED_BUT_TOO_LATE
- ZRC-EUR — BUILDING_ACCELERATION — score 6.396/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- ICX-EUR — BUILDING_ACCELERATION — score 6.244/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- SOON-EUR — BUILDING_ACCELERATION — score 5.640/10 — DETECTED_BUT_TOO_LATE
- YGG-EUR — BUILDING_ACCELERATION — score 5.432/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- NEIRO-EUR — BUILDING_ACCELERATION — score 5.343/10 — DETECTED_BUT_TOO_LATE
- BAND-EUR — BUILDING_ACCELERATION — score 5.325/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- TAI-EUR — BUILDING_ACCELERATION — score 4.898/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- XDC-EUR — ACTIVE_NOW — score mémoire 8.000/10 — sources ACCELERATION, DECISION_LAYER, V4 — BUYABLE_NOW
- SYRUP-EUR — ACTIVE_NOW — score mémoire 7.368/10 — sources ACCELERATION, DECISION_LAYER, V4 — BUYABLE_NOW
- GIGA-EUR — ACTIVE_NOW — score mémoire 10.000/10 — sources ACCELERATION — DETECTED_BUT_TOO_LATE
- QUID-EUR — MEMORY_24H — score mémoire 9.062/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- POND-EUR — MEMORY_24H — score mémoire 9.052/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- SWELL-EUR — MEMORY_24H — score mémoire 9.000/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- DGB-EUR — MEMORY_24H — score mémoire 8.836/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- DYDX-EUR — MEMORY_24H — score mémoire 8.690/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- IMU-EUR — MEMORY_24H — score mémoire 8.632/10 — sources ACCELERATION — MEMORY_ONLY
- U-EUR — MEMORY_24H — score mémoire 8.582/10 — sources ACCELERATION, V4 — MEMORY_ONLY

## Audit des plus fortes hausses

- POND-EUR +40.70% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- NMR-EUR +28.90% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- CRV-EUR +22.49% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- CELO-EUR +19.92% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- SOON-EUR +19.74% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- INIT-EUR +17.23% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- 0G-EUR +16.64% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- ICP-EUR +14.11% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- CVX-EUR +13.96% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE
- SYRUP-EUR +13.47% — DETECTED_EARLY — couche NONE — action INTERPRETATION

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
