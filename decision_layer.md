# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-29T06:59:21.366795+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : XDC-EUR | action ACHETE_MAINTENANT | opportunité 9.243 | entrée 7.650 | trend 8.700 | rang 8.386
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : ROSE-EUR | action PLACE_LIMITE_PASSIVE | opportunité 8.607 | entrée 5.950 | trend 7.600 | rang 7.372
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : MIOTA-EUR | action LATENT_ACCELERATOR | opportunité 7.732 | entrée 4.500 | trend 8.900 | rang 7.421
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : SEI-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.847 | entrée 6.950 | trend 8.500 | rang 8.139
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Tous les achats immédiats

1. XDC-EUR — ACHETE_MAINTENANT — rank 8.386 — opportunité 9.243 — entrée 7.650 — trend 8.700
2. ONDO-EUR — ACHETE_MAINTENANT — rank 8.066 — opportunité 9.192 — entrée 8.050 — trend 7.750
3. VIRTUAL-EUR — ACHETE_MAINTENANT — rank 8.012 — opportunité 9.036 — entrée 7.050 — trend 8.100
4. LTC-EUR — ACHETE_MAINTENANT — rank 7.991 — opportunité 9.146 — entrée 7.450 — trend 7.550
5. LINK-EUR — ACHETE_MAINTENANT — rank 7.987 — opportunité 8.315 — entrée 6.950 — trend 8.900
6. ICP-EUR — ACHETE_MAINTENANT — rank 7.893 — opportunité 8.708 — entrée 7.000 — trend 8.750
7. FET-EUR — ACHETE_MAINTENANT — rank 7.872 — opportunité 9.146 — entrée 7.800 — trend 7.550
8. PEAQ-EUR — ACHETE_MAINTENANT — rank 7.753 — opportunité 9.043 — entrée 7.400 — trend 7.500
9. WLD-EUR — ACHETE_MAINTENANT — rank 7.594 — opportunité 8.825 — entrée 7.500 — trend 7.300
10. GALA-EUR — ACHETE_MAINTENANT — rank 7.321 — opportunité 8.875 — entrée 6.850 — trend 6.750
11. SYRUP-EUR — ACHETE_MAINTENANT — rank 7.274 — opportunité 8.054 — entrée 6.950 — trend 7.450
12. TAO-EUR — ACHETE_MAINTENANT — rank 7.127 — opportunité 8.623 — entrée 7.450 — trend 5.900
13. SOL-EUR — ACHETE_MAINTENANT — rank 7.093 — opportunité 8.275 — entrée 7.850 — trend 6.250
14. AVAX-EUR — ACHETE_MAINTENANT — rank 7.016 — opportunité 8.711 — entrée 7.000 — trend 6.100

## Top cross-sectionnel — aperçu non exhaustif

Ce top est une vue courte multi-buckets. Il ne doit jamais être utilisé comme liste exhaustive des achats immédiats.
1. XDC-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.386
2. SEI-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.139
3. ONDO-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.066

## Accélération indépendante

- JASMY-EUR — CONFIRMED_ACCELERATION — score 9.153/10 — DETECTED_BUT_TOO_LATE
- FUEL-EUR — CONFIRMED_ACCELERATION — score 9.056/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- ETHFI-EUR — CONFIRMED_ACCELERATION — score 8.321/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- CPOOL-EUR — CONFIRMED_ACCELERATION — score 8.245/10 — DETECTED_BUT_TOO_LATE
- LISTA-EUR — CONFIRMED_ACCELERATION — score 6.900/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- ZEUS-EUR — CONFIRMED_ACCELERATION — score 6.834/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- EIGEN-EUR — BUILDING_ACCELERATION — score 6.209/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- TREAD-EUR — BUILDING_ACCELERATION — score 5.533/10 — DETECTED_BUT_TOO_LATE
- SSV-EUR — BUILDING_ACCELERATION — score 5.516/10 — DETECTED_BUT_TOO_LATE
- AZTEC-EUR — BUILDING_ACCELERATION — score 5.441/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- XDC-EUR — ACTIVE_NOW — score mémoire 8.386/10 — sources ACCELERATION, DECISION_LAYER, V4 — BUYABLE_NOW
- ONDO-EUR — ACTIVE_NOW — score mémoire 8.066/10 — sources ACCELERATION, DECISION_LAYER, V4 — BUYABLE_NOW
- CSPR-EUR — MEMORY_24H — score mémoire 9.687/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- JASMY-EUR — ACTIVE_NOW — score mémoire 9.153/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- PUFFER-EUR — MEMORY_24H — score mémoire 9.062/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- FUEL-EUR — ACTIVE_NOW — score mémoire 9.056/10 — sources ACCELERATION, V4 — WATCH_ONLY
- ZRC-EUR — MEMORY_24H — score mémoire 9.000/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- PHA-EUR — MEMORY_24H — score mémoire 8.665/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- IMU-EUR — MEMORY_24H — score mémoire 8.632/10 — sources ACCELERATION — MEMORY_ONLY
- U-EUR — MEMORY_24H — score mémoire 8.582/10 — sources ACCELERATION, V4 — MEMORY_ONLY

## Audit des plus fortes hausses

- NMR-EUR +27.25% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- HBAR-EUR +21.79% — DETECTED_EARLY — couche NONE — action NONE
- 0G-EUR +21.31% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- CRV-EUR +20.82% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ARX-EUR +16.79% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- CELO-EUR +14.82% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ALICE-EUR +13.54% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ALGO-EUR +13.43% — DETECTED_EARLY — couche NONE — action NONE
- CVX-EUR +11.22% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE
- NPC-EUR +10.26% — DETECTED_EARLY — couche NONE — action INTERPRETATION

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
