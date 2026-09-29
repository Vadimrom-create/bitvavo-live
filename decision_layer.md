# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-29T06:11:54.070257+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : LINK-EUR | action ACHETE_MAINTENANT | opportunité 8.540 | entrée 6.800 | trend 8.900 | rang 8.119
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : HBAR-EUR | action PLACE_LIMITE_PASSIVE | opportunité 7.420 | entrée 6.150 | trend 8.400 | rang 6.278
  - Strong structure but imperfect current entry; prefer passive execution. High extension/chase reduces rank but does not erase the setup.
- **MEILLEUR_LATENT_ACCELERATOR** : XLM-EUR | action LATENT_ACCELERATOR | opportunité 7.589 | entrée 4.500 | trend 8.000 | rang 7.084
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : ICP-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.683 | entrée 6.850 | trend 8.750 | rang 7.913
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Tous les achats immédiats

1. LINK-EUR — ACHETE_MAINTENANT — rank 8.119 — opportunité 8.540 — entrée 6.800 — trend 8.900
2. KAS-EUR — ACHETE_MAINTENANT — rank 7.771 — opportunité 8.719 — entrée 7.050 — trend 7.950
3. AERO-EUR — ACHETE_MAINTENANT — rank 7.465 — opportunité 8.777 — entrée 7.450 — trend 7.900
4. AAVE-EUR — ACHETE_MAINTENANT — rank 7.260 — opportunité 8.142 — entrée 6.800 — trend 7.700
5. AVAX-EUR — ACHETE_MAINTENANT — rank 7.179 — opportunité 8.813 — entrée 7.600 — trend 6.100
6. ADA-EUR — ACHETE_MAINTENANT — rank 7.110 — opportunité 8.778 — entrée 7.450 — trend 5.950
7. SOL-EUR — ACHETE_MAINTENANT — rank 6.930 — opportunité 8.228 — entrée 7.450 — trend 6.250
8. BTC-EUR — ACHETE_MAINTENANT — rank 6.547 — opportunité 8.325 — entrée 7.450 — trend 5.000
9. ETH-EUR — ACHETE_MAINTENANT — rank 6.350 — opportunité 8.055 — entrée 7.450 — trend 4.800
10. BNB-EUR — ACHETE_MAINTENANT — rank 6.278 — opportunité 7.995 — entrée 7.000 — trend 4.650

## Top cross-sectionnel — aperçu non exhaustif

Ce top est une vue courte multi-buckets. Il ne doit jamais être utilisé comme liste exhaustive des achats immédiats.
1. LINK-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.119
2. ICP-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.913
3. JASMY-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.887

## Accélération indépendante

- TREAD-EUR — CONFIRMED_ACCELERATION — score 9.173/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- PHA-EUR — CONFIRMED_ACCELERATION — score 8.665/10 — DETECTED_BUT_TOO_LATE
- U-EUR — CONFIRMED_ACCELERATION — score 8.582/10 — DETECTED_BUT_TOO_LATE
- BIO-EUR — CONFIRMED_ACCELERATION — score 7.548/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- FUEL-EUR — CONFIRMED_ACCELERATION — score 7.407/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- SOON-EUR — CONFIRMED_ACCELERATION — score 6.987/10 — DETECTED_BUT_TOO_LATE
- CHILLGUY-EUR — CONFIRMED_ACCELERATION — score 6.803/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- BONK-EUR — CONFIRMED_ACCELERATION — score 6.687/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- GRASS-EUR — BUILDING_ACCELERATION — score 6.483/10 — DETECTED_BUT_TOO_LATE
- PNUT-EUR — BUILDING_ACCELERATION — score 5.500/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- AAVE-EUR — ACTIVE_NOW — score mémoire 7.260/10 — sources ACCELERATION, DECISION_LAYER, V4 — BUYABLE_NOW
- AVAX-EUR — ACTIVE_NOW — score mémoire 7.179/10 — sources ACCELERATION, DECISION_LAYER, V4 — BUYABLE_NOW
- CSPR-EUR — MEMORY_24H — score mémoire 9.687/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- TREAD-EUR — ACTIVE_NOW — score mémoire 9.173/10 — sources ACCELERATION, V4 — WATCH_ONLY
- PUFFER-EUR — MEMORY_24H — score mémoire 9.062/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- ZRC-EUR — MEMORY_24H — score mémoire 9.000/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- ZEUS-EUR — MEMORY_24H — score mémoire 8.844/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- PHA-EUR — ACTIVE_NOW — score mémoire 8.665/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- IMU-EUR — MEMORY_24H — score mémoire 8.632/10 — sources ACCELERATION — MEMORY_ONLY
- U-EUR — ACTIVE_NOW — score mémoire 8.582/10 — sources ACCELERATION, V4 — DETECTED_BUT_TOO_LATE

## Audit des plus fortes hausses

- NMR-EUR +25.48% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- HBAR-EUR +22.16% — DETECTED_EARLY — couche NONE — action NONE
- POND-EUR +18.03% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- 0G-EUR +17.67% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- CRV-EUR +16.85% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ALGO-EUR +14.05% — DETECTED_EARLY — couche NONE — action NONE
- ARX-EUR +12.68% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- CELO-EUR +9.97% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- NPC-EUR +9.57% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- PHA-EUR +9.47% — DETECTED_EARLY — couche NONE — action INTERPRETATION

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
