# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-11-15T01:15:16.565008+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : aucun candidat matériel
- **MEILLEUR_LATENT_ACCELERATOR** : aucun candidat matériel
- **MEILLEUR_PULLBACK_REENTRY** : CAP-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 6.966 | entrée 5.850 | trend 8.200 | rang 6.858
  - Trend remains strong; candidate retained for re-entry instead of discarded.

## Tous les achats immédiats

Aucun ACHETE_MAINTENANT dans le classement complet.

## Top cross-sectionnel — aperçu non exhaustif

Ce top est une vue courte multi-buckets. Il ne doit jamais être utilisé comme liste exhaustive des achats immédiats.
1. CAP-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 6.858
2. DODO-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 6.673
3. KITE-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 6.606

## Accélération indépendante

- NES-EUR — CONFIRMED_ACCELERATION — score 8.757/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- FTT-EUR — BUILDING_ACCELERATION — score 6.125/10 — DETECTED_BUT_TOO_LATE
- WELL-EUR — BUILDING_ACCELERATION — score 5.769/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- TRAC-EUR — BUILDING_ACCELERATION — score 5.271/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- IMU-EUR — MEMORY_24H — score mémoire 9.005/10 — sources ACCELERATION — MEMORY_ONLY
- NES-EUR — ACTIVE_NOW — score mémoire 8.757/10 — sources ACCELERATION — WATCH_ONLY
- ZEUS-EUR — MEMORY_DECAY_24_72H — score mémoire 7.401/10 — sources ACCELERATION — MEMORY_ONLY
- SLX-EUR — MEMORY_24H — score mémoire 7.091/10 — sources ACCELERATION — MEMORY_ONLY
- CAP-EUR — ACTIVE_NOW — score mémoire 6.858/10 — sources ACCELERATION, DECISION_LAYER — WATCH_ONLY
- DODO-EUR — ACTIVE_NOW — score mémoire 6.673/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- KITE-EUR — ACTIVE_NOW — score mémoire 6.606/10 — sources DECISION_LAYER — WATCH_ONLY
- KNTQ-EUR — MEMORY_24H — score mémoire 6.492/10 — sources ACCELERATION — MEMORY_ONLY
- SHELL-EUR — MEMORY_24H — score mémoire 6.487/10 — sources DECISION_LAYER — MEMORY_ONLY
- TAI-EUR — MEMORY_DECAY_24_72H — score mémoire 6.471/10 — sources ACCELERATION — MEMORY_ONLY

## Audit des plus fortes hausses

- BOB-EUR +20.40% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- PROMPT-EUR +18.54% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- DODO-EUR +7.53% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- THQ-EUR +5.83% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- ALLO-EUR +3.00% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE
- CAP-EUR +2.59% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- TAI-EUR +2.22% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- XDP-EUR +1.82% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE
- MERL-EUR +1.26% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE
- CTR-EUR +0.85% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE

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
