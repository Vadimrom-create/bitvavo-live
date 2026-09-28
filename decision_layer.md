# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-28T23:15:11.333053+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : VIRTUAL-EUR | action ACHETE_MAINTENANT | opportunité 8.567 | entrée 7.200 | trend 9.000 | rang 8.121
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : AZTEC-EUR | action PLACE_LIMITE_PASSIVE | opportunité 8.316 | entrée 6.000 | trend 8.900 | rang 7.844
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : MIOTA-EUR | action LATENT_ACCELERATOR | opportunité 7.588 | entrée 5.150 | trend 8.900 | rang 7.449
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : RUNE-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.228 | entrée 6.150 | trend 8.900 | rang 7.945
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Tous les achats immédiats

1. VIRTUAL-EUR — ACHETE_MAINTENANT — rank 8.121 — opportunité 8.567 — entrée 7.200 — trend 9.000
2. ETC-EUR — ACHETE_MAINTENANT — rank 6.997 — opportunité 7.443 — entrée 6.900 — trend 7.400

## Top cross-sectionnel — aperçu non exhaustif

Ce top est une vue courte multi-buckets. Il ne doit jamais être utilisé comme liste exhaustive des achats immédiats.
1. VIRTUAL-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.121
2. RUNE-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.945
3. W-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.924

## Accélération indépendante

- 0G-EUR — CONFIRMED_ACCELERATION — score 6.845/10 — DETECTED_BUT_TOO_LATE
- EDU-EUR — BUILDING_ACCELERATION — score 5.903/10 — DETECTED_BUT_TOO_LATE
- BAT-EUR — BUILDING_ACCELERATION — score 5.714/10 — DETECTED_BUT_TOO_LATE
- ETHFI-EUR — BUILDING_ACCELERATION — score 5.669/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- SAGA-EUR — BUILDING_ACCELERATION — score 5.123/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- SAFE-EUR — BUILDING_ACCELERATION — score 4.975/10 — DETECTED_BUT_TOO_LATE
- PNUT-EUR — BUILDING_ACCELERATION — score 4.866/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- KSM-EUR — BUILDING_ACCELERATION — score 4.843/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- ZRC-EUR — MEMORY_24H — score mémoire 9.275/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- PUFFER-EUR — MEMORY_24H — score mémoire 9.062/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- ZEUS-EUR — MEMORY_24H — score mémoire 8.844/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- VIRTUAL-EUR — ACTIVE_NOW — score mémoire 8.121/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- RUNE-EUR — ACTIVE_NOW — score mémoire 7.945/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- W-EUR — ACTIVE_NOW — score mémoire 7.924/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- LINK-EUR — ACTIVE_NOW — score mémoire 7.886/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- XDC-EUR — ACTIVE_NOW — score mémoire 7.856/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- AZTEC-EUR — ACTIVE_NOW — score mémoire 7.844/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- U-EUR — MEMORY_24H — score mémoire 7.773/10 — sources ACCELERATION, V4 — MEMORY_ONLY

## Audit des plus fortes hausses

- NMR-EUR +44.24% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- HBAR-EUR +28.97% — DETECTED_EARLY — couche NONE — action NONE
- ALGO-EUR +12.88% — DETECTED_EARLY — couche NONE — action NONE
- 0G-EUR +10.00% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- LINK-EUR +9.50% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- TREAD-EUR +9.13% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- IKA-EUR +8.87% — DETECTED_TOO_LATE — couche NONE — action INTERPRETATION
- MIOTA-EUR +8.75% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- AZTEC-EUR +7.52% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- CAP-EUR +5.96% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE

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
