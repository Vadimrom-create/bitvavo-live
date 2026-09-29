# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-29T06:38:28.090933+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : LINK-EUR | action ACHETE_MAINTENANT | opportunité 8.303 | entrée 6.900 | trend 8.900 | rang 7.988
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : XAI-EUR | action PLACE_LIMITE_PASSIVE | opportunité 8.523 | entrée 6.150 | trend 7.500 | rang 7.390
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : DIA-EUR | action LATENT_ACCELERATOR | opportunité 7.486 | entrée 4.500 | trend 8.300 | rang 7.117
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : SEI-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.799 | entrée 6.650 | trend 8.500 | rang 8.130
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Tous les achats immédiats

1. LINK-EUR — ACHETE_MAINTENANT — rank 7.988 — opportunité 8.303 — entrée 6.900 — trend 8.900
2. KAS-EUR — ACHETE_MAINTENANT — rank 7.954 — opportunité 8.953 — entrée 7.300 — trend 7.950
3. VIRTUAL-EUR — ACHETE_MAINTENANT — rank 7.933 — opportunité 8.841 — entrée 7.100 — trend 8.100
4. FET-EUR — ACHETE_MAINTENANT — rank 7.841 — opportunité 9.134 — entrée 7.600 — trend 7.550
5. ONDO-EUR — ACHETE_MAINTENANT — rank 7.763 — opportunité 8.625 — entrée 7.600 — trend 7.750
6. SYRUP-EUR — ACHETE_MAINTENANT — rank 7.709 — opportunité 8.984 — entrée 7.200 — trend 7.450
7. AVAX-EUR — ACHETE_MAINTENANT — rank 7.135 — opportunité 8.813 — entrée 7.600 — trend 6.100
8. SOL-EUR — ACHETE_MAINTENANT — rank 7.016 — opportunité 8.363 — entrée 7.450 — trend 6.250
9. ADA-EUR — ACHETE_MAINTENANT — rank 6.995 — opportunité 8.425 — entrée 7.700 — trend 5.950

## Top cross-sectionnel — aperçu non exhaustif

Ce top est une vue courte multi-buckets. Il ne doit jamais être utilisé comme liste exhaustive des achats immédiats.
1. SEI-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.130
2. LINK-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 7.988
3. KAS-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 7.954

## Accélération indépendante

- DRIFT-EUR — CONFIRMED_ACCELERATION — score 7.792/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- UP-EUR — CONFIRMED_ACCELERATION — score 7.198/10 — DETECTED_BUT_TOO_LATE
- FOLD-EUR — CONFIRMED_ACCELERATION — score 6.547/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- XPL-EUR — BUILDING_ACCELERATION — score 6.315/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- TRAC-EUR — BUILDING_ACCELERATION — score 6.190/10 — DETECTED_BUT_TOO_LATE
- AGI-EUR — BUILDING_ACCELERATION — score 6.132/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- C98-EUR — BUILDING_ACCELERATION — score 6.115/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- ME-EUR — BUILDING_ACCELERATION — score 5.775/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- CVX-EUR — BUILDING_ACCELERATION — score 5.731/10 — DETECTED_BUT_TOO_LATE
- COMP-EUR — BUILDING_ACCELERATION — score 5.601/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- AERO-EUR — ACTIVE_NOW — score mémoire 7.589/10 — sources ACCELERATION, DECISION_LAYER, V4 — BUYABLE_NOW
- AVAX-EUR — ACTIVE_NOW — score mémoire 7.135/10 — sources ACCELERATION, DECISION_LAYER, V4 — BUYABLE_NOW
- AAVE-EUR — ACTIVE_NOW — score mémoire 6.436/10 — sources ACCELERATION, DECISION_LAYER, V4 — BUYABLE_NOW
- CSPR-EUR — MEMORY_24H — score mémoire 9.687/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- TREAD-EUR — MEMORY_24H — score mémoire 9.173/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- PUFFER-EUR — MEMORY_24H — score mémoire 9.062/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- ZRC-EUR — MEMORY_24H — score mémoire 9.000/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- ZEUS-EUR — MEMORY_24H — score mémoire 8.844/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- PHA-EUR — MEMORY_24H — score mémoire 8.665/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- IMU-EUR — MEMORY_24H — score mémoire 8.632/10 — sources ACCELERATION — MEMORY_ONLY

## Audit des plus fortes hausses

- NMR-EUR +29.84% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- HBAR-EUR +20.75% — DETECTED_EARLY — couche NONE — action NONE
- CRV-EUR +19.84% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- 0G-EUR +18.79% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- ARX-EUR +14.52% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- CELO-EUR +14.16% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ALGO-EUR +13.63% — DETECTED_EARLY — couche NONE — action NONE
- CVX-EUR +11.08% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE
- PHA-EUR +10.46% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ALICE-EUR +10.28% — DETECTED_EARLY — couche NONE — action INTERPRETATION

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
