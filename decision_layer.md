# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-11-28T02:57:34.297146+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : aucun candidat matériel
- **MEILLEUR_LATENT_ACCELERATOR** : aucun candidat matériel
- **MEILLEUR_PULLBACK_REENTRY** : ELSA-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 7.087 | entrée 6.250 | trend 8.300 | rang 6.740
  - Trend remains strong; candidate retained for re-entry instead of discarded.

## Tous les achats immédiats

Aucun ACHETE_MAINTENANT dans le classement complet.

## Top cross-sectionnel — aperçu non exhaustif

Ce top est une vue courte multi-buckets. Il ne doit jamais être utilisé comme liste exhaustive des achats immédiats.
1. ELSA-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 6.740
2. DBR-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 6.287

## Accélération indépendante

- SOSO-EUR — CONFIRMED_ACCELERATION — score 8.282/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- INIT-EUR — MEMORY_24H — score mémoire 9.317/10 — sources ACCELERATION — MEMORY_ONLY
- SOSO-EUR — ACTIVE_NOW — score mémoire 8.282/10 — sources ACCELERATION — DETECTED_BUT_TOO_LATE
- PORTAL-EUR — MEMORY_24H — score mémoire 7.613/10 — sources ACCELERATION — MEMORY_ONLY
- NOM-EUR — MEMORY_24H — score mémoire 7.461/10 — sources ACCELERATION — MEMORY_ONLY
- O-EUR — MEMORY_24H — score mémoire 7.422/10 — sources V4 — MEMORY_ONLY
- DODO-EUR — MEMORY_24H — score mémoire 6.879/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- AXIS-EUR — MEMORY_24H — score mémoire 6.826/10 — sources ACCELERATION — MEMORY_ONLY
- ELSA-EUR — ACTIVE_NOW — score mémoire 6.740/10 — sources ACCELERATION, DECISION_LAYER — DETECTED_BUT_TOO_LATE
- VVV-EUR — MEMORY_24H — score mémoire 6.659/10 — sources ACCELERATION, DECISION_LAYER — MEMORY_ONLY
- THE-EUR — MEMORY_24H — score mémoire 6.658/10 — sources ACCELERATION — MEMORY_ONLY

## Audit des plus fortes hausses

- PORTAL-EUR +68.83% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- HAEDAL-EUR +25.11% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- CFG-EUR +21.29% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- ROBO-EUR +11.99% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- SENT-EUR +11.46% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE
- YB-EUR +11.29% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- AVA-EUR +9.77% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE
- THE-EUR +9.64% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- TREAD-EUR +9.25% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- ICNT-EUR +8.85% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE

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
