# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-10-02T05:24:23.687720+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : PUMP-EUR | action ACHETE_MAINTENANT | opportunité 9.318 | entrée 7.650 | trend 8.350 | rang 8.062
  - V4 buy-ready with acceptable current entry; no structural veto. High extension/chase is retained as risk context, not an automatic veto.
- **MEILLEURE_LIMITE_PASSIVE** : DYDX-EUR | action PLACE_LIMITE_PASSIVE | opportunité 8.320 | entrée 6.050 | trend 8.950 | rang 7.903
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : IMX-EUR | action LATENT_ACCELERATOR | opportunité 7.755 | entrée 5.650 | trend 7.900 | rang 7.295
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : HUMA-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.348 | entrée 6.350 | trend 8.600 | rang 7.841
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Tous les achats immédiats

1. PUMP-EUR — ACHETE_MAINTENANT — rank 8.062 — opportunité 9.318 — entrée 7.650 — trend 8.350
2. HBAR-EUR — ACHETE_MAINTENANT — rank 7.974 — opportunité 9.169 — entrée 7.150 — trend 7.650
3. AAVE-EUR — ACHETE_MAINTENANT — rank 7.971 — opportunité 8.730 — entrée 7.050 — trend 8.900
4. WLD-EUR — ACHETE_MAINTENANT — rank 7.842 — opportunité 8.720 — entrée 7.600 — trend 7.900
5. ADA-EUR — ACHETE_MAINTENANT — rank 7.203 — opportunité 8.514 — entrée 7.150 — trend 6.600
6. SUI-EUR — ACHETE_MAINTENANT — rank 7.141 — opportunité 8.035 — entrée 7.150 — trend 6.800
7. XLM-EUR — ACHETE_MAINTENANT — rank 7.093 — opportunité 8.587 — entrée 7.150 — trend 6.200
8. LINK-EUR — ACHETE_MAINTENANT — rank 7.027 — opportunité 8.079 — entrée 7.000 — trend 6.450
9. UNI-EUR — ACHETE_MAINTENANT — rank 6.977 — opportunité 8.114 — entrée 7.400 — trend 6.350
10. DOGE-EUR — ACHETE_MAINTENANT — rank 6.927 — opportunité 8.265 — entrée 6.950 — trend 6.100
11. ONDO-EUR — ACHETE_MAINTENANT — rank 6.730 — opportunité 7.708 — entrée 7.200 — trend 6.150
12. BNB-EUR — ACHETE_MAINTENANT — rank 6.454 — opportunité 7.798 — entrée 6.800 — trend 5.350

## Top cross-sectionnel — aperçu non exhaustif

Ce top est une vue courte multi-buckets. Il ne doit jamais être utilisé comme liste exhaustive des achats immédiats.
1. PUMP-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.062
2. HBAR-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 7.974
3. AAVE-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 7.971

## Accélération indépendante

- SWEAT-EUR — CONFIRMED_ACCELERATION — score 6.790/10 — DETECTED_BUT_TOO_LATE
- NOT-EUR — CONFIRMED_ACCELERATION — score 6.519/10 — DETECTED_BUT_TOO_LATE
- XMN-EUR — BUILDING_ACCELERATION — score 6.044/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- MEME-EUR — BUILDING_ACCELERATION — score 5.907/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- ZBCN-EUR — BUILDING_ACCELERATION — score 5.463/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- DOS-EUR — BUILDING_ACCELERATION — score 5.132/10 — DETECTED_BUT_TOO_LATE
- BIO-EUR — BUILDING_ACCELERATION — score 5.116/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- ZIG-EUR — BUILDING_ACCELERATION — score 4.997/10 — DETECTED_BUT_TOO_LATE
- CPOOL-EUR — BUILDING_ACCELERATION — score 4.788/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- EDGE-EUR — MEMORY_24H — score mémoire 10.000/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- APT-EUR — MEMORY_24H — score mémoire 9.253/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- OPEN-EUR — MEMORY_24H — score mémoire 9.112/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- ZRC-EUR — MEMORY_24H — score mémoire 8.847/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- OSMO-EUR — MEMORY_24H — score mémoire 8.342/10 — sources ACCELERATION — MEMORY_ONLY
- AGI-EUR — MEMORY_24H — score mémoire 8.119/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- HFT-EUR — MEMORY_24H — score mémoire 8.078/10 — sources ACCELERATION — MEMORY_ONLY
- PUMP-EUR — ACTIVE_NOW — score mémoire 8.062/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- U-EUR — MEMORY_24H — score mémoire 8.002/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- GIGA-EUR — MEMORY_24H — score mémoire 7.987/10 — sources ACCELERATION, V4 — MEMORY_ONLY

## Audit des plus fortes hausses

- SWEAT-EUR +152.05% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- GTC-EUR +54.32% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- SCR-EUR +39.18% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- CT-EUR +30.25% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- MEGA-EUR +19.73% — DETECTED_EARLY — couche NONE — action NONE
- ALICE-EUR +14.75% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- SUPER-EUR +14.36% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- SYN-EUR +13.70% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- NOS-EUR +11.03% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- NOM-EUR +10.58% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION

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
