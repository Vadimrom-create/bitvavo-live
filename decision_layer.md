# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-10-03T09:21:41.370288+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : AAVE-EUR | action ACHETE_MAINTENANT | opportunité 8.397 | entrée 7.650 | trend 8.900 | rang 8.140
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : GRASS-EUR | action PLACE_LIMITE_PASSIVE | opportunité 7.660 | entrée 6.250 | trend 8.000 | rang 7.247
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : INIT-EUR | action LATENT_ACCELERATOR | opportunité 7.419 | entrée 5.350 | trend 8.800 | rang 7.453
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : IMX-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.304 | entrée 6.350 | trend 9.200 | rang 7.999
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Tous les achats immédiats

1. AAVE-EUR — ACHETE_MAINTENANT — rank 8.140 — opportunité 8.397 — entrée 7.650 — trend 8.900
2. WLD-EUR — ACHETE_MAINTENANT — rank 7.742 — opportunité 8.128 — entrée 7.050 — trend 8.250
3. SUPER-EUR — ACHETE_MAINTENANT — rank 7.595 — opportunité 8.370 — entrée 7.050 — trend 8.800

## Top cross-sectionnel — aperçu non exhaustif

Ce top est une vue courte multi-buckets. Il ne doit jamais être utilisé comme liste exhaustive des achats immédiats.
1. AAVE-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.140
2. IMX-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.999
3. FLUID-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.925

## Accélération indépendante

- ARK-EUR — CONFIRMED_ACCELERATION — score 8.048/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- MLN-EUR — CONFIRMED_ACCELERATION — score 7.109/10 — DETECTED_BUT_TOO_LATE
- HFT-EUR — BUILDING_ACCELERATION — score 6.000/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- WLD-EUR — ACTIVE_NOW — score mémoire 7.742/10 — sources ACCELERATION, DECISION_LAYER, V4 — BUYABLE_NOW
- EDGE-EUR — MEMORY_DECAY_24_72H — score mémoire 9.098/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- MOVE-EUR — MEMORY_24H — score mémoire 8.978/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- PEOPLE-EUR — MEMORY_DECAY_24_72H — score mémoire 8.957/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- SOSO-EUR — MEMORY_24H — score mémoire 8.156/10 — sources ACCELERATION — MEMORY_ONLY
- AAVE-EUR — ACTIVE_NOW — score mémoire 8.140/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- ARK-EUR — ACTIVE_NOW — score mémoire 8.048/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- IMX-EUR — ACTIVE_NOW — score mémoire 7.999/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- FLUID-EUR — ACTIVE_NOW — score mémoire 7.925/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- CSPR-EUR — MEMORY_DECAY_24_72H — score mémoire 7.822/10 — sources ACCELERATION, V4 — MEMORY_ONLY

## Audit des plus fortes hausses

- SAND-EUR +16.30% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ATH-EUR +13.20% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- FOLD-EUR +12.79% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- QNT-EUR +11.52% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- HFT-EUR +11.17% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- CAP-EUR +7.81% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- SYN-EUR +7.63% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- SUPER-EUR +7.61% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE
- WLD-EUR +6.31% — DETECTED_EARLY — couche NONE — action NONE
- IMX-EUR +6.26% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION

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
