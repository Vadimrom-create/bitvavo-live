# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-10-02T23:59:29.854977+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : AAVE-EUR | action ACHETE_MAINTENANT | opportunité 8.245 | entrée 6.900 | trend 9.200 | rang 8.173
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : HUMA-EUR | action PLACE_LIMITE_PASSIVE | opportunité 8.214 | entrée 5.950 | trend 8.850 | rang 7.841
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : 0G-EUR | action LATENT_ACCELERATOR | opportunité 7.649 | entrée 4.500 | trend 8.000 | rang 6.976
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : MON-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 9.326 | entrée 6.600 | trend 8.450 | rang 8.306
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Tous les achats immédiats

1. AAVE-EUR — ACHETE_MAINTENANT — rank 8.173 — opportunité 8.245 — entrée 6.900 — trend 9.200
2. WLD-EUR — ACHETE_MAINTENANT — rank 7.990 — opportunité 8.804 — entrée 7.050 — trend 8.450
3. ORCA-EUR — ACHETE_MAINTENANT — rank 7.799 — opportunité 8.707 — entrée 6.900 — trend 8.050
4. AXS-EUR — ACHETE_MAINTENANT — rank 7.702 — opportunité 8.973 — entrée 7.800 — trend 7.350
5. SUPER-EUR — ACHETE_MAINTENANT — rank 7.685 — opportunité 8.431 — entrée 6.900 — trend 8.200
6. SYRUP-EUR — ACHETE_MAINTENANT — rank 7.476 — opportunité 7.930 — entrée 6.950 — trend 8.200
7. RENDER-EUR — ACHETE_MAINTENANT — rank 6.991 — opportunité 8.063 — entrée 7.550 — trend 6.550
8. SUI-EUR — ACHETE_MAINTENANT — rank 6.967 — opportunité 8.707 — entrée 7.600 — trend 5.900
9. BCH-EUR — ACHETE_MAINTENANT — rank 6.878 — opportunité 8.319 — entrée 7.200 — trend 5.750

## Top cross-sectionnel — aperçu non exhaustif

Ce top est une vue courte multi-buckets. Il ne doit jamais être utilisé comme liste exhaustive des achats immédiats.
1. MON-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.306
2. AAVE-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.173
3. FLUID-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.013

## Accélération indépendante

- TREE-EUR — CONFIRMED_ACCELERATION — score 7.207/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- SHELL-EUR — BUILDING_ACCELERATION — score 6.302/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- EDU-EUR — BUILDING_ACCELERATION — score 6.253/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- WCT-EUR — BUILDING_ACCELERATION — score 6.030/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- CHILLGUY-EUR — BUILDING_ACCELERATION — score 5.956/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- WLD-EUR — BUILDING_ACCELERATION — score 5.799/10 — DETECTED_BUT_TOO_LATE
- MMT-EUR — BUILDING_ACCELERATION — score 5.468/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- SSV-EUR — BUILDING_ACCELERATION — score 5.430/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- EUL-EUR — BUILDING_ACCELERATION — score 5.189/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- SKL-EUR — BUILDING_ACCELERATION — score 5.042/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- AXS-EUR — ACTIVE_NOW — score mémoire 7.702/10 — sources ACCELERATION, DECISION_LAYER, V4 — BUYABLE_NOW
- WIF-EUR — ACTIVE_NOW — score mémoire 6.734/10 — sources ACCELERATION, DECISION_LAYER, V4 — BUYABLE_NOW
- EDGE-EUR — MEMORY_24H — score mémoire 10.000/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- PEOPLE-EUR — MEMORY_24H — score mémoire 9.036/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- GNS-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- MON-EUR — ACTIVE_NOW — score mémoire 8.306/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- AAVE-EUR — ACTIVE_NOW — score mémoire 8.173/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- SOSO-EUR — MEMORY_24H — score mémoire 8.156/10 — sources ACCELERATION — MEMORY_ONLY
- FLUID-EUR — ACTIVE_NOW — score mémoire 8.013/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- IMX-EUR — ACTIVE_NOW — score mémoire 8.006/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY

## Audit des plus fortes hausses

- SAND-EUR +53.53% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- GALA-EUR +18.16% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- ATH-EUR +14.19% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- MANA-EUR +13.02% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- ENJ-EUR +12.23% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- APE-EUR +11.22% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- WLD-EUR +10.04% — DETECTED_EARLY — couche NONE — action NONE
- SPK-EUR +9.75% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- CNPY-EUR +9.58% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- AXS-EUR +8.54% — DETECTED_EARLY — couche NONE — action INTERPRETATION

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
