# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-10-02T00:00:23.912183+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : WLD-EUR | action ACHETE_MAINTENANT | opportunité 9.342 | entrée 7.400 | trend 8.400 | rang 8.326
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : C-EUR | action PLACE_LIMITE_PASSIVE | opportunité 7.749 | entrée 6.600 | trend 8.700 | rang 7.693
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : PROM-EUR | action LATENT_ACCELERATOR | opportunité 7.738 | entrée 5.300 | trend 8.950 | rang 7.657
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : AVAX-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.142 | entrée 7.800 | trend 8.700 | rang 8.038
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Tous les achats immédiats

1. WLD-EUR — ACHETE_MAINTENANT — rank 8.326 — opportunité 9.342 — entrée 7.400 — trend 8.400
2. AAVE-EUR — ACHETE_MAINTENANT — rank 8.191 — opportunité 8.426 — entrée 7.200 — trend 9.200

## Top cross-sectionnel — aperçu non exhaustif

Ce top est une vue courte multi-buckets. Il ne doit jamais être utilisé comme liste exhaustive des achats immédiats.
1. WLD-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.326
2. AAVE-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.191
3. AVAX-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.038

## Accélération indépendante

- POND-EUR — CONFIRMED_ACCELERATION — score 10.000/10 — DETECTED_BUT_TOO_LATE
- BEL-EUR — BUILDING_ACCELERATION — score 4.798/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- CPOOL-EUR — MEMORY_24H — score mémoire 10.000/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- POND-EUR — ACTIVE_NOW — score mémoire 10.000/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- ZRC-EUR — MEMORY_24H — score mémoire 8.847/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- OSMO-EUR — MEMORY_24H — score mémoire 8.342/10 — sources ACCELERATION — MEMORY_ONLY
- WLD-EUR — ACTIVE_NOW — score mémoire 8.326/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- AAVE-EUR — ACTIVE_NOW — score mémoire 8.191/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- AGI-EUR — MEMORY_24H — score mémoire 8.119/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- AVAX-EUR — ACTIVE_NOW — score mémoire 8.038/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- U-EUR — MEMORY_24H — score mémoire 8.002/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- REZ-EUR — ACTIVE_NOW — score mémoire 7.955/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY

## Audit des plus fortes hausses

- SWEAT-EUR +121.59% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- GTC-EUR +51.06% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- MOVR-EUR +35.12% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ALICE-EUR +25.82% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- CT-EUR +21.64% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- MEGA-EUR +20.47% — DETECTED_EARLY — couche NONE — action NONE
- NOM-EUR +18.14% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- SYN-EUR +16.55% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- SUPER-EUR +16.36% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- NOS-EUR +14.70% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION

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
