# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-10-05T15:32:06.086616+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : ICP-EUR | action ACHETE_MAINTENANT | opportunité 8.349 | entrée 7.500 | trend 8.550 | rang 7.805
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : CATI-EUR | action PLACE_LIMITE_PASSIVE | opportunité 7.401 | entrée 6.650 | trend 8.400 | rang 7.423
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : FLUX-EUR | action LATENT_ACCELERATOR | opportunité 7.479 | entrée 5.300 | trend 8.950 | rang 7.518
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : BAT-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.214 | entrée 6.350 | trend 8.900 | rang 7.917
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Tous les achats immédiats

1. ICP-EUR — ACHETE_MAINTENANT — rank 7.805 — opportunité 8.349 — entrée 7.500 — trend 8.550

## Top cross-sectionnel — aperçu non exhaustif

Ce top est une vue courte multi-buckets. Il ne doit jamais être utilisé comme liste exhaustive des achats immédiats.
1. BAT-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.917
2. YGG-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.827
3. ICP-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 7.805

## Accélération indépendante

- RAD-EUR — CONFIRMED_ACCELERATION — score 9.086/10 — DETECTED_BUT_TOO_LATE
- CHIP-EUR — CONFIRMED_ACCELERATION — score 6.569/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- LSK-EUR — BUILDING_ACCELERATION — score 6.182/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- ZRO-EUR — BUILDING_ACCELERATION — score 5.902/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- LIGHTER-EUR — BUILDING_ACCELERATION — score 5.840/10 — DETECTED_BUT_TOO_LATE
- RED-EUR — BUILDING_ACCELERATION — score 5.699/10 — DETECTED_BUT_TOO_LATE
- CAP-EUR — BUILDING_ACCELERATION — score 5.346/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- SAGA-EUR — BUILDING_ACCELERATION — score 4.827/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- ICP-EUR — ACTIVE_NOW — score mémoire 7.805/10 — sources ACCELERATION, DECISION_LAYER, V4 — BUYABLE_NOW
- EDU-EUR — MEMORY_24H — score mémoire 9.962/10 — sources ACCELERATION — MEMORY_ONLY
- SWELL-EUR — MEMORY_24H — score mémoire 9.171/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- RAD-EUR — ACTIVE_NOW — score mémoire 9.086/10 — sources ACCELERATION — DETECTED_BUT_TOO_LATE
- ACT-EUR — MEMORY_24H — score mémoire 8.838/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- POND-EUR — MEMORY_24H — score mémoire 8.593/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- FIDA-EUR — MEMORY_DECAY_24_72H — score mémoire 8.591/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- TREAD-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- UMA-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- PORTAL-EUR — MEMORY_24H — score mémoire 8.374/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY

## Audit des plus fortes hausses

- GTC-EUR +80.32% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- RLC-EUR +57.55% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- PNT-EUR +43.69% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- FLUID-EUR +21.12% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- MOVR-EUR +19.46% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- CARV-EUR +16.78% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- SCR-EUR +16.22% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- NIL-EUR +15.92% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- PARTI-EUR +13.51% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- EDU-EUR +13.24% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE

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
