# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-10-03T07:37:45.490704+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : AAVE-EUR | action ACHETE_MAINTENANT | opportunité 8.265 | entrée 6.800 | trend 8.900 | rang 8.016
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : ORCA-EUR | action PLACE_LIMITE_PASSIVE | opportunité 7.467 | entrée 6.000 | trend 8.150 | rang 7.310
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : IMX-EUR | action LATENT_ACCELERATOR | opportunité 8.197 | entrée 5.500 | trend 9.200 | rang 7.828
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : FLUID-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.160 | entrée 6.550 | trend 8.750 | rang 7.755
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Tous les achats immédiats

1. AAVE-EUR — ACHETE_MAINTENANT — rank 8.016 — opportunité 8.265 — entrée 6.800 — trend 8.900
2. XDC-EUR — ACHETE_MAINTENANT — rank 7.453 — opportunité 7.843 — entrée 7.150 — trend 7.950
3. ATH-EUR — ACHETE_MAINTENANT — rank 7.093 — opportunité 7.605 — entrée 7.000 — trend 8.050

## Top cross-sectionnel — aperçu non exhaustif

Ce top est une vue courte multi-buckets. Il ne doit jamais être utilisé comme liste exhaustive des achats immédiats.
1. AAVE-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.016
2. IMX-EUR — MEILLEUR_LATENT_ACCELERATOR — LATENT_ACCELERATOR — rank 7.828
3. FLUID-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.755

## Accélération indépendante

- ZEUS-EUR — CONFIRMED_ACCELERATION — score 7.582/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- ALICE-EUR — CONFIRMED_ACCELERATION — score 7.334/10 — DETECTED_BUT_TOO_LATE
- TAI-EUR — CONFIRMED_ACCELERATION — score 7.258/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- ARK-EUR — BUILDING_ACCELERATION — score 6.497/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- ZIG-EUR — BUILDING_ACCELERATION — score 5.657/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- UP-EUR — BUILDING_ACCELERATION — score 5.053/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- EDGE-EUR — MEMORY_DECAY_24_72H — score mémoire 9.459/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- SYN-EUR — MEMORY_24H — score mémoire 9.039/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- PEOPLE-EUR — MEMORY_24H — score mémoire 9.036/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- MOVE-EUR — MEMORY_24H — score mémoire 8.978/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- SWEAT-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- SOSO-EUR — MEMORY_24H — score mémoire 8.156/10 — sources ACCELERATION — MEMORY_ONLY
- AAVE-EUR — ACTIVE_NOW — score mémoire 8.016/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- CSPR-EUR — MEMORY_24H — score mémoire 7.942/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- IMX-EUR — ACTIVE_NOW — score mémoire 7.828/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- AUDIO-EUR — MEMORY_24H — score mémoire 7.805/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY

## Audit des plus fortes hausses

- SAND-EUR +32.98% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- QNT-EUR +14.72% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ALICE-EUR +12.07% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- ATH-EUR +12.01% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- FOLD-EUR +10.78% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- INIT-EUR +10.58% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE
- ENJ-EUR +9.80% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- SUPER-EUR +9.07% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE
- AGI-EUR +8.94% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- IMX-EUR +8.46% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION

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
