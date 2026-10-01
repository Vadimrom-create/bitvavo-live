# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-10-01T15:16:58.339178+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : AAVE-EUR | action ACHETE_MAINTENANT | opportunité 8.327 | entrée 6.950 | trend 8.900 | rang 8.057
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : RED-EUR | action PLACE_LIMITE_PASSIVE | opportunité 7.778 | entrée 6.250 | trend 8.650 | rang 7.634
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : KSM-EUR | action LATENT_ACCELERATOR | opportunité 8.203 | entrée 5.000 | trend 8.900 | rang 7.817
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : AVAX-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 7.960 | entrée 7.100 | trend 8.700 | rang 7.869
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Tous les achats immédiats

1. AAVE-EUR — ACHETE_MAINTENANT — rank 8.057 — opportunité 8.327 — entrée 6.950 — trend 8.900

## Top cross-sectionnel — aperçu non exhaustif

Ce top est une vue courte multi-buckets. Il ne doit jamais être utilisé comme liste exhaustive des achats immédiats.
1. AAVE-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.057
2. AVAX-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.869
3. PROM-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.844

## Accélération indépendante

- GTC-EUR — CONFIRMED_ACCELERATION — score 9.139/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- TLM-EUR — CONFIRMED_ACCELERATION — score 8.981/10 — DETECTED_BUT_TOO_LATE
- XAI-EUR — CONFIRMED_ACCELERATION — score 7.562/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- PORTAL-EUR — CONFIRMED_ACCELERATION — score 6.761/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- ALICE-EUR — CONFIRMED_ACCELERATION — score 6.674/10 — DETECTED_BUT_TOO_LATE
- ICX-EUR — BUILDING_ACCELERATION — score 6.380/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- DYDX-EUR — BUILDING_ACCELERATION — score 5.812/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- MEGA-EUR — BUILDING_ACCELERATION — score 5.746/10 — DETECTED_BUT_TOO_LATE
- ARX-EUR — BUILDING_ACCELERATION — score 5.706/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- PIXEL-EUR — BUILDING_ACCELERATION — score 5.647/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- CPOOL-EUR — MEMORY_24H — score mémoire 10.000/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- XYO-EUR — MEMORY_24H — score mémoire 9.473/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- GTC-EUR — ACTIVE_NOW — score mémoire 9.139/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- TLM-EUR — ACTIVE_NOW — score mémoire 8.981/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- CT-EUR — MEMORY_24H — score mémoire 8.691/10 — sources ACCELERATION — MEMORY_ONLY
- ARPA-EUR — MEMORY_24H — score mémoire 8.595/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- TAI-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- OSMO-EUR — MEMORY_24H — score mémoire 8.342/10 — sources ACCELERATION — MEMORY_ONLY
- AAVE-EUR — ACTIVE_NOW — score mémoire 8.057/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- AVAX-EUR — ACTIVE_NOW — score mémoire 7.869/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY

## Audit des plus fortes hausses

- SWEAT-EUR +79.69% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- MOVR-EUR +52.15% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- ALICE-EUR +43.18% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- CAP-EUR +31.34% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- CT-EUR +23.92% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- SYN-EUR +19.71% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- NOS-EUR +19.68% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- MON-EUR +17.15% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- TRAC-EUR +13.59% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- STX-EUR +12.94% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION

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
