# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-10-02T03:47:56.056456+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : AAVE-EUR | action ACHETE_MAINTENANT | opportunité 9.426 | entrée 7.600 | trend 8.950 | rang 8.598
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : AUDIO-EUR | action PLACE_LIMITE_PASSIVE | opportunité 7.525 | entrée 6.750 | trend 8.650 | rang 7.446
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : ESP-EUR | action LATENT_ACCELERATOR | opportunité 8.978 | entrée 5.650 | trend 7.350 | rang 7.508
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : HUMA-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.275 | entrée 6.450 | trend 8.850 | rang 7.899
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Tous les achats immédiats

1. AAVE-EUR — ACHETE_MAINTENANT — rank 8.598 — opportunité 9.426 — entrée 7.600 — trend 8.950
2. WIF-EUR — ACHETE_MAINTENANT — rank 7.178 — opportunité 8.754 — entrée 7.000 — trend 6.250

## Top cross-sectionnel — aperçu non exhaustif

Ce top est une vue courte multi-buckets. Il ne doit jamais être utilisé comme liste exhaustive des achats immédiats.
1. AAVE-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.598
2. HUMA-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.899
3. RUNE-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.878

## Accélération indépendante

- SCR-EUR — CONFIRMED_ACCELERATION — score 8.481/10 — DETECTED_BUT_TOO_LATE
- CTC-EUR — CONFIRMED_ACCELERATION — score 7.732/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- INIT-EUR — CONFIRMED_ACCELERATION — score 6.803/10 — DETECTED_BUT_TOO_LATE
- PUFFER-EUR — BUILDING_ACCELERATION — score 5.591/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- TOWNS-EUR — BUILDING_ACCELERATION — score 5.021/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- CPOOL-EUR — MEMORY_24H — score mémoire 10.000/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- ICX-EUR — MEMORY_24H — score mémoire 9.062/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- ZRC-EUR — MEMORY_24H — score mémoire 8.847/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- AAVE-EUR — ACTIVE_NOW — score mémoire 8.598/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- SCR-EUR — ACTIVE_NOW — score mémoire 8.481/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- OSMO-EUR — MEMORY_24H — score mémoire 8.342/10 — sources ACCELERATION — MEMORY_ONLY
- AGI-EUR — MEMORY_24H — score mémoire 8.119/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- U-EUR — MEMORY_24H — score mémoire 8.002/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- HUMA-EUR — ACTIVE_NOW — score mémoire 7.899/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- RUNE-EUR — ACTIVE_NOW — score mémoire 7.878/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY

## Audit des plus fortes hausses

- SWEAT-EUR +142.11% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- GTC-EUR +64.81% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- SCR-EUR +41.38% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- CT-EUR +25.83% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- MEGA-EUR +20.23% — DETECTED_EARLY — couche NONE — action NONE
- SYN-EUR +18.31% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ALICE-EUR +16.35% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- NOM-EUR +13.60% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- SUPER-EUR +13.26% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- TOWNS-EUR +11.98% — DETECTED_EARLY — couche NONE — action INTERPRETATION

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
