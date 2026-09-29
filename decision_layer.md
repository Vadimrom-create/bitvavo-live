# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-29T00:31:05.829630+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : XLM-EUR | action ACHETE_MAINTENANT | opportunité 9.434 | entrée 8.000 | trend 8.800 | rang 8.573
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : AZTEC-EUR | action PLACE_LIMITE_PASSIVE | opportunité 7.553 | entrée 6.050 | trend 8.400 | rang 7.413
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : MIOTA-EUR | action LATENT_ACCELERATOR | opportunité 7.505 | entrée 4.750 | trend 8.900 | rang 7.378
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : LINK-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 9.399 | entrée 7.550 | trend 8.650 | rang 8.357
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Tous les achats immédiats

1. XLM-EUR — ACHETE_MAINTENANT — rank 8.573 — opportunité 9.434 — entrée 8.000 — trend 8.800
2. XDC-EUR — ACHETE_MAINTENANT — rank 8.489 — opportunité 9.122 — entrée 7.550 — trend 9.000
3. WLD-EUR — ACHETE_MAINTENANT — rank 7.803 — opportunité 8.684 — entrée 7.450 — trend 7.750
4. ALGO-EUR — ACHETE_MAINTENANT — rank 7.461 — opportunité 8.386 — entrée 7.400 — trend 8.500

## Top cross-sectionnel — aperçu non exhaustif

Ce top est une vue courte multi-buckets. Il ne doit jamais être utilisé comme liste exhaustive des achats immédiats.
1. XLM-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.573
2. XDC-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.489
3. LINK-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.357

## Accélération indépendante

- EDGE-EUR — CONFIRMED_ACCELERATION — score 9.749/10 — DETECTED_BUT_TOO_LATE
- IMU-EUR — CONFIRMED_ACCELERATION — score 8.632/10 — DETECTED_BUT_TOO_LATE
- DATAIP-EUR — CONFIRMED_ACCELERATION — score 8.285/10 — DETECTED_BUT_TOO_LATE
- IKA-EUR — CONFIRMED_ACCELERATION — score 6.727/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- ICX-EUR — BUILDING_ACCELERATION — score 6.459/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- UP-EUR — BUILDING_ACCELERATION — score 5.622/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- ZBCN-EUR — BUILDING_ACCELERATION — score 5.375/10 — DETECTED_BUT_TOO_LATE
- MAVIA-EUR — BUILDING_ACCELERATION — score 5.226/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- ALT-EUR — BUILDING_ACCELERATION — score 5.218/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- SCR-EUR — BUILDING_ACCELERATION — score 5.069/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- XLM-EUR — ACTIVE_NOW — score mémoire 8.573/10 — sources ACCELERATION, DECISION_LAYER, V4 — BUYABLE_NOW
- EDGE-EUR — ACTIVE_NOW — score mémoire 9.749/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- ZRC-EUR — MEMORY_24H — score mémoire 9.275/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- PUFFER-EUR — MEMORY_24H — score mémoire 9.062/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- ZEUS-EUR — MEMORY_24H — score mémoire 8.844/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- IMU-EUR — ACTIVE_NOW — score mémoire 8.632/10 — sources ACCELERATION — DETECTED_BUT_TOO_LATE
- XDC-EUR — ACTIVE_NOW — score mémoire 8.489/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- LINK-EUR — ACTIVE_NOW — score mémoire 8.357/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- DATAIP-EUR — ACTIVE_NOW — score mémoire 8.285/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- AIXBT-EUR — MEMORY_24H — score mémoire 7.962/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY

## Audit des plus fortes hausses

- NMR-EUR +30.65% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- HBAR-EUR +25.88% — DETECTED_EARLY — couche NONE — action NONE
- 0G-EUR +13.55% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- ALGO-EUR +13.31% — DETECTED_EARLY — couche NONE — action NONE
- LINK-EUR +10.87% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- IKA-EUR +10.27% — DETECTED_TOO_LATE — couche NONE — action INTERPRETATION
- NPC-EUR +8.49% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- CRV-EUR +8.17% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- AZTEC-EUR +6.85% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- TREAD-EUR +6.70% — DETECTED_EARLY — couche NONE — action INTERPRETATION

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
