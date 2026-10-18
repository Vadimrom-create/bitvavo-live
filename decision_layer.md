# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-10-18T23:45:25.588411+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : aucun candidat matériel
- **MEILLEUR_LATENT_ACCELERATOR** : aucun candidat matériel
- **MEILLEUR_PULLBACK_REENTRY** : DUSK-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 7.711 | entrée 6.400 | trend 8.050 | rang 7.096
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Tous les achats immédiats

Aucun ACHETE_MAINTENANT dans le classement complet.

## Top cross-sectionnel — aperçu non exhaustif

Ce top est une vue courte multi-buckets. Il ne doit jamais être utilisé comme liste exhaustive des achats immédiats.
1. DUSK-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.096
2. RSR-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 6.716
3. AVA-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 6.431

## Accélération indépendante

- WHUF-EUR — CONFIRMED_ACCELERATION — score 8.811/10 — DETECTED_BUT_TOO_LATE
- RUNE-EUR — BUILDING_ACCELERATION — score 6.376/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- SCR-EUR — BUILDING_ACCELERATION — score 6.318/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- IKA-EUR — BUILDING_ACCELERATION — score 6.028/10 — DETECTED_BUT_TOO_LATE
- VANA-EUR — BUILDING_ACCELERATION — score 5.873/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- SYN-EUR — BUILDING_ACCELERATION — score 5.657/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- CYBER-EUR — BUILDING_ACCELERATION — score 5.641/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- TIA-EUR — BUILDING_ACCELERATION — score 5.444/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- QKC-EUR — BUILDING_ACCELERATION — score 5.371/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- C98-EUR — BUILDING_ACCELERATION — score 5.364/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- WHUF-EUR — ACTIVE_NOW — score mémoire 8.811/10 — sources ACCELERATION — DETECTED_BUT_TOO_LATE
- MANTRA-EUR — MEMORY_24H — score mémoire 8.592/10 — sources ACCELERATION — MEMORY_ONLY
- GTC-EUR — MEMORY_24H — score mémoire 8.028/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- WAL-EUR — MEMORY_24H — score mémoire 7.187/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- DUSK-EUR — ACTIVE_NOW — score mémoire 7.096/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- EDU-EUR — MEMORY_24H — score mémoire 6.958/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- METIS-EUR — MEMORY_DECAY_24_72H — score mémoire 6.917/10 — sources DECISION_LAYER, V4 — MEMORY_ONLY
- KMNO-EUR — MEMORY_24H — score mémoire 6.761/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- RSR-EUR — ACTIVE_NOW — score mémoire 6.716/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- BAT-EUR — MEMORY_24H — score mémoire 6.702/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY

## Audit des plus fortes hausses

- WHUF-EUR +26.05% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- ELSA-EUR +17.45% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- ICNT-EUR +13.61% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- GTC-EUR +12.49% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- AMP-EUR +11.73% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- SENT-EUR +8.73% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE
- OSMO-EUR +7.76% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- CVX-EUR +7.34% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE
- SOLV-EUR +6.49% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- GLMR-EUR +5.59% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE

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
