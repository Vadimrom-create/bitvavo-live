# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-11-14T17:04:46.655165+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : aucun candidat matériel
- **MEILLEUR_LATENT_ACCELERATOR** : aucun candidat matériel
- **MEILLEUR_PULLBACK_REENTRY** : CAP-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 6.774 | entrée 5.900 | trend 8.200 | rang 6.644
  - Trend remains strong; candidate retained for re-entry instead of discarded.

## Tous les achats immédiats

Aucun ACHETE_MAINTENANT dans le classement complet.

## Top cross-sectionnel — aperçu non exhaustif

Ce top est une vue courte multi-buckets. Il ne doit jamais être utilisé comme liste exhaustive des achats immédiats.
1. CAP-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 6.644
2. KITE-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 6.324
3. MERL-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 6.238

## Accélération indépendante

- PROMPT-EUR — CONFIRMED_ACCELERATION — score 10.000/10 — DETECTED_BUT_TOO_LATE
- IMU-EUR — CONFIRMED_ACCELERATION — score 9.005/10 — DETECTED_BUT_TOO_LATE
- KNTQ-EUR — BUILDING_ACCELERATION — score 6.492/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- NOS-EUR — BUILDING_ACCELERATION — score 5.598/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- XMN-EUR — BUILDING_ACCELERATION — score 5.345/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- DODO-EUR — BUILDING_ACCELERATION — score 5.091/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- PROMPT-EUR — ACTIVE_NOW — score mémoire 10.000/10 — sources ACCELERATION — DETECTED_BUT_TOO_LATE
- IMU-EUR — ACTIVE_NOW — score mémoire 9.005/10 — sources ACCELERATION — DETECTED_BUT_TOO_LATE
- ZEUS-EUR — MEMORY_24H — score mémoire 7.598/10 — sources ACCELERATION — MEMORY_ONLY
- TAI-EUR — MEMORY_24H — score mémoire 7.492/10 — sources ACCELERATION — MEMORY_ONLY
- SLX-EUR — MEMORY_24H — score mémoire 7.091/10 — sources ACCELERATION — MEMORY_ONLY
- CAP-EUR — ACTIVE_NOW — score mémoire 6.644/10 — sources ACCELERATION, DECISION_LAYER — WATCH_ONLY
- SXT-EUR — MEMORY_24H — score mémoire 6.517/10 — sources DECISION_LAYER, V4 — MEMORY_ONLY
- KNTQ-EUR — ACTIVE_NOW — score mémoire 6.492/10 — sources ACCELERATION — WATCH_ONLY
- KITE-EUR — ACTIVE_NOW — score mémoire 6.324/10 — sources DECISION_LAYER — WATCH_ONLY
- MERL-EUR — ACTIVE_NOW — score mémoire 6.238/10 — sources DECISION_LAYER — WATCH_ONLY

## Audit des plus fortes hausses

- BOB-EUR +31.27% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- DODO-EUR +14.66% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- PROMPT-EUR +6.85% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- SHELL-EUR +4.77% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- MERL-EUR +4.14% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE
- CNPY-EUR +3.99% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- CAP-EUR +3.96% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- QKC-EUR +3.92% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE
- ZEUS-EUR +2.03% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- ALLO-EUR +1.75% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE

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
