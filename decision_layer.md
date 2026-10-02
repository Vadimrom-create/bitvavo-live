# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-10-02T05:01:52.100967+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : ZRO-EUR | action ACHETE_MAINTENANT | opportunité 9.344 | entrée 6.850 | trend 8.550 | rang 8.261
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : ZIG-EUR | action PLACE_LIMITE_PASSIVE | opportunité 7.464 | entrée 5.850 | trend 8.150 | rang 6.759
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : DYDX-EUR | action LATENT_ACCELERATOR | opportunité 8.659 | entrée 5.600 | trend 8.950 | rang 8.068
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : STX-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.287 | entrée 6.650 | trend 8.650 | rang 7.886
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Tous les achats immédiats

1. ZRO-EUR — ACHETE_MAINTENANT — rank 8.261 — opportunité 9.344 — entrée 6.850 — trend 8.550
2. HBAR-EUR — ACHETE_MAINTENANT — rank 8.094 — opportunité 9.190 — entrée 7.650 — trend 7.950
3. ALGO-EUR — ACHETE_MAINTENANT — rank 7.535 — opportunité 8.552 — entrée 7.200 — trend 7.400
4. WLD-EUR — ACHETE_MAINTENANT — rank 7.514 — opportunité 8.985 — entrée 7.400 — trend 6.900
5. LINK-EUR — ACHETE_MAINTENANT — rank 7.414 — opportunité 8.743 — entrée 8.100 — trend 6.450
6. ADA-EUR — ACHETE_MAINTENANT — rank 7.380 — opportunité 8.928 — entrée 7.600 — trend 6.600
7. SUI-EUR — ACHETE_MAINTENANT — rank 7.372 — opportunité 8.621 — entrée 7.350 — trend 6.800
8. PUMP-EUR — ACHETE_MAINTENANT — rank 7.358 — opportunité 8.064 — entrée 7.650 — trend 7.800
9. AVAX-EUR — ACHETE_MAINTENANT — rank 7.297 — opportunité 8.568 — entrée 7.600 — trend 6.650
10. RENDER-EUR — ACHETE_MAINTENANT — rank 7.251 — opportunité 8.829 — entrée 7.300 — trend 6.550
11. ONDO-EUR — ACHETE_MAINTENANT — rank 7.138 — opportunité 8.683 — entrée 7.850 — trend 5.900
12. XLM-EUR — ACHETE_MAINTENANT — rank 7.124 — opportunité 8.778 — entrée 7.600 — trend 5.950
13. FET-EUR — ACHETE_MAINTENANT — rank 7.090 — opportunité 8.114 — entrée 7.100 — trend 6.800
14. TAO-EUR — ACHETE_MAINTENANT — rank 7.071 — opportunité 8.168 — entrée 7.400 — trend 6.550
15. UNI-EUR — ACHETE_MAINTENANT — rank 6.965 — opportunité 8.619 — entrée 7.400 — trend 5.850
16. DOGE-EUR — ACHETE_MAINTENANT — rank 6.755 — opportunité 8.248 — entrée 7.400 — trend 5.600
17. BNB-EUR — ACHETE_MAINTENANT — rank 6.712 — opportunité 8.475 — entrée 7.000 — trend 5.350

## Top cross-sectionnel — aperçu non exhaustif

Ce top est une vue courte multi-buckets. Il ne doit jamais être utilisé comme liste exhaustive des achats immédiats.
1. ZRO-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.261
2. HBAR-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.094
3. DYDX-EUR — MEILLEUR_LATENT_ACCELERATOR — LATENT_ACCELERATOR — rank 8.068

## Accélération indépendante

- EDGE-EUR — CONFIRMED_ACCELERATION — score 10.000/10 — DETECTED_BUT_TOO_LATE
- ZIG-EUR — CONFIRMED_ACCELERATION — score 10.000/10 — DETECTED_BUT_TOO_LATE
- APT-EUR — CONFIRMED_ACCELERATION — score 9.253/10 — DETECTED_BUT_TOO_LATE
- OPEN-EUR — CONFIRMED_ACCELERATION — score 9.112/10 — DETECTED_BUT_TOO_LATE
- GIGA-EUR — CONFIRMED_ACCELERATION — score 7.987/10 — DETECTED_BUT_TOO_LATE
- TREAD-EUR — BUILDING_ACCELERATION — score 6.353/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- REQ-EUR — BUILDING_ACCELERATION — score 6.263/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- TRAC-EUR — BUILDING_ACCELERATION — score 6.159/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- ZETA-EUR — BUILDING_ACCELERATION — score 6.076/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- ARKM-EUR — BUILDING_ACCELERATION — score 5.817/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- ZRO-EUR — ACTIVE_NOW — score mémoire 8.261/10 — sources ACCELERATION, DECISION_LAYER, V4 — BUYABLE_NOW
- ADA-EUR — ACTIVE_NOW — score mémoire 7.380/10 — sources ACCELERATION, DECISION_LAYER, V4 — BUYABLE_NOW
- CPOOL-EUR — MEMORY_24H — score mémoire 10.000/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- EDGE-EUR — ACTIVE_NOW — score mémoire 10.000/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- ZIG-EUR — ACTIVE_NOW — score mémoire 10.000/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- APT-EUR — ACTIVE_NOW — score mémoire 9.253/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- OPEN-EUR — ACTIVE_NOW — score mémoire 9.112/10 — sources ACCELERATION, V4 — DETECTED_BUT_TOO_LATE
- NEIRO-EUR — MEMORY_24H — score mémoire 8.914/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- ZRC-EUR — MEMORY_24H — score mémoire 8.847/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- OSMO-EUR — MEMORY_24H — score mémoire 8.342/10 — sources ACCELERATION — MEMORY_ONLY

## Audit des plus fortes hausses

- SWEAT-EUR +122.97% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- GTC-EUR +55.42% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- SCR-EUR +40.64% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- CT-EUR +25.35% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- MEGA-EUR +20.56% — DETECTED_EARLY — couche NONE — action NONE
- MOVR-EUR +19.06% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ALICE-EUR +16.07% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- SUPER-EUR +15.37% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- SYN-EUR +14.33% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- AAVE-EUR +13.12% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION

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
