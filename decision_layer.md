# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-10-17T01:32:09.526731+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : INJ-EUR | action ACHETE_MAINTENANT | opportunité 8.397 | entrée 6.950 | trend 8.900 | rang 7.909
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : EDU-EUR | action PLACE_LIMITE_PASSIVE | opportunité 7.603 | entrée 6.700 | trend 8.100 | rang 7.204
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : aucun candidat matériel
- **MEILLEUR_PULLBACK_REENTRY** : METIS-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.111 | entrée 5.550 | trend 8.900 | rang 7.180
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Tous les achats immédiats

1. INJ-EUR — ACHETE_MAINTENANT — rank 7.909 — opportunité 8.397 — entrée 6.950 — trend 8.900

## Top cross-sectionnel — aperçu non exhaustif

Ce top est une vue courte multi-buckets. Il ne doit jamais être utilisé comme liste exhaustive des achats immédiats.
1. INJ-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 7.909
2. EDU-EUR — MEILLEURE_LIMITE_PASSIVE — PLACE_LIMITE_PASSIVE — rank 7.204
3. METIS-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.180

## Accélération indépendante

- CPOOL-EUR — BUILDING_ACCELERATION — score 5.568/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- DODO-EUR — BUILDING_ACCELERATION — score 5.311/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- AMP-EUR — BUILDING_ACCELERATION — score 4.876/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- LMWR-EUR — BUILDING_ACCELERATION — score 4.765/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- BTT-EUR — MEMORY_24H — score mémoire 8.833/10 — sources ACCELERATION — MEMORY_ONLY
- ZRO-EUR — MEMORY_DECAY_24_72H — score mémoire 8.641/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- PUFFER-EUR — MEMORY_DECAY_24_72H — score mémoire 8.063/10 — sources ACCELERATION — MEMORY_ONLY
- INJ-EUR — ACTIVE_NOW — score mémoire 7.909/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- EDGE-EUR — MEMORY_DECAY_24_72H — score mémoire 7.790/10 — sources ACCELERATION — MEMORY_ONLY
- ETHFI-EUR — MEMORY_DECAY_24_72H — score mémoire 7.364/10 — sources ACCELERATION — MEMORY_ONLY
- EDU-EUR — ACTIVE_NOW — score mémoire 7.204/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- METIS-EUR — ACTIVE_NOW — score mémoire 7.180/10 — sources DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- LAPTOP-EUR — MEMORY_24H — score mémoire 7.122/10 — sources ACCELERATION — MEMORY_ONLY
- KMNO-EUR — ACTIVE_NOW — score mémoire 7.094/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY

## Audit des plus fortes hausses

- ICNT-EUR +31.65% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- TIA-EUR +15.84% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- AMP-EUR +15.63% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- DUSK-EUR +13.78% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- METIS-EUR +10.27% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE
- RAD-EUR +10.12% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- MEGA-EUR +8.17% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE
- PHA-EUR +7.40% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- CTR-EUR +6.91% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE
- RECALL-EUR +6.76% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE

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
