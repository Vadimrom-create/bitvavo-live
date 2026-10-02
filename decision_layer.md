# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-10-02T09:39:56.645924+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : WLD-EUR | action ACHETE_MAINTENANT | opportunité 8.487 | entrée 7.200 | trend 8.700 | rang 7.989
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : MON-EUR | action PLACE_LIMITE_PASSIVE | opportunité 7.423 | entrée 5.950 | trend 8.550 | rang 7.443
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : DYDX-EUR | action LATENT_ACCELERATOR | opportunité 7.782 | entrée 5.550 | trend 8.950 | rang 7.686
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : ALGO-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 7.752 | entrée 7.250 | trend 8.650 | rang 7.706
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Tous les achats immédiats

1. WLD-EUR — ACHETE_MAINTENANT — rank 7.989 — opportunité 8.487 — entrée 7.200 — trend 8.700
2. AAVE-EUR — ACHETE_MAINTENANT — rank 7.813 — opportunité 8.507 — entrée 6.800 — trend 8.900

## Top cross-sectionnel — aperçu non exhaustif

Ce top est une vue courte multi-buckets. Il ne doit jamais être utilisé comme liste exhaustive des achats immédiats.
1. WLD-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 7.989
2. AAVE-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 7.813
3. ALGO-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.706

## Accélération indépendante

- ICX-EUR — CONFIRMED_ACCELERATION — score 7.389/10 — DETECTED_BUT_TOO_LATE
- THQ-EUR — BUILDING_ACCELERATION — score 5.970/10 — DETECTED_BUT_TOO_LATE
- MOVR-EUR — BUILDING_ACCELERATION — score 5.691/10 — DETECTED_BUT_TOO_LATE
- PARTI-EUR — BUILDING_ACCELERATION — score 5.199/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- ME-EUR — BUILDING_ACCELERATION — score 5.114/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- EGLD-EUR — BUILDING_ACCELERATION — score 4.996/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- SWELL-EUR — BUILDING_ACCELERATION — score 4.866/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- WLD-EUR — ACTIVE_NOW — score mémoire 7.989/10 — sources ACCELERATION, DECISION_LAYER, V4 — BUYABLE_NOW
- EDGE-EUR — MEMORY_24H — score mémoire 10.000/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- TREAD-EUR — MEMORY_24H — score mémoire 9.258/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- OPEN-EUR — MEMORY_24H — score mémoire 9.112/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- PEOPLE-EUR — MEMORY_24H — score mémoire 9.036/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- OSMO-EUR — MEMORY_24H — score mémoire 8.342/10 — sources ACCELERATION — MEMORY_ONLY
- ZRC-EUR — MEMORY_24H — score mémoire 8.257/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- HFT-EUR — MEMORY_24H — score mémoire 8.078/10 — sources ACCELERATION — MEMORY_ONLY
- GIGA-EUR — MEMORY_24H — score mémoire 7.987/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- CSPR-EUR — MEMORY_24H — score mémoire 7.942/10 — sources ACCELERATION, V4 — MEMORY_ONLY

## Audit des plus fortes hausses

- SWEAT-EUR +197.88% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- SAND-EUR +47.58% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- GTC-EUR +29.54% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- CT-EUR +28.02% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- MAGIC-EUR +16.97% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- MANA-EUR +16.67% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- SCR-EUR +15.56% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ENJ-EUR +15.10% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- SUPER-EUR +13.22% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- SKY-EUR +12.79% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION

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
