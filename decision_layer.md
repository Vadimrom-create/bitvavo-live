# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-11-02T01:57:50.727436+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : aucun candidat matériel
- **MEILLEUR_LATENT_ACCELERATOR** : aucun candidat matériel
- **MEILLEUR_PULLBACK_REENTRY** : SOLV-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 7.622 | entrée 5.950 | trend 8.450 | rang 7.194
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Tous les achats immédiats

Aucun ACHETE_MAINTENANT dans le classement complet.

## Top cross-sectionnel — aperçu non exhaustif

Ce top est une vue courte multi-buckets. Il ne doit jamais être utilisé comme liste exhaustive des achats immédiats.
1. SOLV-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.194
2. INIT-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 6.843
3. PARTI-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 6.535

## Accélération indépendante

- PARTI-EUR — CONFIRMED_ACCELERATION — score 8.689/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- ADX-EUR — MEMORY_DECAY_24_72H — score mémoire 9.178/10 — sources ACCELERATION — MEMORY_ONLY
- PARTI-EUR — ACTIVE_NOW — score mémoire 8.689/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- POWR-EUR — MEMORY_DECAY_24_72H — score mémoire 8.465/10 — sources ACCELERATION — MEMORY_ONLY
- U-EUR — MEMORY_DECAY_24_72H — score mémoire 8.066/10 — sources ACCELERATION — MEMORY_ONLY
- PROMPT-EUR — MEMORY_DECAY_24_72H — score mémoire 7.683/10 — sources ACCELERATION — MEMORY_ONLY
- GNS-EUR — MEMORY_DECAY_24_72H — score mémoire 7.568/10 — sources ACCELERATION — MEMORY_ONLY
- SOLV-EUR — ACTIVE_NOW — score mémoire 7.194/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- PEPE-EUR — MEMORY_24H — score mémoire 6.931/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- STO-EUR — MEMORY_DECAY_24_72H — score mémoire 6.899/10 — sources ACCELERATION — MEMORY_ONLY
- INIT-EUR — ACTIVE_NOW — score mémoire 6.843/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY

## Audit des plus fortes hausses

- HOT-EUR +10.60% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- TREAD-EUR +10.02% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- TRUMP-EUR +9.00% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- BEAM-EUR +8.55% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- INIT-EUR +7.29% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- MAVIA-EUR +6.39% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE
- KITE-EUR +6.25% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE
- NPC-EUR +6.11% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- FLOCK-EUR +5.88% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- XDP-EUR +5.79% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE

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
