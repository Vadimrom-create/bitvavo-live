# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-10-01T07:22:40.087509+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : FET-EUR | action ACHETE_MAINTENANT | opportunité 8.314 | entrée 7.200 | trend 7.550 | rang 7.394
  - V4 buy-ready with acceptable current entry; no structural veto. High extension/chase is retained as risk context, not an automatic veto.
- **MEILLEURE_LIMITE_PASSIVE** : ENA-EUR | action PLACE_LIMITE_PASSIVE | opportunité 7.714 | entrée 5.900 | trend 8.650 | rang 7.461
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : WOO-EUR | action LATENT_ACCELERATOR | opportunité 7.602 | entrée 4.950 | trend 8.500 | rang 7.380
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : KSM-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.427 | entrée 6.500 | trend 8.950 | rang 7.978
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Tous les achats immédiats

1. FET-EUR — ACHETE_MAINTENANT — rank 7.394 — opportunité 8.314 — entrée 7.200 — trend 7.550
2. QNT-EUR — ACHETE_MAINTENANT — rank 7.212 — opportunité 8.245 — entrée 7.700 — trend 7.550

## Top cross-sectionnel — aperçu non exhaustif

Ce top est une vue courte multi-buckets. Il ne doit jamais être utilisé comme liste exhaustive des achats immédiats.
1. KSM-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.978
2. AAVE-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.885
3. DOT-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.871

## Accélération indépendante

- BTT-EUR — CONFIRMED_ACCELERATION — score 9.581/10 — DETECTED_BUT_TOO_LATE
- ICX-EUR — CONFIRMED_ACCELERATION — score 8.736/10 — DETECTED_BUT_TOO_LATE
- SCR-EUR — CONFIRMED_ACCELERATION — score 8.578/10 — DETECTED_BUT_TOO_LATE
- NOM-EUR — CONFIRMED_ACCELERATION — score 7.956/10 — DETECTED_BUT_TOO_LATE
- DUSK-EUR — CONFIRMED_ACCELERATION — score 7.858/10 — DETECTED_BUT_TOO_LATE
- HUMA-EUR — BUILDING_ACCELERATION — score 6.387/10 — DETECTED_BUT_TOO_LATE
- CNPY-EUR — BUILDING_ACCELERATION — score 5.734/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- TOWNS-EUR — BUILDING_ACCELERATION — score 5.646/10 — DETECTED_BUT_TOO_LATE
- ALICE-EUR — BUILDING_ACCELERATION — score 5.519/10 — DETECTED_BUT_TOO_LATE
- AGLD-EUR — BUILDING_ACCELERATION — score 5.276/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- BTT-EUR — ACTIVE_NOW — score mémoire 9.581/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- CAP-EUR — MEMORY_24H — score mémoire 9.090/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- CTR-EUR — MEMORY_24H — score mémoire 8.902/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- ICX-EUR — ACTIVE_NOW — score mémoire 8.736/10 — sources ACCELERATION, V4 — DETECTED_BUT_TOO_LATE
- ARPA-EUR — MEMORY_24H — score mémoire 8.595/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- SCR-EUR — ACTIVE_NOW — score mémoire 8.578/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- PONKE-EUR — MEMORY_24H — score mémoire 8.400/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- CT-EUR — MEMORY_24H — score mémoire 8.105/10 — sources ACCELERATION — MEMORY_ONLY
- KSM-EUR — ACTIVE_NOW — score mémoire 7.978/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- NOM-EUR — ACTIVE_NOW — score mémoire 7.956/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE

## Audit des plus fortes hausses

- MOVR-EUR +67.66% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- CT-EUR +51.46% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- STX-EUR +29.77% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- MON-EUR +26.40% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- NOM-EUR +25.92% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- TRAC-EUR +23.01% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- NOS-EUR +21.97% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- ICX-EUR +21.73% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- CAP-EUR +21.48% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- ESP-EUR +13.70% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE

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
