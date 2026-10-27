# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-10-27T08:06:57.176860+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : INIT-EUR | action PLACE_LIMITE_PASSIVE | opportunité 7.486 | entrée 6.550 | trend 8.150 | rang 6.674
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : aucun candidat matériel
- **MEILLEUR_PULLBACK_REENTRY** : DODO-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 7.451 | entrée 5.450 | trend 8.300 | rang 7.130
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Tous les achats immédiats

Aucun ACHETE_MAINTENANT dans le classement complet.

## Top cross-sectionnel — aperçu non exhaustif

Ce top est une vue courte multi-buckets. Il ne doit jamais être utilisé comme liste exhaustive des achats immédiats.
1. DODO-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.130
2. WIN-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.011
3. REZ-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 6.715

## Accélération indépendante

- CAP-EUR — CONFIRMED_ACCELERATION — score 9.112/10 — DETECTED_BUT_TOO_LATE
- U-EUR — CONFIRMED_ACCELERATION — score 8.500/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- AVA-EUR — CONFIRMED_ACCELERATION — score 6.701/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- SYN-EUR — BUILDING_ACCELERATION — score 6.439/10 — DETECTED_BUT_TOO_LATE
- ADX-EUR — BUILDING_ACCELERATION — score 5.584/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- LIGHTER-EUR — BUILDING_ACCELERATION — score 5.513/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- OSMO-EUR — BUILDING_ACCELERATION — score 5.500/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- SOON-EUR — BUILDING_ACCELERATION — score 4.869/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- CAP-EUR — ACTIVE_NOW — score mémoire 9.112/10 — sources ACCELERATION — DETECTED_BUT_TOO_LATE
- GROVE-EUR — MEMORY_24H — score mémoire 8.703/10 — sources ACCELERATION — MEMORY_ONLY
- U-EUR — ACTIVE_NOW — score mémoire 8.500/10 — sources ACCELERATION — WATCH_ONLY
- PROMPT-EUR — MEMORY_DECAY_24_72H — score mémoire 7.376/10 — sources ACCELERATION — MEMORY_ONLY
- IMU-EUR — MEMORY_24H — score mémoire 7.235/10 — sources ACCELERATION — MEMORY_ONLY
- DODO-EUR — ACTIVE_NOW — score mémoire 7.130/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- PHA-EUR — MEMORY_DECAY_24_72H — score mémoire 7.075/10 — sources ACCELERATION, DECISION_LAYER — MEMORY_ONLY
- WIN-EUR — ACTIVE_NOW — score mémoire 7.011/10 — sources DECISION_LAYER, V4 — WATCH_ONLY
- WHUF-EUR — MEMORY_DECAY_24_72H — score mémoire 7.000/10 — sources ACCELERATION — MEMORY_ONLY
- KAT-EUR — MEMORY_24H — score mémoire 6.995/10 — sources ACCELERATION — MEMORY_ONLY

## Audit des plus fortes hausses

- ZRC-EUR +30.77% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- SYN-EUR +28.26% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- SOON-EUR +15.68% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- CAP-EUR +15.09% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- NIL-EUR +15.06% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- PARTI-EUR +14.79% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- CHIP-EUR +13.29% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- HUMA-EUR +12.56% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- TRIA-EUR +12.02% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- VERONA-EUR +10.83% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE

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
