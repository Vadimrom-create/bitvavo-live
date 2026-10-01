# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-10-01T22:19:25.034645+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : AAVE-EUR | action ACHETE_MAINTENANT | opportunité 9.115 | entrée 7.450 | trend 9.200 | rang 8.544
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : EPIC-EUR | action PLACE_LIMITE_PASSIVE | opportunité 8.548 | entrée 6.100 | trend 8.000 | rang 7.784
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : DIA-EUR | action LATENT_ACCELERATOR | opportunité 8.106 | entrée 4.550 | trend 9.000 | rang 7.703
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : MIOTA-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 9.142 | entrée 6.350 | trend 8.150 | rang 8.073
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Tous les achats immédiats

1. AAVE-EUR — ACHETE_MAINTENANT — rank 8.544 — opportunité 9.115 — entrée 7.450 — trend 9.200
2. BNB-EUR — ACHETE_MAINTENANT — rank 6.562 — opportunité 8.243 — entrée 7.100 — trend 5.200

## Top cross-sectionnel — aperçu non exhaustif

Ce top est une vue courte multi-buckets. Il ne doit jamais être utilisé comme liste exhaustive des achats immédiats.
1. AAVE-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.544
2. MIOTA-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.073
3. HUMA-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.952

## Accélération indépendante

- ZRC-EUR — CONFIRMED_ACCELERATION — score 8.847/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- 2Z-EUR — BUILDING_ACCELERATION — score 6.413/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- ICX-EUR — BUILDING_ACCELERATION — score 5.857/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- CPOOL-EUR — MEMORY_24H — score mémoire 10.000/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- SCR-EUR — MEMORY_24H — score mémoire 10.000/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- ZRC-EUR — ACTIVE_NOW — score mémoire 8.847/10 — sources ACCELERATION, V4 — WATCH_ONLY
- AAVE-EUR — ACTIVE_NOW — score mémoire 8.544/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- OSMO-EUR — MEMORY_24H — score mémoire 8.342/10 — sources ACCELERATION — MEMORY_ONLY
- AGI-EUR — MEMORY_24H — score mémoire 8.119/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- MIOTA-EUR — ACTIVE_NOW — score mémoire 8.073/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- U-EUR — MEMORY_24H — score mémoire 8.002/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- HUMA-EUR — ACTIVE_NOW — score mémoire 7.952/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- DYDX-EUR — ACTIVE_NOW — score mémoire 7.933/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY

## Audit des plus fortes hausses

- SWEAT-EUR +172.80% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- GTC-EUR +45.99% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- MOVR-EUR +39.61% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ALICE-EUR +28.71% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- MEGA-EUR +26.10% — DETECTED_EARLY — couche NONE — action NONE
- CT-EUR +19.05% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- NOM-EUR +18.97% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- SYN-EUR +18.03% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- NOS-EUR +16.45% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- SCR-EUR +14.66% — DETECTED_EARLY — couche NONE — action INTERPRETATION

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
