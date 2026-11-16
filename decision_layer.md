# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-11-16T15:40:15.522966+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : aucun candidat matériel
- **MEILLEUR_LATENT_ACCELERATOR** : aucun candidat matériel
- **MEILLEUR_PULLBACK_REENTRY** : KITE-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 6.509 | entrée 5.200 | trend 7.600 | rang 6.354
  - Trend remains strong; candidate retained for re-entry instead of discarded.

## Tous les achats immédiats

Aucun ACHETE_MAINTENANT dans le classement complet.

## Top cross-sectionnel — aperçu non exhaustif

Ce top est une vue courte multi-buckets. Il ne doit jamais être utilisé comme liste exhaustive des achats immédiats.
1. KITE-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 6.354
2. CAP-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 6.287

## Accélération indépendante

- SOLV-EUR — BUILDING_ACCELERATION — score 5.895/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- HUMA-EUR — BUILDING_ACCELERATION — score 5.775/10 — DETECTED_BUT_TOO_LATE
- CNPY-EUR — BUILDING_ACCELERATION — score 5.473/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- ZIL-EUR — BUILDING_ACCELERATION — score 5.412/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- THE-EUR — BUILDING_ACCELERATION — score 5.408/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- ZEUS-EUR — BUILDING_ACCELERATION — score 5.269/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- TRIA-EUR — BUILDING_ACCELERATION — score 4.822/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- HNT-EUR — MEMORY_DECAY_24_72H — score mémoire 8.131/10 — sources ACCELERATION — MEMORY_ONLY
- ASTER-EUR — MEMORY_24H — score mémoire 7.937/10 — sources ACCELERATION — MEMORY_ONLY
- GLMR-EUR — MEMORY_DECAY_24_72H — score mémoire 7.421/10 — sources ACCELERATION — MEMORY_ONLY
- AMP-EUR — MEMORY_24H — score mémoire 7.254/10 — sources ACCELERATION — MEMORY_ONLY
- DODO-EUR — ACTIVE_NOW — score mémoire 7.072/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- GNS-EUR — MEMORY_DECAY_24_72H — score mémoire 7.024/10 — sources ACCELERATION — MEMORY_ONLY
- CROSS-EUR — MEMORY_24H — score mémoire 6.926/10 — sources V4 — MEMORY_ONLY
- ZRC-EUR — MEMORY_24H — score mémoire 6.696/10 — sources ACCELERATION — MEMORY_ONLY
- SHELL-EUR — MEMORY_24H — score mémoire 6.367/10 — sources DECISION_LAYER — MEMORY_ONLY
- KITE-EUR — ACTIVE_NOW — score mémoire 6.354/10 — sources DECISION_LAYER, V4 — WATCH_ONLY

## Audit des plus fortes hausses

- RARE-EUR +85.83% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- CROSS-EUR +20.34% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- AXIS-EUR +15.13% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- HUMA-EUR +12.91% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- ICP-EUR +9.11% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- FOLD-EUR +8.58% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- O-EUR +7.69% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- CPOOL-EUR +7.19% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE
- SHELL-EUR +6.46% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- MMT-EUR +6.16% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE

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
