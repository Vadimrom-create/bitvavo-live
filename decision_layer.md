# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-10-02T10:40:16.441926+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : HBAR-EUR | action ACHETE_MAINTENANT | opportunité 9.284 | entrée 7.450 | trend 8.200 | rang 8.267
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : DYDX-EUR | action PLACE_LIMITE_PASSIVE | opportunité 7.784 | entrée 6.200 | trend 8.950 | rang 7.718
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : ENJ-EUR | action LATENT_ACCELERATOR | opportunité 7.701 | entrée 5.050 | trend 8.650 | rang 7.089
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : AAVE-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.927 | entrée 7.200 | trend 8.900 | rang 7.906
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Tous les achats immédiats

1. HBAR-EUR — ACHETE_MAINTENANT — rank 8.267 — opportunité 9.284 — entrée 7.450 — trend 8.200
2. ALGO-EUR — ACHETE_MAINTENANT — rank 8.017 — opportunité 8.418 — entrée 7.100 — trend 8.650
3. WLD-EUR — ACHETE_MAINTENANT — rank 7.959 — opportunité 8.110 — entrée 7.800 — trend 8.700
4. AVAX-EUR — ACHETE_MAINTENANT — rank 7.383 — opportunité 8.692 — entrée 7.450 — trend 6.650

## Top cross-sectionnel — aperçu non exhaustif

Ce top est une vue courte multi-buckets. Il ne doit jamais être utilisé comme liste exhaustive des achats immédiats.
1. HBAR-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.267
2. ALGO-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.017
3. WLD-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 7.959

## Accélération indépendante

- FRAX-EUR — CONFIRMED_ACCELERATION — score 7.469/10 — DETECTED_BUT_TOO_LATE
- REQ-EUR — BUILDING_ACCELERATION — score 6.023/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- CT-EUR — BUILDING_ACCELERATION — score 5.454/10 — DETECTED_BUT_TOO_LATE
- APE-EUR — BUILDING_ACCELERATION — score 5.342/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- GALA-EUR — BUILDING_ACCELERATION — score 5.019/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- BAT-EUR — BUILDING_ACCELERATION — score 4.946/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- EDGE-EUR — MEMORY_24H — score mémoire 10.000/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- TREAD-EUR — MEMORY_24H — score mémoire 9.258/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- OPEN-EUR — MEMORY_24H — score mémoire 9.112/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- PEOPLE-EUR — MEMORY_24H — score mémoire 9.036/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- ICX-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- OSMO-EUR — MEMORY_24H — score mémoire 8.342/10 — sources ACCELERATION — MEMORY_ONLY
- HBAR-EUR — ACTIVE_NOW — score mémoire 8.267/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- ZRC-EUR — MEMORY_24H — score mémoire 8.257/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- ALGO-EUR — ACTIVE_NOW — score mémoire 8.017/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- GIGA-EUR — MEMORY_24H — score mémoire 7.987/10 — sources ACCELERATION, V4 — MEMORY_ONLY

## Audit des plus fortes hausses

- SWEAT-EUR +142.88% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- SAND-EUR +48.46% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- GTC-EUR +33.45% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- SCR-EUR +22.24% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- CT-EUR +17.41% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- SUPER-EUR +17.21% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- MANA-EUR +16.52% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- MAGIC-EUR +15.02% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- SKY-EUR +14.83% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- ZK-EUR +13.99% — DETECTED_EARLY — couche NONE — action INTERPRETATION

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
