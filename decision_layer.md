# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-10-02T12:23:29.309291+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : WLD-EUR | action ACHETE_MAINTENANT | opportunité 9.329 | entrée 7.850 | trend 8.400 | rang 8.340
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : AZTEC-EUR | action PLACE_LIMITE_PASSIVE | opportunité 7.744 | entrée 6.200 | trend 8.150 | rang 7.460
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : HUMA-EUR | action LATENT_ACCELERATOR | opportunité 7.860 | entrée 5.300 | trend 8.650 | rang 7.558
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : HBAR-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.495 | entrée 7.850 | trend 8.400 | rang 8.043
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Tous les achats immédiats

1. WLD-EUR — ACHETE_MAINTENANT — rank 8.340 — opportunité 9.329 — entrée 7.850 — trend 8.400
2. ALGO-EUR — ACHETE_MAINTENANT — rank 7.919 — opportunité 8.070 — entrée 7.150 — trend 8.650
3. ZRO-EUR — ACHETE_MAINTENANT — rank 7.700 — opportunité 8.488 — entrée 7.000 — trend 8.800

## Top cross-sectionnel — aperçu non exhaustif

Ce top est une vue courte multi-buckets. Il ne doit jamais être utilisé comme liste exhaustive des achats immédiats.
1. WLD-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.340
2. HBAR-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.043
3. IMX-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.961

## Accélération indépendante

- HNT-EUR — CONFIRMED_ACCELERATION — score 9.345/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- ENJ-EUR — CONFIRMED_ACCELERATION — score 8.534/10 — DETECTED_BUT_TOO_LATE
- TRAC-EUR — CONFIRMED_ACCELERATION — score 6.950/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- TAI-EUR — CONFIRMED_ACCELERATION — score 6.745/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- RON-EUR — BUILDING_ACCELERATION — score 6.408/10 — DETECTED_BUT_TOO_LATE
- MAVIA-EUR — BUILDING_ACCELERATION — score 6.375/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- WLD-EUR — BUILDING_ACCELERATION — score 6.314/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- POND-EUR — BUILDING_ACCELERATION — score 6.276/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- HMSTR-EUR — BUILDING_ACCELERATION — score 6.174/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- SPK-EUR — BUILDING_ACCELERATION — score 5.821/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- WLD-EUR — ACTIVE_NOW — score mémoire 8.340/10 — sources ACCELERATION, DECISION_LAYER, V4 — BUYABLE_NOW
- EDGE-EUR — MEMORY_24H — score mémoire 10.000/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- HNT-EUR — ACTIVE_NOW — score mémoire 9.345/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- TREAD-EUR — MEMORY_24H — score mémoire 9.258/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- OPEN-EUR — MEMORY_24H — score mémoire 9.112/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- PEOPLE-EUR — MEMORY_24H — score mémoire 9.036/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- U-EUR — MEMORY_24H — score mémoire 8.740/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- ENJ-EUR — ACTIVE_NOW — score mémoire 8.534/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- OSMO-EUR — MEMORY_24H — score mémoire 8.342/10 — sources ACCELERATION — MEMORY_ONLY
- ZRC-EUR — MEMORY_24H — score mémoire 8.257/10 — sources ACCELERATION, V4 — MEMORY_ONLY

## Audit des plus fortes hausses

- SAND-EUR +66.26% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ENJ-EUR +36.08% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- GTC-EUR +21.17% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- MANA-EUR +20.82% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- SKY-EUR +18.22% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- GALA-EUR +16.38% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- NOS-EUR +15.98% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- MAGIC-EUR +15.70% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- SUPER-EUR +14.30% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- CT-EUR +14.22% — DETECTED_EARLY — couche NONE — action INTERPRETATION

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
