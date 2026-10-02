# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-10-02T14:56:06.403280+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : ALGO-EUR | action PLACE_LIMITE_PASSIVE | opportunité 7.526 | entrée 5.850 | trend 8.650 | rang 7.518
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : DYDX-EUR | action LATENT_ACCELERATOR | opportunité 8.106 | entrée 5.350 | trend 8.950 | rang 7.794
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : MON-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.195 | entrée 6.200 | trend 8.850 | rang 7.736
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Tous les achats immédiats

Aucun ACHETE_MAINTENANT dans le classement complet.

## Top cross-sectionnel — aperçu non exhaustif

Ce top est une vue courte multi-buckets. Il ne doit jamais être utilisé comme liste exhaustive des achats immédiats.
1. DYDX-EUR — MEILLEUR_LATENT_ACCELERATOR — LATENT_ACCELERATOR — rank 7.794
2. MON-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.736
3. NOM-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.564

## Accélération indépendante

- MOVR-EUR — BUILDING_ACCELERATION — score 5.737/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- W-EUR — BUILDING_ACCELERATION — score 5.563/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- AGI-EUR — BUILDING_ACCELERATION — score 5.263/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- CELR-EUR — BUILDING_ACCELERATION — score 5.062/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- EDGE-EUR — MEMORY_24H — score mémoire 10.000/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- TREAD-EUR — MEMORY_24H — score mémoire 9.258/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- PEOPLE-EUR — MEMORY_24H — score mémoire 9.036/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- AIOZ-EUR — MEMORY_24H — score mémoire 8.925/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- U-EUR — MEMORY_24H — score mémoire 8.740/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- ZRC-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- SAND-EUR — MEMORY_24H — score mémoire 8.000/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- OSMO-EUR — MEMORY_DECAY_24_72H — score mémoire 7.943/10 — sources ACCELERATION — MEMORY_ONLY
- CSPR-EUR — MEMORY_24H — score mémoire 7.942/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- ZIG-EUR — ACTIVE_NOW — score mémoire 7.863/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY

## Audit des plus fortes hausses

- SAND-EUR +50.31% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- GTC-EUR +28.52% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- ZRO-EUR +18.31% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- MAGIC-EUR +17.04% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- GALA-EUR +16.39% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- NOS-EUR +16.31% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- SKY-EUR +16.31% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- BAT-EUR +16.06% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE
- APE-EUR +15.84% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- MANA-EUR +14.10% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE

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
