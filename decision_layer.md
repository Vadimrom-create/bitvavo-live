# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-10-02T19:05:26.987933+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : SKY-EUR | action PLACE_LIMITE_PASSIVE | opportunité 7.629 | entrée 6.000 | trend 8.650 | rang 7.404
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : GALA-EUR | action LATENT_ACCELERATOR | opportunité 8.016 | entrée 5.700 | trend 8.700 | rang 7.615
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : AAVE-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 7.990 | entrée 6.150 | trend 8.900 | rang 7.798
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Tous les achats immédiats

Aucun ACHETE_MAINTENANT dans le classement complet.

## Top cross-sectionnel — aperçu non exhaustif

Ce top est une vue courte multi-buckets. Il ne doit jamais être utilisé comme liste exhaustive des achats immédiats.
1. AAVE-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.798
2. IMX-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.654
3. HUMA-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.631

## Accélération indépendante

- BOME-EUR — CONFIRMED_ACCELERATION — score 6.676/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- TREAD-EUR — CONFIRMED_ACCELERATION — score 6.631/10 — DETECTED_BUT_TOO_LATE
- AMP-EUR — BUILDING_ACCELERATION — score 6.353/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- ROBO-EUR — BUILDING_ACCELERATION — score 5.959/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- MAGIC-EUR — BUILDING_ACCELERATION — score 5.957/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- CNPY-EUR — BUILDING_ACCELERATION — score 5.879/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- SOLV-EUR — BUILDING_ACCELERATION — score 5.831/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- ACH-EUR — BUILDING_ACCELERATION — score 5.775/10 — DETECTED_BUT_TOO_LATE
- SAGA-EUR — BUILDING_ACCELERATION — score 5.630/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- XMN-EUR — BUILDING_ACCELERATION — score 5.604/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- EDGE-EUR — MEMORY_24H — score mémoire 10.000/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- PEOPLE-EUR — MEMORY_24H — score mémoire 9.036/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- CAP-EUR — MEMORY_24H — score mémoire 8.954/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- GNS-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- ZRC-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- CSPR-EUR — MEMORY_24H — score mémoire 7.942/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- MOVR-EUR — MEMORY_24H — score mémoire 7.820/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- AAVE-EUR — ACTIVE_NOW — score mémoire 7.798/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- IMX-EUR — ACTIVE_NOW — score mémoire 7.654/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- HUMA-EUR — ACTIVE_NOW — score mémoire 7.631/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY

## Audit des plus fortes hausses

- SAND-EUR +36.90% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- GTC-EUR +28.75% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- ENJ-EUR +17.73% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- SCR-EUR +16.56% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ATH-EUR +11.57% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- WLD-EUR +9.66% — DETECTED_EARLY — couche NONE — action NONE
- MANA-EUR +9.49% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- APE-EUR +8.20% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- GALA-EUR +7.48% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- SUPER-EUR +7.16% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION

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
