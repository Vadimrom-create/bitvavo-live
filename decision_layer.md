# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-10-19T14:35:50.232152+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : aucun candidat matériel
- **MEILLEUR_LATENT_ACCELERATOR** : aucun candidat matériel
- **MEILLEUR_PULLBACK_REENTRY** : DODO-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 7.198 | entrée 5.650 | trend 8.300 | rang 6.968
  - Trend remains strong; candidate retained for re-entry instead of discarded.

## Tous les achats immédiats

Aucun ACHETE_MAINTENANT dans le classement complet.

## Top cross-sectionnel — aperçu non exhaustif

Ce top est une vue courte multi-buckets. Il ne doit jamais être utilisé comme liste exhaustive des achats immédiats.
1. DODO-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 6.968
2. DUSK-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 6.509
3. AVA-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 6.465

## Accélération indépendante

- CTR-EUR — CONFIRMED_ACCELERATION — score 9.247/10 — DETECTED_BUT_TOO_LATE
- OSMO-EUR — CONFIRMED_ACCELERATION — score 8.496/10 — DETECTED_BUT_TOO_LATE
- TREAD-EUR — BUILDING_ACCELERATION — score 5.767/10 — DETECTED_BUT_TOO_LATE
- ZEUS-EUR — BUILDING_ACCELERATION — score 5.467/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- CFG-EUR — BUILDING_ACCELERATION — score 5.012/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- MORPHO-EUR — BUILDING_ACCELERATION — score 4.927/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- CTR-EUR — ACTIVE_NOW — score mémoire 9.247/10 — sources ACCELERATION — DETECTED_BUT_TOO_LATE
- WHUF-EUR — MEMORY_24H — score mémoire 8.811/10 — sources ACCELERATION — MEMORY_ONLY
- MANTRA-EUR — MEMORY_24H — score mémoire 8.592/10 — sources ACCELERATION — MEMORY_ONLY
- OSMO-EUR — ACTIVE_NOW — score mémoire 8.496/10 — sources ACCELERATION, DECISION_LAYER — DETECTED_BUT_TOO_LATE
- VVV-EUR — MEMORY_24H — score mémoire 8.341/10 — sources ACCELERATION — MEMORY_ONLY
- LSK-EUR — MEMORY_24H — score mémoire 7.457/10 — sources ACCELERATION — MEMORY_ONLY
- ALT-EUR — MEMORY_24H — score mémoire 7.064/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- HUMA-EUR — MEMORY_24H — score mémoire 6.991/10 — sources ACCELERATION — MEMORY_ONLY
- DODO-EUR — ACTIVE_NOW — score mémoire 6.968/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- KMNO-EUR — MEMORY_24H — score mémoire 6.758/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY

## Audit des plus fortes hausses

- OSMO-EUR +36.96% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- GTC-EUR +21.45% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- AMP-EUR +20.07% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- POND-EUR +17.97% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- NIL-EUR +11.48% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- ACU-EUR +9.56% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE
- ARB-EUR +9.26% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE
- CTR-EUR +8.88% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- KAT-EUR +8.71% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE
- CT-EUR +7.76% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE

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
