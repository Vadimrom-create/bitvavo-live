# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-10-02T23:46:05.799963+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : SYRUP-EUR | action ACHETE_MAINTENANT | opportunité 8.973 | entrée 7.150 | trend 8.200 | rang 7.980
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : MAGIC-EUR | action PLACE_LIMITE_PASSIVE | opportunité 7.863 | entrée 5.900 | trend 8.650 | rang 7.619
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : ZIG-EUR | action LATENT_ACCELERATOR | opportunité 7.690 | entrée 4.500 | trend 8.750 | rang 7.361
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : FLUID-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 9.389 | entrée 6.550 | trend 8.800 | rang 8.435
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Tous les achats immédiats

1. SYRUP-EUR — ACHETE_MAINTENANT — rank 7.980 — opportunité 8.973 — entrée 7.150 — trend 8.200
2. WLD-EUR — ACHETE_MAINTENANT — rank 7.798 — opportunité 8.331 — entrée 7.250 — trend 8.450
3. SUPER-EUR — ACHETE_MAINTENANT — rank 7.763 — opportunité 8.536 — entrée 7.150 — trend 8.200
4. AXS-EUR — ACHETE_MAINTENANT — rank 7.521 — opportunité 8.632 — entrée 7.600 — trend 7.350
5. XLM-EUR — ACHETE_MAINTENANT — rank 7.063 — opportunité 8.599 — entrée 7.600 — trend 5.700
6. BCH-EUR — ACHETE_MAINTENANT — rank 7.040 — opportunité 8.660 — entrée 7.250 — trend 5.750
7. WIF-EUR — ACHETE_MAINTENANT — rank 6.827 — opportunité 8.715 — entrée 6.800 — trend 6.000

## Top cross-sectionnel — aperçu non exhaustif

Ce top est une vue courte multi-buckets. Il ne doit jamais être utilisé comme liste exhaustive des achats immédiats.
1. FLUID-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.435
2. AAVE-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.333
3. ENJ-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.106

## Accélération indépendante

- SAND-EUR — CONFIRMED_ACCELERATION — score 7.364/10 — DETECTED_BUT_TOO_LATE
- EDU-EUR — BUILDING_ACCELERATION — score 6.253/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- EUL-EUR — BUILDING_ACCELERATION — score 5.872/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- BONK-EUR — BUILDING_ACCELERATION — score 5.762/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- CRV-EUR — BUILDING_ACCELERATION — score 5.662/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- SIGN-EUR — BUILDING_ACCELERATION — score 5.441/10 — DETECTED_BUT_TOO_LATE
- GLM-EUR — BUILDING_ACCELERATION — score 5.321/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- CAP-EUR — BUILDING_ACCELERATION — score 5.223/10 — DETECTED_BUT_TOO_LATE
- SPK-EUR — BUILDING_ACCELERATION — score 5.031/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- AERO-EUR — BUILDING_ACCELERATION — score 5.025/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- WLD-EUR — ACTIVE_NOW — score mémoire 7.798/10 — sources ACCELERATION, DECISION_LAYER, V4 — BUYABLE_NOW
- WIF-EUR — ACTIVE_NOW — score mémoire 6.827/10 — sources ACCELERATION, DECISION_LAYER, V4 — BUYABLE_NOW
- EDGE-EUR — MEMORY_24H — score mémoire 10.000/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- CNPY-EUR — MEMORY_24H — score mémoire 9.238/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- PEOPLE-EUR — MEMORY_24H — score mémoire 9.036/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- GNS-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- FLUID-EUR — ACTIVE_NOW — score mémoire 8.435/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- AAVE-EUR — ACTIVE_NOW — score mémoire 8.333/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- SOSO-EUR — MEMORY_24H — score mémoire 8.156/10 — sources ACCELERATION — MEMORY_ONLY
- ENJ-EUR — ACTIVE_NOW — score mémoire 8.106/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE

## Audit des plus fortes hausses

- SAND-EUR +49.95% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- GALA-EUR +16.70% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- MANA-EUR +13.56% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- ATH-EUR +12.81% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ENJ-EUR +11.65% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- APE-EUR +11.61% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- SPK-EUR +9.75% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- WLD-EUR +9.55% — DETECTED_EARLY — couche NONE — action NONE
- CNPY-EUR +8.67% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- NOS-EUR +8.32% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION

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
