# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-10-18T21:50:12.969141+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : aucun candidat matériel
- **MEILLEUR_LATENT_ACCELERATOR** : aucun candidat matériel
- **MEILLEUR_PULLBACK_REENTRY** : DUSK-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 6.972 | entrée 5.200 | trend 8.050 | rang 6.664
  - Trend remains strong; candidate retained for re-entry instead of discarded.

## Tous les achats immédiats

Aucun ACHETE_MAINTENANT dans le classement complet.

## Top cross-sectionnel — aperçu non exhaustif

Ce top est une vue courte multi-buckets. Il ne doit jamais être utilisé comme liste exhaustive des achats immédiats.
1. DUSK-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 6.664
2. ALT-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 6.524
3. RSR-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 6.511

## Accélération indépendante

- MANTRA-EUR — CONFIRMED_ACCELERATION — score 8.592/10 — DETECTED_BUT_TOO_LATE
- USELESS-EUR — BUILDING_ACCELERATION — score 6.095/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- ZBCN-EUR — BUILDING_ACCELERATION — score 5.702/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- BICO-EUR — BUILDING_ACCELERATION — score 5.694/10 — DETECTED_BUT_TOO_LATE
- RUNE-EUR — BUILDING_ACCELERATION — score 5.387/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- AKT-EUR — BUILDING_ACCELERATION — score 5.216/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- C-EUR — BUILDING_ACCELERATION — score 5.201/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- BLEND-EUR — BUILDING_ACCELERATION — score 5.153/10 — DETECTED_BUT_TOO_LATE
- ZRO-EUR — BUILDING_ACCELERATION — score 4.850/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- ZKC-EUR — BUILDING_ACCELERATION — score 4.793/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- MANTRA-EUR — ACTIVE_NOW — score mémoire 8.592/10 — sources ACCELERATION — DETECTED_BUT_TOO_LATE
- GTC-EUR — MEMORY_24H — score mémoire 8.028/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- WAL-EUR — MEMORY_24H — score mémoire 7.187/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- METIS-EUR — MEMORY_24H — score mémoire 6.971/10 — sources DECISION_LAYER, V4 — MEMORY_ONLY
- EDU-EUR — MEMORY_24H — score mémoire 6.958/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- KMNO-EUR — MEMORY_24H — score mémoire 6.761/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- BAT-EUR — ACTIVE_NOW — score mémoire 6.702/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- TIA-EUR — MEMORY_24H — score mémoire 6.693/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- DUSK-EUR — ACTIVE_NOW — score mémoire 6.664/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- ICNT-EUR — MEMORY_24H — score mémoire 6.609/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY

## Audit des plus fortes hausses

- WHUF-EUR +21.20% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- GTC-EUR +16.27% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- ELSA-EUR +16.27% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- MANTRA-EUR +12.92% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- AMP-EUR +10.00% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ICNT-EUR +8.10% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- OSMO-EUR +7.68% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- CVX-EUR +6.33% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE
- GLMR-EUR +5.88% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- XDP-EUR +5.13% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE

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
