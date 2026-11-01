# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-11-01T19:04:32.173468+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : aucun candidat matériel
- **MEILLEUR_LATENT_ACCELERATOR** : SOLV-EUR | action LATENT_ACCELERATOR | opportunité 7.423 | entrée 5.600 | trend 8.750 | rang 7.293
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : PEPE-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 7.331 | entrée 6.800 | trend 8.100 | rang 7.143
  - Trend remains strong; candidate retained for re-entry instead of discarded.

## Tous les achats immédiats

Aucun ACHETE_MAINTENANT dans le classement complet.

## Top cross-sectionnel — aperçu non exhaustif

Ce top est une vue courte multi-buckets. Il ne doit jamais être utilisé comme liste exhaustive des achats immédiats.
1. SOLV-EUR — MEILLEUR_LATENT_ACCELERATOR — LATENT_ACCELERATOR — rank 7.293
2. PEPE-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.143
3. PARTI-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 6.466

## Accélération indépendante

- AGI-EUR — BUILDING_ACCELERATION — score 5.336/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- ADX-EUR — MEMORY_24H — score mémoire 10.000/10 — sources ACCELERATION — MEMORY_ONLY
- U-EUR — MEMORY_DECAY_24_72H — score mémoire 9.423/10 — sources ACCELERATION — MEMORY_ONLY
- PROMPT-EUR — MEMORY_DECAY_24_72H — score mémoire 8.975/10 — sources ACCELERATION — MEMORY_ONLY
- POWR-EUR — MEMORY_24H — score mémoire 8.642/10 — sources ACCELERATION — MEMORY_ONLY
- GNS-EUR — MEMORY_24H — score mémoire 8.246/10 — sources ACCELERATION — MEMORY_ONLY
- STO-EUR — MEMORY_DECAY_24_72H — score mémoire 8.059/10 — sources ACCELERATION — MEMORY_ONLY
- LAPTOP-EUR — MEMORY_DECAY_24_72H — score mémoire 7.982/10 — sources ACCELERATION — MEMORY_ONLY
- SOLV-EUR — ACTIVE_NOW — score mémoire 7.293/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- PEPE-EUR — ACTIVE_NOW — score mémoire 7.143/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- XMN-EUR — MEMORY_24H — score mémoire 7.062/10 — sources ACCELERATION — MEMORY_ONLY

## Audit des plus fortes hausses

- HOT-EUR +14.92% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- TREAD-EUR +10.56% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- INIT-EUR +10.01% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- G-EUR +9.40% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- FLOCK-EUR +9.04% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- TRUMP-EUR +7.73% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- BIO-EUR +7.65% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- POWR-EUR +7.35% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- FUN-EUR +6.90% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE
- ZEUS-EUR +6.73% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE

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
