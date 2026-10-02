# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-10-02T08:56:35.924431+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : ALGO-EUR | action ACHETE_MAINTENANT | opportunité 7.975 | entrée 6.950 | trend 8.650 | rang 7.618
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : ZIG-EUR | action PLACE_LIMITE_PASSIVE | opportunité 8.062 | entrée 6.000 | trend 8.950 | rang 7.837
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : MAGIC-EUR | action LATENT_ACCELERATOR | opportunité 9.267 | entrée 4.950 | trend 8.650 | rang 7.836
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : MON-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.172 | entrée 6.450 | trend 8.550 | rang 7.825
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Tous les achats immédiats

1. ALGO-EUR — ACHETE_MAINTENANT — rank 7.618 — opportunité 7.975 — entrée 6.950 — trend 8.650
2. ZRO-EUR — ACHETE_MAINTENANT — rank 7.401 — opportunité 8.143 — entrée 7.000 — trend 8.800
3. LTC-EUR — ACHETE_MAINTENANT — rank 7.220 — opportunité 8.501 — entrée 7.450 — trend 6.600
4. RENDER-EUR — ACHETE_MAINTENANT — rank 6.834 — opportunité 7.721 — entrée 6.850 — trend 6.800
5. DOGE-EUR — ACHETE_MAINTENANT — rank 6.647 — opportunité 7.985 — entrée 7.250 — trend 5.850
6. EIGEN-EUR — ACHETE_MAINTENANT — rank 6.597 — opportunité 7.823 — entrée 7.200 — trend 6.100

## Top cross-sectionnel — aperçu non exhaustif

Ce top est une vue courte multi-buckets. Il ne doit jamais être utilisé comme liste exhaustive des achats immédiats.
1. ZIG-EUR — MEILLEURE_LIMITE_PASSIVE — PLACE_LIMITE_PASSIVE — rank 7.837
2. MAGIC-EUR — MEILLEUR_LATENT_ACCELERATOR — LATENT_ACCELERATOR — rank 7.836
3. MON-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.825

## Accélération indépendante

- PEOPLE-EUR — CONFIRMED_ACCELERATION — score 9.036/10 — DETECTED_BUT_TOO_LATE
- VELO-EUR — CONFIRMED_ACCELERATION — score 6.771/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- NES-EUR — CONFIRMED_ACCELERATION — score 6.741/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- MAGIC-EUR — BUILDING_ACCELERATION — score 6.381/10 — DETECTED_BUT_TOO_LATE
- ACT-EUR — BUILDING_ACCELERATION — score 6.267/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- TURBO-EUR — BUILDING_ACCELERATION — score 5.997/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- REQ-EUR — BUILDING_ACCELERATION — score 4.965/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- POND-EUR — BUILDING_ACCELERATION — score 4.868/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- ALGO-EUR — ACTIVE_NOW — score mémoire 7.618/10 — sources ACCELERATION, DECISION_LAYER, V4 — BUYABLE_NOW
- EIGEN-EUR — ACTIVE_NOW — score mémoire 6.597/10 — sources ACCELERATION, DECISION_LAYER, V4 — BUYABLE_NOW
- EDGE-EUR — MEMORY_24H — score mémoire 10.000/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- ICX-EUR — MEMORY_24H — score mémoire 9.403/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- TREAD-EUR — MEMORY_24H — score mémoire 9.258/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- OPEN-EUR — MEMORY_24H — score mémoire 9.112/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- PEOPLE-EUR — ACTIVE_NOW — score mémoire 9.036/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- OSMO-EUR — MEMORY_24H — score mémoire 8.342/10 — sources ACCELERATION — MEMORY_ONLY
- ZRC-EUR — MEMORY_24H — score mémoire 8.257/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- HFT-EUR — MEMORY_24H — score mémoire 8.078/10 — sources ACCELERATION — MEMORY_ONLY

## Audit des plus fortes hausses

- SWEAT-EUR +175.91% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- CT-EUR +45.19% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- SAND-EUR +42.94% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- GTC-EUR +28.12% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- SCR-EUR +18.89% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ZRO-EUR +14.41% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- SUPER-EUR +13.15% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- MANA-EUR +12.91% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- MAGIC-EUR +11.18% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- USELESS-EUR +11.15% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE

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
