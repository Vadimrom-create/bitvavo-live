# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-10-01T17:38:44.564203+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : AVAX-EUR | action ACHETE_MAINTENANT | opportunité 9.086 | entrée 7.800 | trend 8.450 | rang 8.357
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : DIA-EUR | action PLACE_LIMITE_PASSIVE | opportunité 8.152 | entrée 6.150 | trend 8.750 | rang 7.878
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : KSM-EUR | action LATENT_ACCELERATOR | opportunité 8.018 | entrée 5.200 | trend 9.200 | rang 7.843
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : HUMA-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 9.349 | entrée 7.200 | trend 8.550 | rang 8.174
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Tous les achats immédiats

1. AVAX-EUR — ACHETE_MAINTENANT — rank 8.357 — opportunité 9.086 — entrée 7.800 — trend 8.450
2. GALA-EUR — ACHETE_MAINTENANT — rank 8.186 — opportunité 9.288 — entrée 6.900 — trend 8.450
3. AAVE-EUR — ACHETE_MAINTENANT — rank 8.125 — opportunité 8.675 — entrée 7.300 — trend 8.700
4. SUI-EUR — ACHETE_MAINTENANT — rank 7.954 — opportunité 9.005 — entrée 7.850 — trend 7.900
5. RENDER-EUR — ACHETE_MAINTENANT — rank 7.253 — opportunité 8.795 — entrée 7.200 — trend 6.400
6. WIF-EUR — ACHETE_MAINTENANT — rank 7.170 — opportunité 8.687 — entrée 7.000 — trend 7.000
7. BNB-EUR — ACHETE_MAINTENANT — rank 6.557 — opportunité 8.450 — entrée 7.250 — trend 4.900
8. ETH-EUR — ACHETE_MAINTENANT — rank 6.462 — opportunité 8.072 — entrée 7.700 — trend 5.100

## Top cross-sectionnel — aperçu non exhaustif

Ce top est une vue courte multi-buckets. Il ne doit jamais être utilisé comme liste exhaustive des achats immédiats.
1. AVAX-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.357
2. GALA-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.186
3. HUMA-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.174

## Accélération indépendante

- GRASS-EUR — CONFIRMED_ACCELERATION — score 10.000/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- CHILLGUY-EUR — CONFIRMED_ACCELERATION — score 8.548/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- ARK-EUR — CONFIRMED_ACCELERATION — score 8.500/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- JTO-EUR — CONFIRMED_ACCELERATION — score 8.165/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- USELESS-EUR — CONFIRMED_ACCELERATION — score 8.043/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- ETHFI-EUR — CONFIRMED_ACCELERATION — score 7.290/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- FARTCOIN-EUR — CONFIRMED_ACCELERATION — score 7.091/10 — DETECTED_BUT_TOO_LATE
- SWELL-EUR — BUILDING_ACCELERATION — score 6.409/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- PENDLE-EUR — BUILDING_ACCELERATION — score 6.281/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- NEIRO-EUR — BUILDING_ACCELERATION — score 6.210/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- SUI-EUR — ACTIVE_NOW — score mémoire 7.954/10 — sources ACCELERATION, DECISION_LAYER, V4 — BUYABLE_NOW
- WIF-EUR — ACTIVE_NOW — score mémoire 7.170/10 — sources ACCELERATION, DECISION_LAYER, V4 — BUYABLE_NOW
- CPOOL-EUR — MEMORY_24H — score mémoire 10.000/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- GRASS-EUR — ACTIVE_NOW — score mémoire 10.000/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- MOVR-EUR — MEMORY_24H — score mémoire 10.000/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- CT-EUR — MEMORY_24H — score mémoire 8.691/10 — sources ACCELERATION — MEMORY_ONLY
- CHILLGUY-EUR — ACTIVE_NOW — score mémoire 8.548/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- ARK-EUR — ACTIVE_NOW — score mémoire 8.500/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- AVAX-EUR — ACTIVE_NOW — score mémoire 8.357/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- OSMO-EUR — MEMORY_24H — score mémoire 8.342/10 — sources ACCELERATION — MEMORY_ONLY

## Audit des plus fortes hausses

- SWEAT-EUR +117.72% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- MOVR-EUR +81.79% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- CAP-EUR +33.47% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- CT-EUR +28.17% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- ALICE-EUR +27.16% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- MEGA-EUR +24.52% — DETECTED_EARLY — couche NONE — action NONE
- MON-EUR +22.12% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- SYN-EUR +20.89% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- NOS-EUR +19.82% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- ARK-EUR +16.18% — DETECTED_EARLY — couche NONE — action INTERPRETATION

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
