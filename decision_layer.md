# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-11-14T03:50:16.989743+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : DODO-EUR | action PLACE_LIMITE_PASSIVE | opportunité 7.563 | entrée 6.350 | trend 8.850 | rang 7.226
  - Strong structure but imperfect current entry; prefer passive execution. High extension/chase reduces rank but does not erase the setup.
- **MEILLEUR_LATENT_ACCELERATOR** : aucun candidat matériel
- **MEILLEUR_PULLBACK_REENTRY** : CAP-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 7.109 | entrée 6.800 | trend 7.850 | rang 6.825
  - Trend remains strong; candidate retained for re-entry instead of discarded.

## Tous les achats immédiats

Aucun ACHETE_MAINTENANT dans le classement complet.

## Top cross-sectionnel — aperçu non exhaustif

Ce top est une vue courte multi-buckets. Il ne doit jamais être utilisé comme liste exhaustive des achats immédiats.
1. DODO-EUR — MEILLEURE_LIMITE_PASSIVE — PLACE_LIMITE_PASSIVE — rank 7.226
2. CAP-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 6.825

## Accélération indépendante

- SLX-EUR — CONFIRMED_ACCELERATION — score 7.091/10 — DETECTED_BUT_TOO_LATE
- SENT-EUR — BUILDING_ACCELERATION — score 5.132/10 — DETECTED_BUT_TOO_LATE
- KMNO-EUR — BUILDING_ACCELERATION — score 5.070/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- ZEUS-EUR — MEMORY_24H — score mémoire 7.598/10 — sources ACCELERATION — MEMORY_ONLY
- TAI-EUR — MEMORY_24H — score mémoire 7.492/10 — sources ACCELERATION — MEMORY_ONLY
- DODO-EUR — ACTIVE_NOW — score mémoire 7.226/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- SLX-EUR — ACTIVE_NOW — score mémoire 7.091/10 — sources ACCELERATION — DETECTED_BUT_TOO_LATE
- CAP-EUR — ACTIVE_NOW — score mémoire 6.825/10 — sources ACCELERATION, DECISION_LAYER — WATCH_ONLY
- ALIGN-EUR — MEMORY_DECAY_24_72H — score mémoire 6.738/10 — sources ACCELERATION — MEMORY_ONLY
- INIT-EUR — MEMORY_DECAY_24_72H — score mémoire 6.720/10 — sources ACCELERATION — MEMORY_ONLY
- SXT-EUR — MEMORY_24H — score mémoire 6.517/10 — sources DECISION_LAYER, V4 — MEMORY_ONLY
- CROSS-EUR — MEMORY_24H — score mémoire 6.478/10 — sources V4 — MEMORY_ONLY
- KITE-EUR — MEMORY_DECAY_24_72H — score mémoire 6.440/10 — sources DECISION_LAYER — MEMORY_ONLY

## Audit des plus fortes hausses

- SHELL-EUR +75.63% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- SLX-EUR +14.66% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE
- ZEUS-EUR +13.94% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- ARX-EUR +12.59% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- DODO-EUR +10.72% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- BILL-EUR +9.38% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- SQD-EUR +8.81% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE
- INJ-EUR +8.45% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE
- BOB-EUR +7.87% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- BLEND-EUR +7.80% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE

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
