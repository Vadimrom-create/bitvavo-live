# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-10-15T15:11:10.133999+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : PYTH-EUR | action PLACE_LIMITE_PASSIVE | opportunité 8.169 | entrée 6.250 | trend 9.200 | rang 7.263
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : aucun candidat matériel
- **MEILLEUR_PULLBACK_REENTRY** : OP-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 7.976 | entrée 6.850 | trend 8.650 | rang 7.402
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Tous les achats immédiats

Aucun ACHETE_MAINTENANT dans le classement complet.

## Top cross-sectionnel — aperçu non exhaustif

Ce top est une vue courte multi-buckets. Il ne doit jamais être utilisé comme liste exhaustive des achats immédiats.
1. OP-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.402
2. PYTH-EUR — MEILLEURE_LIMITE_PASSIVE — PLACE_LIMITE_PASSIVE — rank 7.263
3. DODO-EUR — MEILLEURE_LIMITE_PASSIVE — PLACE_LIMITE_PASSIVE — rank 7.126

## Accélération indépendante

- ETHFI-EUR — CONFIRMED_ACCELERATION — score 9.389/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- BANANA-EUR — CONFIRMED_ACCELERATION — score 9.000/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- BREV-EUR — CONFIRMED_ACCELERATION — score 9.000/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- COW-EUR — CONFIRMED_ACCELERATION — score 8.909/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- PYTH-EUR — CONFIRMED_ACCELERATION — score 8.803/10 — DETECTED_BUT_TOO_LATE
- HOME-EUR — CONFIRMED_ACCELERATION — score 8.559/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- IRYS-EUR — CONFIRMED_ACCELERATION — score 8.481/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- TURBO-EUR — CONFIRMED_ACCELERATION — score 8.332/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- NEO-EUR — CONFIRMED_ACCELERATION — score 8.151/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- REQ-EUR — CONFIRMED_ACCELERATION — score 8.077/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- ETHFI-EUR — ACTIVE_NOW — score mémoire 9.389/10 — sources ACCELERATION — WATCH_ONLY
- MAGIC-EUR — MEMORY_24H — score mémoire 9.346/10 — sources ACCELERATION — MEMORY_ONLY
- BANANA-EUR — ACTIVE_NOW — score mémoire 9.000/10 — sources ACCELERATION — WATCH_ONLY
- BREV-EUR — ACTIVE_NOW — score mémoire 9.000/10 — sources ACCELERATION — WATCH_ONLY
- COW-EUR — ACTIVE_NOW — score mémoire 8.909/10 — sources ACCELERATION — WATCH_ONLY
- PYTH-EUR — ACTIVE_NOW — score mémoire 8.803/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- NES-EUR — MEMORY_DECAY_24_72H — score mémoire 8.776/10 — sources ACCELERATION — MEMORY_ONLY
- HOME-EUR — ACTIVE_NOW — score mémoire 8.559/10 — sources ACCELERATION — WATCH_ONLY
- EPIC-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION — MEMORY_ONLY
- IRYS-EUR — ACTIVE_NOW — score mémoire 8.481/10 — sources ACCELERATION — WATCH_ONLY

## Audit des plus fortes hausses

- PUFFER-EUR +85.19% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- OSMO-EUR +19.35% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- FUN-EUR +18.81% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- NIL-EUR +16.89% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- ZK-EUR +15.41% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- DUSK-EUR +14.64% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- ICNT-EUR +14.34% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- RLC-EUR +13.78% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- MLN-EUR +11.76% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- ELSA-EUR +10.86% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE

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
