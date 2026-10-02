# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-10-02T01:14:14.923649+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : RARE-EUR | action ACHETE_MAINTENANT | opportunité 9.075 | entrée 7.450 | trend 7.700 | rang 7.625
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : EPIC-EUR | action PLACE_LIMITE_PASSIVE | opportunité 7.762 | entrée 5.850 | trend 8.200 | rang 7.465
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : MIOTA-EUR | action LATENT_ACCELERATOR | opportunité 8.713 | entrée 5.250 | trend 8.450 | rang 7.915
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : AAVE-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.500 | entrée 7.500 | trend 8.700 | rang 8.066
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Tous les achats immédiats

1. RARE-EUR — ACHETE_MAINTENANT — rank 7.625 — opportunité 9.075 — entrée 7.450 — trend 7.700
2. LTC-EUR — ACHETE_MAINTENANT — rank 7.450 — opportunité 8.869 — entrée 7.650 — trend 6.600
3. SOL-EUR — ACHETE_MAINTENANT — rank 7.092 — opportunité 8.744 — entrée 7.600 — trend 5.800
4. WIF-EUR — ACHETE_MAINTENANT — rank 6.892 — opportunité 8.423 — entrée 7.000 — trend 6.000

## Top cross-sectionnel — aperçu non exhaustif

Ce top est une vue courte multi-buckets. Il ne doit jamais être utilisé comme liste exhaustive des achats immédiats.
1. AAVE-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.066
2. MIOTA-EUR — MEILLEUR_LATENT_ACCELERATOR — LATENT_ACCELERATOR — rank 7.915
3. STX-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.786

## Accélération indépendante

- SCR-EUR — CONFIRMED_ACCELERATION — score 8.572/10 — DETECTED_BUT_TOO_LATE
- ZKC-EUR — BUILDING_ACCELERATION — score 6.080/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- CPOOL-EUR — MEMORY_24H — score mémoire 10.000/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- POND-EUR — MEMORY_24H — score mémoire 10.000/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- ZRC-EUR — MEMORY_24H — score mémoire 8.847/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- SCR-EUR — ACTIVE_NOW — score mémoire 8.572/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- OSMO-EUR — MEMORY_24H — score mémoire 8.342/10 — sources ACCELERATION — MEMORY_ONLY
- AGI-EUR — MEMORY_24H — score mémoire 8.119/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- AAVE-EUR — ACTIVE_NOW — score mémoire 8.066/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- U-EUR — MEMORY_24H — score mémoire 8.002/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- MIOTA-EUR — ACTIVE_NOW — score mémoire 7.915/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- MMT-EUR — ACTIVE_NOW — score mémoire 7.788/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY

## Audit des plus fortes hausses

- SWEAT-EUR +101.34% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- GTC-EUR +64.22% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- MOVR-EUR +30.37% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ALICE-EUR +28.96% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- MEGA-EUR +25.66% — DETECTED_EARLY — couche NONE — action NONE
- SYN-EUR +17.76% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- CT-EUR +17.35% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- SCR-EUR +15.68% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- NOM-EUR +14.77% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- HUMA-EUR +12.05% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION

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
