# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-10-20T07:43:13.791959+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : aucun candidat matériel
- **MEILLEUR_LATENT_ACCELERATOR** : aucun candidat matériel
- **MEILLEUR_PULLBACK_REENTRY** : AMP-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 6.994 | entrée 5.800 | trend 8.100 | rang 6.650
  - Trend remains strong; candidate retained for re-entry instead of discarded.

## Tous les achats immédiats

Aucun ACHETE_MAINTENANT dans le classement complet.

## Top cross-sectionnel — aperçu non exhaustif

Ce top est une vue courte multi-buckets. Il ne doit jamais être utilisé comme liste exhaustive des achats immédiats.
1. AMP-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 6.650
2. DUSK-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 6.632
3. ALT-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 5.482

## Accélération indépendante

- GNS-EUR — CONFIRMED_ACCELERATION — score 9.505/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- ALT-EUR — CONFIRMED_ACCELERATION — score 7.981/10 — DETECTED_BUT_TOO_LATE
- WHUF-EUR — CONFIRMED_ACCELERATION — score 7.643/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- AVA-EUR — CONFIRMED_ACCELERATION — score 7.332/10 — DETECTED_BUT_TOO_LATE
- IO-EUR — CONFIRMED_ACCELERATION — score 6.506/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- IMU-EUR — BUILDING_ACCELERATION — score 5.528/10 — DETECTED_BUT_TOO_LATE
- ZBCN-EUR — BUILDING_ACCELERATION — score 5.289/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- BAT-EUR — BUILDING_ACCELERATION — score 4.962/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- GNS-EUR — ACTIVE_NOW — score mémoire 9.505/10 — sources ACCELERATION — WATCH_ONLY
- CTR-EUR — MEMORY_24H — score mémoire 9.247/10 — sources ACCELERATION — MEMORY_ONLY
- POND-EUR — MEMORY_24H — score mémoire 8.833/10 — sources ACCELERATION — MEMORY_ONLY
- ALT-EUR — ACTIVE_NOW — score mémoire 7.981/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- WHUF-EUR — ACTIVE_NOW — score mémoire 7.643/10 — sources ACCELERATION — WATCH_ONLY
- LSK-EUR — MEMORY_DECAY_24_72H — score mémoire 7.342/10 — sources ACCELERATION — MEMORY_ONLY
- AVA-EUR — ACTIVE_NOW — score mémoire 7.332/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- VVV-EUR — MEMORY_DECAY_24_72H — score mémoire 7.322/10 — sources ACCELERATION — MEMORY_ONLY
- BEAM-EUR — MEMORY_24H — score mémoire 7.244/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- DODO-EUR — MEMORY_24H — score mémoire 6.968/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY

## Audit des plus fortes hausses

- GTC-EUR +28.88% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- PHA-EUR +22.21% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- ALT-EUR +21.79% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- GNS-EUR +18.95% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- IMU-EUR +14.19% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- NIL-EUR +10.27% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- BEAM-EUR +10.19% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE
- METIS-EUR +9.31% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE
- OSMO-EUR +9.05% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- TREAD-EUR +8.47% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE

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
