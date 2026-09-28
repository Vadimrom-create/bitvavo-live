# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-28T19:42:27.649855+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : MIOTA-EUR | action PLACE_LIMITE_PASSIVE | opportunité 7.737 | entrée 6.150 | trend 8.900 | rang 7.661
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : LINEA-EUR | action LATENT_ACCELERATOR | opportunité 7.886 | entrée 5.250 | trend 8.550 | rang 7.380
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : AZTEC-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.163 | entrée 6.650 | trend 9.200 | rang 8.027
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Tous les achats immédiats

Aucun ACHETE_MAINTENANT dans le classement complet.

## Top cross-sectionnel — aperçu non exhaustif

Ce top est une vue courte multi-buckets. Il ne doit jamais être utilisé comme liste exhaustive des achats immédiats.
1. AZTEC-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.027
2. LINK-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.861
3. XLM-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.683

## Accélération indépendante

- WMTX-EUR — BUILDING_ACCELERATION — score 6.301/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- ZRC-EUR — BUILDING_ACCELERATION — score 6.169/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- ICX-EUR — BUILDING_ACCELERATION — score 5.127/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- PUFFER-EUR — MEMORY_24H — score mémoire 9.062/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- ZEUS-EUR — MEMORY_24H — score mémoire 8.844/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- XDP-EUR — MEMORY_24H — score mémoire 8.173/10 — sources ACCELERATION — MEMORY_ONLY
- ACX-EUR — MEMORY_24H — score mémoire 8.120/10 — sources ACCELERATION — MEMORY_ONLY
- AZTEC-EUR — ACTIVE_NOW — score mémoire 8.027/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- LINK-EUR — ACTIVE_NOW — score mémoire 7.861/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- U-EUR — MEMORY_24H — score mémoire 7.773/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- WIN-EUR — MEMORY_24H — score mémoire 7.764/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- XLM-EUR — ACTIVE_NOW — score mémoire 7.683/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- NMR-EUR — ACTIVE_NOW — score mémoire 7.667/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE

## Audit des plus fortes hausses

- HBAR-EUR +32.71% — DETECTED_EARLY — couche NONE — action NONE
- QNT-EUR +24.07% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ALGO-EUR +11.09% — DETECTED_EARLY — couche NONE — action NONE
- NMR-EUR +10.81% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- IKA-EUR +9.35% — DETECTED_TOO_LATE — couche NONE — action INTERPRETATION
- XDC-EUR +8.12% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- MIOTA-EUR +7.26% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- LINK-EUR +6.14% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- CAP-EUR +5.38% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE
- PUMP-EUR +5.00% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION

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
