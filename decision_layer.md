# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-10-11T12:43:37.466450+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : JUP-EUR | action ACHETE_MAINTENANT | opportunité 9.189 | entrée 7.150 | trend 8.200 | rang 8.181
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : AERO-EUR | action PLACE_LIMITE_PASSIVE | opportunité 7.872 | entrée 6.100 | trend 8.850 | rang 7.521
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : AVNT-EUR | action LATENT_ACCELERATOR | opportunité 7.878 | entrée 5.400 | trend 8.450 | rang 7.438
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : C98-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 7.636 | entrée 5.400 | trend 8.650 | rang 7.489
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Tous les achats immédiats

1. JUP-EUR — ACHETE_MAINTENANT — rank 8.181 — opportunité 9.189 — entrée 7.150 — trend 8.200

## Top cross-sectionnel — aperçu non exhaustif

Ce top est une vue courte multi-buckets. Il ne doit jamais être utilisé comme liste exhaustive des achats immédiats.
1. JUP-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.181
2. AERO-EUR — MEILLEURE_LIMITE_PASSIVE — PLACE_LIMITE_PASSIVE — rank 7.521
3. C98-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.489

## Accélération indépendante

- IO-EUR — CONFIRMED_ACCELERATION — score 8.545/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- RON-EUR — CONFIRMED_ACCELERATION — score 8.054/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- BRETT-EUR — BUILDING_ACCELERATION — score 5.729/10 — DETECTED_BUT_TOO_LATE
- YB-EUR — BUILDING_ACCELERATION — score 5.563/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- ZEUS-EUR — BUILDING_ACCELERATION — score 5.514/10 — DETECTED_BUT_TOO_LATE
- RLC-EUR — BUILDING_ACCELERATION — score 5.024/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- GTC-EUR — MEMORY_24H — score mémoire 9.580/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- TREAD-EUR — MEMORY_24H — score mémoire 8.918/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- IO-EUR — ACTIVE_NOW — score mémoire 8.545/10 — sources ACCELERATION — WATCH_ONLY
- JUP-EUR — ACTIVE_NOW — score mémoire 8.181/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- RON-EUR — ACTIVE_NOW — score mémoire 8.054/10 — sources ACCELERATION — WATCH_ONLY
- AERO-EUR — ACTIVE_NOW — score mémoire 7.521/10 — sources DECISION_LAYER, V4 — WATCH_ONLY
- C98-EUR — ACTIVE_NOW — score mémoire 7.489/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- LRC-EUR — MEMORY_DECAY_24_72H — score mémoire 7.478/10 — sources ACCELERATION — MEMORY_ONLY
- AVNT-EUR — ACTIVE_NOW — score mémoire 7.438/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- SENT-EUR — MEMORY_24H — score mémoire 7.432/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY

## Audit des plus fortes hausses

- ZEUS-EUR +62.93% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- STRK-EUR +58.71% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- CHIP-EUR +27.27% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- LUMIA-EUR +24.13% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- TIA-EUR +19.85% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- SENT-EUR +16.12% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- RLC-EUR +15.06% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- S-EUR +14.13% — DETECTED_TOO_LATE — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- ZK-EUR +12.85% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- MAGIC-EUR +11.30% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE

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
