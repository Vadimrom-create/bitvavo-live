# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-28T19:03:47.817472+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : XLM-EUR | action ACHETE_MAINTENANT | opportunité 9.364 | entrée 7.700 | trend 8.550 | rang 8.268
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : SEI-EUR | action PLACE_LIMITE_PASSIVE | opportunité 8.071 | entrée 5.800 | trend 8.600 | rang 7.479
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : GRT-EUR | action LATENT_ACCELERATOR | opportunité 7.902 | entrée 5.200 | trend 7.900 | rang 7.103
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : JUP-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 9.155 | entrée 7.150 | trend 7.900 | rang 8.071
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Tous les achats immédiats

1. XLM-EUR — ACHETE_MAINTENANT — rank 8.268 — opportunité 9.364 — entrée 7.700 — trend 8.550

## Top cross-sectionnel — aperçu non exhaustif

Ce top est une vue courte multi-buckets. Il ne doit jamais être utilisé comme liste exhaustive des achats immédiats.
1. XLM-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.268
2. JUP-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.071
3. SENT-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.943

## Accélération indépendante

- BTT-EUR — BUILDING_ACCELERATION — score 5.957/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- NMR-EUR — BUILDING_ACCELERATION — score 5.892/10 — DETECTED_BUT_TOO_LATE
- DOS-EUR — BUILDING_ACCELERATION — score 5.772/10 — DETECTED_BUT_TOO_LATE
- QNT-EUR — BUILDING_ACCELERATION — score 5.630/10 — DETECTED_BUT_TOO_LATE
- LINEA-EUR — BUILDING_ACCELERATION — score 5.188/10 — DETECTED_BUT_TOO_LATE
- PONKE-EUR — BUILDING_ACCELERATION — score 5.151/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- LAPTOP-EUR — BUILDING_ACCELERATION — score 4.806/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- XLM-EUR — ACTIVE_NOW — score mémoire 8.268/10 — sources ACCELERATION, DECISION_LAYER, V4 — BUYABLE_NOW
- PUFFER-EUR — MEMORY_24H — score mémoire 9.062/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- ZEUS-EUR — MEMORY_24H — score mémoire 8.844/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- ACX-EUR — MEMORY_24H — score mémoire 8.120/10 — sources ACCELERATION — MEMORY_ONLY
- JUP-EUR — ACTIVE_NOW — score mémoire 8.071/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- SENT-EUR — ACTIVE_NOW — score mémoire 7.943/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- VIRTUAL-EUR — ACTIVE_NOW — score mémoire 7.928/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- GRAM-EUR — ACTIVE_NOW — score mémoire 7.841/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- AZTEC-EUR — ACTIVE_NOW — score mémoire 7.835/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- LINK-EUR — ACTIVE_NOW — score mémoire 7.796/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY

## Audit des plus fortes hausses

- HBAR-EUR +34.41% — DETECTED_EARLY — couche NONE — action NONE
- QNT-EUR +27.30% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ALGO-EUR +12.30% — DETECTED_EARLY — couche NONE — action NONE
- XDC-EUR +12.20% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- NMR-EUR +11.04% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- IKA-EUR +10.55% — DETECTED_TOO_LATE — couche NONE — action INTERPRETATION
- MIOTA-EUR +9.35% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- LINK-EUR +7.63% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- XLM-EUR +7.50% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- LINEA-EUR +5.84% — DETECTED_EARLY — couche NONE — action INTERPRETATION

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
