# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-10-07T21:55:32.043594+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : aucun candidat matériel
- **MEILLEUR_LATENT_ACCELERATOR** : aucun candidat matériel
- **MEILLEUR_PULLBACK_REENTRY** : SENT-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 7.727 | entrée 6.650 | trend 8.550 | rang 7.348
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Tous les achats immédiats

Aucun ACHETE_MAINTENANT dans le classement complet.

## Top cross-sectionnel — aperçu non exhaustif

Ce top est une vue courte multi-buckets. Il ne doit jamais être utilisé comme liste exhaustive des achats immédiats.
1. SENT-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.348
2. MAGIC-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.326
3. PARTI-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.235

## Accélération indépendante

- VELO-EUR — CONFIRMED_ACCELERATION — score 7.495/10 — DETECTED_BUT_TOO_LATE
- WIN-EUR — BUILDING_ACCELERATION — score 6.266/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- POND-EUR — MEMORY_24H — score mémoire 10.000/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- SWELL-EUR — MEMORY_24H — score mémoire 9.284/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- CHIP-EUR — MEMORY_DECAY_24_72H — score mémoire 8.220/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- SOSO-EUR — MEMORY_DECAY_24_72H — score mémoire 7.562/10 — sources ACCELERATION — MEMORY_ONLY
- VELO-EUR — ACTIVE_NOW — score mémoire 7.495/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- STX-EUR — MEMORY_24H — score mémoire 7.349/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- SENT-EUR — ACTIVE_NOW — score mémoire 7.348/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- MAGIC-EUR — ACTIVE_NOW — score mémoire 7.326/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- ARPA-EUR — MEMORY_24H — score mémoire 7.305/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- PARTI-EUR — ACTIVE_NOW — score mémoire 7.235/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY

## Audit des plus fortes hausses

- ZEUS-EUR +77.19% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- MET-EUR +36.72% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- SAND-EUR +18.51% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- LAPTOP-EUR +18.21% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- GTC-EUR +16.84% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- GLMR-EUR +16.03% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- RAY-EUR +11.83% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- FLUID-EUR +7.91% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE
- MOVR-EUR +6.62% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- PROM-EUR +5.13% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE

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
