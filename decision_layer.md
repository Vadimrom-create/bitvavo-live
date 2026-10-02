# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-10-02T11:57:32.410734+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : WLD-EUR | action ACHETE_MAINTENANT | opportunité 9.008 | entrée 7.800 | trend 8.400 | rang 8.235
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : IMX-EUR | action PLACE_LIMITE_PASSIVE | opportunité 8.038 | entrée 6.100 | trend 8.650 | rang 7.656
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : HUMA-EUR | action LATENT_ACCELERATOR | opportunité 8.136 | entrée 5.550 | trend 8.650 | rang 7.763
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : MON-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.375 | entrée 6.400 | trend 8.550 | rang 7.868
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Tous les achats immédiats

1. WLD-EUR — ACHETE_MAINTENANT — rank 8.235 — opportunité 9.008 — entrée 7.800 — trend 8.400

## Top cross-sectionnel — aperçu non exhaustif

Ce top est une vue courte multi-buckets. Il ne doit jamais être utilisé comme liste exhaustive des achats immédiats.
1. WLD-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.235
2. MON-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.868
3. MIOTA-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.861

## Accélération indépendante

- SAND-EUR — CONFIRMED_ACCELERATION — score 8.000/10 — DETECTED_BUT_TOO_LATE
- NOS-EUR — CONFIRMED_ACCELERATION — score 7.672/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- ENJ-EUR — CONFIRMED_ACCELERATION — score 6.757/10 — DETECTED_BUT_TOO_LATE
- MASK-EUR — CONFIRMED_ACCELERATION — score 6.590/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- GALA-EUR — BUILDING_ACCELERATION — score 6.180/10 — DETECTED_BUT_TOO_LATE
- APE-EUR — BUILDING_ACCELERATION — score 5.623/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- EDGE-EUR — MEMORY_24H — score mémoire 10.000/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- TREAD-EUR — MEMORY_24H — score mémoire 9.258/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- OPEN-EUR — MEMORY_24H — score mémoire 9.112/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- PEOPLE-EUR — MEMORY_24H — score mémoire 9.036/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- U-EUR — MEMORY_24H — score mémoire 8.740/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- OSMO-EUR — MEMORY_24H — score mémoire 8.342/10 — sources ACCELERATION — MEMORY_ONLY
- ZRC-EUR — MEMORY_24H — score mémoire 8.257/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- WLD-EUR — ACTIVE_NOW — score mémoire 8.235/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- SAND-EUR — ACTIVE_NOW — score mémoire 8.000/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- GIGA-EUR — MEMORY_24H — score mémoire 7.987/10 — sources ACCELERATION, V4 — MEMORY_ONLY

## Audit des plus fortes hausses

- SAND-EUR +64.43% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- CT-EUR +23.08% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- GTC-EUR +22.88% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- MANA-EUR +22.26% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- SKY-EUR +18.87% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- MAGIC-EUR +17.61% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- SUPER-EUR +15.44% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- GALA-EUR +15.13% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- SCR-EUR +14.86% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ENJ-EUR +13.35% — DETECTED_EARLY — couche NONE — action INTERPRETATION

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
