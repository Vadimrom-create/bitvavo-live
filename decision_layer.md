# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-11-08T23:40:35.752819+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : aucun candidat matériel
- **MEILLEUR_LATENT_ACCELERATOR** : aucun candidat matériel
- **MEILLEUR_PULLBACK_REENTRY** : TRUST-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 7.202 | entrée 6.450 | trend 8.100 | rang 6.742
  - Trend remains strong; candidate retained for re-entry instead of discarded.

## Tous les achats immédiats

Aucun ACHETE_MAINTENANT dans le classement complet.

## Top cross-sectionnel — aperçu non exhaustif

Ce top est une vue courte multi-buckets. Il ne doit jamais être utilisé comme liste exhaustive des achats immédiats.
1. TRUST-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 6.742
2. BIRB-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 6.550

## Accélération indépendante

- WIN-EUR — CONFIRMED_ACCELERATION — score 9.248/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- NES-EUR — BUILDING_ACCELERATION — score 6.202/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- NOS-EUR — BUILDING_ACCELERATION — score 6.063/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- CTR-EUR — BUILDING_ACCELERATION — score 5.517/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- WIN-EUR — ACTIVE_NOW — score mémoire 9.248/10 — sources ACCELERATION — WATCH_ONLY
- WHUF-EUR — MEMORY_24H — score mémoire 8.877/10 — sources ACCELERATION — MEMORY_ONLY
- EPIC-EUR — MEMORY_24H — score mémoire 8.694/10 — sources ACCELERATION — MEMORY_ONLY
- DGB-EUR — MEMORY_DECAY_24_72H — score mémoire 8.589/10 — sources ACCELERATION — MEMORY_ONLY
- XMN-EUR — MEMORY_24H — score mémoire 7.777/10 — sources ACCELERATION — MEMORY_ONLY
- MEGA-EUR — MEMORY_24H — score mémoire 7.050/10 — sources DECISION_LAYER, V4 — MEMORY_ONLY
- INJ-EUR — MEMORY_DECAY_24_72H — score mémoire 6.941/10 — sources DECISION_LAYER, V4 — MEMORY_ONLY
- BLEND-EUR — MEMORY_24H — score mémoire 6.827/10 — sources ACCELERATION — MEMORY_ONLY
- GNS-EUR — MEMORY_24H — score mémoire 6.780/10 — sources ACCELERATION — MEMORY_ONLY
- TRUST-EUR — ACTIVE_NOW — score mémoire 6.742/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY

## Audit des plus fortes hausses

- GNS-EUR +45.43% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- HOT-EUR +14.00% — DETECTED_TOO_LATE — couche NONE — action INTERPRETATION
- ICNT-EUR +8.37% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- RSR-EUR +7.33% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- BLEND-EUR +6.81% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- MERL-EUR +5.45% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- WIN-EUR +4.97% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE
- O-EUR +4.40% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- PEPE-EUR +3.28% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE
- BEAM-EUR +3.07% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE

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
