# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-10-16T21:01:37.289498+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : EDU-EUR | action PLACE_LIMITE_PASSIVE | opportunité 7.797 | entrée 6.200 | trend 8.750 | rang 7.484
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : aucun candidat matériel
- **MEILLEUR_PULLBACK_REENTRY** : INJ-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 7.683 | entrée 6.100 | trend 8.950 | rang 7.548
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Tous les achats immédiats

Aucun ACHETE_MAINTENANT dans le classement complet.

## Top cross-sectionnel — aperçu non exhaustif

Ce top est une vue courte multi-buckets. Il ne doit jamais être utilisé comme liste exhaustive des achats immédiats.
1. INJ-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.548
2. EDU-EUR — MEILLEURE_LIMITE_PASSIVE — PLACE_LIMITE_PASSIVE — rank 7.484
3. PYTH-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.136

## Accélération indépendante

- BTT-EUR — CONFIRMED_ACCELERATION — score 8.833/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- LAPTOP-EUR — CONFIRMED_ACCELERATION — score 7.122/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- ELSA-EUR — BUILDING_ACCELERATION — score 5.864/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- SIGN-EUR — BUILDING_ACCELERATION — score 5.494/10 — DETECTED_BUT_TOO_LATE
- ACX-EUR — BUILDING_ACCELERATION — score 5.009/10 — DETECTED_BUT_TOO_LATE
- CT-EUR — BUILDING_ACCELERATION — score 4.951/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- GNS-EUR — MEMORY_DECAY_24_72H — score mémoire 9.372/10 — sources ACCELERATION — MEMORY_ONLY
- BTT-EUR — ACTIVE_NOW — score mémoire 8.833/10 — sources ACCELERATION — WATCH_ONLY
- ZRO-EUR — MEMORY_24H — score mémoire 8.832/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- ETHFI-EUR — MEMORY_DECAY_24_72H — score mémoire 8.246/10 — sources ACCELERATION — MEMORY_ONLY
- PUFFER-EUR — MEMORY_24H — score mémoire 8.241/10 — sources ACCELERATION — MEMORY_ONLY
- BAT-EUR — MEMORY_DECAY_24_72H — score mémoire 8.067/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- EDGE-EUR — MEMORY_24H — score mémoire 7.962/10 — sources ACCELERATION — MEMORY_ONLY
- BANANA-EUR — MEMORY_DECAY_24_72H — score mémoire 7.905/10 — sources ACCELERATION — MEMORY_ONLY
- BREV-EUR — MEMORY_DECAY_24_72H — score mémoire 7.905/10 — sources ACCELERATION — MEMORY_ONLY
- COW-EUR — MEMORY_DECAY_24_72H — score mémoire 7.825/10 — sources ACCELERATION — MEMORY_ONLY

## Audit des plus fortes hausses

- ICNT-EUR +26.02% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- RAD-EUR +16.19% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- TIA-EUR +13.87% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- DUSK-EUR +10.18% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- AMP-EUR +9.33% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- POND-EUR +8.34% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ALIGN-EUR +8.17% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- STRAX-EUR +7.23% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- BEAM-EUR +6.51% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- SHELL-EUR +5.57% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE

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
