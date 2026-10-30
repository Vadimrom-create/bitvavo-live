# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-10-30T01:54:18.542407+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : aucun candidat matériel
- **MEILLEUR_LATENT_ACCELERATOR** : aucun candidat matériel
- **MEILLEUR_PULLBACK_REENTRY** : WIN-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 6.281 | entrée 5.400 | trend 7.950 | rang 6.365
  - Trend remains strong; candidate retained for re-entry instead of discarded.

## Tous les achats immédiats

Aucun ACHETE_MAINTENANT dans le classement complet.

## Top cross-sectionnel — aperçu non exhaustif

Ce top est une vue courte multi-buckets. Il ne doit jamais être utilisé comme liste exhaustive des achats immédiats.
1. WIN-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 6.365
2. HAEDAL-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 6.138

## Accélération indépendante

- BTT-EUR — CONFIRMED_ACCELERATION — score 7.500/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- PTB-EUR — CONFIRMED_ACCELERATION — score 6.844/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- LRC-EUR — CONFIRMED_ACCELERATION — score 6.527/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- ZBCN-EUR — BUILDING_ACCELERATION — score 5.755/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- CTC-EUR — BUILDING_ACCELERATION — score 5.556/10 — DETECTED_BUT_TOO_LATE
- MERL-EUR — BUILDING_ACCELERATION — score 5.367/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- LAPTOP-EUR — BUILDING_ACCELERATION — score 4.775/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- GROVE-EUR — MEMORY_24H — score mémoire 8.937/10 — sources ACCELERATION — MEMORY_ONLY
- SOON-EUR — MEMORY_24H — score mémoire 8.747/10 — sources ACCELERATION — MEMORY_ONLY
- TRX-EUR — MEMORY_24H — score mémoire 8.541/10 — sources ACCELERATION — MEMORY_ONLY
- XMN-EUR — MEMORY_24H — score mémoire 8.101/10 — sources ACCELERATION — MEMORY_ONLY
- ETHFI-EUR — MEMORY_24H — score mémoire 7.846/10 — sources ACCELERATION — MEMORY_ONLY
- ZEUS-EUR — MEMORY_DECAY_24_72H — score mémoire 7.799/10 — sources ACCELERATION — MEMORY_ONLY
- ALIGN-EUR — MEMORY_24H — score mémoire 7.716/10 — sources ACCELERATION — MEMORY_ONLY
- CNPY-EUR — MEMORY_24H — score mémoire 7.713/10 — sources ACCELERATION — MEMORY_ONLY
- BTT-EUR — ACTIVE_NOW — score mémoire 7.500/10 — sources ACCELERATION — WATCH_ONLY
- AGI-EUR — MEMORY_DECAY_24_72H — score mémoire 7.019/10 — sources ACCELERATION — MEMORY_ONLY

## Audit des plus fortes hausses

- PARTI-EUR +48.16% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- HYPE-EUR +12.66% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- TRX-EUR +8.81% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- CAP-EUR +7.32% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- HUMA-EUR +3.79% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE
- MERL-EUR +3.64% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- RUNE-EUR +3.20% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- LSK-EUR +2.08% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- ICNT-EUR +2.03% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- NES-EUR +1.32% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE

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
