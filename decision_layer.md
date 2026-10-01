# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-10-01T08:01:08.310441+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : QNT-EUR | action ACHETE_MAINTENANT | opportunité 8.156 | entrée 7.400 | trend 7.550 | rang 7.235
  - V4 buy-ready with acceptable current entry; no structural veto. High extension/chase is retained as risk context, not an automatic veto.
- **MEILLEURE_LIMITE_PASSIVE** : XDC-EUR | action PLACE_LIMITE_PASSIVE | opportunité 7.478 | entrée 6.600 | trend 8.700 | rang 7.600
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : AVNT-EUR | action LATENT_ACCELERATOR | opportunité 8.137 | entrée 5.200 | trend 8.250 | rang 7.577
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : KSM-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.192 | entrée 6.350 | trend 9.200 | rang 8.064
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Tous les achats immédiats

1. QNT-EUR — ACHETE_MAINTENANT — rank 7.235 — opportunité 8.156 — entrée 7.400 — trend 7.550

## Top cross-sectionnel — aperçu non exhaustif

Ce top est une vue courte multi-buckets. Il ne doit jamais être utilisé comme liste exhaustive des achats immédiats.
1. KSM-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.064
2. ALICE-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.010
3. ICP-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.848

## Accélération indépendante

- JASMY-EUR — CONFIRMED_ACCELERATION — score 8.810/10 — DETECTED_BUT_TOO_LATE
- TOWNS-EUR — BUILDING_ACCELERATION — score 6.376/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- HUMA-EUR — BUILDING_ACCELERATION — score 5.895/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- QNT-EUR — BUILDING_ACCELERATION — score 5.580/10 — DETECTED_BUT_TOO_LATE
- NOM-EUR — BUILDING_ACCELERATION — score 4.821/10 — DETECTED_BUT_TOO_LATE
- CT-EUR — BUILDING_ACCELERATION — score 4.775/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- BTT-EUR — MEMORY_24H — score mémoire 9.581/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- CAP-EUR — MEMORY_24H — score mémoire 9.090/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- CTR-EUR — MEMORY_24H — score mémoire 8.902/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- JASMY-EUR — ACTIVE_NOW — score mémoire 8.810/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- ICX-EUR — MEMORY_24H — score mémoire 8.736/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- ARPA-EUR — MEMORY_24H — score mémoire 8.595/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- PONKE-EUR — MEMORY_24H — score mémoire 8.400/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- KSM-EUR — ACTIVE_NOW — score mémoire 8.064/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- ALICE-EUR — ACTIVE_NOW — score mémoire 8.010/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- ICP-EUR — ACTIVE_NOW — score mémoire 7.848/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY

## Audit des plus fortes hausses

- MOVR-EUR +69.68% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- CT-EUR +53.77% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- NOM-EUR +37.65% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- STX-EUR +27.67% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- CAP-EUR +20.42% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- MON-EUR +18.15% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- NOS-EUR +17.00% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- TRAC-EUR +14.50% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- ESP-EUR +12.12% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE
- RED-EUR +11.74% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION

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
