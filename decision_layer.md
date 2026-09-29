# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-29T07:42:38.399078+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : LINK-EUR | action ACHETE_MAINTENANT | opportunité 8.523 | entrée 7.400 | trend 8.900 | rang 8.038
  - V4 buy-ready with acceptable current entry; no structural veto. High extension/chase is retained as risk context, not an automatic veto.
- **MEILLEURE_LIMITE_PASSIVE** : ZRO-EUR | action PLACE_LIMITE_PASSIVE | opportunité 8.722 | entrée 5.950 | trend 7.550 | rang 7.405
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : RUNE-EUR | action LATENT_ACCELERATOR | opportunité 7.678 | entrée 4.500 | trend 8.650 | rang 7.399
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : W-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.600 | entrée 7.050 | trend 8.650 | rang 7.875
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Tous les achats immédiats

1. LINK-EUR — ACHETE_MAINTENANT — rank 8.038 — opportunité 8.523 — entrée 7.400 — trend 8.900
2. XLM-EUR — ACHETE_MAINTENANT — rank 7.933 — opportunité 8.964 — entrée 7.500 — trend 8.000
3. ONDO-EUR — ACHETE_MAINTENANT — rank 7.920 — opportunité 8.969 — entrée 7.500 — trend 7.750
4. PYTH-EUR — ACHETE_MAINTENANT — rank 7.750 — opportunité 8.282 — entrée 6.800 — trend 8.150
5. WLD-EUR — ACHETE_MAINTENANT — rank 7.531 — opportunité 8.878 — entrée 7.600 — trend 7.300
6. VIRTUAL-EUR — ACHETE_MAINTENANT — rank 7.495 — opportunité 7.953 — entrée 6.800 — trend 8.100
7. FET-EUR — ACHETE_MAINTENANT — rank 7.303 — opportunité 8.157 — entrée 7.150 — trend 7.550
8. UNI-EUR — ACHETE_MAINTENANT — rank 7.087 — opportunité 8.755 — entrée 7.650 — trend 5.900
9. TAO-EUR — ACHETE_MAINTENANT — rank 7.069 — opportunité 8.755 — entrée 7.650 — trend 5.900
10. ADA-EUR — ACHETE_MAINTENANT — rank 7.068 — opportunité 8.766 — entrée 7.250 — trend 5.950
11. GALA-EUR — ACHETE_MAINTENANT — rank 7.068 — opportunité 8.670 — entrée 7.250 — trend 6.750

## Top cross-sectionnel — aperçu non exhaustif

Ce top est une vue courte multi-buckets. Il ne doit jamais être utilisé comme liste exhaustive des achats immédiats.
1. LINK-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.038
2. XLM-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 7.933
3. ONDO-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 7.920

## Accélération indépendante

- INIT-EUR — CONFIRMED_ACCELERATION — score 8.846/10 — DETECTED_BUT_TOO_LATE
- HUMA-EUR — CONFIRMED_ACCELERATION — score 7.066/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- XDP-EUR — CONFIRMED_ACCELERATION — score 6.988/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- KMNO-EUR — CONFIRMED_ACCELERATION — score 6.565/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- AAVE-EUR — BUILDING_ACCELERATION — score 6.396/10 — DETECTED_BUT_TOO_LATE
- MLN-EUR — BUILDING_ACCELERATION — score 6.238/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- REQ-EUR — BUILDING_ACCELERATION — score 6.186/10 — DETECTED_BUT_TOO_LATE
- LQTY-EUR — BUILDING_ACCELERATION — score 5.873/10 — DETECTED_BUT_TOO_LATE
- GMT-EUR — BUILDING_ACCELERATION — score 5.642/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- IO-EUR — BUILDING_ACCELERATION — score 5.555/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- ONDO-EUR — ACTIVE_NOW — score mémoire 7.920/10 — sources ACCELERATION, DECISION_LAYER, V4 — BUYABLE_NOW
- WLD-EUR — ACTIVE_NOW — score mémoire 7.531/10 — sources ACCELERATION, DECISION_LAYER, V4 — BUYABLE_NOW
- PUFFER-EUR — MEMORY_24H — score mémoire 9.732/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- CSPR-EUR — MEMORY_24H — score mémoire 9.687/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- QUID-EUR — MEMORY_24H — score mémoire 9.062/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- FUEL-EUR — MEMORY_24H — score mémoire 9.056/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- ZRC-EUR — MEMORY_24H — score mémoire 9.000/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- INIT-EUR — ACTIVE_NOW — score mémoire 8.846/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- IMU-EUR — MEMORY_24H — score mémoire 8.632/10 — sources ACCELERATION — MEMORY_ONLY
- U-EUR — MEMORY_24H — score mémoire 8.582/10 — sources ACCELERATION, V4 — MEMORY_ONLY

## Audit des plus fortes hausses

- NMR-EUR +30.45% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- CRV-EUR +22.11% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ARX-EUR +21.90% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- POND-EUR +21.70% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- HBAR-EUR +20.19% — DETECTED_EARLY — couche NONE — action NONE
- CELO-EUR +16.17% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- GRASS-EUR +15.36% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- 0G-EUR +15.34% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- ALICE-EUR +14.33% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- MIOTA-EUR +13.03% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE

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
