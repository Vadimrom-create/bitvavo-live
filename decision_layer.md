# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-10-02T23:11:27.202446+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : SYRUP-EUR | action ACHETE_MAINTENANT | opportunité 8.361 | entrée 7.400 | trend 8.200 | rang 7.628
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : AAVE-EUR | action PLACE_LIMITE_PASSIVE | opportunité 8.598 | entrée 6.050 | trend 9.200 | rang 8.233
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : MAGIC-EUR | action LATENT_ACCELERATOR | opportunité 8.035 | entrée 5.700 | trend 8.650 | rang 7.691
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : ENJ-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 9.283 | entrée 7.800 | trend 8.500 | rang 8.334
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Tous les achats immédiats

1. SYRUP-EUR — ACHETE_MAINTENANT — rank 7.628 — opportunité 8.361 — entrée 7.400 — trend 8.200
2. AXS-EUR — ACHETE_MAINTENANT — rank 7.539 — opportunité 8.573 — entrée 7.300 — trend 7.350
3. BCH-EUR — ACHETE_MAINTENANT — rank 7.068 — opportunité 8.672 — entrée 7.600 — trend 5.750
4. RENDER-EUR — ACHETE_MAINTENANT — rank 6.901 — opportunité 7.941 — entrée 7.150 — trend 6.550

## Top cross-sectionnel — aperçu non exhaustif

Ce top est une vue courte multi-buckets. Il ne doit jamais être utilisé comme liste exhaustive des achats immédiats.
1. ENJ-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.334
2. AAVE-EUR — MEILLEURE_LIMITE_PASSIVE — PLACE_LIMITE_PASSIVE — rank 8.233
3. IMX-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.196

## Accélération indépendante

- INIT-EUR — BUILDING_ACCELERATION — score 5.902/10 — DETECTED_BUT_TOO_LATE
- NEIRO-EUR — BUILDING_ACCELERATION — score 5.156/10 — DETECTED_BUT_TOO_LATE
- ZBT-EUR — BUILDING_ACCELERATION — score 4.987/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- EDGE-EUR — MEMORY_24H — score mémoire 10.000/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- PEOPLE-EUR — MEMORY_24H — score mémoire 9.036/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- GNS-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- ENJ-EUR — ACTIVE_NOW — score mémoire 8.334/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- AAVE-EUR — ACTIVE_NOW — score mémoire 8.233/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- IMX-EUR — ACTIVE_NOW — score mémoire 8.196/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- SOSO-EUR — MEMORY_24H — score mémoire 8.156/10 — sources ACCELERATION — MEMORY_ONLY
- HUMA-EUR — ACTIVE_NOW — score mémoire 8.115/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- CSPR-EUR — MEMORY_24H — score mémoire 7.942/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- FLUID-EUR — ACTIVE_NOW — score mémoire 7.935/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY

## Audit des plus fortes hausses

- SAND-EUR +46.87% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- GALA-EUR +15.87% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- ATH-EUR +12.91% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- MANA-EUR +12.03% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- ENJ-EUR +10.55% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- APE-EUR +10.24% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- NOS-EUR +9.24% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- SPK-EUR +8.14% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- WLD-EUR +8.03% — DETECTED_EARLY — couche NONE — action NONE
- INIT-EUR +7.76% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE

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
