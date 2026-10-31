# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-10-31T22:00:57.600963+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : aucun candidat matériel
- **MEILLEUR_LATENT_ACCELERATOR** : aucun candidat matériel
- **MEILLEUR_PULLBACK_REENTRY** : SOLV-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 7.344 | entrée 5.400 | trend 8.700 | rang 7.193
  - Trend remains strong; candidate retained for re-entry instead of discarded.

## Tous les achats immédiats

Aucun ACHETE_MAINTENANT dans le classement complet.

## Top cross-sectionnel — aperçu non exhaustif

Ce top est une vue courte multi-buckets. Il ne doit jamais être utilisé comme liste exhaustive des achats immédiats.
1. SOLV-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.193
2. PARTI-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 6.529
3. INIT-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 6.493

## Accélération indépendante

- ADX-EUR — CONFIRMED_ACCELERATION — score 10.000/10 — DETECTED_BUT_TOO_LATE
- GNS-EUR — CONFIRMED_ACCELERATION — score 8.246/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- XMN-EUR — CONFIRMED_ACCELERATION — score 7.062/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- CHR-EUR — BUILDING_ACCELERATION — score 6.143/10 — DETECTED_BUT_TOO_LATE
- GROVE-EUR — BUILDING_ACCELERATION — score 5.430/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- BREV-EUR — BUILDING_ACCELERATION — score 4.828/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- ADX-EUR — ACTIVE_NOW — score mémoire 10.000/10 — sources ACCELERATION — DETECTED_BUT_TOO_LATE
- U-EUR — MEMORY_24H — score mémoire 9.449/10 — sources ACCELERATION — MEMORY_ONLY
- RECALL-EUR — MEMORY_24H — score mémoire 9.168/10 — sources ACCELERATION — MEMORY_ONLY
- PROMPT-EUR — MEMORY_24H — score mémoire 9.000/10 — sources ACCELERATION — MEMORY_ONLY
- OSMO-EUR — MEMORY_24H — score mémoire 8.400/10 — sources ACCELERATION, DECISION_LAYER — MEMORY_ONLY
- GNS-EUR — ACTIVE_NOW — score mémoire 8.246/10 — sources ACCELERATION — WATCH_ONLY
- STO-EUR — MEMORY_24H — score mémoire 8.082/10 — sources ACCELERATION — MEMORY_ONLY
- LAPTOP-EUR — MEMORY_24H — score mémoire 8.004/10 — sources ACCELERATION — MEMORY_ONLY
- GWEI-EUR — MEMORY_DECAY_24_72H — score mémoire 7.338/10 — sources ACCELERATION — MEMORY_ONLY
- SOLV-EUR — ACTIVE_NOW — score mémoire 7.193/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY

## Audit des plus fortes hausses

- ADX-EUR +32.29% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- LSK-EUR +18.32% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- U-EUR +18.01% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- LIGHTER-EUR +16.24% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- MORPHO-EUR +15.45% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE
- STX-EUR +13.85% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- BEAM-EUR +13.33% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- NES-EUR +9.99% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE
- COW-EUR +9.76% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- INX-EUR +9.54% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE

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
