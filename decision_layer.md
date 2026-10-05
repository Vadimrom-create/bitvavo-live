# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-10-05T17:44:47.404881+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : ICP-EUR | action ACHETE_MAINTENANT | opportunité 7.947 | entrée 7.250 | trend 8.700 | rang 7.772
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : MAGIC-EUR | action PLACE_LIMITE_PASSIVE | opportunité 7.854 | entrée 5.800 | trend 8.650 | rang 7.561
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : CELO-EUR | action LATENT_ACCELERATOR | opportunité 7.544 | entrée 5.650 | trend 8.150 | rang 7.233
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : FET-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.326 | entrée 6.950 | trend 9.200 | rang 8.014
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Tous les achats immédiats

1. ICP-EUR — ACHETE_MAINTENANT — rank 7.772 — opportunité 7.947 — entrée 7.250 — trend 8.700

## Top cross-sectionnel — aperçu non exhaustif

Ce top est une vue courte multi-buckets. Il ne doit jamais être utilisé comme liste exhaustive des achats immédiats.
1. FET-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.014
2. AVNT-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.907
3. ICP-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 7.772

## Accélération indépendante

- ARX-EUR — CONFIRMED_ACCELERATION — score 8.155/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- AVNT-EUR — CONFIRMED_ACCELERATION — score 7.662/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- BTT-EUR — CONFIRMED_ACCELERATION — score 7.073/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- MANA-EUR — BUILDING_ACCELERATION — score 6.476/10 — DETECTED_BUT_TOO_LATE
- INIT-EUR — BUILDING_ACCELERATION — score 6.084/10 — DETECTED_BUT_TOO_LATE
- XYO-EUR — BUILDING_ACCELERATION — score 5.611/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- ZEUS-EUR — BUILDING_ACCELERATION — score 4.910/10 — DETECTED_BUT_TOO_LATE
- BEAM-EUR — BUILDING_ACCELERATION — score 4.827/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- EDU-EUR — MEMORY_24H — score mémoire 9.962/10 — sources ACCELERATION — MEMORY_ONLY
- SWELL-EUR — MEMORY_24H — score mémoire 9.171/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- ACT-EUR — MEMORY_24H — score mémoire 8.838/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- TREAD-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- UMA-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- PORTAL-EUR — MEMORY_24H — score mémoire 8.374/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- ZKP-EUR — MEMORY_24H — score mémoire 8.310/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- FIDA-EUR — MEMORY_DECAY_24_72H — score mémoire 8.169/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- ARX-EUR — ACTIVE_NOW — score mémoire 8.155/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- XMN-EUR — MEMORY_24H — score mémoire 8.050/10 — sources ACCELERATION, V4 — MEMORY_ONLY

## Audit des plus fortes hausses

- RLC-EUR +62.09% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- GTC-EUR +37.80% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- NIL-EUR +28.51% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- ZEUS-EUR +25.67% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- FLUID-EUR +22.77% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- PNT-EUR +19.64% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- MOVR-EUR +16.67% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- RAD-EUR +14.94% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- EDU-EUR +13.94% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- PARTI-EUR +13.35% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE

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
