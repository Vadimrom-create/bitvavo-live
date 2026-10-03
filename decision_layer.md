# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-10-03T04:29:54.913989+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : AXS-EUR | action ACHETE_MAINTENANT | opportunité 8.370 | entrée 7.050 | trend 9.000 | rang 7.858
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : HUMA-EUR | action PLACE_LIMITE_PASSIVE | opportunité 7.534 | entrée 5.950 | trend 8.650 | rang 7.534
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : FLUID-EUR | action LATENT_ACCELERATOR | opportunité 7.916 | entrée 5.500 | trend 9.000 | rang 7.765
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : ORCA-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.414 | entrée 6.650 | trend 8.750 | rang 7.981
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Tous les achats immédiats

1. AXS-EUR — ACHETE_MAINTENANT — rank 7.858 — opportunité 8.370 — entrée 7.050 — trend 9.000

## Top cross-sectionnel — aperçu non exhaustif

Ce top est une vue courte multi-buckets. Il ne doit jamais être utilisé comme liste exhaustive des achats immédiats.
1. ORCA-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.981
2. AXS-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 7.858
3. NOM-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.806

## Accélération indépendante

- SAND-EUR — BUILDING_ACCELERATION — score 6.139/10 — DETECTED_BUT_TOO_LATE
- HFT-EUR — BUILDING_ACCELERATION — score 6.038/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- AXS-EUR — ACTIVE_NOW — score mémoire 7.858/10 — sources ACCELERATION, DECISION_LAYER, V4 — BUYABLE_NOW
- EDGE-EUR — MEMORY_24H — score mémoire 10.000/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- PEOPLE-EUR — MEMORY_24H — score mémoire 9.036/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- MOVE-EUR — MEMORY_24H — score mémoire 8.978/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- GNS-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- SOSO-EUR — MEMORY_24H — score mémoire 8.156/10 — sources ACCELERATION — MEMORY_ONLY
- ORCA-EUR — ACTIVE_NOW — score mémoire 7.981/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- CSPR-EUR — MEMORY_24H — score mémoire 7.942/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- NOM-EUR — ACTIVE_NOW — score mémoire 7.806/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- FLUID-EUR — ACTIVE_NOW — score mémoire 7.765/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY

## Audit des plus fortes hausses

- SAND-EUR +78.50% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ENJ-EUR +19.56% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- MANA-EUR +19.44% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- GALA-EUR +11.96% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- BAT-EUR +10.83% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE
- APE-EUR +10.77% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- BIGTIME-EUR +10.47% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ATH-EUR +10.46% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- AXS-EUR +10.40% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- TREAD-EUR +9.76% — DETECTED_EARLY — couche NONE — action INTERPRETATION

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
