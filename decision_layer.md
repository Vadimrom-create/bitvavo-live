# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-10-11T20:39:42.329992+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : FLUID-EUR | action PLACE_LIMITE_PASSIVE | opportunité 7.420 | entrée 6.200 | trend 8.200 | rang 7.146
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : BAND-EUR | action LATENT_ACCELERATOR | opportunité 7.490 | entrée 5.400 | trend 8.900 | rang 7.255
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : ZK-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.131 | entrée 6.450 | trend 8.950 | rang 7.689
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Tous les achats immédiats

Aucun ACHETE_MAINTENANT dans le classement complet.

## Top cross-sectionnel — aperçu non exhaustif

Ce top est une vue courte multi-buckets. Il ne doit jamais être utilisé comme liste exhaustive des achats immédiats.
1. ZK-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.689
2. CHIP-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.489
3. RAY-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.463

## Accélération indépendante

- ZKP-EUR — BUILDING_ACCELERATION — score 5.968/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- AXL-EUR — BUILDING_ACCELERATION — score 5.629/10 — DETECTED_BUT_TOO_LATE
- ZRC-EUR — BUILDING_ACCELERATION — score 4.892/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- TREAD-EUR — MEMORY_24H — score mémoire 8.918/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- IO-EUR — MEMORY_24H — score mémoire 8.545/10 — sources ACCELERATION — MEMORY_ONLY
- OSMO-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION — MEMORY_ONLY
- BEL-EUR — MEMORY_24H — score mémoire 8.196/10 — sources ACCELERATION — MEMORY_ONLY
- RON-EUR — MEMORY_24H — score mémoire 8.054/10 — sources ACCELERATION — MEMORY_ONLY
- GTC-EUR — MEMORY_DECAY_24_72H — score mémoire 8.051/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- MANTA-EUR — MEMORY_24H — score mémoire 7.990/10 — sources ACCELERATION — MEMORY_ONLY
- LRC-EUR — MEMORY_24H — score mémoire 7.831/10 — sources ACCELERATION — MEMORY_ONLY
- ZK-EUR — ACTIVE_NOW — score mémoire 7.689/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- CHIP-EUR — ACTIVE_NOW — score mémoire 7.489/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE

## Audit des plus fortes hausses

- ZRC-EUR +76.21% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- ZEUS-EUR +57.42% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- S-EUR +38.95% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- MAGIC-EUR +34.05% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- W-EUR +27.48% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- LUMIA-EUR +24.45% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- PLUME-EUR +18.53% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- BAT-EUR +18.37% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- IO-EUR +18.09% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- GRASS-EUR +17.42% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE

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
