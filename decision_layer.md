# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-10-10T20:45:19.109995+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : EDU-EUR | action PLACE_LIMITE_PASSIVE | opportunité 7.798 | entrée 6.150 | trend 8.850 | rang 7.498
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : IMX-EUR | action LATENT_ACCELERATOR | opportunité 7.502 | entrée 4.950 | trend 9.000 | rang 7.345
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : APT-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 7.493 | entrée 6.600 | trend 8.500 | rang 7.295
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Tous les achats immédiats

Aucun ACHETE_MAINTENANT dans le classement complet.

## Top cross-sectionnel — aperçu non exhaustif

Ce top est une vue courte multi-buckets. Il ne doit jamais être utilisé comme liste exhaustive des achats immédiats.
1. EDU-EUR — MEILLEURE_LIMITE_PASSIVE — PLACE_LIMITE_PASSIVE — rank 7.498
2. IMX-EUR — MEILLEUR_LATENT_ACCELERATOR — LATENT_ACCELERATOR — rank 7.345
3. APT-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.295

## Accélération indépendante

- C98-EUR — CONFIRMED_ACCELERATION — score 8.963/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- BRETT-EUR — CONFIRMED_ACCELERATION — score 8.610/10 — DETECTED_BUT_TOO_LATE
- DUSK-EUR — CONFIRMED_ACCELERATION — score 7.292/10 — DETECTED_BUT_TOO_LATE
- ZEUS-EUR — BUILDING_ACCELERATION — score 5.629/10 — DETECTED_BUT_TOO_LATE
- CHIP-EUR — BUILDING_ACCELERATION — score 5.578/10 — DETECTED_BUT_TOO_LATE
- TIA-EUR — BUILDING_ACCELERATION — score 5.013/10 — DETECTED_BUT_TOO_LATE
- VVV-EUR — BUILDING_ACCELERATION — score 4.953/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- GTC-EUR — MEMORY_24H — score mémoire 9.580/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- C98-EUR — ACTIVE_NOW — score mémoire 8.963/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- CELR-EUR — MEMORY_DECAY_24_72H — score mémoire 8.649/10 — sources ACCELERATION — MEMORY_ONLY
- CT-EUR — MEMORY_DECAY_24_72H — score mémoire 8.624/10 — sources ACCELERATION — MEMORY_ONLY
- BRETT-EUR — ACTIVE_NOW — score mémoire 8.610/10 — sources ACCELERATION — DETECTED_BUT_TOO_LATE
- LRC-EUR — MEMORY_24H — score mémoire 8.600/10 — sources ACCELERATION — MEMORY_ONLY
- O-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- OP-EUR — MEMORY_DECAY_24_72H — score mémoire 8.440/10 — sources ACCELERATION — MEMORY_ONLY
- MAGIC-EUR — MEMORY_24H — score mémoire 8.251/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- ZORA-EUR — MEMORY_24H — score mémoire 7.933/10 — sources ACCELERATION — MEMORY_ONLY

## Audit des plus fortes hausses

- STRK-EUR +47.84% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- CHIP-EUR +32.36% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- LUMIA-EUR +29.51% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- TIA-EUR +23.43% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- AZTEC-EUR +16.65% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE
- AERO-EUR +15.45% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- NEAR-EUR +15.05% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE
- WLD-EUR +13.46% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- DUSK-EUR +12.69% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- CAP-EUR +12.55% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION

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
