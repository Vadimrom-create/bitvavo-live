# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-10-02T21:22:38.716622+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : NMR-EUR | action PLACE_LIMITE_PASSIVE | opportunité 7.633 | entrée 5.900 | trend 8.300 | rang 7.250
  - Strong structure but imperfect current entry; prefer passive execution. High extension/chase reduces rank but does not erase the setup.
- **MEILLEUR_LATENT_ACCELERATOR** : MAGIC-EUR | action LATENT_ACCELERATOR | opportunité 8.270 | entrée 5.450 | trend 8.650 | rang 7.812
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : AAVE-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.189 | entrée 5.850 | trend 9.200 | rang 7.985
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Tous les achats immédiats

Aucun ACHETE_MAINTENANT dans le classement complet.

## Top cross-sectionnel — aperçu non exhaustif

Ce top est une vue courte multi-buckets. Il ne doit jamais être utilisé comme liste exhaustive des achats immédiats.
1. AAVE-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.985
2. MAGIC-EUR — MEILLEUR_LATENT_ACCELERATOR — LATENT_ACCELERATOR — rank 7.812
3. WLD-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.761

## Accélération indépendante

- STRK-EUR — CONFIRMED_ACCELERATION — score 7.241/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- REQ-EUR — CONFIRMED_ACCELERATION — score 7.041/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- PUFFER-EUR — BUILDING_ACCELERATION — score 6.433/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- XAN-EUR — BUILDING_ACCELERATION — score 6.314/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- SCR-EUR — BUILDING_ACCELERATION — score 6.090/10 — DETECTED_BUT_TOO_LATE
- WELL-EUR — BUILDING_ACCELERATION — score 5.678/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- TAI-EUR — BUILDING_ACCELERATION — score 5.587/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- SWEAT-EUR — BUILDING_ACCELERATION — score 5.500/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- LSK-EUR — BUILDING_ACCELERATION — score 5.398/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- INIT-EUR — BUILDING_ACCELERATION — score 5.072/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- EDGE-EUR — MEMORY_24H — score mémoire 10.000/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- PEOPLE-EUR — MEMORY_24H — score mémoire 9.036/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- ZRC-EUR — MEMORY_24H — score mémoire 8.935/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- GNS-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- SOSO-EUR — MEMORY_24H — score mémoire 8.156/10 — sources ACCELERATION — MEMORY_ONLY
- AAVE-EUR — ACTIVE_NOW — score mémoire 7.985/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- CSPR-EUR — MEMORY_24H — score mémoire 7.942/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- MOVR-EUR — MEMORY_24H — score mémoire 7.820/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- MAGIC-EUR — ACTIVE_NOW — score mémoire 7.812/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- WLD-EUR — ACTIVE_NOW — score mémoire 7.761/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE

## Audit des plus fortes hausses

- SAND-EUR +40.87% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- GTC-EUR +13.11% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- CT-EUR +13.08% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- SCR-EUR +12.19% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ATH-EUR +11.99% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- GALA-EUR +11.80% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- APE-EUR +10.68% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- WLD-EUR +10.48% — DETECTED_EARLY — couche NONE — action NONE
- ENJ-EUR +9.05% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- MANA-EUR +8.48% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE

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
