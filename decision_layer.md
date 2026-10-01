# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-10-01T08:49:30.814088+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : AAVE-EUR | action ACHETE_MAINTENANT | opportunité 8.059 | entrée 6.850 | trend 8.700 | rang 7.860
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : DRIFT-EUR | action PLACE_LIMITE_PASSIVE | opportunité 7.556 | entrée 6.100 | trend 8.000 | rang 7.291
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : DIA-EUR | action LATENT_ACCELERATOR | opportunité 7.970 | entrée 5.600 | trend 8.500 | rang 7.465
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : XDC-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.130 | entrée 7.150 | trend 8.700 | rang 7.955
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Tous les achats immédiats

1. AAVE-EUR — ACHETE_MAINTENANT — rank 7.860 — opportunité 8.059 — entrée 6.850 — trend 8.700

## Top cross-sectionnel — aperçu non exhaustif

Ce top est une vue courte multi-buckets. Il ne doit jamais être utilisé comme liste exhaustive des achats immédiats.
1. XDC-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.955
2. ALICE-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.939
3. AAVE-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 7.860

## Accélération indépendante

- NOM-EUR — CONFIRMED_ACCELERATION — score 9.086/10 — DETECTED_BUT_TOO_LATE
- CTR-EUR — CONFIRMED_ACCELERATION — score 9.026/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- FUEL-EUR — BUILDING_ACCELERATION — score 6.447/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- ALICE-EUR — BUILDING_ACCELERATION — score 5.812/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- CAP-EUR — MEMORY_24H — score mémoire 9.090/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- NOM-EUR — ACTIVE_NOW — score mémoire 9.086/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- CTR-EUR — ACTIVE_NOW — score mémoire 9.026/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- ICX-EUR — MEMORY_24H — score mémoire 8.736/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- ARPA-EUR — MEMORY_24H — score mémoire 8.595/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- TRAC-EUR — MEMORY_24H — score mémoire 8.542/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- PONKE-EUR — MEMORY_24H — score mémoire 8.400/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- XDC-EUR — ACTIVE_NOW — score mémoire 7.955/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- ALICE-EUR — ACTIVE_NOW — score mémoire 7.939/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- AAVE-EUR — ACTIVE_NOW — score mémoire 7.860/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY

## Audit des plus fortes hausses

- CT-EUR +52.13% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- NOM-EUR +47.90% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- MOVR-EUR +43.45% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- STX-EUR +24.26% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- TRAC-EUR +22.36% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- CAP-EUR +19.92% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- MON-EUR +19.76% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- DUSK-EUR +17.69% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- NOS-EUR +17.05% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- JASMY-EUR +16.02% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION

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
