# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-10-29T11:40:58.875227+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : aucun candidat matériel
- **MEILLEUR_LATENT_ACCELERATOR** : aucun candidat matériel
- **MEILLEUR_PULLBACK_REENTRY** : PEPE-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 7.341 | entrée 6.650 | trend 8.350 | rang 7.171
  - Trend remains strong; candidate retained for re-entry instead of discarded.

## Tous les achats immédiats

Aucun ACHETE_MAINTENANT dans le classement complet.

## Top cross-sectionnel — aperçu non exhaustif

Ce top est une vue courte multi-buckets. Il ne doit jamais être utilisé comme liste exhaustive des achats immédiats.
1. PEPE-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.171
2. BEAM-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 6.661
3. HAEDAL-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 6.471

## Accélération indépendante

- GROVE-EUR — CONFIRMED_ACCELERATION — score 8.937/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- EPIC-EUR — CONFIRMED_ACCELERATION — score 7.607/10 — DETECTED_BUT_TOO_LATE
- HFT-EUR — BUILDING_ACCELERATION — score 5.982/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- FLOCK-EUR — BUILDING_ACCELERATION — score 5.174/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- CSPR-EUR — BUILDING_ACCELERATION — score 5.162/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- WHUF-EUR — BUILDING_ACCELERATION — score 4.899/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- WOO-EUR — BUILDING_ACCELERATION — score 4.837/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- ZEUS-EUR — MEMORY_24H — score mémoire 10.000/10 — sources ACCELERATION — MEMORY_ONLY
- AGI-EUR — MEMORY_24H — score mémoire 9.000/10 — sources ACCELERATION — MEMORY_ONLY
- GROVE-EUR — ACTIVE_NOW — score mémoire 8.937/10 — sources ACCELERATION — WATCH_ONLY
- SOON-EUR — MEMORY_24H — score mémoire 8.747/10 — sources ACCELERATION — MEMORY_ONLY
- BLUR-EUR — MEMORY_DECAY_24_72H — score mémoire 7.925/10 — sources ACCELERATION — MEMORY_ONLY
- ICNT-EUR — MEMORY_DECAY_24_72H — score mémoire 7.925/10 — sources ACCELERATION — MEMORY_ONLY
- CELO-EUR — MEMORY_24H — score mémoire 7.853/10 — sources ACCELERATION — MEMORY_ONLY
- ETHFI-EUR — MEMORY_24H — score mémoire 7.846/10 — sources ACCELERATION — MEMORY_ONLY
- ALIGN-EUR — MEMORY_24H — score mémoire 7.716/10 — sources ACCELERATION — MEMORY_ONLY
- CNPY-EUR — MEMORY_24H — score mémoire 7.713/10 — sources ACCELERATION — MEMORY_ONLY

## Audit des plus fortes hausses

- XMN-EUR +61.31% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- ZEUS-EUR +33.91% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- EPIC-EUR +17.70% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- CSPR-EUR +15.17% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- QUID-EUR +12.93% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- BLEND-EUR +12.62% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- CPOOL-EUR +7.38% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- HYPE-EUR +6.07% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- INIT-EUR +5.95% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- KAT-EUR +5.72% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE

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
