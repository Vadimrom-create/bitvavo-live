# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-10-19T01:51:27.253356+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : WAL-EUR | action PLACE_LIMITE_PASSIVE | opportunité 7.514 | entrée 6.050 | trend 7.550 | rang 6.582
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : aucun candidat matériel
- **MEILLEUR_PULLBACK_REENTRY** : ALT-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 7.852 | entrée 4.800 | trend 8.700 | rang 7.071
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Tous les achats immédiats

Aucun ACHETE_MAINTENANT dans le classement complet.

## Top cross-sectionnel — aperçu non exhaustif

Ce top est une vue courte multi-buckets. Il ne doit jamais être utilisé comme liste exhaustive des achats immédiats.
1. ALT-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.071
2. DUSK-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 6.830
3. AVA-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 6.713

## Accélération indépendante

- VVV-EUR — CONFIRMED_ACCELERATION — score 8.341/10 — DETECTED_BUT_TOO_LATE
- TRAC-EUR — CONFIRMED_ACCELERATION — score 6.752/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- ME-EUR — BUILDING_ACCELERATION — score 6.387/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- GTC-EUR — BUILDING_ACCELERATION — score 5.145/10 — DETECTED_BUT_TOO_LATE
- SQD-EUR — BUILDING_ACCELERATION — score 4.933/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- ICNT-EUR — BUILDING_ACCELERATION — score 4.871/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- WHUF-EUR — MEMORY_24H — score mémoire 8.811/10 — sources ACCELERATION — MEMORY_ONLY
- MANTRA-EUR — MEMORY_24H — score mémoire 8.592/10 — sources ACCELERATION — MEMORY_ONLY
- VVV-EUR — ACTIVE_NOW — score mémoire 8.341/10 — sources ACCELERATION — DETECTED_BUT_TOO_LATE
- ALT-EUR — ACTIVE_NOW — score mémoire 7.071/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- EDU-EUR — MEMORY_24H — score mémoire 6.958/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- DUSK-EUR — ACTIVE_NOW — score mémoire 6.830/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- KMNO-EUR — ACTIVE_NOW — score mémoire 6.758/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- TRAC-EUR — ACTIVE_NOW — score mémoire 6.752/10 — sources ACCELERATION — WATCH_ONLY
- RSR-EUR — MEMORY_24H — score mémoire 6.716/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- AVA-EUR — ACTIVE_NOW — score mémoire 6.713/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE

## Audit des plus fortes hausses

- WHUF-EUR +21.29% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- ELSA-EUR +17.38% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- ICNT-EUR +13.83% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- AMP-EUR +13.43% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- GTC-EUR +12.84% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- QKC-EUR +9.11% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- SENT-EUR +8.69% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE
- CVX-EUR +6.58% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE
- VVV-EUR +6.41% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- GWEI-EUR +6.27% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE

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
