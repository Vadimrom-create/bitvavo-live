# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-10-30T07:51:42.042909+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : aucun candidat matériel
- **MEILLEUR_LATENT_ACCELERATOR** : aucun candidat matériel
- **MEILLEUR_PULLBACK_REENTRY** : PEPE-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 7.042 | entrée 6.050 | trend 7.900 | rang 6.809
  - Trend remains strong; candidate retained for re-entry instead of discarded.

## Tous les achats immédiats

Aucun ACHETE_MAINTENANT dans le classement complet.

## Top cross-sectionnel — aperçu non exhaustif

Ce top est une vue courte multi-buckets. Il ne doit jamais être utilisé comme liste exhaustive des achats immédiats.
1. PEPE-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 6.809
2. HAEDAL-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 6.471

## Accélération indépendante

- AZTEC-EUR — BUILDING_ACCELERATION — score 6.102/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- SOMI-EUR — BUILDING_ACCELERATION — score 5.517/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- MERL-EUR — BUILDING_ACCELERATION — score 5.494/10 — DETECTED_BUT_TOO_LATE
- BEAM-EUR — BUILDING_ACCELERATION — score 5.052/10 — DETECTED_BUT_TOO_LATE
- SYRUP-EUR — BUILDING_ACCELERATION — score 4.979/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- POND-EUR — BUILDING_ACCELERATION — score 4.962/10 — DETECTED_BUT_TOO_LATE
- CRV-EUR — BUILDING_ACCELERATION — score 4.955/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- GROVE-EUR — MEMORY_24H — score mémoire 8.937/10 — sources ACCELERATION — MEMORY_ONLY
- TRX-EUR — MEMORY_24H — score mémoire 8.541/10 — sources ACCELERATION — MEMORY_ONLY
- SOON-EUR — MEMORY_DECAY_24_72H — score mémoire 8.302/10 — sources ACCELERATION — MEMORY_ONLY
- XMN-EUR — MEMORY_24H — score mémoire 8.101/10 — sources ACCELERATION — MEMORY_ONLY
- BTT-EUR — MEMORY_24H — score mémoire 7.500/10 — sources ACCELERATION — MEMORY_ONLY
- ETHFI-EUR — MEMORY_DECAY_24_72H — score mémoire 7.447/10 — sources ACCELERATION — MEMORY_ONLY
- ALIGN-EUR — MEMORY_DECAY_24_72H — score mémoire 7.324/10 — sources ACCELERATION — MEMORY_ONLY
- CNPY-EUR — MEMORY_DECAY_24_72H — score mémoire 7.321/10 — sources ACCELERATION — MEMORY_ONLY
- DODO-EUR — MEMORY_24H — score mémoire 6.906/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- ICNT-EUR — MEMORY_24H — score mémoire 6.884/10 — sources ACCELERATION — MEMORY_ONLY

## Audit des plus fortes hausses

- PARTI-EUR +32.37% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- BEAM-EUR +23.88% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- HYPE-EUR +16.24% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- MERL-EUR +12.70% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- RUNE-EUR +10.78% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- CAP-EUR +9.72% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- BIRB-EUR +8.95% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- SOMI-EUR +6.89% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- SOLV-EUR +6.84% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- LSK-EUR +6.71% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE

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
