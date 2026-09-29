# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-29T19:50:27.678971+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : ICP-EUR | action ACHETE_MAINTENANT | opportunité 8.688 | entrée 7.600 | trend 9.200 | rang 7.926
  - V4 buy-ready with acceptable current entry; no structural veto. High extension/chase is retained as risk context, not an automatic veto.
- **MEILLEURE_LIMITE_PASSIVE** : CRV-EUR | action PLACE_LIMITE_PASSIVE | opportunité 7.705 | entrée 6.550 | trend 8.800 | rang 7.653
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : COMP-EUR | action LATENT_ACCELERATOR | opportunité 8.274 | entrée 5.750 | trend 8.650 | rang 7.765
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : HUMA-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.445 | entrée 6.100 | trend 8.900 | rang 7.959
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Tous les achats immédiats

1. ICP-EUR — ACHETE_MAINTENANT — rank 7.926 — opportunité 8.688 — entrée 7.600 — trend 9.200
2. SUI-EUR — ACHETE_MAINTENANT — rank 7.675 — opportunité 7.857 — entrée 8.050 — trend 8.000
3. ETHFI-EUR — ACHETE_MAINTENANT — rank 7.618 — opportunité 8.248 — entrée 6.950 — trend 8.750
4. ONDO-EUR — ACHETE_MAINTENANT — rank 7.599 — opportunité 7.874 — entrée 7.600 — trend 8.000

## Top cross-sectionnel — aperçu non exhaustif

Ce top est une vue courte multi-buckets. Il ne doit jamais être utilisé comme liste exhaustive des achats immédiats.
1. HUMA-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.959
2. ICP-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 7.926
3. SYRUP-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.850

## Accélération indépendante

- POND-EUR — CONFIRMED_ACCELERATION — score 9.190/10 — DETECTED_BUT_TOO_LATE
- IMU-EUR — CONFIRMED_ACCELERATION — score 8.866/10 — DETECTED_BUT_TOO_LATE
- FUEL-EUR — CONFIRMED_ACCELERATION — score 7.721/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- ZIG-EUR — CONFIRMED_ACCELERATION — score 6.599/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- GRASS-EUR — BUILDING_ACCELERATION — score 6.368/10 — DETECTED_BUT_TOO_LATE
- ZEUS-EUR — BUILDING_ACCELERATION — score 5.556/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- MOVR-EUR — BUILDING_ACCELERATION — score 5.252/10 — DETECTED_BUT_TOO_LATE
- FET-EUR — BUILDING_ACCELERATION — score 4.779/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- GIGA-EUR — MEMORY_24H — score mémoire 10.000/10 — sources ACCELERATION — MEMORY_ONLY
- POND-EUR — ACTIVE_NOW — score mémoire 9.190/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- QUID-EUR — MEMORY_24H — score mémoire 9.062/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- SWELL-EUR — MEMORY_24H — score mémoire 9.000/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- IMU-EUR — ACTIVE_NOW — score mémoire 8.866/10 — sources ACCELERATION — DETECTED_BUT_TOO_LATE
- WMTX-EUR — MEMORY_24H — score mémoire 8.145/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- SOLV-EUR — MEMORY_24H — score mémoire 8.017/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- ZRC-EUR — MEMORY_24H — score mémoire 7.961/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- HUMA-EUR — ACTIVE_NOW — score mémoire 7.959/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- ICP-EUR — ACTIVE_NOW — score mémoire 7.926/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE

## Audit des plus fortes hausses

- POND-EUR +40.05% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- GRASS-EUR +29.73% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- SOON-EUR +25.25% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- MOVR-EUR +22.78% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- 0G-EUR +21.92% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- ZBCN-EUR +21.05% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- PUMP-EUR +15.55% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- PHA-EUR +15.41% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ALICE-EUR +14.50% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ICP-EUR +13.48% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION

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
