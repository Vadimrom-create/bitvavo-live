# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-10-10T23:55:33.648196+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : AERO-EUR | action PLACE_LIMITE_PASSIVE | opportunité 7.589 | entrée 6.050 | trend 8.850 | rang 6.884
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : aucun candidat matériel
- **MEILLEUR_PULLBACK_REENTRY** : IMX-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.432 | entrée 6.000 | trend 9.000 | rang 7.868
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Tous les achats immédiats

Aucun ACHETE_MAINTENANT dans le classement complet.

## Top cross-sectionnel — aperçu non exhaustif

Ce top est une vue courte multi-buckets. Il ne doit jamais être utilisé comme liste exhaustive des achats immédiats.
1. IMX-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.868
2. RAY-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.242
3. JUP-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.040

## Accélération indépendante

- TREAD-EUR — CONFIRMED_ACCELERATION — score 8.918/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- BAT-EUR — BUILDING_ACCELERATION — score 6.194/10 — DETECTED_BUT_TOO_LATE
- PNT-EUR — BUILDING_ACCELERATION — score 5.615/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- ZEUS-EUR — BUILDING_ACCELERATION — score 5.460/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- GTC-EUR — MEMORY_24H — score mémoire 9.580/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- C98-EUR — MEMORY_24H — score mémoire 8.963/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- TREAD-EUR — ACTIVE_NOW — score mémoire 8.918/10 — sources ACCELERATION, V4 — WATCH_ONLY
- BRETT-EUR — MEMORY_24H — score mémoire 8.610/10 — sources ACCELERATION — MEMORY_ONLY
- LRC-EUR — MEMORY_24H — score mémoire 8.600/10 — sources ACCELERATION — MEMORY_ONLY
- O-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- CT-EUR — MEMORY_DECAY_24_72H — score mémoire 8.022/10 — sources ACCELERATION — MEMORY_ONLY
- CELR-EUR — MEMORY_DECAY_24_72H — score mémoire 8.019/10 — sources ACCELERATION — MEMORY_ONLY
- ZORA-EUR — MEMORY_24H — score mémoire 7.933/10 — sources ACCELERATION — MEMORY_ONLY
- IMX-EUR — ACTIVE_NOW — score mémoire 7.868/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY

## Audit des plus fortes hausses

- STRK-EUR +42.41% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- CHIP-EUR +31.43% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- TIA-EUR +29.72% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- LUMIA-EUR +25.35% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- AERO-EUR +16.10% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- AZTEC-EUR +15.37% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE
- BRETT-EUR +11.04% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- EIGEN-EUR +10.19% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE
- INJ-EUR +9.85% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE
- WLD-EUR +9.17% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE

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
