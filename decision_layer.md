# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-11-15T07:57:35.916128+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : aucun candidat matériel
- **MEILLEUR_LATENT_ACCELERATOR** : aucun candidat matériel
- **MEILLEUR_PULLBACK_REENTRY** : DODO-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 7.144 | entrée 5.850 | trend 8.300 | rang 6.815
  - Trend remains strong; candidate retained for re-entry instead of discarded.

## Tous les achats immédiats

Aucun ACHETE_MAINTENANT dans le classement complet.

## Top cross-sectionnel — aperçu non exhaustif

Ce top est une vue courte multi-buckets. Il ne doit jamais être utilisé comme liste exhaustive des achats immédiats.
1. DODO-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 6.815
2. KITE-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 6.595

## Accélération indépendante

- LAPTOP-EUR — CONFIRMED_ACCELERATION — score 8.516/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- IMU-EUR — MEMORY_24H — score mémoire 9.005/10 — sources ACCELERATION — MEMORY_ONLY
- NES-EUR — MEMORY_24H — score mémoire 8.757/10 — sources ACCELERATION — MEMORY_ONLY
- LAPTOP-EUR — ACTIVE_NOW — score mémoire 8.516/10 — sources ACCELERATION — WATCH_ONLY
- CAP-EUR — MEMORY_24H — score mémoire 6.858/10 — sources ACCELERATION, DECISION_LAYER — MEMORY_ONLY
- DODO-EUR — ACTIVE_NOW — score mémoire 6.815/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- KITE-EUR — ACTIVE_NOW — score mémoire 6.595/10 — sources DECISION_LAYER — WATCH_ONLY
- KNTQ-EUR — MEMORY_24H — score mémoire 6.492/10 — sources ACCELERATION — MEMORY_ONLY
- SHELL-EUR — MEMORY_24H — score mémoire 6.487/10 — sources DECISION_LAYER — MEMORY_ONLY
- SLX-EUR — MEMORY_DECAY_24_72H — score mémoire 6.482/10 — sources ACCELERATION — MEMORY_ONLY
- ZEUS-EUR — MEMORY_DECAY_24_72H — score mémoire 6.339/10 — sources ACCELERATION — MEMORY_ONLY

## Audit des plus fortes hausses

- NES-EUR +20.38% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- BOB-EUR +19.13% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- PROMPT-EUR +11.00% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- MEGA-EUR +9.18% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- VVV-EUR +5.57% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- INIT-EUR +4.86% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- GIGA-EUR +4.45% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- THQ-EUR +4.34% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- KITE-EUR +3.53% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE
- XAN-EUR +2.98% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE

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
