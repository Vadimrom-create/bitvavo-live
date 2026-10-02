# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-10-02T00:30:58.759516+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : WLD-EUR | action ACHETE_MAINTENANT | opportunité 9.108 | entrée 7.400 | trend 8.400 | rang 8.226
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : PROM-EUR | action PLACE_LIMITE_PASSIVE | opportunité 7.920 | entrée 6.000 | trend 8.950 | rang 7.794
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : ORCA-EUR | action LATENT_ACCELERATOR | opportunité 7.539 | entrée 5.550 | trend 8.200 | rang 7.240
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : ZRO-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.213 | entrée 6.200 | trend 8.900 | rang 7.865
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Tous les achats immédiats

1. WLD-EUR — ACHETE_MAINTENANT — rank 8.226 — opportunité 9.108 — entrée 7.400 — trend 8.400
2. AAVE-EUR — ACHETE_MAINTENANT — rank 8.217 — opportunité 8.447 — entrée 7.450 — trend 9.200
3. AVAX-EUR — ACHETE_MAINTENANT — rank 8.050 — opportunité 8.373 — entrée 7.000 — trend 8.700
4. LTC-EUR — ACHETE_MAINTENANT — rank 6.968 — opportunité 8.540 — entrée 7.850 — trend 5.850

## Top cross-sectionnel — aperçu non exhaustif

Ce top est une vue courte multi-buckets. Il ne doit jamais être utilisé comme liste exhaustive des achats immédiats.
1. WLD-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.226
2. AAVE-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.217
3. AVAX-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.050

## Accélération indépendante

- MEGA-EUR — CONFIRMED_ACCELERATION — score 9.402/10 — DETECTED_BUT_TOO_LATE
- TAI-EUR — CONFIRMED_ACCELERATION — score 7.533/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- TRAC-EUR — CONFIRMED_ACCELERATION — score 7.312/10 — DETECTED_BUT_TOO_LATE
- HNT-EUR — CONFIRMED_ACCELERATION — score 7.280/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- COW-EUR — CONFIRMED_ACCELERATION — score 6.526/10 — DETECTED_BUT_TOO_LATE
- USELESS-EUR — BUILDING_ACCELERATION — score 5.867/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- SCR-EUR — BUILDING_ACCELERATION — score 5.555/10 — DETECTED_BUT_TOO_LATE
- GLMR-EUR — BUILDING_ACCELERATION — score 5.451/10 — DETECTED_BUT_TOO_LATE
- NEIRO-EUR — BUILDING_ACCELERATION — score 5.237/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- SKY-EUR — BUILDING_ACCELERATION — score 5.096/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- CPOOL-EUR — MEMORY_24H — score mémoire 10.000/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- POND-EUR — MEMORY_24H — score mémoire 10.000/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- MEGA-EUR — ACTIVE_NOW — score mémoire 9.402/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- ZRC-EUR — MEMORY_24H — score mémoire 8.847/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- OSMO-EUR — MEMORY_24H — score mémoire 8.342/10 — sources ACCELERATION — MEMORY_ONLY
- WLD-EUR — ACTIVE_NOW — score mémoire 8.226/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- AAVE-EUR — ACTIVE_NOW — score mémoire 8.217/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- AGI-EUR — MEMORY_24H — score mémoire 8.119/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- AVAX-EUR — ACTIVE_NOW — score mémoire 8.050/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- U-EUR — MEMORY_24H — score mémoire 8.002/10 — sources ACCELERATION, V4 — MEMORY_ONLY

## Audit des plus fortes hausses

- SWEAT-EUR +103.20% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- GTC-EUR +54.02% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- MOVR-EUR +34.83% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ALICE-EUR +30.94% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- MEGA-EUR +28.27% — DETECTED_EARLY — couche NONE — action NONE
- CT-EUR +26.42% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- NOM-EUR +18.83% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- SUPER-EUR +17.16% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- SYN-EUR +16.39% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- VELO-EUR +14.52% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION

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
