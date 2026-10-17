# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-10-17T06:04:50.202399+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : aucun candidat matériel
- **MEILLEUR_LATENT_ACCELERATOR** : aucun candidat matériel
- **MEILLEUR_PULLBACK_REENTRY** : INJ-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.273 | entrée 6.200 | trend 8.900 | rang 7.777
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Tous les achats immédiats

Aucun ACHETE_MAINTENANT dans le classement complet.

## Top cross-sectionnel — aperçu non exhaustif

Ce top est une vue courte multi-buckets. Il ne doit jamais être utilisé comme liste exhaustive des achats immédiats.
1. INJ-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.777
2. EIGEN-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.165
3. DUSK-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.032

## Accélération indépendante

- EPIC-EUR — CONFIRMED_ACCELERATION — score 10.000/10 — DETECTED_BUT_TOO_LATE
- AXL-EUR — CONFIRMED_ACCELERATION — score 9.132/10 — DETECTED_BUT_TOO_LATE
- CAP-EUR — BUILDING_ACCELERATION — score 6.311/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- GNS-EUR — BUILDING_ACCELERATION — score 6.200/10 — DETECTED_BUT_TOO_LATE
- AVA-EUR — BUILDING_ACCELERATION — score 5.761/10 — DETECTED_BUT_TOO_LATE
- U-EUR — BUILDING_ACCELERATION — score 5.479/10 — DETECTED_BUT_TOO_LATE
- NIL-EUR — BUILDING_ACCELERATION — score 4.814/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- EPIC-EUR — ACTIVE_NOW — score mémoire 10.000/10 — sources ACCELERATION — DETECTED_BUT_TOO_LATE
- AXL-EUR — ACTIVE_NOW — score mémoire 9.132/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- BTT-EUR — MEMORY_24H — score mémoire 8.833/10 — sources ACCELERATION — MEMORY_ONLY
- ZRO-EUR — MEMORY_DECAY_24_72H — score mémoire 7.805/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- INJ-EUR — ACTIVE_NOW — score mémoire 7.777/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- METIS-EUR — ACTIVE_NOW — score mémoire 7.360/10 — sources DECISION_LAYER, V4 — WATCH_ONLY
- PUFFER-EUR — MEMORY_DECAY_24_72H — score mémoire 7.283/10 — sources ACCELERATION — MEMORY_ONLY
- EIGEN-EUR — ACTIVE_NOW — score mémoire 7.165/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- LAPTOP-EUR — MEMORY_24H — score mémoire 7.122/10 — sources ACCELERATION — MEMORY_ONLY
- DODO-EUR — ACTIVE_NOW — score mémoire 7.077/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY

## Audit des plus fortes hausses

- ICNT-EUR +35.88% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- GTC-EUR +26.37% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- EPIC-EUR +25.47% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- TIA-EUR +19.65% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- EIGEN-EUR +11.14% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- DUSK-EUR +8.95% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- ELSA-EUR +8.44% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE
- RAD-EUR +7.82% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- AMP-EUR +7.19% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- LIGHTER-EUR +6.94% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE

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
