# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-10-07T13:38:47.570997+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : aucun candidat matériel
- **MEILLEUR_LATENT_ACCELERATOR** : aucun candidat matériel
- **MEILLEUR_PULLBACK_REENTRY** : ESP-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 7.926 | entrée 5.100 | trend 8.450 | rang 7.360
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Tous les achats immédiats

Aucun ACHETE_MAINTENANT dans le classement complet.

## Top cross-sectionnel — aperçu non exhaustif

Ce top est une vue courte multi-buckets. Il ne doit jamais être utilisé comme liste exhaustive des achats immédiats.
1. ESP-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.360
2. FLUX-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.246
3. RENDER-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.085

## Accélération indépendante

- SWELL-EUR — CONFIRMED_ACCELERATION — score 9.284/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- RAY-EUR — CONFIRMED_ACCELERATION — score 7.050/10 — DETECTED_BUT_TOO_LATE
- CSPR-EUR — BUILDING_ACCELERATION — score 5.297/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- DOS-EUR — BUILDING_ACCELERATION — score 5.256/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- POND-EUR — MEMORY_24H — score mémoire 10.000/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- SWELL-EUR — ACTIVE_NOW — score mémoire 9.284/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- UMA-EUR — MEMORY_DECAY_24_72H — score mémoire 8.595/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- CHIP-EUR — MEMORY_24H — score mémoire 8.278/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- SOSO-EUR — MEMORY_24H — score mémoire 7.615/10 — sources ACCELERATION — MEMORY_ONLY
- ESP-EUR — ACTIVE_NOW — score mémoire 7.360/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- STX-EUR — MEMORY_24H — score mémoire 7.349/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- ARPA-EUR — MEMORY_24H — score mémoire 7.305/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- FLUX-EUR — ACTIVE_NOW — score mémoire 7.246/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- MIOTA-EUR — MEMORY_24H — score mémoire 7.205/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY

## Audit des plus fortes hausses

- ZEUS-EUR +205.83% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- RAY-EUR +15.84% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- SWELL-EUR +11.73% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- POND-EUR +9.03% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- GTC-EUR +7.67% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- SOSO-EUR +7.39% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- ORCA-EUR +7.28% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- BTT-EUR +6.75% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE
- GLMR-EUR +6.45% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- SAND-EUR +5.75% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE

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
