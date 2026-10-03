# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-10-03T08:58:31.299023+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : AAVE-EUR | action ACHETE_MAINTENANT | opportunité 8.596 | entrée 7.250 | trend 8.900 | rang 8.193
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : ENJ-EUR | action PLACE_LIMITE_PASSIVE | opportunité 7.604 | entrée 6.000 | trend 8.400 | rang 7.422
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : IMX-EUR | action LATENT_ACCELERATOR | opportunité 8.353 | entrée 5.400 | trend 9.200 | rang 7.904
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : FLUID-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.105 | entrée 6.650 | trend 8.950 | rang 7.974
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Tous les achats immédiats

1. AAVE-EUR — ACHETE_MAINTENANT — rank 8.193 — opportunité 8.596 — entrée 7.250 — trend 8.900
2. WLD-EUR — ACHETE_MAINTENANT — rank 7.643 — opportunité 8.085 — entrée 7.150 — trend 8.250
3. UNI-EUR — ACHETE_MAINTENANT — rank 7.356 — opportunité 8.858 — entrée 7.250 — trend 6.350

## Top cross-sectionnel — aperçu non exhaustif

Ce top est une vue courte multi-buckets. Il ne doit jamais être utilisé comme liste exhaustive des achats immédiats.
1. AAVE-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.193
2. FLUID-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.974
3. IMX-EUR — MEILLEUR_LATENT_ACCELERATOR — LATENT_ACCELERATOR — rank 7.904

## Accélération indépendante

- GTC-EUR — CONFIRMED_ACCELERATION — score 8.049/10 — DETECTED_BUT_TOO_LATE
- SWEAT-EUR — CONFIRMED_ACCELERATION — score 7.500/10 — DETECTED_BUT_TOO_LATE
- ZRO-EUR — BUILDING_ACCELERATION — score 6.397/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- GLMR-EUR — BUILDING_ACCELERATION — score 6.036/10 — DETECTED_BUT_TOO_LATE
- PEAQ-EUR — BUILDING_ACCELERATION — score 6.030/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- IMU-EUR — BUILDING_ACCELERATION — score 5.965/10 — DETECTED_BUT_TOO_LATE
- IMX-EUR — BUILDING_ACCELERATION — score 5.381/10 — DETECTED_BUT_TOO_LATE
- AVA-EUR — BUILDING_ACCELERATION — score 5.306/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- EDGE-EUR — MEMORY_DECAY_24_72H — score mémoire 9.178/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- PEOPLE-EUR — MEMORY_DECAY_24_72H — score mémoire 9.030/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- MOVE-EUR — MEMORY_24H — score mémoire 8.978/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- HFT-EUR — MEMORY_24H — score mémoire 8.388/10 — sources ACCELERATION — MEMORY_ONLY
- AAVE-EUR — ACTIVE_NOW — score mémoire 8.193/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- SOSO-EUR — MEMORY_24H — score mémoire 8.156/10 — sources ACCELERATION — MEMORY_ONLY
- GTC-EUR — ACTIVE_NOW — score mémoire 8.049/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- FLUID-EUR — ACTIVE_NOW — score mémoire 7.974/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- IMX-EUR — ACTIVE_NOW — score mémoire 7.904/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- CSPR-EUR — MEMORY_DECAY_24_72H — score mémoire 7.886/10 — sources ACCELERATION, V4 — MEMORY_ONLY

## Audit des plus fortes hausses

- SAND-EUR +19.45% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- FOLD-EUR +13.59% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- QNT-EUR +12.10% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ATH-EUR +11.18% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- IMX-EUR +10.01% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- HFT-EUR +9.20% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- SYN-EUR +8.16% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- GLMR-EUR +7.41% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- XDP-EUR +6.40% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- SUPER-EUR +6.20% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE

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
