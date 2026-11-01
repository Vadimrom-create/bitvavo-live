# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-11-01T14:19:22.134153+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : aucun candidat matériel
- **MEILLEUR_LATENT_ACCELERATOR** : aucun candidat matériel
- **MEILLEUR_PULLBACK_REENTRY** : PEPE-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 7.221 | entrée 6.000 | trend 8.100 | rang 7.018
  - Trend remains strong; candidate retained for re-entry instead of discarded.

## Tous les achats immédiats

Aucun ACHETE_MAINTENANT dans le classement complet.

## Top cross-sectionnel — aperçu non exhaustif

Ce top est une vue courte multi-buckets. Il ne doit jamais être utilisé comme liste exhaustive des achats immédiats.
1. PEPE-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.018
2. SOLV-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 6.517
3. WIN-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 6.213

## Accélération indépendante

- G-EUR — CONFIRMED_ACCELERATION — score 6.751/10 — DETECTED_BUT_TOO_LATE
- BIO-EUR — BUILDING_ACCELERATION — score 5.852/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- CSPR-EUR — BUILDING_ACCELERATION — score 5.653/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- GROVE-EUR — BUILDING_ACCELERATION — score 5.630/10 — DETECTED_BUT_TOO_LATE
- AERO-EUR — BUILDING_ACCELERATION — score 5.522/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- TRUMP-EUR — BUILDING_ACCELERATION — score 5.436/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- SHELL-EUR — BUILDING_ACCELERATION — score 5.203/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- TAI-EUR — BUILDING_ACCELERATION — score 5.093/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- AZTEC-EUR — BUILDING_ACCELERATION — score 4.826/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- ADX-EUR — MEMORY_24H — score mémoire 10.000/10 — sources ACCELERATION — MEMORY_ONLY
- U-EUR — MEMORY_24H — score mémoire 9.449/10 — sources ACCELERATION — MEMORY_ONLY
- PROMPT-EUR — MEMORY_24H — score mémoire 9.000/10 — sources ACCELERATION — MEMORY_ONLY
- POWR-EUR — MEMORY_24H — score mémoire 8.642/10 — sources ACCELERATION — MEMORY_ONLY
- GNS-EUR — MEMORY_24H — score mémoire 8.246/10 — sources ACCELERATION — MEMORY_ONLY
- STO-EUR — MEMORY_24H — score mémoire 8.082/10 — sources ACCELERATION — MEMORY_ONLY
- LAPTOP-EUR — MEMORY_24H — score mémoire 8.004/10 — sources ACCELERATION — MEMORY_ONLY
- OSMO-EUR — MEMORY_DECAY_24_72H — score mémoire 7.446/10 — sources ACCELERATION, DECISION_LAYER — MEMORY_ONLY
- COW-EUR — MEMORY_24H — score mémoire 7.102/10 — sources ACCELERATION — MEMORY_ONLY
- XMN-EUR — MEMORY_24H — score mémoire 7.062/10 — sources ACCELERATION — MEMORY_ONLY

## Audit des plus fortes hausses

- G-EUR +18.81% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- LIGHTER-EUR +16.84% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- INIT-EUR +15.24% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- FLOCK-EUR +14.42% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- SOLV-EUR +11.91% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- ZRO-EUR +10.75% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE
- U-EUR +9.58% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- TREAD-EUR +9.48% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE
- POWR-EUR +9.05% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- BIO-EUR +8.90% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE

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
