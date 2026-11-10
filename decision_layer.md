# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-11-10T11:58:58.663722+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : aucun candidat matériel
- **MEILLEUR_LATENT_ACCELERATOR** : aucun candidat matériel
- **MEILLEUR_PULLBACK_REENTRY** : MEGA-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 6.590 | entrée 5.550 | trend 7.600 | rang 6.433
  - Trend remains strong; candidate retained for re-entry instead of discarded.

## Tous les achats immédiats

Aucun ACHETE_MAINTENANT dans le classement complet.

## Top cross-sectionnel — aperçu non exhaustif

Ce top est une vue courte multi-buckets. Il ne doit jamais être utilisé comme liste exhaustive des achats immédiats.
1. MEGA-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 6.433

## Accélération indépendante

- CYBER-EUR — CONFIRMED_ACCELERATION — score 8.500/10 — DETECTED_BUT_TOO_LATE
- CELR-EUR — CONFIRMED_ACCELERATION — score 8.204/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- XMN-EUR — BUILDING_ACCELERATION — score 6.260/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- PUFFER-EUR — BUILDING_ACCELERATION — score 6.027/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- SUPER-EUR — BUILDING_ACCELERATION — score 4.968/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- ZIL-EUR — MEMORY_DECAY_24_72H — score mémoire 9.653/10 — sources ACCELERATION — MEMORY_ONLY
- CYBER-EUR — ACTIVE_NOW — score mémoire 8.500/10 — sources ACCELERATION — DETECTED_BUT_TOO_LATE
- CELR-EUR — ACTIVE_NOW — score mémoire 8.204/10 — sources ACCELERATION — WATCH_ONLY
- USELESS-EUR — MEMORY_DECAY_24_72H — score mémoire 7.988/10 — sources ACCELERATION — MEMORY_ONLY
- QUID-EUR — MEMORY_DECAY_24_72H — score mémoire 7.477/10 — sources ACCELERATION — MEMORY_ONLY
- CHILLGUY-EUR — MEMORY_DECAY_24_72H — score mémoire 7.447/10 — sources ACCELERATION — MEMORY_ONLY
- TRUST-EUR — MEMORY_DECAY_24_72H — score mémoire 6.998/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- WIN-EUR — MEMORY_DECAY_24_72H — score mémoire 6.877/10 — sources ACCELERATION — MEMORY_ONLY
- SCR-EUR — MEMORY_DECAY_24_72H — score mémoire 6.711/10 — sources ACCELERATION — MEMORY_ONLY
- BIRB-EUR — MEMORY_24H — score mémoire 6.501/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY

## Audit des plus fortes hausses

- CYBER-EUR +22.24% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- INIT-EUR +11.73% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- ACT-EUR +10.30% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- JUP-EUR +7.53% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE
- BEAM-EUR +7.44% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE
- DEGEN-EUR +6.58% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- PYTH-EUR +5.83% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE
- CPOOL-EUR +5.80% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- HOT-EUR +5.71% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- ONDO-EUR +5.46% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE

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
