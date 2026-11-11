# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-11-11T00:07:08.904771+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : aucun candidat matériel
- **MEILLEUR_LATENT_ACCELERATOR** : aucun candidat matériel
- **MEILLEUR_PULLBACK_REENTRY** : BEAM-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 6.532 | entrée 5.600 | trend 7.650 | rang 6.372
  - Trend remains strong; candidate retained for re-entry instead of discarded.

## Tous les achats immédiats

Aucun ACHETE_MAINTENANT dans le classement complet.

## Top cross-sectionnel — aperçu non exhaustif

Ce top est une vue courte multi-buckets. Il ne doit jamais être utilisé comme liste exhaustive des achats immédiats.
1. BEAM-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 6.372

## Accélération indépendante

- CPOOL-EUR — CONFIRMED_ACCELERATION — score 9.000/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- FOLD-EUR — CONFIRMED_ACCELERATION — score 7.719/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- QKC-EUR — BUILDING_ACCELERATION — score 5.941/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- C98-EUR — BUILDING_ACCELERATION — score 5.789/10 — DETECTED_BUT_TOO_LATE
- SFP-EUR — BUILDING_ACCELERATION — score 5.170/10 — DETECTED_BUT_TOO_LATE
- PUFFER-EUR — BUILDING_ACCELERATION — score 5.066/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- TRUST-EUR — BUILDING_ACCELERATION — score 5.000/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- GLM-EUR — BUILDING_ACCELERATION — score 4.994/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- FTT-EUR — BUILDING_ACCELERATION — score 4.992/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- PEPE-EUR — BUILDING_ACCELERATION — score 4.882/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- THQ-EUR — MEMORY_24H — score mémoire 9.396/10 — sources ACCELERATION — MEMORY_ONLY
- MERL-EUR — MEMORY_24H — score mémoire 9.228/10 — sources ACCELERATION, DECISION_LAYER — MEMORY_ONLY
- CPOOL-EUR — ACTIVE_NOW — score mémoire 9.000/10 — sources ACCELERATION — WATCH_ONLY
- CYBER-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION — MEMORY_ONLY
- CELR-EUR — MEMORY_24H — score mémoire 8.204/10 — sources ACCELERATION — MEMORY_ONLY
- FOLD-EUR — ACTIVE_NOW — score mémoire 7.719/10 — sources ACCELERATION — WATCH_ONLY
- PEPE-EUR — ACTIVE_NOW — score mémoire 7.235/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- ZIL-EUR — MEMORY_DECAY_24_72H — score mémoire 7.181/10 — sources ACCELERATION — MEMORY_ONLY
- XMN-EUR — MEMORY_24H — score mémoire 6.804/10 — sources ACCELERATION — MEMORY_ONLY
- BIRB-EUR — MEMORY_24H — score mémoire 6.501/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY

## Audit des plus fortes hausses

- AGI-EUR +17.24% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- ACT-EUR +10.73% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- GRAM-EUR +10.63% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE
- CYBER-EUR +10.48% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- LIGHTER-EUR +8.15% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- DOGS-EUR +7.21% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE
- HOME-EUR +6.87% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE
- CPOOL-EUR +6.80% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- ICP-EUR +6.77% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE
- PEPE-EUR +6.02% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE

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
