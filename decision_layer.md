# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-10-02T04:46:51.900429+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : ZRO-EUR | action ACHETE_MAINTENANT | opportunité 9.284 | entrée 6.850 | trend 8.550 | rang 8.304
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : ALGO-EUR | action PLACE_LIMITE_PASSIVE | opportunité 8.196 | entrée 6.700 | trend 7.400 | rang 7.357
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : DYDX-EUR | action LATENT_ACCELERATOR | opportunité 7.975 | entrée 4.500 | trend 8.950 | rang 7.668
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : AAVE-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 9.272 | entrée 8.200 | trend 8.950 | rang 8.294
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Tous les achats immédiats

1. ZRO-EUR — ACHETE_MAINTENANT — rank 8.304 — opportunité 9.284 — entrée 6.850 — trend 8.550
2. HBAR-EUR — ACHETE_MAINTENANT — rank 8.050 — opportunité 9.054 — entrée 7.650 — trend 7.950
3. SUI-EUR — ACHETE_MAINTENANT — rank 7.556 — opportunité 8.914 — entrée 7.850 — trend 6.800
4. WLD-EUR — ACHETE_MAINTENANT — rank 7.511 — opportunité 8.925 — entrée 7.650 — trend 6.900
5. LINK-EUR — ACHETE_MAINTENANT — rank 7.447 — opportunité 8.893 — entrée 7.600 — trend 6.450
6. AVAX-EUR — ACHETE_MAINTENANT — rank 7.426 — opportunité 8.939 — entrée 7.600 — trend 6.650
7. ADA-EUR — ACHETE_MAINTENANT — rank 7.337 — opportunité 8.730 — entrée 7.600 — trend 6.600
8. PEPE-EUR — ACHETE_MAINTENANT — rank 7.129 — opportunité 8.812 — entrée 7.400 — trend 6.150
9. XLM-EUR — ACHETE_MAINTENANT — rank 7.045 — opportunité 8.719 — entrée 7.850 — trend 5.950
10. TAO-EUR — ACHETE_MAINTENANT — rank 7.034 — opportunité 8.015 — entrée 7.600 — trend 6.550
11. CRV-EUR — ACHETE_MAINTENANT — rank 6.951 — opportunité 8.645 — entrée 7.250 — trend 5.750
12. FET-EUR — ACHETE_MAINTENANT — rank 6.787 — opportunité 7.736 — entrée 7.650 — trend 6.050
13. UNI-EUR — ACHETE_MAINTENANT — rank 6.785 — opportunité 8.743 — entrée 7.500 — trend 5.850
14. VIRTUAL-EUR — ACHETE_MAINTENANT — rank 6.733 — opportunité 8.737 — entrée 7.250 — trend 6.150
15. BNB-EUR — ACHETE_MAINTENANT — rank 6.576 — opportunité 8.279 — entrée 7.250 — trend 5.350
16. DOGE-EUR — ACHETE_MAINTENANT — rank 6.552 — opportunité 8.448 — entrée 7.500 — trend 5.600
17. XRP-EUR — ACHETE_MAINTENANT — rank 6.518 — opportunité 8.096 — entrée 7.600 — trend 4.900
18. SHIB-EUR — ACHETE_MAINTENANT — rank 6.218 — opportunité 8.556 — entrée 7.450 — trend 5.050

## Top cross-sectionnel — aperçu non exhaustif

Ce top est une vue courte multi-buckets. Il ne doit jamais être utilisé comme liste exhaustive des achats immédiats.
1. ZRO-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.304
2. AAVE-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.294
3. AZTEC-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.115

## Accélération indépendante

- NEIRO-EUR — CONFIRMED_ACCELERATION — score 8.914/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- ICX-EUR — CONFIRMED_ACCELERATION — score 8.500/10 — DETECTED_BUT_TOO_LATE
- ACT-EUR — CONFIRMED_ACCELERATION — score 7.996/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- 2Z-EUR — CONFIRMED_ACCELERATION — score 7.648/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- MET-EUR — CONFIRMED_ACCELERATION — score 7.094/10 — DETECTED_BUT_TOO_LATE
- AAVE-EUR — CONFIRMED_ACCELERATION — score 7.090/10 — DETECTED_BUT_TOO_LATE
- BOME-EUR — CONFIRMED_ACCELERATION — score 6.935/10 — DETECTED_BUT_TOO_LATE
- WIF-EUR — BUILDING_ACCELERATION — score 6.039/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- TRB-EUR — BUILDING_ACCELERATION — score 5.901/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- KAITO-EUR — BUILDING_ACCELERATION — score 5.791/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- PEPE-EUR — ACTIVE_NOW — score mémoire 7.129/10 — sources ACCELERATION, DECISION_LAYER, V4 — BUYABLE_NOW
- WIF-EUR — ACTIVE_NOW — score mémoire 6.947/10 — sources ACCELERATION, DECISION_LAYER, V4 — BUYABLE_NOW
- CPOOL-EUR — MEMORY_24H — score mémoire 10.000/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- NEIRO-EUR — ACTIVE_NOW — score mémoire 8.914/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- ZRC-EUR — MEMORY_24H — score mémoire 8.847/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- ICX-EUR — ACTIVE_NOW — score mémoire 8.500/10 — sources ACCELERATION, V4 — DETECTED_BUT_TOO_LATE
- OSMO-EUR — MEMORY_24H — score mémoire 8.342/10 — sources ACCELERATION — MEMORY_ONLY
- ZRO-EUR — ACTIVE_NOW — score mémoire 8.304/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- AAVE-EUR — ACTIVE_NOW — score mémoire 8.294/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- AGI-EUR — MEMORY_24H — score mémoire 8.119/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY

## Audit des plus fortes hausses

- SWEAT-EUR +120.88% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- GTC-EUR +57.13% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- SCR-EUR +40.86% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- MOVR-EUR +24.40% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- CT-EUR +22.61% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- MEGA-EUR +22.54% — DETECTED_EARLY — couche NONE — action NONE
- SYN-EUR +16.67% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ALICE-EUR +16.40% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- SUPER-EUR +15.96% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- NOS-EUR +13.19% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION

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
