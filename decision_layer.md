# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-10-12T05:30:25.501667+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : aucun candidat matériel
- **MEILLEUR_LATENT_ACCELERATOR** : JUP-EUR | action LATENT_ACCELERATOR | opportunité 7.538 | entrée 5.750 | trend 7.600 | rang 6.917
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : TIA-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 7.837 | entrée 7.100 | trend 8.900 | rang 7.668
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Tous les achats immédiats

Aucun ACHETE_MAINTENANT dans le classement complet.

## Top cross-sectionnel — aperçu non exhaustif

Ce top est une vue courte multi-buckets. Il ne doit jamais être utilisé comme liste exhaustive des achats immédiats.
1. TIA-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.668
2. RAY-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.600
3. AERO-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.419

## Accélération indépendante

- DBR-EUR — CONFIRMED_ACCELERATION — score 8.500/10 — DETECTED_BUT_TOO_LATE
- SXT-EUR — CONFIRMED_ACCELERATION — score 8.267/10 — DETECTED_BUT_TOO_LATE
- ZEUS-EUR — CONFIRMED_ACCELERATION — score 6.732/10 — DETECTED_BUT_TOO_LATE
- CTC-EUR — BUILDING_ACCELERATION — score 6.173/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- RSR-EUR — BUILDING_ACCELERATION — score 6.014/10 — DETECTED_BUT_TOO_LATE
- CHIP-EUR — BUILDING_ACCELERATION — score 4.925/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- STRK-EUR — MEMORY_24H — score mémoire 8.918/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- DBR-EUR — ACTIVE_NOW — score mémoire 8.500/10 — sources ACCELERATION — DETECTED_BUT_TOO_LATE
- OSMO-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION — MEMORY_ONLY
- SXT-EUR — ACTIVE_NOW — score mémoire 8.267/10 — sources ACCELERATION — DETECTED_BUT_TOO_LATE
- BEL-EUR — MEMORY_24H — score mémoire 8.196/10 — sources ACCELERATION — MEMORY_ONLY
- RON-EUR — MEMORY_24H — score mémoire 8.054/10 — sources ACCELERATION — MEMORY_ONLY
- MANTA-EUR — MEMORY_24H — score mémoire 7.990/10 — sources ACCELERATION — MEMORY_ONLY
- TREAD-EUR — MEMORY_DECAY_24_72H — score mémoire 7.881/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- LRC-EUR — MEMORY_24H — score mémoire 7.831/10 — sources ACCELERATION — MEMORY_ONLY
- TIA-EUR — ACTIVE_NOW — score mémoire 7.668/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY

## Audit des plus fortes hausses

- ZEUS-EUR +82.18% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- W-EUR +59.75% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- RSR-EUR +53.12% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- ZRC-EUR +39.38% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- S-EUR +26.89% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- GRASS-EUR +23.39% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- IO-EUR +22.06% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- PLUME-EUR +17.21% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- METIS-EUR +16.79% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- ZRO-EUR +16.49% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE

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
