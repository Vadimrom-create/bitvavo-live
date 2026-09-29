# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-29T04:37:26.416411+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : POL-EUR | action ACHETE_MAINTENANT | opportunité 8.054 | entrée 6.900 | trend 6.850 | rang 6.944
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : MIOTA-EUR | action PLACE_LIMITE_PASSIVE | opportunité 8.295 | entrée 5.900 | trend 8.700 | rang 7.752
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : XDC-EUR | action LATENT_ACCELERATOR | opportunité 7.472 | entrée 5.500 | trend 8.500 | rang 7.397
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : W-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 9.173 | entrée 7.100 | trend 8.650 | rang 8.234
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Tous les achats immédiats

1. POL-EUR — ACHETE_MAINTENANT — rank 6.944 — opportunité 8.054 — entrée 6.900 — trend 6.850

## Top cross-sectionnel — aperçu non exhaustif

Ce top est une vue courte multi-buckets. Il ne doit jamais être utilisé comme liste exhaustive des achats immédiats.
1. W-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.234
2. RUNE-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.072
3. LINK-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.878

## Accélération indépendante

- TRIA-EUR — CONFIRMED_ACCELERATION — score 7.298/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- FOLD-EUR — CONFIRMED_ACCELERATION — score 6.903/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- ARX-EUR — CONFIRMED_ACCELERATION — score 6.849/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- PYTH-EUR — CONFIRMED_ACCELERATION — score 6.722/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- AGLD-EUR — BUILDING_ACCELERATION — score 5.907/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- CELO-EUR — BUILDING_ACCELERATION — score 5.728/10 — DETECTED_BUT_TOO_LATE
- SUPER-EUR — BUILDING_ACCELERATION — score 5.469/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- WMTX-EUR — BUILDING_ACCELERATION — score 5.326/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- CHILLGUY-EUR — BUILDING_ACCELERATION — score 5.178/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- GRASS-EUR — BUILDING_ACCELERATION — score 4.831/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- PUFFER-EUR — MEMORY_24H — score mémoire 9.062/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- ZRC-EUR — MEMORY_24H — score mémoire 9.000/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- ZEUS-EUR — MEMORY_24H — score mémoire 8.844/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- IMU-EUR — MEMORY_24H — score mémoire 8.632/10 — sources ACCELERATION — MEMORY_ONLY
- W-EUR — ACTIVE_NOW — score mémoire 8.234/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- QUID-EUR — MEMORY_24H — score mémoire 8.100/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- RUNE-EUR — ACTIVE_NOW — score mémoire 8.072/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- OSMO-EUR — MEMORY_24H — score mémoire 7.990/10 — sources ACCELERATION — MEMORY_ONLY
- AIXBT-EUR — MEMORY_24H — score mémoire 7.962/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- LINK-EUR — ACTIVE_NOW — score mémoire 7.878/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY

## Audit des plus fortes hausses

- NMR-EUR +38.19% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- HBAR-EUR +25.46% — DETECTED_EARLY — couche NONE — action NONE
- ALGO-EUR +17.14% — DETECTED_EARLY — couche NONE — action NONE
- 0G-EUR +16.17% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- CRV-EUR +15.25% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- CELO-EUR +10.64% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- GRASS-EUR +9.09% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- ARX-EUR +7.88% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- MIOTA-EUR +7.12% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- IKA-EUR +7.08% — DETECTED_TOO_LATE — couche NONE — action INTERPRETATION

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
