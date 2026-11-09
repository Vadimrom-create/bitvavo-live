# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-11-09T03:03:46.571075+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : aucun candidat matériel
- **MEILLEUR_LATENT_ACCELERATOR** : aucun candidat matériel
- **MEILLEUR_PULLBACK_REENTRY** : RSR-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 6.915 | entrée 6.100 | trend 7.750 | rang 6.495
  - Trend remains strong; candidate retained for re-entry instead of discarded.

## Tous les achats immédiats

Aucun ACHETE_MAINTENANT dans le classement complet.

## Top cross-sectionnel — aperçu non exhaustif

Ce top est une vue courte multi-buckets. Il ne doit jamais être utilisé comme liste exhaustive des achats immédiats.
1. RSR-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 6.495
2. BIRB-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 6.493
3. MEGA-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 6.236

## Accélération indépendante

- OSMO-EUR — CONFIRMED_ACCELERATION — score 7.500/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- WHUF-EUR — CONFIRMED_ACCELERATION — score 7.060/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- RE-EUR — BUILDING_ACCELERATION — score 4.861/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- WIN-EUR — MEMORY_24H — score mémoire 9.248/10 — sources ACCELERATION — MEMORY_ONLY
- EPIC-EUR — MEMORY_24H — score mémoire 8.694/10 — sources ACCELERATION — MEMORY_ONLY
- DGB-EUR — MEMORY_DECAY_24_72H — score mémoire 7.926/10 — sources ACCELERATION — MEMORY_ONLY
- XMN-EUR — MEMORY_24H — score mémoire 7.777/10 — sources ACCELERATION — MEMORY_ONLY
- OSMO-EUR — ACTIVE_NOW — score mémoire 7.500/10 — sources ACCELERATION — WATCH_ONLY
- WHUF-EUR — ACTIVE_NOW — score mémoire 7.060/10 — sources ACCELERATION — WATCH_ONLY
- GNS-EUR — MEMORY_24H — score mémoire 6.780/10 — sources ACCELERATION — MEMORY_ONLY
- TRUST-EUR — MEMORY_24H — score mémoire 6.742/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- BLEND-EUR — MEMORY_DECAY_24_72H — score mémoire 6.685/10 — sources ACCELERATION — MEMORY_ONLY
- RSR-EUR — ACTIVE_NOW — score mémoire 6.495/10 — sources ACCELERATION, DECISION_LAYER — DETECTED_BUT_TOO_LATE

## Audit des plus fortes hausses

- GNS-EUR +24.90% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- GTC-EUR +13.61% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- HOT-EUR +13.24% — DETECTED_TOO_LATE — couche NONE — action INTERPRETATION
- RSR-EUR +10.39% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- ICNT-EUR +9.17% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- MERL-EUR +7.72% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- O-EUR +6.79% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- SAFE-EUR +5.56% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE
- INIT-EUR +5.41% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE
- PEPE-EUR +5.30% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE

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
