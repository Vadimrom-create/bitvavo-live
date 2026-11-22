# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-11-22T00:05:19.100995+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : aucun candidat matériel
- **MEILLEUR_LATENT_ACCELERATOR** : aucun candidat matériel
- **MEILLEUR_PULLBACK_REENTRY** : VVV-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 6.756 | entrée 6.500 | trend 8.300 | rang 6.160
  - Trend remains strong; candidate retained for re-entry instead of discarded.

## Tous les achats immédiats

Aucun ACHETE_MAINTENANT dans le classement complet.

## Top cross-sectionnel — aperçu non exhaustif

Ce top est une vue courte multi-buckets. Il ne doit jamais être utilisé comme liste exhaustive des achats immédiats.
1. VVV-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 6.160

## Accélération indépendante

- PUFFER-EUR — CONFIRMED_ACCELERATION — score 8.565/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- ORCA-EUR — CONFIRMED_ACCELERATION — score 7.601/10 — DETECTED_BUT_TOO_LATE
- ZEUS-EUR — CONFIRMED_ACCELERATION — score 7.367/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- TRAC-EUR — BUILDING_ACCELERATION — score 6.293/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- IRYS-EUR — BUILDING_ACCELERATION — score 4.892/10 — DETECTED_BUT_TOO_LATE
- BOB-EUR — BUILDING_ACCELERATION — score 4.881/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- PUFFER-EUR — ACTIVE_NOW — score mémoire 8.565/10 — sources ACCELERATION — WATCH_ONLY
- NPC-EUR — MEMORY_24H — score mémoire 8.217/10 — sources ACCELERATION — MEMORY_ONLY
- ORCA-EUR — ACTIVE_NOW — score mémoire 7.601/10 — sources ACCELERATION — DETECTED_BUT_TOO_LATE
- ZEUS-EUR — ACTIVE_NOW — score mémoire 7.367/10 — sources ACCELERATION — WATCH_ONLY
- ELSA-EUR — MEMORY_24H — score mémoire 7.143/10 — sources ACCELERATION — MEMORY_ONLY
- O-EUR — MEMORY_24H — score mémoire 7.124/10 — sources V4 — MEMORY_ONLY
- HOT-EUR — MEMORY_24H — score mémoire 7.098/10 — sources ACCELERATION — MEMORY_ONLY
- DODO-EUR — MEMORY_24H — score mémoire 6.698/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- PROMPT-EUR — MEMORY_24H — score mémoire 6.516/10 — sources ACCELERATION — MEMORY_ONLY
- CROSS-EUR — MEMORY_24H — score mémoire 6.475/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY

## Audit des plus fortes hausses

- DRV-EUR +35.04% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- NPC-EUR +27.03% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- VVV-EUR +19.24% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- IMU-EUR +17.10% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- DODO-EUR +15.99% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- PROMPT-EUR +13.66% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- PARTI-EUR +12.52% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- ORCA-EUR +12.35% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- ENSO-EUR +12.29% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- PROM-EUR +11.43% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE

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
