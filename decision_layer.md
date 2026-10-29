# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-10-29T17:38:29.257480+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : aucun candidat matériel
- **MEILLEUR_LATENT_ACCELERATOR** : aucun candidat matériel
- **MEILLEUR_PULLBACK_REENTRY** : BEAM-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 6.997 | entrée 5.650 | trend 8.400 | rang 6.862
  - Trend remains strong; candidate retained for re-entry instead of discarded.

## Tous les achats immédiats

Aucun ACHETE_MAINTENANT dans le classement complet.

## Top cross-sectionnel — aperçu non exhaustif

Ce top est une vue courte multi-buckets. Il ne doit jamais être utilisé comme liste exhaustive des achats immédiats.
1. BEAM-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 6.862
2. HAEDAL-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 6.491

## Accélération indépendante

- XMN-EUR — CONFIRMED_ACCELERATION — score 8.101/10 — DETECTED_BUT_TOO_LATE
- EPIC-EUR — CONFIRMED_ACCELERATION — score 6.752/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- BIGTIME-EUR — CONFIRMED_ACCELERATION — score 6.676/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- PARTI-EUR — BUILDING_ACCELERATION — score 6.000/10 — DETECTED_BUT_TOO_LATE
- GNS-EUR — BUILDING_ACCELERATION — score 5.975/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- TREAD-EUR — BUILDING_ACCELERATION — score 5.551/10 — DETECTED_BUT_TOO_LATE
- NEWT-EUR — BUILDING_ACCELERATION — score 5.421/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- NES-EUR — BUILDING_ACCELERATION — score 5.118/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- U-EUR — BUILDING_ACCELERATION — score 4.813/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- TAI-EUR — BUILDING_ACCELERATION — score 4.757/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- ZEUS-EUR — MEMORY_DECAY_24_72H — score mémoire 9.520/10 — sources ACCELERATION — MEMORY_ONLY
- GROVE-EUR — MEMORY_24H — score mémoire 8.937/10 — sources ACCELERATION — MEMORY_ONLY
- SOON-EUR — MEMORY_24H — score mémoire 8.747/10 — sources ACCELERATION — MEMORY_ONLY
- AGI-EUR — MEMORY_DECAY_24_72H — score mémoire 8.568/10 — sources ACCELERATION — MEMORY_ONLY
- XMN-EUR — ACTIVE_NOW — score mémoire 8.101/10 — sources ACCELERATION — DETECTED_BUT_TOO_LATE
- ETHFI-EUR — MEMORY_24H — score mémoire 7.846/10 — sources ACCELERATION — MEMORY_ONLY
- ALIGN-EUR — MEMORY_24H — score mémoire 7.716/10 — sources ACCELERATION — MEMORY_ONLY
- CNPY-EUR — MEMORY_24H — score mémoire 7.713/10 — sources ACCELERATION — MEMORY_ONLY
- CELO-EUR — MEMORY_DECAY_24_72H — score mémoire 7.476/10 — sources ACCELERATION — MEMORY_ONLY
- BABY-EUR — MEMORY_24H — score mémoire 7.170/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY

## Audit des plus fortes hausses

- XMN-EUR +40.07% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- PARTI-EUR +33.63% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- LSK-EUR +29.89% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- HYPE-EUR +18.21% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- PEPE-EUR +11.28% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- QUID-EUR +11.06% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- BICO-EUR +10.74% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- MERL-EUR +10.45% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- GNS-EUR +9.73% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- BLEND-EUR +9.34% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE

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
