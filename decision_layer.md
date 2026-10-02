# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-10-02T16:23:18.770097+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : AAVE-EUR | action ACHETE_MAINTENANT | opportunité 8.840 | entrée 7.250 | trend 8.650 | rang 8.090
  - V4 buy-ready with acceptable current entry; no structural veto. High extension/chase is retained as risk context, not an automatic veto.
- **MEILLEURE_LIMITE_PASSIVE** : aucun candidat matériel
- **MEILLEUR_LATENT_ACCELERATOR** : RUNE-EUR | action LATENT_ACCELERATOR | opportunité 7.515 | entrée 5.100 | trend 8.650 | rang 7.421
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : SPK-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.640 | entrée 6.450 | trend 9.200 | rang 7.829
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Tous les achats immédiats

1. AAVE-EUR — ACHETE_MAINTENANT — rank 8.090 — opportunité 8.840 — entrée 7.250 — trend 8.650
2. ALGO-EUR — ACHETE_MAINTENANT — rank 8.010 — opportunité 8.510 — entrée 7.000 — trend 8.650
3. RENDER-EUR — ACHETE_MAINTENANT — rank 7.371 — opportunité 8.550 — entrée 7.050 — trend 7.150
4. TAO-EUR — ACHETE_MAINTENANT — rank 7.047 — opportunité 8.045 — entrée 7.200 — trend 6.800

## Top cross-sectionnel — aperçu non exhaustif

Ce top est une vue courte multi-buckets. Il ne doit jamais être utilisé comme liste exhaustive des achats immédiats.
1. AAVE-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.090
2. ALGO-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.010
3. SPK-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.829

## Accélération indépendante

- AGI-EUR — CONFIRMED_ACCELERATION — score 8.283/10 — DETECTED_BUT_TOO_LATE
- ATH-EUR — CONFIRMED_ACCELERATION — score 7.079/10 — DETECTED_BUT_TOO_LATE
- GTC-EUR — CONFIRMED_ACCELERATION — score 6.909/10 — DETECTED_BUT_TOO_LATE
- GALA-EUR — CONFIRMED_ACCELERATION — score 6.867/10 — DETECTED_BUT_TOO_LATE
- MANA-EUR — CONFIRMED_ACCELERATION — score 6.777/10 — DETECTED_BUT_TOO_LATE
- CT-EUR — BUILDING_ACCELERATION — score 6.265/10 — DETECTED_BUT_TOO_LATE
- SAND-EUR — BUILDING_ACCELERATION — score 5.846/10 — DETECTED_BUT_TOO_LATE
- OP-EUR — BUILDING_ACCELERATION — score 5.658/10 — DETECTED_BUT_TOO_LATE
- SUPER-EUR — BUILDING_ACCELERATION — score 5.582/10 — DETECTED_BUT_TOO_LATE
- MEGA-EUR — BUILDING_ACCELERATION — score 5.244/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- EDGE-EUR — MEMORY_24H — score mémoire 10.000/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- TREAD-EUR — MEMORY_24H — score mémoire 9.258/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- PEOPLE-EUR — MEMORY_24H — score mémoire 9.036/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- CAP-EUR — MEMORY_24H — score mémoire 8.954/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- AIOZ-EUR — MEMORY_24H — score mémoire 8.925/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- U-EUR — MEMORY_24H — score mémoire 8.740/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- ZRC-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- AGI-EUR — ACTIVE_NOW — score mémoire 8.283/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- DBR-EUR — MEMORY_24H — score mémoire 8.273/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- AAVE-EUR — ACTIVE_NOW — score mémoire 8.090/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE

## Audit des plus fortes hausses

- SAND-EUR +46.89% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- GTC-EUR +28.98% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- GALA-EUR +19.74% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- WLD-EUR +19.07% — DETECTED_EARLY — couche NONE — action NONE
- ATH-EUR +16.70% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- SKY-EUR +15.66% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- APE-EUR +15.09% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- MANA-EUR +14.71% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- SPK-EUR +13.49% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- NOS-EUR +13.16% — DETECTED_EARLY — couche NONE — action INTERPRETATION

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
