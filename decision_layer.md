# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-11-10T19:03:59.760115+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : aucun candidat matériel
- **MEILLEUR_LATENT_ACCELERATOR** : aucun candidat matériel
- **MEILLEUR_PULLBACK_REENTRY** : PEPE-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 6.975 | entrée 7.250 | trend 8.050 | rang 6.924
  - Trend remains strong; candidate retained for re-entry instead of discarded.

## Tous les achats immédiats

Aucun ACHETE_MAINTENANT dans le classement complet.

## Top cross-sectionnel — aperçu non exhaustif

Ce top est une vue courte multi-buckets. Il ne doit jamais être utilisé comme liste exhaustive des achats immédiats.
1. PEPE-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 6.924
2. BEAM-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 6.276
3. MERL-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 5.998

## Accélération indépendante

- THQ-EUR — CONFIRMED_ACCELERATION — score 9.396/10 — DETECTED_BUT_TOO_LATE
- MERL-EUR — CONFIRMED_ACCELERATION — score 9.228/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- XMN-EUR — CONFIRMED_ACCELERATION — score 6.804/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- PROM-EUR — BUILDING_ACCELERATION — score 5.539/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- RAD-EUR — BUILDING_ACCELERATION — score 5.433/10 — DETECTED_BUT_TOO_LATE
- LAPTOP-EUR — BUILDING_ACCELERATION — score 5.383/10 — DETECTED_BUT_TOO_LATE
- ARX-EUR — BUILDING_ACCELERATION — score 4.964/10 — DETECTED_BUT_TOO_LATE
- LUMIA-EUR — BUILDING_ACCELERATION — score 4.896/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- THQ-EUR — ACTIVE_NOW — score mémoire 9.396/10 — sources ACCELERATION — DETECTED_BUT_TOO_LATE
- MERL-EUR — ACTIVE_NOW — score mémoire 9.228/10 — sources ACCELERATION, DECISION_LAYER — WATCH_ONLY
- CYBER-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION — MEMORY_ONLY
- ZIL-EUR — MEMORY_DECAY_24_72H — score mémoire 8.210/10 — sources ACCELERATION — MEMORY_ONLY
- CELR-EUR — MEMORY_24H — score mémoire 8.204/10 — sources ACCELERATION — MEMORY_ONLY
- PEPE-EUR — ACTIVE_NOW — score mémoire 6.924/10 — sources DECISION_LAYER — WATCH_ONLY
- XMN-EUR — ACTIVE_NOW — score mémoire 6.804/10 — sources ACCELERATION — WATCH_ONLY
- USELESS-EUR — MEMORY_DECAY_24_72H — score mémoire 6.794/10 — sources ACCELERATION — MEMORY_ONLY
- BIRB-EUR — MEMORY_24H — score mémoire 6.501/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- MEGA-EUR — MEMORY_24H — score mémoire 6.433/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY

## Audit des plus fortes hausses

- CYBER-EUR +12.82% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- ACT-EUR +12.54% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- AGI-EUR +11.01% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- GRAM-EUR +8.41% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE
- NES-EUR +6.10% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- MOCA-EUR +5.04% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- O-EUR +4.68% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- RECALL-EUR +4.35% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE
- XDP-EUR +4.34% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE
- THQ-EUR +4.23% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE

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
