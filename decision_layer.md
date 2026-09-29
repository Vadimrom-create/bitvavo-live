# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-29T08:45:32.098603+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : LINK-EUR | action ACHETE_MAINTENANT | opportunité 8.452 | entrée 7.350 | trend 9.200 | rang 7.982
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : GALA-EUR | action PLACE_LIMITE_PASSIVE | opportunité 8.143 | entrée 6.550 | trend 9.000 | rang 7.647
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : MIOTA-EUR | action LATENT_ACCELERATOR | opportunité 7.861 | entrée 5.450 | trend 9.200 | rang 7.429
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : JASMY-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.578 | entrée 6.800 | trend 8.700 | rang 8.064
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Tous les achats immédiats

1. LINK-EUR — ACHETE_MAINTENANT — rank 7.982 — opportunité 8.452 — entrée 7.350 — trend 9.200
2. NEAR-EUR — ACHETE_MAINTENANT — rank 7.860 — opportunité 9.007 — entrée 7.850 — trend 7.300
3. SYRUP-EUR — ACHETE_MAINTENANT — rank 7.723 — opportunité 8.658 — entrée 7.600 — trend 8.500
4. VIRTUAL-EUR — ACHETE_MAINTENANT — rank 7.688 — opportunité 8.274 — entrée 6.950 — trend 8.100
5. AVAX-EUR — ACHETE_MAINTENANT — rank 7.014 — opportunité 8.228 — entrée 7.150 — trend 6.900
6. UNI-EUR — ACHETE_MAINTENANT — rank 6.680 — opportunité 8.213 — entrée 7.400 — trend 5.650

## Top cross-sectionnel — aperçu non exhaustif

Ce top est une vue courte multi-buckets. Il ne doit jamais être utilisé comme liste exhaustive des achats immédiats.
1. JASMY-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.064
2. LINK-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 7.982
3. NEAR-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 7.860

## Accélération indépendante

- SOON-EUR — CONFIRMED_ACCELERATION — score 7.908/10 — DETECTED_BUT_TOO_LATE
- AIXBT-EUR — CONFIRMED_ACCELERATION — score 7.640/10 — DETECTED_BUT_TOO_LATE
- MOVE-EUR — CONFIRMED_ACCELERATION — score 6.981/10 — DETECTED_BUT_TOO_LATE
- ACT-EUR — BUILDING_ACCELERATION — score 6.454/10 — DETECTED_BUT_TOO_LATE
- BOB-EUR — BUILDING_ACCELERATION — score 5.675/10 — DETECTED_BUT_TOO_LATE
- ETHFI-EUR — BUILDING_ACCELERATION — score 5.463/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- ZBCN-EUR — BUILDING_ACCELERATION — score 5.319/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- GLM-EUR — BUILDING_ACCELERATION — score 5.270/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- AVAX-EUR — ACTIVE_NOW — score mémoire 7.014/10 — sources ACCELERATION, DECISION_LAYER, V4 — BUYABLE_NOW
- UNI-EUR — ACTIVE_NOW — score mémoire 6.680/10 — sources ACCELERATION, DECISION_LAYER, V4 — BUYABLE_NOW
- QUID-EUR — MEMORY_24H — score mémoire 9.062/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- POND-EUR — MEMORY_24H — score mémoire 9.052/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- SWELL-EUR — MEMORY_24H — score mémoire 9.000/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- ZRC-EUR — MEMORY_24H — score mémoire 9.000/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- INIT-EUR — MEMORY_24H — score mémoire 8.846/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- DGB-EUR — MEMORY_24H — score mémoire 8.836/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- DYDX-EUR — MEMORY_24H — score mémoire 8.690/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- IMU-EUR — MEMORY_24H — score mémoire 8.632/10 — sources ACCELERATION — MEMORY_ONLY

## Audit des plus fortes hausses

- POND-EUR +40.79% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- NMR-EUR +32.03% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- CRV-EUR +21.58% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- SOON-EUR +20.49% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- CELO-EUR +17.78% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- CVX-EUR +15.08% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE
- GRASS-EUR +15.03% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- INIT-EUR +14.94% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- 0G-EUR +14.56% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- SYRUP-EUR +13.43% — DETECTED_EARLY — couche NONE — action INTERPRETATION

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
