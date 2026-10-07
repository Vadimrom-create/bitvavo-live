# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-10-07T23:18:11.534725+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : PARTI-EUR | action PLACE_LIMITE_PASSIVE | opportunité 7.648 | entrée 6.550 | trend 8.600 | rang 7.563
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : aucun candidat matériel
- **MEILLEUR_PULLBACK_REENTRY** : WAL-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.313 | entrée 6.700 | trend 8.450 | rang 7.824
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Tous les achats immédiats

Aucun ACHETE_MAINTENANT dans le classement complet.

## Top cross-sectionnel — aperçu non exhaustif

Ce top est une vue courte multi-buckets. Il ne doit jamais être utilisé comme liste exhaustive des achats immédiats.
1. WAL-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.824
2. PARTI-EUR — MEILLEURE_LIMITE_PASSIVE — PLACE_LIMITE_PASSIVE — rank 7.563
3. SENT-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.405

## Accélération indépendante

- W-EUR — CONFIRMED_ACCELERATION — score 7.488/10 — DETECTED_BUT_TOO_LATE
- ZEUS-EUR — BUILDING_ACCELERATION — score 4.802/10 — DETECTED_BUT_TOO_LATE
- O-EUR — BUILDING_ACCELERATION — score 4.782/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- POND-EUR — MEMORY_24H — score mémoire 10.000/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- SWELL-EUR — MEMORY_24H — score mémoire 9.284/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- NOS-EUR — MEMORY_24H — score mémoire 8.214/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- CHIP-EUR — MEMORY_DECAY_24_72H — score mémoire 7.983/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- WAL-EUR — ACTIVE_NOW — score mémoire 7.824/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- PARTI-EUR — ACTIVE_NOW — score mémoire 7.563/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- VELO-EUR — MEMORY_24H — score mémoire 7.495/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- W-EUR — ACTIVE_NOW — score mémoire 7.488/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- SENT-EUR — ACTIVE_NOW — score mémoire 7.405/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- MAGIC-EUR — ACTIVE_NOW — score mémoire 7.365/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY

## Audit des plus fortes hausses

- ZEUS-EUR +74.57% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- MET-EUR +39.83% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- GTC-EUR +26.54% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- LAPTOP-EUR +20.58% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- SAND-EUR +16.94% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- GLMR-EUR +16.38% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- RAY-EUR +12.92% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- W-EUR +8.81% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- FLUID-EUR +7.78% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE
- PROM-EUR +7.08% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE

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
