# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-10-03T14:42:34.656940+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : AAVE-EUR | action ACHETE_MAINTENANT | opportunité 7.922 | entrée 7.200 | trend 8.900 | rang 7.772
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : AUDIO-EUR | action PLACE_LIMITE_PASSIVE | opportunité 7.579 | entrée 5.850 | trend 8.650 | rang 7.296
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : aucun candidat matériel
- **MEILLEUR_PULLBACK_REENTRY** : FLUID-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.001 | entrée 6.600 | trend 8.950 | rang 7.754
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Tous les achats immédiats

1. AAVE-EUR — ACHETE_MAINTENANT — rank 7.772 — opportunité 7.922 — entrée 7.200 — trend 8.900

## Top cross-sectionnel — aperçu non exhaustif

Ce top est une vue courte multi-buckets. Il ne doit jamais être utilisé comme liste exhaustive des achats immédiats.
1. AAVE-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 7.772
2. FLUID-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.754
3. IMX-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.689

## Accélération indépendante

- WIN-EUR — CONFIRMED_ACCELERATION — score 8.500/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- SUPER-EUR — CONFIRMED_ACCELERATION — score 8.359/10 — DETECTED_BUT_TOO_LATE
- TIA-EUR — CONFIRMED_ACCELERATION — score 6.724/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- REQ-EUR — CONFIRMED_ACCELERATION — score 6.555/10 — DETECTED_BUT_TOO_LATE
- IO-EUR — BUILDING_ACCELERATION — score 6.164/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- GTC-EUR — BUILDING_ACCELERATION — score 5.607/10 — DETECTED_BUT_TOO_LATE
- EIGEN-EUR — BUILDING_ACCELERATION — score 5.480/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- USELESS-EUR — BUILDING_ACCELERATION — score 5.231/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- LDO-EUR — BUILDING_ACCELERATION — score 4.813/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- MOVE-EUR — MEMORY_24H — score mémoire 8.978/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- GLMR-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- WIN-EUR — ACTIVE_NOW — score mémoire 8.500/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- SUPER-EUR — ACTIVE_NOW — score mémoire 8.359/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- SOSO-EUR — MEMORY_24H — score mémoire 8.156/10 — sources ACCELERATION — MEMORY_ONLY
- ARK-EUR — MEMORY_24H — score mémoire 8.048/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- EDGE-EUR — MEMORY_DECAY_24_72H — score mémoire 7.984/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- PEOPLE-EUR — MEMORY_DECAY_24_72H — score mémoire 7.950/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- AAVE-EUR — ACTIVE_NOW — score mémoire 7.772/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- FLUID-EUR — ACTIVE_NOW — score mémoire 7.754/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY

## Audit des plus fortes hausses

- GLMR-EUR +42.61% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- TREAD-EUR +26.50% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- SUPER-EUR +18.45% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- WIN-EUR +15.11% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- SAND-EUR +14.94% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- WLD-EUR +9.47% — DETECTED_EARLY — couche NONE — action NONE
- ATH-EUR +8.83% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- AGI-EUR +8.82% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- HFT-EUR +8.56% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- GRASS-EUR +8.29% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE

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
