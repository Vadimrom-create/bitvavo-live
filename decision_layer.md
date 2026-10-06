# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-10-06T16:01:58.529012+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : MAGIC-EUR | action PLACE_LIMITE_PASSIVE | opportunité 7.401 | entrée 6.100 | trend 8.600 | rang 6.828
  - Strong structure but imperfect current entry; prefer passive execution. High extension/chase reduces rank but does not erase the setup.
- **MEILLEUR_LATENT_ACCELERATOR** : API3-EUR | action LATENT_ACCELERATOR | opportunité 7.415 | entrée 5.100 | trend 8.950 | rang 7.070
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : RENDER-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 7.630 | entrée 7.150 | trend 8.950 | rang 7.581
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Tous les achats immédiats

Aucun ACHETE_MAINTENANT dans le classement complet.

## Top cross-sectionnel — aperçu non exhaustif

Ce top est une vue courte multi-buckets. Il ne doit jamais être utilisé comme liste exhaustive des achats immédiats.
1. RENDER-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.581
2. ADA-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.566
3. BAT-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.446

## Accélération indépendante

- WELL-EUR — CONFIRMED_ACCELERATION — score 10.000/10 — DETECTED_BUT_TOO_LATE
- FLUX-EUR — CONFIRMED_ACCELERATION — score 7.206/10 — DETECTED_BUT_TOO_LATE
- PARTI-EUR — BUILDING_ACCELERATION — score 6.473/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- HAEDAL-EUR — BUILDING_ACCELERATION — score 6.368/10 — DETECTED_BUT_TOO_LATE
- CAT-EUR — BUILDING_ACCELERATION — score 5.768/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- WELL-EUR — ACTIVE_NOW — score mémoire 10.000/10 — sources ACCELERATION, V4 — DETECTED_BUT_TOO_LATE
- UMA-EUR — MEMORY_24H — score mémoire 9.443/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- ARX-EUR — MEMORY_24H — score mémoire 8.155/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- XMN-EUR — MEMORY_DECAY_24_72H — score mémoire 7.909/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- SWEAT-EUR — MEMORY_DECAY_24_72H — score mémoire 7.885/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- ICP-EUR — MEMORY_24H — score mémoire 7.875/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- ACT-EUR — MEMORY_DECAY_24_72H — score mémoire 7.873/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- TREAD-EUR — MEMORY_DECAY_24_72H — score mémoire 7.712/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- RENDER-EUR — ACTIVE_NOW — score mémoire 7.581/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- ADA-EUR — ACTIVE_NOW — score mémoire 7.566/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY

## Audit des plus fortes hausses

- ZEUS-EUR +102.65% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- RLC-EUR +47.19% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- NMR-EUR +44.46% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- ORCA-EUR +32.62% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- CAP-EUR +29.76% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- WELL-EUR +18.09% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- C98-EUR +16.76% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- VTHO-EUR +16.12% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- FLUX-EUR +15.91% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- TRB-EUR +12.77% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE

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
