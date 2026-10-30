# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-10-30T14:41:03.512860+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : aucun candidat matériel
- **MEILLEUR_LATENT_ACCELERATOR** : aucun candidat matériel
- **MEILLEUR_PULLBACK_REENTRY** : SOLV-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 7.261 | entrée 6.050 | trend 8.700 | rang 6.805
  - Trend remains strong; candidate retained for re-entry instead of discarded.

## Tous les achats immédiats

Aucun ACHETE_MAINTENANT dans le classement complet.

## Top cross-sectionnel — aperçu non exhaustif

Ce top est une vue courte multi-buckets. Il ne doit jamais être utilisé comme liste exhaustive des achats immédiats.
1. SOLV-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 6.805
2. HAEDAL-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 6.700
3. WIN-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 6.398

## Accélération indépendante

- GWEI-EUR — CONFIRMED_ACCELERATION — score 8.661/10 — DETECTED_BUT_TOO_LATE
- BIRB-EUR — CONFIRMED_ACCELERATION — score 7.000/10 — DETECTED_BUT_TOO_LATE
- SOON-EUR — BUILDING_ACCELERATION — score 6.409/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- VVV-EUR — BUILDING_ACCELERATION — score 6.139/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- KERNEL-EUR — BUILDING_ACCELERATION — score 5.728/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- GRT-EUR — BUILDING_ACCELERATION — score 5.615/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- USELESS-EUR — BUILDING_ACCELERATION — score 5.583/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- AAVE-EUR — BUILDING_ACCELERATION — score 5.423/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- SUPER-EUR — BUILDING_ACCELERATION — score 5.381/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- AVA-EUR — BUILDING_ACCELERATION — score 5.248/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- GWEI-EUR — ACTIVE_NOW — score mémoire 8.661/10 — sources ACCELERATION — DETECTED_BUT_TOO_LATE
- TRX-EUR — MEMORY_24H — score mémoire 8.541/10 — sources ACCELERATION — MEMORY_ONLY
- GROVE-EUR — MEMORY_DECAY_24_72H — score mémoire 8.378/10 — sources ACCELERATION — MEMORY_ONLY
- XMN-EUR — MEMORY_24H — score mémoire 8.101/10 — sources ACCELERATION — MEMORY_ONLY
- BTT-EUR — MEMORY_24H — score mémoire 7.500/10 — sources ACCELERATION — MEMORY_ONLY
- PEPE-EUR — ACTIVE_NOW — score mémoire 7.062/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- BIRB-EUR — ACTIVE_NOW — score mémoire 7.000/10 — sources ACCELERATION — DETECTED_BUT_TOO_LATE
- DODO-EUR — MEMORY_24H — score mémoire 6.906/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- ICNT-EUR — MEMORY_24H — score mémoire 6.884/10 — sources ACCELERATION — MEMORY_ONLY
- PTB-EUR — MEMORY_24H — score mémoire 6.844/10 — sources ACCELERATION — MEMORY_ONLY

## Audit des plus fortes hausses

- PARTI-EUR +58.63% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- BEAM-EUR +48.56% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- ZRC-EUR +16.50% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- SOLV-EUR +14.09% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- BIRB-EUR +13.09% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- NIL-EUR +10.10% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- PUNDIX-EUR +6.64% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- CAP-EUR +6.00% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- LSK-EUR +5.13% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- SKY-EUR +4.23% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE

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
