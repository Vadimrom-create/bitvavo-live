# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-10-02T08:38:20.506496+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : ALGO-EUR | action ACHETE_MAINTENANT | opportunité 8.220 | entrée 6.800 | trend 8.650 | rang 7.670
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : DYDX-EUR | action PLACE_LIMITE_PASSIVE | opportunité 8.504 | entrée 6.050 | trend 8.950 | rang 8.039
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : KSM-EUR | action LATENT_ACCELERATOR | opportunité 8.168 | entrée 5.450 | trend 8.700 | rang 7.783
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : C-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.455 | entrée 6.850 | trend 8.200 | rang 7.820
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Tous les achats immédiats

1. ALGO-EUR — ACHETE_MAINTENANT — rank 7.670 — opportunité 8.220 — entrée 6.800 — trend 8.650
2. EIGEN-EUR — ACHETE_MAINTENANT — rank 6.996 — opportunité 8.738 — entrée 7.250 — trend 6.100
3. DOGE-EUR — ACHETE_MAINTENANT — rank 6.994 — opportunité 8.681 — entrée 7.500 — trend 5.850
4. RENDER-EUR — ACHETE_MAINTENANT — rank 6.913 — opportunité 8.784 — entrée 7.050 — trend 6.800
5. SUI-EUR — ACHETE_MAINTENANT — rank 6.130 — opportunité 7.193 — entrée 6.950 — trend 5.400

## Top cross-sectionnel — aperçu non exhaustif

Ce top est une vue courte multi-buckets. Il ne doit jamais être utilisé comme liste exhaustive des achats immédiats.
1. DYDX-EUR — MEILLEURE_LIMITE_PASSIVE — PLACE_LIMITE_PASSIVE — rank 8.039
2. ZIG-EUR — MEILLEURE_LIMITE_PASSIVE — PLACE_LIMITE_PASSIVE — rank 7.952
3. KAIA-EUR — MEILLEURE_LIMITE_PASSIVE — PLACE_LIMITE_PASSIVE — rank 7.931

## Accélération indépendante

- ICX-EUR — CONFIRMED_ACCELERATION — score 9.403/10 — DETECTED_BUT_TOO_LATE
- GALA-EUR — CONFIRMED_ACCELERATION — score 8.964/10 — DETECTED_BUT_TOO_LATE
- SAND-EUR — CONFIRMED_ACCELERATION — score 8.052/10 — DETECTED_BUT_TOO_LATE
- CSPR-EUR — CONFIRMED_ACCELERATION — score 7.942/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- SWEAT-EUR — CONFIRMED_ACCELERATION — score 7.438/10 — DETECTED_BUT_TOO_LATE
- ALT-EUR — CONFIRMED_ACCELERATION — score 6.633/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- AUCTION-EUR — BUILDING_ACCELERATION — score 6.153/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- MANA-EUR — BUILDING_ACCELERATION — score 5.713/10 — DETECTED_BUT_TOO_LATE
- GMT-EUR — BUILDING_ACCELERATION — score 5.632/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- AXS-EUR — BUILDING_ACCELERATION — score 5.593/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- ALGO-EUR — ACTIVE_NOW — score mémoire 7.670/10 — sources ACCELERATION, DECISION_LAYER, V4 — BUYABLE_NOW
- EIGEN-EUR — ACTIVE_NOW — score mémoire 6.996/10 — sources ACCELERATION, DECISION_LAYER, V4 — BUYABLE_NOW
- EDGE-EUR — MEMORY_24H — score mémoire 10.000/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- ICX-EUR — ACTIVE_NOW — score mémoire 9.403/10 — sources ACCELERATION, V4 — DETECTED_BUT_TOO_LATE
- TREAD-EUR — MEMORY_24H — score mémoire 9.258/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- OPEN-EUR — MEMORY_24H — score mémoire 9.112/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- GALA-EUR — ACTIVE_NOW — score mémoire 8.964/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- OSMO-EUR — MEMORY_24H — score mémoire 8.342/10 — sources ACCELERATION — MEMORY_ONLY
- ZRC-EUR — MEMORY_24H — score mémoire 8.257/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- HFT-EUR — MEMORY_24H — score mémoire 8.078/10 — sources ACCELERATION — MEMORY_ONLY

## Audit des plus fortes hausses

- SWEAT-EUR +182.54% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- CT-EUR +48.47% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- SAND-EUR +45.25% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- GTC-EUR +28.89% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- SCR-EUR +16.26% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- MANA-EUR +16.10% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- SUPER-EUR +14.25% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- GALA-EUR +12.81% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- ZRO-EUR +11.67% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- USELESS-EUR +11.31% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE

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
