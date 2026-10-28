# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-10-28T15:20:22.119044+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : BABY-EUR | action PLACE_LIMITE_PASSIVE | opportunité 7.620 | entrée 6.100 | trend 8.650 | rang 7.256
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : BEAM-EUR | action LATENT_ACCELERATOR | opportunité 7.528 | entrée 5.100 | trend 8.300 | rang 7.103
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : PARTI-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 7.376 | entrée 4.850 | trend 8.450 | rang 7.077
  - Trend remains strong; candidate retained for re-entry instead of discarded.

## Tous les achats immédiats

Aucun ACHETE_MAINTENANT dans le classement complet.

## Top cross-sectionnel — aperçu non exhaustif

Ce top est une vue courte multi-buckets. Il ne doit jamais être utilisé comme liste exhaustive des achats immédiats.
1. BABY-EUR — MEILLEURE_LIMITE_PASSIVE — PLACE_LIMITE_PASSIVE — rank 7.256
2. BEAM-EUR — MEILLEUR_LATENT_ACCELERATOR — LATENT_ACCELERATOR — rank 7.103
3. PARTI-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.077

## Accélération indépendante

- ZEUS-EUR — CONFIRMED_ACCELERATION — score 10.000/10 — DETECTED_BUT_TOO_LATE
- AGI-EUR — CONFIRMED_ACCELERATION — score 9.000/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- CELO-EUR — CONFIRMED_ACCELERATION — score 7.853/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- BABY-EUR — CONFIRMED_ACCELERATION — score 6.917/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- MAGIC-EUR — BUILDING_ACCELERATION — score 5.709/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- BTT-EUR — BUILDING_ACCELERATION — score 5.602/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- DYDX-EUR — BUILDING_ACCELERATION — score 5.283/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- KAT-EUR — BUILDING_ACCELERATION — score 5.154/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- ALLO-EUR — BUILDING_ACCELERATION — score 5.093/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- ZEUS-EUR — ACTIVE_NOW — score mémoire 10.000/10 — sources ACCELERATION — DETECTED_BUT_TOO_LATE
- AGI-EUR — ACTIVE_NOW — score mémoire 9.000/10 — sources ACCELERATION — WATCH_ONLY
- BLUR-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION — MEMORY_ONLY
- ICNT-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION — MEMORY_ONLY
- CELO-EUR — ACTIVE_NOW — score mémoire 7.853/10 — sources ACCELERATION — WATCH_ONLY
- GROVE-EUR — MEMORY_DECAY_24_72H — score mémoire 7.832/10 — sources ACCELERATION — MEMORY_ONLY
- BABY-EUR — ACTIVE_NOW — score mémoire 7.256/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- U-EUR — MEMORY_DECAY_24_72H — score mémoire 7.221/10 — sources ACCELERATION — MEMORY_ONLY
- MEGA-EUR — ACTIVE_NOW — score mémoire 7.207/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- BEAM-EUR — ACTIVE_NOW — score mémoire 7.103/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY

## Audit des plus fortes hausses

- GROVE-EUR +185.03% — DETECTED_TOO_LATE — couche NONE — action INTERPRETATION
- XAN-EUR +37.55% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- DOS-EUR +36.99% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- INIT-EUR +27.00% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- ZEUS-EUR +17.15% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- SHELL-EUR +14.80% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- BLUR-EUR +12.57% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- PEPE-EUR +11.26% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- ICNT-EUR +11.21% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- PUFFER-EUR +11.20% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE

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
