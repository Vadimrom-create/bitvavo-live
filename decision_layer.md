# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-28T22:56:48.742371+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : VIRTUAL-EUR | action ACHETE_MAINTENANT | opportunité 8.564 | entrée 7.200 | trend 9.000 | rang 8.244
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : XLM-EUR | action PLACE_LIMITE_PASSIVE | opportunité 7.499 | entrée 6.250 | trend 8.450 | rang 7.481
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : AZTEC-EUR | action LATENT_ACCELERATOR | opportunité 8.074 | entrée 5.100 | trend 8.900 | rang 7.728
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : XDC-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.050 | entrée 6.400 | trend 9.000 | rang 7.945
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Tous les achats immédiats

1. VIRTUAL-EUR — ACHETE_MAINTENANT — rank 8.244 — opportunité 8.564 — entrée 7.200 — trend 9.000
2. ETC-EUR — ACHETE_MAINTENANT — rank 7.740 — opportunité 9.005 — entrée 7.400 — trend 7.400

## Top cross-sectionnel — aperçu non exhaustif

Ce top est une vue courte multi-buckets. Il ne doit jamais être utilisé comme liste exhaustive des achats immédiats.
1. VIRTUAL-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.244
2. XDC-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.945
3. RUNE-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.888

## Accélération indépendante

- NMR-EUR — CONFIRMED_ACCELERATION — score 7.508/10 — DETECTED_BUT_TOO_LATE
- RARE-EUR — BUILDING_ACCELERATION — score 5.466/10 — DETECTED_BUT_TOO_LATE
- PEAQ-EUR — BUILDING_ACCELERATION — score 5.395/10 — DETECTED_BUT_TOO_LATE
- RSR-EUR — BUILDING_ACCELERATION — score 5.246/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- XDC-EUR — BUILDING_ACCELERATION — score 5.151/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- ICX-EUR — BUILDING_ACCELERATION — score 5.084/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- LPT-EUR — BUILDING_ACCELERATION — score 4.802/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- ZRC-EUR — MEMORY_24H — score mémoire 9.275/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- PUFFER-EUR — MEMORY_24H — score mémoire 9.062/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- ZEUS-EUR — MEMORY_24H — score mémoire 8.844/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- VIRTUAL-EUR — ACTIVE_NOW — score mémoire 8.244/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- XDC-EUR — ACTIVE_NOW — score mémoire 7.945/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- RUNE-EUR — ACTIVE_NOW — score mémoire 7.888/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- LINK-EUR — ACTIVE_NOW — score mémoire 7.879/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- W-EUR — ACTIVE_NOW — score mémoire 7.809/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- U-EUR — MEMORY_24H — score mémoire 7.773/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- GRAM-EUR — ACTIVE_NOW — score mémoire 7.742/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY

## Audit des plus fortes hausses

- NMR-EUR +43.30% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- HBAR-EUR +30.37% — DETECTED_EARLY — couche NONE — action NONE
- ALGO-EUR +14.30% — DETECTED_EARLY — couche NONE — action NONE
- MIOTA-EUR +9.90% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- IKA-EUR +9.20% — DETECTED_TOO_LATE — couche NONE — action INTERPRETATION
- LINK-EUR +8.92% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- AZTEC-EUR +6.54% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- 0G-EUR +6.41% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- NPC-EUR +5.80% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- CAP-EUR +5.63% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE

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
