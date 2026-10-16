# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-10-16T00:29:59.356905+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : DODO-EUR | action PLACE_LIMITE_PASSIVE | opportunité 7.713 | entrée 6.500 | trend 9.000 | rang 7.577
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : AVA-EUR | action LATENT_ACCELERATOR | opportunité 7.415 | entrée 5.650 | trend 7.750 | rang 6.801
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : INJ-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.121 | entrée 7.750 | trend 8.700 | rang 7.572
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Tous les achats immédiats

Aucun ACHETE_MAINTENANT dans le classement complet.

## Top cross-sectionnel — aperçu non exhaustif

Ce top est une vue courte multi-buckets. Il ne doit jamais être utilisé comme liste exhaustive des achats immédiats.
1. DODO-EUR — MEILLEURE_LIMITE_PASSIVE — PLACE_LIMITE_PASSIVE — rank 7.577
2. INJ-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.572
3. DEEP-EUR — MEILLEURE_LIMITE_PASSIVE — PLACE_LIMITE_PASSIVE — rank 7.494

## Accélération indépendante

- ZRO-EUR — CONFIRMED_ACCELERATION — score 8.832/10 — DETECTED_BUT_TOO_LATE
- PUFFER-EUR — CONFIRMED_ACCELERATION — score 8.241/10 — DETECTED_BUT_TOO_LATE
- EDGE-EUR — CONFIRMED_ACCELERATION — score 7.962/10 — DETECTED_BUT_TOO_LATE
- AVA-EUR — CONFIRMED_ACCELERATION — score 7.652/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- GIGA-EUR — CONFIRMED_ACCELERATION — score 7.000/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- GNS-EUR — MEMORY_24H — score mémoire 9.754/10 — sources ACCELERATION — MEMORY_ONLY
- ETHFI-EUR — MEMORY_24H — score mémoire 9.389/10 — sources ACCELERATION — MEMORY_ONLY
- MAGIC-EUR — MEMORY_24H — score mémoire 9.346/10 — sources ACCELERATION — MEMORY_ONLY
- BANANA-EUR — MEMORY_24H — score mémoire 9.000/10 — sources ACCELERATION — MEMORY_ONLY
- BREV-EUR — MEMORY_24H — score mémoire 9.000/10 — sources ACCELERATION — MEMORY_ONLY
- COW-EUR — MEMORY_24H — score mémoire 8.909/10 — sources ACCELERATION — MEMORY_ONLY
- ZRO-EUR — ACTIVE_NOW — score mémoire 8.832/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- HOME-EUR — MEMORY_24H — score mémoire 8.559/10 — sources ACCELERATION — MEMORY_ONLY
- IRYS-EUR — MEMORY_24H — score mémoire 8.481/10 — sources ACCELERATION — MEMORY_ONLY
- BAT-EUR — MEMORY_24H — score mémoire 8.396/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY

## Audit des plus fortes hausses

- PUFFER-EUR +100.14% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- ICNT-EUR +33.58% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- BAT-EUR +22.95% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- POND-EUR +22.88% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ELSA-EUR +15.52% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- ZRO-EUR +14.62% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- ANIME-EUR +12.28% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- STRK-EUR +12.00% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- INJ-EUR +11.40% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- INIT-EUR +11.21% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION

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
