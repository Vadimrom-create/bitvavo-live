# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-30T13:44:17.289914+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : ICP-EUR | action ACHETE_MAINTENANT | opportunité 8.030 | entrée 6.900 | trend 9.200 | rang 7.955
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : COMP-EUR | action PLACE_LIMITE_PASSIVE | opportunité 8.070 | entrée 6.150 | trend 9.000 | rang 7.885
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : KSM-EUR | action LATENT_ACCELERATOR | opportunité 7.621 | entrée 4.500 | trend 9.200 | rang 7.502
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : ZRO-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.750 | entrée 7.000 | trend 8.950 | rang 8.080
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Tous les achats immédiats

1. ICP-EUR — ACHETE_MAINTENANT — rank 7.955 — opportunité 8.030 — entrée 6.900 — trend 9.200
2. XLM-EUR — ACHETE_MAINTENANT — rank 7.783 — opportunité 7.712 — entrée 7.600 — trend 8.700
3. SYRUP-EUR — ACHETE_MAINTENANT — rank 7.620 — opportunité 7.920 — entrée 7.200 — trend 8.450
4. FET-EUR — ACHETE_MAINTENANT — rank 7.463 — opportunité 8.077 — entrée 7.550 — trend 7.900
5. SUI-EUR — ACHETE_MAINTENANT — rank 7.382 — opportunité 7.862 — entrée 7.850 — trend 7.900
6. DOGE-EUR — ACHETE_MAINTENANT — rank 7.092 — opportunité 8.339 — entrée 6.800 — trend 6.600
7. SOL-EUR — ACHETE_MAINTENANT — rank 7.055 — opportunité 7.909 — entrée 7.400 — trend 6.800
8. WIF-EUR — ACHETE_MAINTENANT — rank 6.579 — opportunité 7.307 — entrée 7.200 — trend 6.100
9. ADA-EUR — ACHETE_MAINTENANT — rank 6.344 — opportunité 7.474 — entrée 7.200 — trend 5.700
10. NEAR-EUR — ACHETE_MAINTENANT — rank 6.317 — opportunité 7.234 — entrée 6.900 — trend 6.050
11. PEPE-EUR — ACHETE_MAINTENANT — rank 5.874 — opportunité 7.118 — entrée 7.400 — trend 4.900

## Top cross-sectionnel — aperçu non exhaustif

Ce top est une vue courte multi-buckets. Il ne doit jamais être utilisé comme liste exhaustive des achats immédiats.
1. ZRO-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.080
2. ICP-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 7.955
3. COMP-EUR — MEILLEURE_LIMITE_PASSIVE — PLACE_LIMITE_PASSIVE — rank 7.885

## Accélération indépendante

- NOS-EUR — CONFIRMED_ACCELERATION — score 8.131/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- AGI-EUR — CONFIRMED_ACCELERATION — score 7.055/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- IRYS-EUR — BUILDING_ACCELERATION — score 5.514/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- WMTX-EUR — BUILDING_ACCELERATION — score 5.200/10 — DETECTED_BUT_TOO_LATE
- DOS-EUR — BUILDING_ACCELERATION — score 5.195/10 — DETECTED_BUT_TOO_LATE
- XMN-EUR — BUILDING_ACCELERATION — score 4.849/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- FET-EUR — ACTIVE_NOW — score mémoire 7.463/10 — sources ACCELERATION, DECISION_LAYER, V4 — BUYABLE_NOW
- SUI-EUR — ACTIVE_NOW — score mémoire 7.382/10 — sources ACCELERATION, DECISION_LAYER, V4 — BUYABLE_NOW
- SOON-EUR — MEMORY_24H — score mémoire 10.000/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- NOM-EUR — MEMORY_24H — score mémoire 9.770/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- BTT-EUR — MEMORY_24H — score mémoire 9.062/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- CTR-EUR — MEMORY_24H — score mémoire 8.902/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- GWEI-EUR — MEMORY_24H — score mémoire 8.731/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- AIOZ-EUR — MEMORY_24H — score mémoire 8.688/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- DGB-EUR — MEMORY_24H — score mémoire 8.670/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- CVC-EUR — MEMORY_24H — score mémoire 8.565/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY

## Audit des plus fortes hausses

- ARK-EUR +55.08% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- MOVR-EUR +49.07% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- CT-EUR +36.80% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- SOON-EUR +35.99% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- NOM-EUR +18.62% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- GLMR-EUR +17.94% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- QNT-EUR +15.80% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- PROM-EUR +14.45% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- SOMI-EUR +12.95% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- GTC-EUR +11.86% — DETECTED_EARLY — couche NONE — action INTERPRETATION

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
