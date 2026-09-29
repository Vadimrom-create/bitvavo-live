# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-29T07:59:39.839880+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : XLM-EUR | action ACHETE_MAINTENANT | opportunité 9.250 | entrée 7.900 | trend 8.000 | rang 8.092
  - V4 buy-ready with acceptable current entry; no structural veto. High extension/chase is retained as risk context, not an automatic veto.
- **MEILLEURE_LIMITE_PASSIVE** : SUPER-EUR | action PLACE_LIMITE_PASSIVE | opportunité 8.967 | entrée 6.700 | trend 7.350 | rang 7.582
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : KMNO-EUR | action LATENT_ACCELERATOR | opportunité 8.553 | entrée 5.750 | trend 7.550 | rang 7.297
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : NOM-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 9.002 | entrée 7.300 | trend 7.900 | rang 7.989
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Tous les achats immédiats

1. XLM-EUR — ACHETE_MAINTENANT — rank 8.092 — opportunité 9.250 — entrée 7.900 — trend 8.000
2. LINK-EUR — ACHETE_MAINTENANT — rank 7.941 — opportunité 8.484 — entrée 7.350 — trend 8.900
3. RENDER-EUR — ACHETE_MAINTENANT — rank 7.668 — opportunité 8.959 — entrée 7.500 — trend 7.050
4. VIRTUAL-EUR — ACHETE_MAINTENANT — rank 7.647 — opportunité 8.250 — entrée 6.850 — trend 8.100
5. PYTH-EUR — ACHETE_MAINTENANT — rank 7.564 — opportunité 8.010 — entrée 6.800 — trend 8.150
6. KAS-EUR — ACHETE_MAINTENANT — rank 7.487 — opportunité 8.062 — entrée 7.100 — trend 7.950
7. SYRUP-EUR — ACHETE_MAINTENANT — rank 7.421 — opportunité 8.776 — entrée 6.950 — trend 7.450
8. WLD-EUR — ACHETE_MAINTENANT — rank 7.159 — opportunité 8.161 — entrée 7.350 — trend 7.300
9. UNI-EUR — ACHETE_MAINTENANT — rank 7.100 — opportunité 8.755 — entrée 7.900 — trend 5.900
10. GALA-EUR — ACHETE_MAINTENANT — rank 7.060 — opportunité 8.450 — entrée 7.250 — trend 6.750
11. ADA-EUR — ACHETE_MAINTENANT — rank 7.052 — opportunité 8.696 — entrée 7.450 — trend 5.950
12. TAO-EUR — ACHETE_MAINTENANT — rank 7.048 — opportunité 8.767 — entrée 7.400 — trend 5.900

## Top cross-sectionnel — aperçu non exhaustif

Ce top est une vue courte multi-buckets. Il ne doit jamais être utilisé comme liste exhaustive des achats immédiats.
1. XLM-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.092
2. NOM-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.989
3. HUMA-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.978

## Accélération indépendante

- DGB-EUR — CONFIRMED_ACCELERATION — score 8.836/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- QNT-EUR — CONFIRMED_ACCELERATION — score 8.153/10 — DETECTED_BUT_TOO_LATE
- ESP-EUR — CONFIRMED_ACCELERATION — score 7.220/10 — DETECTED_BUT_TOO_LATE
- PHA-EUR — BUILDING_ACCELERATION — score 6.425/10 — DETECTED_BUT_TOO_LATE
- KMNO-EUR — BUILDING_ACCELERATION — score 6.017/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- AVAX-EUR — BUILDING_ACCELERATION — score 5.934/10 — DETECTED_BUT_TOO_LATE
- SOON-EUR — BUILDING_ACCELERATION — score 5.820/10 — DETECTED_BUT_TOO_LATE
- NMR-EUR — BUILDING_ACCELERATION — score 5.651/10 — DETECTED_BUT_TOO_LATE
- HUMA-EUR — BUILDING_ACCELERATION — score 5.523/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- PUFFER-EUR — BUILDING_ACCELERATION — score 5.510/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- UNI-EUR — ACTIVE_NOW — score mémoire 7.100/10 — sources ACCELERATION, DECISION_LAYER, V4 — BUYABLE_NOW
- GALA-EUR — ACTIVE_NOW — score mémoire 7.060/10 — sources ACCELERATION, DECISION_LAYER, V4 — BUYABLE_NOW
- TAO-EUR — ACTIVE_NOW — score mémoire 7.048/10 — sources ACCELERATION, DECISION_LAYER, V4 — BUYABLE_NOW
- CSPR-EUR — MEMORY_24H — score mémoire 9.687/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- QUID-EUR — MEMORY_24H — score mémoire 9.062/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- FUEL-EUR — MEMORY_24H — score mémoire 9.056/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- ZRC-EUR — MEMORY_24H — score mémoire 9.000/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- INIT-EUR — MEMORY_24H — score mémoire 8.846/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- DGB-EUR — ACTIVE_NOW — score mémoire 8.836/10 — sources ACCELERATION, V4 — WATCH_ONLY
- IMU-EUR — MEMORY_24H — score mémoire 8.632/10 — sources ACCELERATION — MEMORY_ONLY

## Audit des plus fortes hausses

- NMR-EUR +30.48% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- POND-EUR +25.82% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- CRV-EUR +22.11% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- HBAR-EUR +20.73% — DETECTED_EARLY — couche NONE — action NONE
- CELO-EUR +16.19% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- GRASS-EUR +15.77% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- ARX-EUR +15.56% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- PHA-EUR +14.65% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ALICE-EUR +14.26% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ICP-EUR +14.00% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION

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
