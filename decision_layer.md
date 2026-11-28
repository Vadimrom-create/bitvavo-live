# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-11-28T18:58:55.728158+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : aucun candidat matériel
- **MEILLEUR_LATENT_ACCELERATOR** : aucun candidat matériel
- **MEILLEUR_PULLBACK_REENTRY** : ACT-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 6.585 | entrée 5.950 | trend 7.850 | rang 6.532
  - Trend remains strong; candidate retained for re-entry instead of discarded.

## Tous les achats immédiats

Aucun ACHETE_MAINTENANT dans le classement complet.

## Top cross-sectionnel — aperçu non exhaustif

Ce top est une vue courte multi-buckets. Il ne doit jamais être utilisé comme liste exhaustive des achats immédiats.
1. ACT-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 6.532
2. ELSA-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 6.068

## Accélération indépendante

- TAI-EUR — CONFIRMED_ACCELERATION — score 9.000/10 — DETECTED_BUT_TOO_LATE
- WLFI-EUR — CONFIRMED_ACCELERATION — score 6.825/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- LAPTOP-EUR — CONFIRMED_ACCELERATION — score 6.651/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- INIT-EUR — BUILDING_ACCELERATION — score 5.974/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- CVC-EUR — BUILDING_ACCELERATION — score 5.592/10 — DETECTED_BUT_TOO_LATE
- LUNA-EUR — BUILDING_ACCELERATION — score 5.189/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- O-EUR — MEMORY_24H — score mémoire 9.678/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- TAI-EUR — ACTIVE_NOW — score mémoire 9.000/10 — sources ACCELERATION — DETECTED_BUT_TOO_LATE
- SOSO-EUR — MEMORY_24H — score mémoire 8.282/10 — sources ACCELERATION — MEMORY_ONLY
- NOM-EUR — MEMORY_24H — score mémoire 7.461/10 — sources ACCELERATION — MEMORY_ONLY
- SENT-EUR — ACTIVE_NOW — score mémoire 7.314/10 — sources DECISION_LAYER, V4 — WATCH_ONLY
- DODO-EUR — MEMORY_24H — score mémoire 6.879/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- WLFI-EUR — ACTIVE_NOW — score mémoire 6.825/10 — sources ACCELERATION — WATCH_ONLY
- VVV-EUR — MEMORY_24H — score mémoire 6.659/10 — sources ACCELERATION, DECISION_LAYER — MEMORY_ONLY
- THE-EUR — MEMORY_24H — score mémoire 6.658/10 — sources ACCELERATION — MEMORY_ONLY
- LAPTOP-EUR — ACTIVE_NOW — score mémoire 6.651/10 — sources ACCELERATION — WATCH_ONLY

## Audit des plus fortes hausses

- O-EUR +42.24% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- TAI-EUR +22.33% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- NES-EUR +16.70% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ELSA-EUR +15.01% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- LISTA-EUR +12.75% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- RAD-EUR +10.37% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- PARTI-EUR +8.77% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- IQ-EUR +7.07% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- SENT-EUR +5.59% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE
- THE-EUR +5.49% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE

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
