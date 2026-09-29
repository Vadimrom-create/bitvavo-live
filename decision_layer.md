# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-29T01:31:55.059662+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : XLM-EUR | action PLACE_LIMITE_PASSIVE | opportunité 7.683 | entrée 6.700 | trend 8.800 | rang 7.746
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : MIOTA-EUR | action LATENT_ACCELERATOR | opportunité 7.471 | entrée 5.100 | trend 8.900 | rang 7.493
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : VIRTUAL-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.902 | entrée 5.800 | trend 9.000 | rang 8.271
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Tous les achats immédiats

Aucun ACHETE_MAINTENANT dans le classement complet.

## Top cross-sectionnel — aperçu non exhaustif

Ce top est une vue courte multi-buckets. Il ne doit jamais être utilisé comme liste exhaustive des achats immédiats.
1. VIRTUAL-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.271
2. XDC-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.019
3. RUNE-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.783

## Accélération indépendante

- IKA-EUR — BUILDING_ACCELERATION — score 6.426/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- NMR-EUR — BUILDING_ACCELERATION — score 5.191/10 — DETECTED_BUT_TOO_LATE
- CAP-EUR — BUILDING_ACCELERATION — score 5.076/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- PUFFER-EUR — MEMORY_24H — score mémoire 9.062/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- ZEUS-EUR — MEMORY_24H — score mémoire 8.844/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- IMU-EUR — MEMORY_24H — score mémoire 8.632/10 — sources ACCELERATION — MEMORY_ONLY
- VIRTUAL-EUR — ACTIVE_NOW — score mémoire 8.271/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- XDC-EUR — ACTIVE_NOW — score mémoire 8.019/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- AIXBT-EUR — MEMORY_24H — score mémoire 7.962/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- RUNE-EUR — ACTIVE_NOW — score mémoire 7.783/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- U-EUR — MEMORY_24H — score mémoire 7.773/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- XLM-EUR — ACTIVE_NOW — score mémoire 7.746/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- W-EUR — ACTIVE_NOW — score mémoire 7.738/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY

## Audit des plus fortes hausses

- NMR-EUR +34.14% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- HBAR-EUR +21.98% — DETECTED_EARLY — couche NONE — action NONE
- ALGO-EUR +10.01% — DETECTED_EARLY — couche NONE — action NONE
- CAP-EUR +9.57% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE
- IKA-EUR +8.87% — DETECTED_TOO_LATE — couche NONE — action INTERPRETATION
- 0G-EUR +8.66% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- LINK-EUR +8.13% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- ZBCN-EUR +7.48% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- CRV-EUR +6.48% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- NPC-EUR +4.98% — DETECTED_EARLY — couche NONE — action INTERPRETATION

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
