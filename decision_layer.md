# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-10-10T17:46:20.983119+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : ESP-EUR | action PLACE_LIMITE_PASSIVE | opportunité 7.493 | entrée 5.900 | trend 8.400 | rang 7.202
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : IMX-EUR | action LATENT_ACCELERATOR | opportunité 7.866 | entrée 5.200 | trend 9.000 | rang 7.410
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : ZK-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 7.387 | entrée 6.550 | trend 8.600 | rang 7.260
  - Trend remains strong; candidate retained for re-entry instead of discarded.

## Tous les achats immédiats

Aucun ACHETE_MAINTENANT dans le classement complet.

## Top cross-sectionnel — aperçu non exhaustif

Ce top est une vue courte multi-buckets. Il ne doit jamais être utilisé comme liste exhaustive des achats immédiats.
1. IMX-EUR — MEILLEUR_LATENT_ACCELERATOR — LATENT_ACCELERATOR — rank 7.410
2. ZK-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.260
3. ESP-EUR — MEILLEURE_LIMITE_PASSIVE — PLACE_LIMITE_PASSIVE — rank 7.202

## Accélération indépendante

- RLC-EUR — BUILDING_ACCELERATION — score 5.797/10 — DETECTED_BUT_TOO_LATE
- STRK-EUR — BUILDING_ACCELERATION — score 5.228/10 — DETECTED_BUT_TOO_LATE
- CHIP-EUR — BUILDING_ACCELERATION — score 5.190/10 — DETECTED_BUT_TOO_LATE
- ARPA-EUR — BUILDING_ACCELERATION — score 5.028/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- TREAD-EUR — BUILDING_ACCELERATION — score 4.943/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- GTC-EUR — MEMORY_24H — score mémoire 9.580/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- CELR-EUR — MEMORY_DECAY_24_72H — score mémoire 9.241/10 — sources ACCELERATION — MEMORY_ONLY
- CT-EUR — MEMORY_24H — score mémoire 9.114/10 — sources ACCELERATION — MEMORY_ONLY
- OP-EUR — MEMORY_DECAY_24_72H — score mémoire 9.018/10 — sources ACCELERATION — MEMORY_ONLY
- LRC-EUR — MEMORY_24H — score mémoire 8.600/10 — sources ACCELERATION — MEMORY_ONLY
- O-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- MAGIC-EUR — MEMORY_24H — score mémoire 8.251/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- ZORA-EUR — MEMORY_24H — score mémoire 7.933/10 — sources ACCELERATION — MEMORY_ONLY
- PORTAL-EUR — MEMORY_DECAY_24_72H — score mémoire 7.889/10 — sources ACCELERATION — MEMORY_ONLY
- IMX-EUR — ACTIVE_NOW — score mémoire 7.410/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY

## Audit des plus fortes hausses

- LUMIA-EUR +33.52% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- STRK-EUR +25.73% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- CAP-EUR +21.95% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- RLC-EUR +17.05% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- CHIP-EUR +16.38% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- TREAD-EUR +14.50% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- NEAR-EUR +14.46% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE
- WLD-EUR +12.44% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- AERO-EUR +11.94% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- C98-EUR +11.57% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE

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
