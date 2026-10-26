# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-10-26T19:56:52.025472+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : aucun candidat matériel
- **MEILLEUR_LATENT_ACCELERATOR** : DODO-EUR | action LATENT_ACCELERATOR | opportunité 7.450 | entrée 5.650 | trend 8.450 | rang 7.118
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : ELSA-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 7.092 | entrée 5.850 | trend 8.250 | rang 6.703
  - Trend remains strong; candidate retained for re-entry instead of discarded.

## Tous les achats immédiats

Aucun ACHETE_MAINTENANT dans le classement complet.

## Top cross-sectionnel — aperçu non exhaustif

Ce top est une vue courte multi-buckets. Il ne doit jamais être utilisé comme liste exhaustive des achats immédiats.
1. DODO-EUR — MEILLEUR_LATENT_ACCELERATOR — LATENT_ACCELERATOR — rank 7.118
2. ELSA-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 6.703
3. INIT-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 6.686

## Accélération indépendante

- GROVE-EUR — CONFIRMED_ACCELERATION — score 8.703/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- IMU-EUR — CONFIRMED_ACCELERATION — score 7.235/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- VERONA-EUR — BUILDING_ACCELERATION — score 5.189/10 — DETECTED_BUT_TOO_LATE
- ELSA-EUR — BUILDING_ACCELERATION — score 4.805/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- PTB-EUR — MEMORY_24H — score mémoire 8.912/10 — sources ACCELERATION — MEMORY_ONLY
- WHUF-EUR — MEMORY_24H — score mémoire 8.890/10 — sources ACCELERATION — MEMORY_ONLY
- GROVE-EUR — ACTIVE_NOW — score mémoire 8.703/10 — sources ACCELERATION — WATCH_ONLY
- PROMPT-EUR — MEMORY_24H — score mémoire 8.512/10 — sources ACCELERATION — MEMORY_ONLY
- TREAD-EUR — MEMORY_DECAY_24_72H — score mémoire 7.588/10 — sources ACCELERATION — MEMORY_ONLY
- PHA-EUR — MEMORY_24H — score mémoire 7.246/10 — sources ACCELERATION, DECISION_LAYER — MEMORY_ONLY
- IMU-EUR — ACTIVE_NOW — score mémoire 7.235/10 — sources ACCELERATION — WATCH_ONLY
- DODO-EUR — ACTIVE_NOW — score mémoire 7.118/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- AMP-EUR — MEMORY_DECAY_24_72H — score mémoire 7.098/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- HAEDAL-EUR — MEMORY_24H — score mémoire 7.035/10 — sources ACCELERATION — MEMORY_ONLY

## Audit des plus fortes hausses

- ZRC-EUR +32.59% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- VERONA-EUR +22.30% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- CHIP-EUR +17.78% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- BEAM-EUR +14.35% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- PARTI-EUR +14.17% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- NEX-EUR +13.24% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- HAEDAL-EUR +12.06% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE
- SOON-EUR +9.41% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- TOSHI-EUR +8.79% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- KAT-EUR +8.74% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE

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
