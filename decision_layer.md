# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-11-12T23:01:10.832525+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : aucun candidat matériel
- **MEILLEUR_LATENT_ACCELERATOR** : aucun candidat matériel
- **MEILLEUR_PULLBACK_REENTRY** : KITE-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 6.934 | entrée 5.500 | trend 8.050 | rang 6.745
  - Trend remains strong; candidate retained for re-entry instead of discarded.

## Tous les achats immédiats

Aucun ACHETE_MAINTENANT dans le classement complet.

## Top cross-sectionnel — aperçu non exhaustif

Ce top est une vue courte multi-buckets. Il ne doit jamais être utilisé comme liste exhaustive des achats immédiats.
1. KITE-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 6.745
2. SXT-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 6.567

## Accélération indépendante

- INIT-EUR — CONFIRMED_ACCELERATION — score 9.440/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- BOB-EUR — BUILDING_ACCELERATION — score 5.765/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- PLUME-EUR — BUILDING_ACCELERATION — score 5.745/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- PEAQ-EUR — BUILDING_ACCELERATION — score 5.550/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- CVC-EUR — BUILDING_ACCELERATION — score 4.799/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- WIN-EUR — MEMORY_24H — score mémoire 9.693/10 — sources ACCELERATION — MEMORY_ONLY
- INIT-EUR — ACTIVE_NOW — score mémoire 9.440/10 — sources ACCELERATION — WATCH_ONLY
- HUMA-EUR — MEMORY_24H — score mémoire 8.528/10 — sources ACCELERATION — MEMORY_ONLY
- ALIGN-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION — MEMORY_ONLY
- KITE-EUR — ACTIVE_NOW — score mémoire 6.745/10 — sources DECISION_LAYER — WATCH_ONLY
- SXT-EUR — ACTIVE_NOW — score mémoire 6.567/10 — sources DECISION_LAYER, V4 — WATCH_ONLY
- CT-EUR — MEMORY_24H — score mémoire 6.476/10 — sources ACCELERATION — MEMORY_ONLY
- BEAM-EUR — MEMORY_24H — score mémoire 6.466/10 — sources DECISION_LAYER — MEMORY_ONLY
- OPEN-EUR — MEMORY_24H — score mémoire 6.406/10 — sources DECISION_LAYER — MEMORY_ONLY
- MLN-EUR — MEMORY_24H — score mémoire 6.326/10 — sources ACCELERATION — MEMORY_ONLY

## Audit des plus fortes hausses

- DODO-EUR +20.86% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- TRIA-EUR +10.21% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE
- CNPY-EUR +8.58% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- PROM-EUR +8.29% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE
- PLUME-EUR +7.32% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE
- S-EUR +6.30% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE
- MOCA-EUR +6.04% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE
- TIA-EUR +5.78% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- MON-EUR +5.64% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE
- MERL-EUR +5.53% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE

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
