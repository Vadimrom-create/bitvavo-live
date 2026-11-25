# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-11-25T19:33:26.290381+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : aucun candidat matériel
- **MEILLEUR_LATENT_ACCELERATOR** : aucun candidat matériel
- **MEILLEUR_PULLBACK_REENTRY** : DODO-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 7.040 | entrée 4.900 | trend 8.400 | rang 6.831
  - Trend remains strong; candidate retained for re-entry instead of discarded.

## Tous les achats immédiats

Aucun ACHETE_MAINTENANT dans le classement complet.

## Top cross-sectionnel — aperçu non exhaustif

Ce top est une vue courte multi-buckets. Il ne doit jamais être utilisé comme liste exhaustive des achats immédiats.
1. DODO-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 6.831
2. VVV-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 6.299

## Accélération indépendante

- THQ-EUR — CONFIRMED_ACCELERATION — score 9.864/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- NES-EUR — CONFIRMED_ACCELERATION — score 9.564/10 — DETECTED_BUT_TOO_LATE
- KITE-EUR — BUILDING_ACCELERATION — score 6.449/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- SSV-EUR — BUILDING_ACCELERATION — score 6.374/10 — DETECTED_BUT_TOO_LATE
- MOVE-EUR — BUILDING_ACCELERATION — score 6.253/10 — DETECTED_BUT_TOO_LATE
- TAI-EUR — BUILDING_ACCELERATION — score 6.006/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- BIGTIME-EUR — BUILDING_ACCELERATION — score 5.938/10 — DETECTED_BUT_TOO_LATE
- IMX-EUR — BUILDING_ACCELERATION — score 5.724/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- VVV-EUR — BUILDING_ACCELERATION — score 5.641/10 — DETECTED_BUT_TOO_LATE
- MON-EUR — BUILDING_ACCELERATION — score 5.452/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- THQ-EUR — ACTIVE_NOW — score mémoire 9.864/10 — sources ACCELERATION — WATCH_ONLY
- NES-EUR — ACTIVE_NOW — score mémoire 9.564/10 — sources ACCELERATION — DETECTED_BUT_TOO_LATE
- IRYS-EUR — MEMORY_24H — score mémoire 7.372/10 — sources ACCELERATION, DECISION_LAYER — MEMORY_ONLY
- LISTA-EUR — MEMORY_DECAY_24_72H — score mémoire 7.268/10 — sources ACCELERATION, DECISION_LAYER — MEMORY_ONLY
- MMT-EUR — MEMORY_DECAY_24_72H — score mémoire 7.005/10 — sources ACCELERATION — MEMORY_ONLY
- DODO-EUR — ACTIVE_NOW — score mémoire 6.831/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- KITE-EUR — ACTIVE_NOW — score mémoire 6.764/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- SSV-EUR — ACTIVE_NOW — score mémoire 6.374/10 — sources ACCELERATION — DETECTED_BUT_TOO_LATE
- POND-EUR — MEMORY_24H — score mémoire 6.325/10 — sources ACCELERATION — MEMORY_ONLY
- VVV-EUR — ACTIVE_NOW — score mémoire 6.299/10 — sources ACCELERATION, DECISION_LAYER — DETECTED_BUT_TOO_LATE

## Audit des plus fortes hausses

- MANTRA-EUR +95.23% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- BIGTIME-EUR +65.11% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- SSV-EUR +44.46% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- MMT-EUR +36.02% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- BLUR-EUR +35.99% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- SLX-EUR +22.94% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- NES-EUR +20.83% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- MOODENG-EUR +19.85% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- MON-EUR +19.62% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- SOSO-EUR +19.34% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE

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
